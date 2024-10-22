import asyncio
import json
import random
import uuid

from fastapi import HTTPException
from starlette.concurrency import run_in_threadpool

from api.files import get_image_size, get_file_extension, determine_file_use_case
from api.models import model_proxy
from chatgpt.authorization import get_req_token, verify_token
from chatgpt.chatFormat import api_messages_to_chat, stream_response, format_not_stream_response, head_process_response
from chatgpt.chatLimit import check_is_limit, handle_request_limit
from chatgpt.proofofWork import get_config, get_dpl, get_answer_token, get_requirements_token

from utils.Client import Client
from utils.Logger import logger
from utils.config import proxy_url_list, chatgpt_base_url_list

class ChatService:
    def __init__(self, req_token):
        self.req_token = req_token

    # Define other methods as needed
