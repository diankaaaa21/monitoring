from django.conf import settings
from django.shortcuts import redirect


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if not hasattr(request, "user"):
            print("request.user not found. Middleware s executing too early.")
            return self.get_response(request)

        if not request.user.is_authenticated and request.path not in settings.LOGIN_URL:
            return redirect(settings.LOGIN_URL)

        return self.get_response(request)
