from glob import glob
from dataclasses import dataclass
from types import ModuleType
from typing import Callable, Text



@dataclass
class BaseAction:
    name:str
    parser:Callable=None
    onfailure:Callable=None
    extractor:ModuleType=None
    refresh:bool=False
    force_refresh:bool=False
    only_if_cached:bool=False
    expire_after:int=None
    delay:int=None
    ignore_status_codes:list=None
    allowable_status_codes:list=None
    workers:int=None,
    bfo:bool=False,
    follow_each:bool=True
    pipeline:Callable=None
    urlfilter:Callable=None
    payload:str=None
    response_filter:Callable=None
    runtimes:int=None

    def __post_init__(self, *args, **kwargs):
        if not self.name:
            raise NotImplementedError("action name must be specified")

    def as_kwargs(self):
        return self.__dict__


@dataclass
class HttpAction(BaseAction):
    headers:dict=None
    cookies:dict=None
    payloader:Callable=None
    fields:list=None
    method:str=None



@dataclass
class UrlRenderAction(HttpAction):
    url:str = None
    urlrenderer:Callable=None

    def __post_init__(self, *args, **kwargs):
        if not (self.url or self.urlrenderer):
            raise NotImplementedError("an url or urlrenderer must be specified")
    


@dataclass
class UrlPatternAction(HttpAction):
    urlpattern:str=None
    urlpattern_renderer:Callable=None
    remove_duplicates:bool=None
    attrs:dict=None
    css_selector:str=None
    recursive:bool=False
    reverse:bool=False

    def __post_init__(self, *args, **kwargs):
        if not (self.urlpattern or self.urlpattern_renderer):
            raise NotImplementedError("urlpattern or urlpattern_renderer must be specified")


@dataclass
class FileAction(BaseAction):
    path:str=None
    path_renderer:Callable=None
    method:str='get'

    def __post_init__(self):
        if not (self.path or self.path_renderer):
            raise NotImplementedError("path or path_renderer must be specified")
        self._check_globpath()

    def _check_globpath(self):
        if '*' in self.path:
            self.path_renderer = self.path_renderer or (lambda: glob(self.path, recursive=True))



@dataclass
class CurlAction(BaseAction):
    command:str=None
    command_renderer:Callable=None

    def __post_init__(self):
        if not (self.command or self.command_renderer):
            raise NotImplementedError("command or command_renderer must be specified")



def urlrender(
    url=None, 
    urlrenderer=None,
    fields:list=None,
    payloader=None,
    payload=None,
    parser=None,
    extractor=None,
    onfailure=None,
    headers:dict=None,
    cookies:dict=None,
    method:str=None,
    refresh:bool=False,
    force_refresh:bool=False,
    only_if_cached:bool=False,
    expire_after:int=None,
    delay:int=None,
    ignore_status_codes:list=None,
    allowable_status_codes:list=None,
    follow_each:bool=False,
    workers:int=None,
    bfo:bool=False,
    pipeline:Callable=lambda *args, **kwargs: None,
    urlfilter:Callable=None,
    response_filter:Callable=None,
    runtimes:int=None,
    name:str=None):
    return UrlRenderAction(**locals())


def urlpattern(
    urlpattern:str=None,
    urlpattern_renderer=None,
    fields:list=None,
    payloader=None,
    parser=None,
    extractor=None,
    onfailure=None,
    remove_duplicates:bool=None,
    attrs:dict=None,
    css_selector:str=None,
    reverse:bool=False,
    headers:dict=None,
    cookies:dict=None, method:str=None,
    refresh:bool=False,
    force_refresh:bool=False,
    only_if_cached:bool=False,
    expire_after:int=None,
    delay:int=None,
    ignore_status_codes:list=None,
    allowable_status_codes:list=None,
    follow_each:bool=False,
    workers:int=None,
    bfo:bool=False,
    pipeline:Callable=lambda *args, **kwargs: None,
    urlfilter:Callable=None,
    response_filter:Callable=None,
    runtimes:int=None,
    name:str=None):
    return UrlPatternAction(**locals())


def curl(
    command:str=None,
    command_renderer=None,
    parser=None, extractor=None,
    onfailure=None,
    refresh:bool=False,
    force_refresh:bool=False,
    only_if_cached:bool=False,
    expire_after:int=None,
    delay:int=None,
    ignore_status_codes:list=None,
    allowable_status_codes:list=None,
    follow_each:bool=False,
    workers:int=None,
    bfo:bool=False,
    pipeline:Callable=lambda *args, **kwargs: None,
    urlfilter:Callable=None,
    response_filter:Callable=None,
    runtimes:int=None,
    name:str=None):
    return CurlAction(**locals())


def file(
    path:str=None,
    path_renderer=None,
    parser=None,
    onfailure=None,
    extractor=None,
    refresh:bool=False,
    force_refresh:bool=False,
    only_if_cached:bool=False,
    expire_after:int=None,
    delay:int=None,
    follow_each:bool=False,
    workers:int=None,
    bfo:bool=False,
    pipeline:Callable=lambda *args, **kwargs: None,
    response_filter:Callable=None,
    runtimes:int=None,
    name:str=None):
    return FileAction(**locals())
