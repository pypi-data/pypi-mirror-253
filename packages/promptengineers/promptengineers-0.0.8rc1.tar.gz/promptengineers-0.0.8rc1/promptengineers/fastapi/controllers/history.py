from bson.objectid import ObjectId

from promptengineers.core.config import MONGO_CONNECTION, MONGO_DB_NAME
from promptengineers.core.interfaces.controllers import IController
from promptengineers.core.interfaces.repos import IUserRepo
from promptengineers.repos.user import UserRepo
from promptengineers.mongo.service import MongoService


class HistoryController(IController):
	def __init__(
		self,
		user_id: str = None,
		request = None,
		user_repo: IUserRepo = None,
		db_name: str = None,
		col_name: str = None
	):
		self.request = request
		self.user_id = user_id or getattr(request.state, "user_id", None)
		self.user_repo = user_repo or UserRepo()
		self.history_service = MongoService(
			host=MONGO_CONNECTION,
			db=db_name or MONGO_DB_NAME,
			collection=col_name or 'history'
		)

	##############################################################
	### Create Chat History
	##############################################################
	async def index(self, page: int = 1, limit: int = 10, **kwargs):
		# Base query with user_id
		query = {'user_id': ObjectId(self.user_id)}

		# Add additional filters passed as keyword arguments
		for key, value in kwargs.items():
			if value is not None:  # Ensure that a value is provided for the filter
				# Convert to ObjectId if necessary, for example, if key ends with "_id"
				if key in {'setting'}:
					query[key] = ObjectId(value)
				else:
					query[key] = value

		# Get the result from the history_service
		result = await self.history_service.list_docs(query, limit, page)
		return result

	##############################################################
	### Create Chat History
	##############################################################
	async def create(
			self, 
			body, 
			keys: set[str] = {'setting', 'messages', 'tags', 'title'}
		):
		body = await self.request.json() if self.request else body
		body = dict((k, body[k]) for k in keys if k in body)
		body['user_id'] = ObjectId(self.user_id)
		if body.get('setting', False):
			body['setting'] = ObjectId(body['setting'])
		result = await self.history_service.create(dict(body))
		return result

	##############################################################
	### Show Chat History
	##############################################################
	async def show(self, id: str = None, query = None):
		result = await self.history_service.read_one(
			query or {'_id': ObjectId(id), 'user_id': ObjectId(self.user_id)}
		)
		return result

	##############################################################
	### Update Chat History
	##############################################################
	async def update(
			self, 
			id: str, 
			body: any, 
			keys: set[str] = {'setting', 'messages', 'tags', 'title'}
		):
		body = await self.request.json() if self.request else body
		body = dict((k, body[k]) for k in keys if k in body)
		if body.get('setting', False):
			body['setting'] = ObjectId(body['setting'])
		result = await self.history_service.update_one(
			{'_id': ObjectId(id), 'user_id': ObjectId(self.user_id)},
			dict(body)
		)
		return result

	##############################################################
	### Delete Chat History
	##############################################################
	async def delete(self, id: str):
		result = await self.history_service.delete_one(
			{'_id': ObjectId(id), 'user_id': ObjectId(self.user_id)}
		)
		return result
