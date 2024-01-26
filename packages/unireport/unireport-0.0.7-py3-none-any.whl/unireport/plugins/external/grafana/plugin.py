import base64
import uuid
from urllib.parse import parse_qs, urlparse

from jinja2 import Environment

from unireport.exceptions import RendererException
from unireport.logger import logger
from unireport.plugin import Plugin

from .api import GrafanaAPI


class GrafanaPlugin(Plugin):
    def __init__(
        self,
        api: GrafanaAPI,
        render_path_template="/render{path}",
        stub_dashboard_image_on_exception=False,
    ):
        super().__init__()

        self.api: GrafanaAPI = api
        self.render_path_template: str = render_path_template
        self.stub_dashboard_image_on_exception: bool = stub_dashboard_image_on_exception

    def setup(self, env: Environment):
        super().setup(env)

        env.globals["render_grafana_dashboard"] = self.render_grafana_dashboard

    def render_grafana_dashboard(self, url: str, **kwargs) -> str:
        logger.info(f"render grafana dashboard {url}, {kwargs}")

        result = urlparse(url)
        params = parse_qs(result.query)
        params.update(**kwargs)

        render_url = self.render_path_template.format(path=result.path)

        dashboard_id = "_".join(result.path.split("/")[-2:])
        dashboard_filename = (
            self.context.get_images_dir() / f"{dashboard_id}_{uuid.uuid1()}.png"
        )
        try:
            response = self.api.query_raw(render_url, params=params)
            response.raise_for_status()

            header = response.headers
            content_type = header.get("content-type")
            if content_type not in ("image/png",):
                raise RendererException(f"Invalid content-type {content_type}")

            with open(dashboard_filename, "wb") as f:
                f.write(response.content)
        except Exception as e:
            if not self.stub_dashboard_image_on_exception:
                raise

            logger.exception(
                f"failed to get dashboard request, use stub instead image - {e}"
            )
            with open(dashboard_filename, "wb") as f:
                f.write(base64.urlsafe_b64decode(self.context.error_image_base64))

        relative = dashboard_filename.relative_to(self.context.output_dir)
        return str(relative)
