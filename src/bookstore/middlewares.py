from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class DarthVaderMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if (request.user.is_authenticated 
            and request.user.username == 'Darth Vader' 
            and request.method == 'POST' 
            and request.path == '/books/userbooks/'):
            return HttpResponse("You are not authorized to publish your work on this endpoint.")
