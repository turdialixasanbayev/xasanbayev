class HostBasedRoutingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(":")[0]

        if host == "admin.xasanbayev.uz":
            request.urlconf = "config.admin_urls"
        else:
            request.urlconf = "config.urls"

        return self.get_response(request)
