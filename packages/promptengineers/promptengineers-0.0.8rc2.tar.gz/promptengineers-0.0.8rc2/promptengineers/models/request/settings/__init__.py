from promptengineers.models.settings import ChatSettings, CHAT_SETTINGS

class ReqBodySettings(ChatSettings): # pylint: disable=too-few-public-methods

	__config__ = {
		"json_schema_extra": {
			"example": CHAT_SETTINGS
		}
	}