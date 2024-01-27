from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from SSubdomains.utilities.ip_checker import is_ip_in_range
from SSubdomains.utilities.domain_handler import domain_handler

user_model = get_user_model()


class SubdomainManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    #     check if the user allowed to access the subdomain

    def is_allowed(self, request):
        request = domain_handler(request)
        domain = request.domain
        user = request.user
        if not user.is_authenticated:
            user_role = "none"

        else:
            user_role = getattr(user, settings.SSUBDOMAINS_CONFIG["ROLE_FIELD"])
            if user_role is None:
                user_role = "none"

        try:
            qs = self.get(
                Q(subdomain=domain.subdomain)
                & Q(Q(base_domain=domain.base_domain) | Q(base_domain="*"))
            )
        except :
            return (False,"redirect")
        # check if is active
        if not qs.is_active:
            raise Exception("Subdomain Does Not Active")

        if qs.allow_none == True and user_role == "none":
            return True

        # check if the user is allowed to access the subdomain by role
        if qs.included_by_role and user_role in qs.included_role.split(","):
            return True

        # check if the user is allowed to access the subdomain by group
        if qs.included_by_groups and user.groups.filter(id__in=qs.included_groups.all()).exists():
            return True
        # check if the user is allowed to access the subdomain by user

        if qs.included_by_users and user in qs.included_users.all():
            return True

            # check if the user is allowed to access the subdomain by ip
        ip_range_from = qs.included_ip_range_from
        ip_range_to = qs.included_ip_range_to
        # user ip
        ip = request.META.get('REMOTE_ADDR')
        if is_ip_in_range(ip, ip_range_from, ip_range_to):
            return True

        # else:
        if qs.excluded_by_role and user_role in qs.excluded_role.split(","):
            return False
        # check if the user is allowed to access the subdomain by group
        if qs.excluded_by_groups and user.groups.filter(id__in=qs.excluded_groups.all()).exists():
            return False
        # check if the user is allowed to access the subdomain by user

        if qs.excluded_by_users and user in qs.excluded_users.all():
            return False
        # check if the user is allowed to access the subdomain by ip
        excluded_ip_range = qs.excluded_ip_range

        ip = request.META.get('REMOTE_ADDR')

        if excluded_ip_range.exists():
            ip_range_from = excluded_ip_range.excluded_ip_range_from
            ip_range_to = excluded_ip_range.excluded_ip_range_to
            if is_ip_in_range(ip, ip_range_from, ip_range_to):
                return False
        return qs.default_access
