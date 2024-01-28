import os
from typing import Callable, Union, Text
from string import Formatter
from requests.models import Response
import listorm

from ..lib import fsave, fbasename, fjoin, select_kwargs






def pipe2file(save_to:Union[Callable, Text]=None, basedir='', commit:bool=False):
    '''
    pipe2file(RESULTS_PATH, "{titleName}({titleId})/thumbnail")
    :param save_to: lamabda response, **context: return dir, defaults to None
    '''
    
    def pipe(response:Union[Text, Response], context:dict, commit=commit, **_):
        if isinstance(response, Text):
            url = response
        elif isinstance(response, Response):
            url = response.url
        else:
            url = response
    
        if save_to:
            if isinstance(save_to, str):
                save_dir = save_to.format_map(context)
                _, ext = os.path.splitext(save_to)
                if ext:
                    save_path = fjoin(basedir, save_dir)
                else:
                    save_path = fjoin(basedir, save_dir, fbasename(url))
            elif isinstance(save_to, Callable):
                save_path = select_kwargs(save_to, response, **context)
                save_path = fjoin(basedir, save_path)
            else:
                raise ValueError(save_to)
        else:
            save_path = fjoin(basedir, fbasename(url))

        if commit is True:
            fsave(response.content, save_path)

        return save_path

    return pipe