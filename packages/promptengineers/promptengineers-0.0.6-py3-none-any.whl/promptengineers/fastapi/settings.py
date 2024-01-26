"""Routes to get chat history"""
import json
import traceback

from fastapi import APIRouter, HTTPException, Response, Depends, Request, status
from promptengineers.core.interfaces.controllers import IController
from promptengineers.fastapi.controllers import SettingsController
from promptengineers.models.request import ReqBodySettings
from promptengineers.models.response import (ResponseSettingsList, ResponseSetting,
                                            ResponseCreate, ResponseUpdate)
from promptengineers.mongo.utils import JSONEncoder
from promptengineers.core.utils import logger
from promptengineers.core.exceptions import NotFoundException

router = APIRouter()
TAG = "Chat"

def get_controller(request: Request) -> IController:
	try:
		return SettingsController(request=request, user_repo=request.state.user_repo)
	except NotFoundException as e:
		# Handle specific NotFoundException with a custom message or logging
		logger.warn(f"Failed to initialize HistoryController: {str(e)}")
		raise HTTPException(status_code=404, detail=f"Initialization failed: {str(e)}") from e
	except Exception as e:
		# Catch all other exceptions
		logger.error(f"Unexpected error initializing HistoryController: {str(e)}")
		raise HTTPException(status_code=500, detail="Internal server error") from e

#################################################
# List Chat Histories
#################################################
@router.get(
	"/chat/settings",
	tags=[TAG],
	name='settings_list',
	response_model=ResponseSettingsList
)
async def index(
	page: int = 1,
	limit: int = 50,
	controller: IController = Depends(get_controller),
):
	"""List settings"""
	try:
		result = await controller.index(page, limit)
		# Format Response
		data = json.dumps({
			'settings': result,
		}, cls=JSONEncoder)
		return Response(
			content=data,
			media_type='application/json',
			status_code=200
		)
	except HTTPException as err:
		logger.error(err.detail)
		raise
	except BaseException as err:
		tb = traceback.format_exc()
		logger.error("[controllers.settings.index]: %s\n%s", err, tb)
		raise HTTPException(
			status_code=500,
			detail=f"An unexpected error occurred. {str(err)}"
		) from err

#################################################
# Create Chat History
#################################################
@router.post(
	"/chat/settings",
	tags=[TAG],
	name='settings_create',
	response_model=ResponseCreate
)
async def create(
	body: ReqBodySettings,
	controller: IController = Depends(get_controller)
):
	"""Creates settings"""
	try:
		result = await controller.create(body)
		# Format Response
		data = json.dumps({
			**result
		})
		return Response(
			content=data,
			media_type='application/json',
			status_code=200
		)
	except HTTPException as err:
		logger.error(err.detail)
		raise
	except BaseException as err:
		tb = traceback.format_exc()
		logger.error("[controllers.settings.create]: %s\n%s", err, tb)
		raise HTTPException(
			status_code=500,
			detail=f"An unexpected error occurred. {str(err)}"
		) from err

#################################################
# Show Chat History
#################################################
@router.get(
	"/chat/settings/{setting_id}",
	tags=[TAG],
	name='settings_show',
	response_model=ResponseSetting,
)
async def show(
    setting_id: str,
    controller: IController = Depends(get_controller),
):
	"""Retrieve settings"""
	try:
		result = await controller.show(setting_id)

		# Format Response
		data = json.dumps({
			'setting': result
		}, cls=JSONEncoder)
		return Response(
			content=data,
			media_type='application/json',
			status_code=200
		)
	except HTTPException as err:
		logger.error("%s", err.detail)
		raise
	except BaseException as err:
		tb = traceback.format_exc()
		logger.error("[controllers.settings.show]: %s\n%s", err, tb)
		raise HTTPException(
			status_code=500,
			detail=f"An unexpected error occurred. {str(err)}"
		) from err

#################################################
# Update Chat History
#################################################
@router.put(
	"/chat/settings/{setting_id}",
	tags=[TAG],
	name='settings_update',
	response_model=ResponseUpdate,
)
async def update(
	setting_id: str,
	body: ReqBodySettings,
	controller: IController = Depends(get_controller),
):
	"""Update settings"""
	try:
		await controller.update(setting_id, body)
		data = json.dumps({
			'message': f'Setting [{setting_id}] updated successfully.'
		})
		# Format Response
		return Response(status_code=200, content=data)
	except HTTPException as err:
		logger.error("%s", err.detail)
		raise
	except BaseException as err:
		tb = traceback.format_exc()
		logger.error("[controllers.settings.update]: %s\n%s", err, tb)
		raise HTTPException(
			status_code=500,
			detail=f"An unexpected error occurred. {str(err)}"
		) from err

#################################################
# Delete Chat History
#################################################
@router.delete(
	"/chat/settings/{setting_id}",
	tags=[TAG],
	name='settings_delete',
	status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
	setting_id: str,
	controller: IController = Depends(get_controller),
):
	"""Delete settings"""
	try:
		await controller.delete(setting_id)
		# Format Response
		return Response(status_code=204)
	except BaseException as err:
		tb = traceback.format_exc()
		logger.error("[controllers.settings.delete]: %s\n%s", err, tb)
		raise HTTPException(status_code=404, detail=str(err)) from err