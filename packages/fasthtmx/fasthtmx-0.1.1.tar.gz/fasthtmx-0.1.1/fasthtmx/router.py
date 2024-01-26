from functools import wraps

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


class HXRouter(APIRouter):
    def __init__(self, templates: Jinja2Templates, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.templates = templates

    def hx_get(
        self,
        path: str,
        template: str,
        hx_template: str = "",
        enable_json_route: bool = True,
        json_route_prefix: str = "api",
        *args,
        **kwargs,
    ):
        """
        Extended APIRouter.get method with additional parameters.

        Parameters:
        - path (str): The endpoint path.
        - template (str): Optional template name.
        - hx_template (Optional[str]): Optional HX template name for partial page updates based on the HX-Request Header.
        - json_route_prefix (Optional[str]): The API prefix to use for the endpoint and tag separated by a slash.
            - Example: "api/v4"
        - **kwargs: Additional keyword arguments, same as APIRouter.get.
        """

        def decorator(func):
            @self.get(path, *args, **kwargs)
            @wraps(func)
            def html_route(*args, **kwargs) -> HTMLResponse:
                response = func(*args, **kwargs)
                context = {"request": kwargs["request"], **response}

                if hx_template and kwargs["request"].headers.get("HX-Request"):
                    return self.templates.TemplateResponse(hx_template, context)

                return self.templates.TemplateResponse(template, context)

            if enable_json_route:

                @self.get(
                    f"/{json_route_prefix}{path}",
                    *args,
                    **kwargs,
                    tags=[json_route_prefix.upper()],
                )
                @wraps(func)
                def json_route(*args, **kwargs):
                    response = func(*args, **kwargs)
                    return response

        return decorator
