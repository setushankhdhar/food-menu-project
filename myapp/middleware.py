import time
from django.http import HttpResponseForbidden
class logMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        #process before
        print(f'[middleware] request path:{request.path}')
        response  = self.get_response(request)
        #process after view
        print(f'[middleware] response status:{response.status_code}')
        return response

class TimerMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        start = time.time()
        response = self.get_response(request)
        duration = time.time() - start
        print(f'[middleware] request took:{duration:.2f} seconds. ')
        return response

class BlockIPMiddleware:
    
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        blocked_IP = []
        ip = request.META.get("REMOTE_ADDR")
        if ip in blocked_IP:
            return HttpResponseForbidden("Your IP is blocked!")
        return self.get_response(request)
