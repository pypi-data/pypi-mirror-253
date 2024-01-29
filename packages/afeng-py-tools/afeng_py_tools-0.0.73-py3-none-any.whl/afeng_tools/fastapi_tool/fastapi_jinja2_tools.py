from starlette.responses import Response
from starlette.templating import Jinja2Templates, _TemplateResponse
from starlette.requests import Request

from afeng_tools.application_tool import settings_tools
from afeng_tools.application_tool.settings_enum import SettingsKeyEnum

jinja2_templates = Jinja2Templates(directory=settings_tools.get_config(SettingsKeyEnum.server_template_path))


def create_template_response(request: Request, template_file: str, context: dict = None) -> _TemplateResponse:
    """
    创建模板响应
    :param request: Request
    :param template_file: 模板文件
    :param context: 上下文内容
    :return:
    """
    if isinstance(context, Response):
        return context
    if not context:
        context = dict()
    if 'request' not in context:
        context['request'] = request
    return jinja2_templates.TemplateResponse(template_file, context=context)
