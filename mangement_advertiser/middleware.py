class ExtractUserIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_ip = request.META.get('HTTP_X_FORWARDED_FOR', None)
        
        if not user_ip:
            user_ip = request.META.get('REMOTE_ADDR', None)

        request.ip = user_ip

        response = self.get_response(request)
        return response
