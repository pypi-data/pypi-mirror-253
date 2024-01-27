"""
FastAPI路由工具
"""
import importlib
import os

from fastapi import APIRouter


def create_router(prefix: str, tags: list[str]) -> APIRouter:
    """创建路由"""
    router = APIRouter(prefix=prefix, tags=tags)
    return router


def auto_load_routers(web_root_path: str, web_root_name: str = None,
                      view_file_name: str = 'views', router_name='router') -> list[APIRouter]:
    """自动加载web.{app}.views文件中的路由"""
    router_list = []
    if web_root_name is None:
        web_root_name = os.path.split(web_root_path)[1]
    if os.path.exists(web_root_path):
        for app_name in os.listdir(web_root_path):
            if os.path.isdir(os.path.join(web_root_path, app_name)) and app_name != '__pycache__' and app_name != 'admin':
                if os.path.exists(os.path.join(web_root_path, app_name, view_file_name+'.py')):
                    web_app_views = importlib.import_module(f'{web_root_name}.{app_name}.{view_file_name}')
                    router_list.append(web_app_views.__getattribute__(router_name))
    return router_list
