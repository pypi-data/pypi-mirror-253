from django.conf import settings
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

from SSubdomains.middleware.handler import base_handler
from SSubdomains.models import Subdomain

from SSubdomains.utilities.domain_handler import domain_handler


class SubdaomainsManagerMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request = base_handler(request)
        request = domain_handler(request)

        role_field = settings.SSUBDOMAINS_CONFIG["ROLE_FIELD"]

        if request.user.is_authenticated and getattr(request.user, role_field) is not None:
            user_role = getattr(request.user, role_field)
        else:
            user_role = "none"

        if type(Subdomain.objects.is_allowed(request)) == bool:
            return self.get_response(request)
        elif type(Subdomain.objects.is_allowed(request)) == tuple:
            if Subdomain.objects.is_allowed(request)[1] == "redirect":

                return  self.get_response(request)
                return redirect(to="https://www.google.com")
            else:
                return self.get_response(request)
        else:
            return HttpResponseForbidden(
                f"Access denied for {request.domain.base_domain} domain for {user_role} role \nError code E103", )
