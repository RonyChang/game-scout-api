from rest_framework.throttling import SimpleRateThrottle


class ApiClientRateThrottle(SimpleRateThrottle):
    scope = "api_client"

    def get_cache_key(self, request, view):
        # Placeholder key until API key auth is implemented.
        return self.cache_format % {"scope": self.scope, "ident": self.get_ident(request)}
