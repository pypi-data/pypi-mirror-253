import json
import random

from database_mysql_local.generic_crud import GenericCRUD
from dotenv import load_dotenv
from logger_local.LoggerLocal import Logger
from profiles_local.profiles_local import ProfilesLocal
from variable_local.template import ReplaceFieldsWithValues

from .MessageChannels import MessageChannel
from .MessageConstants import object_message
from .MessageTemplates import MessageTemplates
from .Recipient import Recipient

load_dotenv()
# TODO Should be in sync with json_version schema in the database
VERSION = "20240118"

logger = Logger.create_logger(object=object_message)

lang_code_cache = {}

class CompoundMessage(GenericCRUD):
    def __init__(self, campaign_id: int = None, body: str = None, subject: str = None,
                 recipients: list[Recipient] = None, message_id: int = None):
        if campaign_id is not None:
            GenericCRUD.__init__(self, default_schema_name="campaign", default_table_name="campaign_table",
                                 default_view_table_name="campaign_view", default_id_column_name="campaign_id")

        self.campaign_id = campaign_id
        self.body = body
        self.subject = subject
        self.recipients = recipients
        self.message_id = message_id
        self.__compound_message = {}

        self.profile_local = ProfilesLocal()
        self.message_template = MessageTemplates()
        self.set_compound_message_after_text_template()

    def set_compound_message_after_text_template(
            self, campaign_id: int = None, body: str = None, subject: str = None,
            recipients: list[Recipient] = None, message_id: int = None) -> None:
        """:returns
    {
        'DEFAULT': {
            'bodyBlocks': {
                'blockId': ...,
                'blockTypeId': ...,
                'blockTypeName': ...,
                'questionId': ...,
                'questionTypeId': ...,
                'questionTitle': ...,
                'questionTypeName': ...,
                'profileBlocks': [{'profileId': ..., 'template': ..., 'processedTemplate': ...}, ...]
            },

            'subjuctBlocks': {...}  // same as body
        },

        'EMAIL': {...},  // same as default
        'SMS': {...},
        'WHATSAPP': {...}
    }
        """
        logger.start()

        # Allow overiding instance vars
        campaign_id = campaign_id or self.campaign_id
        body = body or self.body
        subject = subject or self.subject
        recipients = recipients or self.recipients or []
        message_id = message_id or self.message_id

        compound_message = {"DEFAULT": {},
                            "WEB": {},
                            "EMAIL": {},
                            "SMS": {},
                            "WHATSAPP": {}
                            }

        channels_mapping = {
            MessageChannel.SMS.name: {"body": "sms_body_template", "subject": None},
            MessageChannel.EMAIL.name: {"body": "email_body_html_template", "subject": "email_subject_template"},
            MessageChannel.WHATSAPP.name: {"body": "whatsapp_body_template", "subject": None},
            "DEFAULT": {"body": "default_body_template", "subject": "default_subject_template"},
        }

        criteria_json = {}
        if body:
            textblocks_and_attributes = [{}]  # one textblock
            for message_channel, template_header in channels_mapping.items():
                textblocks_and_attributes[0][template_header["body"]] = body
                textblocks_and_attributes[0][template_header["subject"]] = subject

        else:  # If body is not given, get it from the database
            textblocks_and_attributes = self.message_template.get_textblocks_and_attributes()
            if campaign_id is not None:
                message_template_ids = super().select_multi_tuple_by_id(view_table_name="campaign_view",
                                                                        id_column_name="campaign_id",
                                                                        id_column_value=campaign_id,
                                                                        select_clause_value="message_template_id")

                message_template_ids = [message_template_id[0] for message_template_id in message_template_ids]
                criteria_json = self.message_template.get_critiria_json(
                    message_template_id=random.choice(message_template_ids))
        logger.info({"textblocks_and_attributes": textblocks_and_attributes})

        for message_template_textblock_and_attributes in textblocks_and_attributes:
            for message_channel, template_header in channels_mapping.items():
                for part in ("body", "subject"):
                    compound_message[message_channel][f"{part}Blocks"] = {
                        "blockId": message_template_textblock_and_attributes.get("blockId"),
                        "blockTypeId": message_template_textblock_and_attributes.get("blockTypeId"),
                        "blockTypeName": message_template_textblock_and_attributes.get("blockTypeName"),
                        "questionId": message_template_textblock_and_attributes.get("questionId"),
                        "questionTypeId": message_template_textblock_and_attributes.get("questionTypeId"),
                        "questionTitle": message_template_textblock_and_attributes.get("questionTitle"),
                        "questionTypeName": message_template_textblock_and_attributes.get("questionTypeName"),
                        "profileBlocks": []
                    }
                    templates = [x for x in (message_template_textblock_and_attributes.get(template_header[part]),
                                             message_template_textblock_and_attributes.get("questionTitle"))
                                 if x]

                    message_template = " ".join(templates)
                    if not message_template:
                        logger.warning("message_template is empty", object={
                            "message_template_textblock_and_attributes": message_template_textblock_and_attributes})
                        continue
                    for recipient in recipients:
                        if recipient.get_profile_id() not in lang_code_cache:
                            lang_code_cache[recipient.get_profile_id()] = self.profile_local.get_preferred_lang_code_by_profile_id(
                                recipient.get_profile_id()).value
                        preferred_lang_code = lang_code_cache[recipient.get_profile_id()]
                        if (self.message_template.get_potentials_receipients(
                                criteria_json, recipient.get_profile_id())
                                and preferred_lang_code == message_template_textblock_and_attributes.get("langCode")):
                            compound_message[message_channel][f"{part}Blocks"]["profileBlocks"].append(
                                # each profile has its own template, because of the language
                                {"profileId": recipient.get_profile_id(),
                                 "template": message_template,
                                 "processedTemplate": self._process_text_block(message_template, recipient=recipient),
                                 })

        # save in message table
        if message_id:
            super().set_schema(schema_name="message")
            super().update_by_id(
                table_name="message_table", id_column_name="message_id", id_column_value=message_id,
                data_json={"compound_message": json.dumps(compound_message)})
        logger.end(object={"compound_message": compound_message})
        self.__compound_message = compound_message

    def _process_text_block(self, text_block_body: str, recipient: Recipient) -> str:
        template = ReplaceFieldsWithValues(message=text_block_body,
                                           language=recipient.get_preferred_language(),
                                           variable=recipient.get_profile_variables())
        # TODO: get the sender name
        processed_text_block = template.get_variable_values_and_chosen_option(
            profile_id=recipient.get_profile_id(), kwargs={"target name": recipient.get_person_id(),  # TODO ?
                                                           "message_id": self.message_id})
        return processed_text_block

    def get_compound_message_dict(self, channel: MessageChannel = None) -> dict:
        logger.start(object={"channel": channel})
        compound_message = {}
        if channel is None:
            compound_message = self.__compound_message
        else:
            compound_message["DEFAULT"] = self.__compound_message["DEFAULT"]
            compound_message[channel.name] = self.__compound_message[channel.name]
        logger.end(object={"compound_message": compound_message})
        return compound_message

    def get_compound_message_str(self, channel: MessageChannel = None) -> str:
        return json.dumps(self.get_compound_message_dict(channel=channel))

    def get_profile_block(self, profile_id: int, channel: MessageChannel, part: str = "body") -> dict:
        """Returns a dict with the following keys:
        profileId, template, processedTemplate, blockId, blockTypeId, blockTypeName, questionId,
            questionTypeId, questionTitle, questionTypeName
        """
        logger.start(object={"profile_id": profile_id, "channel": channel, "part": part})
        assert part in ("body", "subject")
        full_profile_block = self.__compound_message.get(channel.name, {}).get(f"{part}Blocks", {})
        for _profile_block in full_profile_block.get("profileBlocks", []):
            if _profile_block.get("profileId") == profile_id:
                profile_block = {**_profile_block, **{k: v for k, v in full_profile_block.items()
                                                      if k != "profileBlocks"}}
                logger.end(object={"profile_block": profile_block})
                return profile_block
        logger.end(object={"profile_block": {}})
        return {}

    def getMessageFields(self) -> dict:
        recipients_obj = {

        }
        if self.recipients is not None:
            for recipient in self.recipients:
                recipients_obj[recipient.get_profile_id] = recipient.to_json()
                recipient.to_json()
        obj = {
            "campaign_id": self.campaign_id,
            "body": self.body,
            "subject": self.subject,
            "message_id": self.message_id,
            "recipients": recipients_obj
        }
        return obj
