import json
from collections import defaultdict, abc
from concurrent import futures

from scrapgo.core import SoupParser, RequestsBase, CachedRequests
from scrapgo.core.http import RequestsBase
from scrapgo.lib import pluralize, try2json

from .actions import resolve_link, ReduceMixin



class CrawlMixin(ReduceMixin, SoupParser):
    urlorders = None

    def crawl(self, _urlorders=None, _results=None, parent_response=None, _composed:dict=None, _context:dict=None, **kwargs):
        if _urlorders == []:
            return 

        action, *rest = _urlorders or self.urlorders
        _context = _context or kwargs
        _composed = _composed or defaultdict(list)

        if action.runtimes is not None:
            action.runtimes -= 1
            if action.runtimes < 0:
                return self.crawl(rest, _results, parent_response, _composed, _context)
        
        def build_requests():
            def __resolve(link):
                url = resolve_link(action, link, parent_response)
                return self.dispatch_fields(action, url)

            def _build_urls():
                links = self.dispatch_renderer(action, _results, parent_response, _context)
                for link in filter(None, links):
                    url = __resolve(link)
                    if self.dispatch_urlfilter(action, url, _results, _context) is False:
                        continue
                    yield url

            def _build_payloads():
                yield from self.dispatch_payloader(action, _results, _context)
                
            def __build_kwargs(url, payload):
                cookies = self.dispatch_cookies(action)
                headers = self.dispatch_headers(action)
                payload = payload or None
                kwargs = dict(url=url, headers=headers, cookies=cookies)
                if content_type := headers.get('Content-Type'):
                    if 'application/json' in content_type:
                        if isinstance(payload, (dict, list)):
                            payload = json.dumps(payload)
                kwargs['data'] = payload
                return kwargs

            for url in _build_urls():
                for payload in _build_payloads():
                    kwargs = __build_kwargs(url, payload)
                    yield kwargs
        
        def process_response(kwarg):
            def _retrieve(kw):
                try:
                    r = self.dispatch_response(action, **kw)
                except Exception as e:
                    self.dispatch_onfailure(action, e, parent_response, _results, _context, **kw)
                    raise
                else:
                    if self.dispatch_ignore_status_codes(action, r) is True:
                        return False
                    if not self.dispatch_response_filter(action, r, _results, _context):
                        return False
                    return r
                    
            def _parse(r):
                is_parsable = self._is_parsable(r)
                soup = self._load_soup(r.content) if is_parsable else r.content
                data = try2json(r)
                extracted = self.dispatch_extractor(action, soup, data, r, _results, _composed, _context)
                return self.dispatch_parser(action, r, extracted, soup, data, _results, _composed, _context)
            
            if (response:= _retrieve(kwarg)) is not False:
                return  _parse(response), response
        
        requests_kwargs = build_requests()
        max_workers = self.settings.get('REQUEST_MAX_WORKERS')

        if action.workers:
            with futures.ThreadPoolExecutor(min(action.workers, max_workers)) as excutor:
                processeds = excutor.map(process_response, requests_kwargs)
        else:
            processeds = map(process_response, requests_kwargs)


        for results, response in filter(None, processeds):
            if action.bfo is True:
                ret = results or _results
                if ret:
                    _composed[action.name] += pluralize(ret)
                    action.pipeline(records=ret, response=response, context=_context, commit=True)
                self.crawl(rest, ret, response, _composed, _context)

            if isinstance(results, abc.Iterator):
                for row in results:
                    if row is not None:
                        _composed[action.name].append(row)
                        action.pipeline(records=row, response=response, context=_context, commit=True)
                    self.crawl(rest, row, response, _composed, _context)
            else:
                if self._is_parsable(response):
                    if results:
                        _composed[action.name] += pluralize(results)
                        action.pipeline(records=results, response=response, context=_context, commit=True)
                    self.crawl(rest, results, response, _composed, _context)
                else:
                    action.pipeline(records=results, response=response, context=_context, commit=True)
                    self.crawl(rest, _results, parent_response, _composed, _context)
            

        if _urlorders is None:
            self.dispatch_compose(_composed)



class RequestsCrawler(CrawlMixin, RequestsBase):
    pass


class CachedRequestsCrawler(CrawlMixin, CachedRequests):
    pass
