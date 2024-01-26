from bson.objectid import ObjectId

from promptengineers.core.config import MONGO_CONNECTION, MONGO_DB_NAME
from promptengineers.core.interfaces.controllers import IController
from promptengineers.core.interfaces.repos import IUserRepo
from promptengineers.repos.user import UserRepo
from promptengineers.mongo.service import MongoService
from promptengineers.models.request import ReqBodySettings

class SettingsController(IController):
	def __init__(
		self, 
		request = None,
		user_repo: IUserRepo = None, 
		db_name: str = None,
		col_name: str = None
	):
		self.request = request
		self.user_id = getattr(request.state, "user_id", None)
		self.user_repo = user_repo or UserRepo()
		self.settings_service = MongoService(
			host=MONGO_CONNECTION,
			db=db_name or MONGO_DB_NAME,
			collection=col_name or 'settings'
		)

	##############################################################
	### Index
	##############################################################
	async def index(self, page: int = 1, limit: int = 10):
		result = await self.settings_service.list_docs(
			{'user_id': ObjectId(self.user_id)},
			limit,
			page
		)
		return result

	##############################################################
	### Create
	##############################################################
	async def create(
			self, 
			body: ReqBodySettings, 
			keys: set[str] = {'system', 'temperature', 'retrieval', 'tags',
		  						'functions', 'tools', 'plugins', 'title', 'model', 'stream'}
		):
		body = await self.request.json()
		body = dict((k, body[k]) for k in keys if k in body)
		body['user_id'] = ObjectId(self.user_id)
		result = await self.settings_service.create(dict(body))
		return result

	##############################################################
	### Show
	##############################################################
	async def show(self, id: str):
		result = await self.settings_service.read_one(
			{'_id': ObjectId(id), 'user_id': ObjectId(self.user_id)}
		)
		return result


	##############################################################
	### Update
	##############################################################
	async def update(
		self, 
		id: str, 
		body: ReqBodySettings,
		keys: set[str] = {'system', 'temperature', 'retrieval', 'tags',
		  						'functions', 'tools', 'plugins', 'title', 'model', 'stream'}
	):
		body = await self.request.json()
		body = dict((k, body[k]) for k in keys if k in body)
		result = await self.settings_service.update_one(
			{'_id': ObjectId(id), 'user_id': ObjectId(self.user_id)},
			dict(body)
		)
		return result

	##############################################################
	### Delete
	##############################################################
	async def delete(self, id: str):
		result = await self.settings_service.delete_one(
			{'_id': ObjectId(id), 'user_id': ObjectId(self.user_id)}
		)
		return result