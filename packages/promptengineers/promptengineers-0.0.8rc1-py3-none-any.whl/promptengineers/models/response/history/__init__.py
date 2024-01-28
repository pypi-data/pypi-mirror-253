from promptengineers.models.history import HistoryDocument, HISTORY_DOCUMENT

class ResponseHistoryIndex(HistoryDocument): # pylint: disable=too-few-public-methods
	histories: list[HistoryDocument]

	__config__ = {
		"json_schema_extra": {
			"example": {
				"histories": [HISTORY_DOCUMENT]
            }
		}
	}

class ResponseHistoryShow(HistoryDocument): # pylint: disable=too-few-public-methods
	history: HistoryDocument

	__config__ = {
		"json_schema_extra": {
			"example": {
				"history": HISTORY_DOCUMENT
            }
		}
	}