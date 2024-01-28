# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import Iterable

import fastapi
from canonical.protocols import ITemplateService
from jinja2 import BaseLoader
from jinja2 import ChoiceLoader
from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import PackageLoader

from oauthx.lib.params import CurrentSettings


class TemplateService(ITemplateService):
    default_extensions: list[str] = [
        'jinja2.ext.i18n',
        'jinja_markdown.MarkdownExtension'
    ]
    default_loaders: list[BaseLoader] = [
        PackageLoader('oauthx.lib')
    ]
    default_dirs: list[str] = [
        'templates/oauthx'
    ]

    def __init__(
        self,
        env: Environment | None = None,
        request: fastapi.Request | None = None,
        settings: CurrentSettings | None = None,
        template_dirs: Iterable[str] | None = None,
        packages: Iterable[str] | None = None
    ) -> None:
        self.env = env or Environment(
            extensions=self.default_extensions,
            loader=ChoiceLoader([
                FileSystemLoader([*(template_dirs or []), *self.default_dirs]),
                *[PackageLoader(x) for x in packages or []],
                *self.default_loaders,
            ])
        )
        if env is None:
            self.env.install_null_translations() # type: ignore
        self.request = request
        self.settings = settings

    def clone(
        self,
        request: fastapi.Request,
        settings: CurrentSettings,
        template_dirs: Iterable[str] | None,
        packages: Iterable[str] | None,
    ) -> ITemplateService:
        return type(self)(
            request=request,
            settings=settings,
            template_dirs=template_dirs,
            packages=packages
        )

    def inject(
        self,
        template_dirs: Iterable[str] | None = None,
        packages: Iterable[str] | None = None,
    ) -> Any:
        def f(request: fastapi.Request, settings: CurrentSettings) -> None:
            templates = self.clone(
                request=request,
                settings=settings,
                template_dirs=template_dirs,
                packages=packages
            )
            setattr(request, 'templates', templates)
        return fastapi.Depends(f)

    async def get_template(self, template_name: str, using: str | None = None):
        return self.env.get_template(template_name)

    async def render_template(
        self,
        templates: list[str] | str,
        context: dict[str, Any]
    ) -> str:
        if not isinstance(templates, list):
            templates = [templates]
        t = self.env.select_template(templates)
        if self.request is not None:
            context.setdefault('request', self.request)
        if self.settings is not None:
            context.setdefault('settings', self.settings)
        return t.render(**context)
    
    async def select_template(self, templates: list[str], using: str | None = None):
        return self.env.select_template(templates)