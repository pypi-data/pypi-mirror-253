from collections import abc
from typing import Callable, Text, Mapping

from scrapgo.lib import select_kwargs, filter_params, find_function, curl2requests, assingles
from .base import UrlRenderAction, UrlPatternAction, FileAction, CurlAction
from .exceptions import *



class ReduceMixin:

    def get_action(self, name):
        for action in self.urlorders:
            if action.name == name:
                return action    

    def dispatch_response(self, action, **kwargs):
        if isinstance(action, CurlAction):
            command = kwargs.get('url')
            request_kwargs = curl2requests(command)
            for key in ['headers', 'cookies', 'proxies']:
                curlval = request_kwargs.get(key)
                cmnval = kwargs.get(key)
                if curlval is not None or cmnval is not None:
                    curlval = curlval or {}
                    curlval.update(cmnval or {})
                    request_kwargs[key] = curlval

            return self.fetch(refresh=action.refresh, delay=action.delay, **request_kwargs)

        method = action.method or ('post' if kwargs.get('data') else 'get')
    
        return self.fetch(
            method=method, delay=action.delay,
            ignore_status_codes=action.ignore_status_codes,
            allowable_status_codes=action.allowable_status_codes,
            refresh=action.refresh,
            force_refresh=action.force_refresh,
            only_if_cached=action.only_if_cached,
            expire_after=action.expire_after,
            **kwargs
        )

    @assingles
    def dispatch_renderer(self, action, prev_results, parent_response, context):
        if isinstance(action, UrlRenderAction):
            if urlrenderer := action.urlrenderer:
                return self.dispatch(
                    'urlrenderer', urlrenderer,
                    url=action.url, prev=prev_results, context=context, **context
                )
            elif isinstance(action.url, str):
                try:
                    next_url = context[action.url]
                except KeyError:
                    return action.url.format_map(context)
                else:
                    return next_url

            elif isinstance(action.url, Callable):
                return select_kwargs(action.url, prev=prev_results, context=context, **context)
            raise ValueError(f'{action.url}')

        elif isinstance(action, UrlPatternAction):
            if urlpattern_renderer := action.urlpattern_renderer:
                urlpattern = self.dispatch(
                    'urlpattern_renderer', urlpattern_renderer, pattern=action.urlpattern, prev=prev_results,
                    context=context, **context
                )
                if urlpattern is None:
                    raise UrlRendererError(f"{urlpattern_renderer} must return regex pattern of url, not {urlpattern}")
            else:
                urlpattern = action.urlpattern
            kwargs = {
                **action.as_kwargs(),
                'urlpattern': urlpattern
            }
            return self.parse_linkpattern(parent_response.content, **kwargs)
    
        elif isinstance(action, CurlAction):
            if command_renderer:= action.command_renderer:
                return self.dispatch(
                    'curlrenderer', command_renderer,
                    command=action.command,
                    prev=prev_results,
                    context=context,
                    **context
                )
            return action.command
        elif isinstance(action, FileAction):
            if path_renderer := action.path_renderer:
                return self.dispatch(
                    'path_renderer', path_renderer, path=action.path,
                    prev=prev_results, context=context, **context
                )
            return action.path
        else:
            raise CannotFindAction(f'{action} is not memeber of renderer action')

    @assingles
    def dispatch_payloader(self, action, prev_results, context):
        # if not hasattr(action, 'payloader') or not action.payloader:
        #     return {}
        
        # if isinstance(action.payloader, Text):
        #     if not hasattr(self, action.payloader):
        #         return action.payloader.format_map(context)
        
        # if isinstance(action.payloader, Mapping):
        #     for key, val in context.items():
        #         if key in action.payloader:
        #             action.payloader[key] = val
        #     return action.payloader

        if hasattr(action, 'payloader') or hasattr(action, 'payload'):        
            if payloader := action.payloader:
                return self.dispatch(
                    'payloader', payloader, payload=action.payload, 
                    prev=prev_results, context=context, **context
                )
            elif isinstance(action.payload, Text):
                # print(action.payload)
                return action.payload.format_map(context)
            elif isinstance(action.payload, bytes):
                return action.payload
            elif isinstance(action.payload, Mapping):
                payload = {k:v for k, v in action.payload.items()}
                for key, val in context.items():
                    if key in payload:
                        payload[key] = val
                return payload
        return {}
    

            
    def dispatch_fields(self, action, url):
        if not hasattr(action, 'fields'):
            return url
        url = filter_params(url, action.fields)
        return url

    def dispatch_headers(self, action):
        headers = self.get_headers()
        if hasattr(action, 'headers'):
            headers.update(action.headers or {})
        return headers
    
    def dispatch_cookies(self, action):
        cookies = self.get_cookies()
        if hasattr(action, 'cookies'):
            cookies.update(action.cookies or {})
        return cookies

    def dispatch_extractor(self, action, soup, data, response, prev_results, results_cache, context):
        extractset = {}
        if module := action.extractor:
            pat = r'^extract_(?P<ext>\w+)$'
            for g, func in find_function(module, pat):
                extracted = select_kwargs(
                    func,
                    response=response,
                    soup=soup,
                    data=data,
                    prev=prev_results,
                    results_set=results_cache, context=context, **context
                )
                extractset[g('ext')] = self.validate_extracted(extracted, func, soup)
        return extractset

    def dispatch_parser(self, action, response, extracted, soup, data,  prev_results, results_cache, context):
        results = self.dispatch(
            'parser', action.parser,
            response=response, parsed=extracted, soup=soup, data=data,
            prev=prev_results,
            results_set=results_cache, context=context, **context
        )

        def _reduce_parsed_type(parsed):
            if isinstance(parsed, tuple):
                row, ctx = parsed
                context.update(ctx)
                return row
            return parsed
        
        if isinstance(results, abc.Generator):
            return map(_reduce_parsed_type, results)
        else:
            return _reduce_parsed_type(results)
        
        


        # resultset = []

        # if isinstance(results, abc.Generator):
        #     for result in results:
        #         if isinstance(result, tuple):
        #             if len(result) != 2:
        #                 raise ParsedResultsError('Parsed results consist of two parts tuple: results, context.')
        #             res, ctx = result
        #             resultset.append((res, {**context, **ctx}))
        #         else:
        #             resultset.append((result, context))
        # else:
        #     if results is None:
        #         resultset.append(([], context))
        #     if isinstance(results, tuple):
        #         if len(results) != 2:
        #             raise ParsedResultsError('Parsed results consist of two parts tuple: results, context.')
        #         res, ctx = results
        #         resultset.append((res, {**context, **ctx}))
        #     else:
        #         resultset.append((results, context))

        # return resultset

            
    def dispatch_urlfilter(self, action, url, prev_results, context):
        if not hasattr(action, 'urlfilter'):
            return True

        return self.dispatch(
            'urlfilter', action.urlfilter,
            url=url, prev=prev_results, action=action, context=context, **context
        ) 

    def dispatch_response_filter(self, action, response, prev_results, context):
        if not hasattr(action, 'response_filter'):
            return True
        
        return self.dispatch(
            'response_filter', action.response_filter,
            response=response, prev=prev_results, action=action, context=context, **context
        )

    # def dispatch_referer(self, action, response):
    #     headers = self.get_headers()
    #     if not hasattr(action, 'referer'):
    #         return headers
        
    #     if action.referer and response:
    #         try:
    #             referer = response.crawler.responsemap[action.referer]
    #         except KeyError:
    #             raise CannotFindAction(f"An action named {action.referer} could not be found at urlorders.")
    #         else:
    #             headers['Referer'] = referer.url
    #     return headers

    def dispatch_compose(self, results_set):
        if hasattr(self, 'compose'):
            for action in self.urlorders:
                results_set.setdefault(action.name, [])
            composed = self.dispatch(
                'compose', self.compose,
                **results_set
            )
            return composed

    def dispatch_onfailure(self, action, exception, response, prev_results, context, **requests_kwargs):
        self.dispatch(
            'onfailure', action.onfailure,
            response=response,
            exception=exception,
            prev=prev_results,
            action=action,
            context=context,
            **context,
            **requests_kwargs
        )

    def dispatch_ignore_status_codes(self, action, response):
        if hasattr(action, 'ignore_status_codes'):
            ignore_codes =  action.ignore_status_codes or []
            return response.status_code in ignore_codes
        return False
    
    def dispatch_allowable_status_codes(self, action, response):
        if hasattr(action, 'allowable_status_codes'):
            alloable_codes = action.allowable_status_codes or []
            return response.status_code in alloable_codes
        return False

    def dispatch(self, type, func, *args, **kwargs):
        if callable(func):
            f = func
        elif isinstance(func, str):
            if hasattr(self, func):
                f = getattr(self, func)
            else:
                raise NotImplementedError(f"The method {func} is not implemented!")
        else:
            f = {
                'urlfilter': self.default_urlfilter,
                'response_filter': self.default_response_filter,
                'parser': self.default_parser,
                'urlrenderer': self.default_urlrenderer,
                'urlpattern_renderer': self.default_pattern_renderer,
                'breaker': self.default_breaker,
                'onfailure': self.onfailure,
                'payloader': self.default_payloader,
                'curlrenderer': self.default_curlrenderer,
                'path_renderer': self.default_path_renderer,
            }[type]

        return select_kwargs(f, *args, **kwargs)
    

    def default_urlfilter(self, url, **kwargs):
        return True

    def default_response_filter(self, response, **kwargs):
        return True

    def onfailure(self, exception, **kwargs):
        raise
    
    def default_breaker(self, response, **kwargs):
        return False

    def default_parser(self, response, prev, parsed, context, **kwargs):
        return prev, parsed
    
    def default_urlrenderer(self, url, response, **kwargs):
        yield url
    
    def default_curlrenderer(self, curl, resposne, **kwargs):
        return curl
    
    def default_path_renderer(self, path, response, **kwargs):        
        return path
        
    def default_pattern_renderer(self, pattern, resposne, **kwargs):
        return pattern
    
    def default_breaker(self, response, **kwargs):
        return False
    
    def default_payloader(self):
        yield