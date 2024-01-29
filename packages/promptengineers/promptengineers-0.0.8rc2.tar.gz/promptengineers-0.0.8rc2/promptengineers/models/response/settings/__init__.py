from typing import List
from pydantic import BaseModel

from promptengineers.models.settings import ChatSettingDocument, CHAT_SETTING_DOCUMENT

class ResponseSettingsList(ChatSettingDocument): # pylint: disable=too-few-public-methods
	settings: List[ChatSettingDocument] = []

	__config__ = {
		"json_schema_extra": {
			"example": {
				"settings": [CHAT_SETTING_DOCUMENT]
			}
		}
	}

class ResponseSetting(ChatSettingDocument): # pylint: disable=too-few-public-methods
	setting: ChatSettingDocument

	__config__ = {
		"json_schema_extra": {
			"example": {
				"setting": CHAT_SETTING_DOCUMENT
			}
		}
	}

