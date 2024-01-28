from promptengineers.models.history import History, HISTORY

class ReqBodyHistory(History): # pylint: disable=too-few-public-methods

	__config__ = {
		"json_schema_extra": {
			"example": HISTORY
		}
	}