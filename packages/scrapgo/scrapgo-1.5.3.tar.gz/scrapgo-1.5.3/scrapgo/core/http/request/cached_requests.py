import requests_cache
from requests import PreparedRequest

from scrapgo.lib.module import select_kwargs

from .base import RequestsBase


class CachedRequests(RequestsBase):
    cached_session_params = [
        'backend', 'key_fn', 'ignored_parameters', 'match_headers', 'stale_if_error', 'filter_fn', 'cache_control', 'allowable_codes', 'allowable_methods',
        'always_revalidate', 'expire_after', 'urls_expire_after',
    ]
    cached_request_params = [
        'refresh', 'only_if_cached', 'expire_after', 'force_refresh ',
    ]

    def load_session(self):
        return self.apply_settings(
            requests_cache.CachedSession,
            prefix='REQUEST_CACHE_',
            allowed_params=self.cached_session_params
        )
    
    def delete_cache(self, **requests_kwargs):
        if not requests_kwargs.get('request'):
            preq = PreparedRequest()
            select_kwargs(preq.prepare, **requests_kwargs)
            requests_kwargs['request'] = preq
        key = self.session.cache.create_key(**requests_kwargs)


    def fetch(self, *args, **kwargs):
        allowed_params = self.request_params + self.cached_request_params
        return super().fetch(*args, allowed_params=allowed_params, **kwargs)