from django.conf import settings
from django.db.models import Q

from SSubdomains.models import Subdomain
from SSubdomains.utilities.domain_handler import domain_handler
from django.apps import apps

def base_handler( request):
    request = domain_handler(request)
    domain = request.domain



    if domain.subdomain in settings.SSUBDOMAINS_CONFIG["SUBDOMAIN_URLCONFS"]:
        request.urlconf = settings.SSUBDOMAINS_CONFIG["SUBDOMAIN_URLCONFS"][domain.subdomain]
        print("point exit 0")
    else:


        if not settings.SSUBDOMAINS_CONFIG["USE_MODEL"] :
            request.urlconf = settings.ROOT_URLCONF
            print("point exit 1")
            return request

        try:
            model = settings.SSUBDOMAINS_CONFIG["MODEL"]
            Subdomain_Class = apps.get_model(model.split(".")[0], model.split(".")[1])
            subdomain = Subdomain_Class.objects.get(
                Q(subdomain=domain.subdomain) & Q(is_active=True)
                & Q(Q(base_domain=domain.base_domain) | Q(base_domain="*"))
            )
            print("subdomain:", subdomain)
            request.urlconf = subdomain.urlconf
        except Subdomain.DoesNotExist:
            request.urlconf = settings.ROOT_URLCONF


    return request