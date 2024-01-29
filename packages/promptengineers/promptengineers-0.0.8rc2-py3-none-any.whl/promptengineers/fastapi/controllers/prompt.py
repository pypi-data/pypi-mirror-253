from bson.objectid import ObjectId
# from fastapi import Request

from promptengineers.core.config import MONGO_CONNECTION, MONGO_DB_NAME
from promptengineers.core.interfaces.controllers import IController
from promptengineers.core.interfaces.repos import IUserRepo
from promptengineers.repos.user import UserRepo
from promptengineers.mongo.service import MongoService
from promptengineers.models.request import ReqBodyPromptSystem

class PromptController(IController):
	def __init__(
		self, 
		# request: Request = None, 
		request = None,
		user_repo: IUserRepo = None, 
		db_name: str = None,
		col_name: str = None
	):
		self.request = request
		self.user_id = getattr(request.state, "user_id", None)
		self.user_repo = user_repo or UserRepo()
		self.prompt_service = MongoService(
			host=MONGO_CONNECTION,
			db=db_name or MONGO_DB_NAME,
			collection=col_name or 'prompts'
		)

	##############################################################
	### Create Chat History
	##############################################################
	async def index(self, page: int = 1, limit: int = 10):
		result = await self.prompt_service.list_docs(
			{'user_id': ObjectId(self.user_id)},
			limit,
			page
		)
		return result

	##############################################################
	### Create Chat History
	##############################################################
	async def create(self, body: ReqBodyPromptSystem):
		body = await self.request.json()
		body['user_id'] = ObjectId(self.user_id)
		result = await self.prompt_service.create(dict(body))
		return result

	##############################################################
	### Update Chat History
	##############################################################
	async def show(self, chat_id: str):
		result = await self.prompt_service.read_one(
			{'_id': ObjectId(chat_id), 'user_id': ObjectId(self.user_id)}
		)
		return result


	##############################################################
	### Update Chat History
	##############################################################
	async def update(self, chat_id: str, body: ReqBodyPromptSystem):
		body = await self.request.json()
		result = await self.prompt_service.update_one(
			{'_id': ObjectId(chat_id), 'user_id': ObjectId(self.user_id)},
			dict(body)
		)
		return result

	##############################################################
	### Delete Chat History
	##############################################################
	async def delete(self, chat_id: str):
		result = await self.prompt_service.delete_one(
			{'_id': ObjectId(chat_id), 'user_id': ObjectId(self.user_id)}
		)
		return result