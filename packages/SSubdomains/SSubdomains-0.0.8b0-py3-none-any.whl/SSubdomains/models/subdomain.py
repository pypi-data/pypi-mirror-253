from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import models
from django.utils.translation import gettext_lazy as _
from SSubdomains.models.subdomain_manager import SubdomainManager

user_model = get_user_model()


class SubdomainBase(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64,
                            unique=True,
                            null=True, blank=True,
                            default="Test Subdomain")
    subdomain = models.CharField(max_length=255, unique=True)
    base_domain = models.CharField(max_length=255, default="*", null=False, blank=False, verbose_name=_("Base Domain"),
                                   help_text=_("Leave * for all domains"))
    created_at = models.DateTimeField(auto_now_add=True)
    urlconf = models.CharField(max_length=255, null=False, blank=False, default=settings.ROOT_URLCONF)
    last_update = models.DateTimeField(null=True, blank=True)
    # when user is not authenticated or not in role
    allow_none = models.BooleanField(default=True, verbose_name=_("Allow None"),
                                     help_text=_("Allow None Role Access"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"),
                                    help_text=_("Is This Subdomain Active"))
    default_access = models.BooleanField(default=False, verbose_name=_("Default Access"),
                                         help_text=_("Default Access For This Subdomain If No Other Access Is Set"))

    #  settings access Part
    excluded_by_groups = models.BooleanField(default=False, verbose_name=_("Excluded By Groups"),
                                             help_text=_("Deny By Groups is Active For This Subdomain or Not"),
                                             blank=True
                                             )
    excluded_by_users = models.BooleanField(default=False, verbose_name=_("Excluded By Users"),
                                            help_text=_("Deny By Users is Active For This Subdomain or Not"))
    excluded_by_role = models.BooleanField(default=False, verbose_name=_("Excluded By Role"),
                                           help_text=_("Deny By Role is Active For This Subdomain or Not"))
    excluded_by_ip_range = models.BooleanField(default=False, verbose_name=_("Excluded By IP Range"),
                                               help_text=_("Deny By IP Range is Active For This Subdomain or Not"))

    # access Part
    excluded_groups = models.ManyToManyField(Group, related_name="excluded_groups_subdomains",
                                             help_text=_("Groups Denied Access to this Subdomain"),
                                             blank=True
                                             )
    excluded_users = models.ManyToManyField(user_model, related_name="excluded_users_subdomains", blank=True,
                                            help_text=_("Users Denied Access to this Subdomain"))

    excluded_role = models.TextField(max_length=255, null=True, blank=True, default="",
                                     verbose_name=_("Roles Excluded"),
                                     help_text=_(
                                         "Roles Denied Access to this Subdomain If More Than One Role Separate Them With Comma")
                                     )
    excluded_ip_range_from = models.GenericIPAddressField(max_length=255, null=True, blank=True, default="",
                                                          verbose_name=_("IP Range Denied From"),
                                                          help_text=_("IP Range Denied From")
                                                          )
    excluded_ip_range_to = models.GenericIPAddressField(max_length=255, null=True, blank=True, default="",
                                                        verbose_name=_("IP Range Denied To"),
                                                        help_text=_("IP Range Denied To")
                                                        )
    #  allow access settings
    included_by_groups = models.BooleanField(default=False, verbose_name=_("Included By Groups"),
                                             help_text=_("Allow By Groups is Active For This Subdomain or Not"))
    included_by_users = models.BooleanField(default=False, verbose_name=_("Included By Users"),
                                            help_text=_("Allow By Users is Active For This Subdomain or Not"))

    included_by_role = models.BooleanField(default=False, verbose_name=_("Included By Role"),
                                           help_text=_("Allow By Role is Active For This Subdomain or Not"))

    included_by_ip_range = models.BooleanField(default=False, verbose_name=_("Included By IP Range"),
                                               help_text=_("Allow By IP Range is Active For This Subdomain or Not"))

    # included_by_groups, included_by_users, included_by_role, included_by_ip_range
    # excluded_by_groups, excluded_by_users, excluded_by_role, excluded_by_ip_range

    #  allow access

    included_groups = models.ManyToManyField(Group, related_name="included_groups_subdomains", blank=True,
                                             help_text=_("Groups Allowed Access to this Subdomain"))
    included_users = models.ManyToManyField(user_model, related_name="included_users_subdomains", blank=True,
                                            help_text=_("Users Allowed Access to this Subdomain"))
    included_role = models.TextField(max_length=255, null=True, blank=True, default="",
                                     verbose_name=_("Roles Included"),
                                     help_text=_(
                                         "Roles Allowed Access to this Subdomain If More Than One Role Separate Them With Comma")
                                     )
    included_ip_range_from = models.GenericIPAddressField(max_length=255, null=True, blank=True, default="",
                                                          verbose_name=_("IP Range Allowed From"),
                                                          help_text=_("IP Range Allowed From")
                                                          )
    included_ip_range_to = models.GenericIPAddressField(max_length=255, null=True, blank=True, default="",
                                                        verbose_name=_("IP Range Allowed To"),
                                                        help_text=_("IP Range Allowed To")
                                                        )

    objects = SubdomainManager()

    def __str__(self):
        return self.name + " " + self.subdomain + "." + self.base_domain

    class Meta:
        verbose_name_plural = _("SSubdomains")
        verbose_name = _("SSubdomain")
        unique_together = ('base_domain', 'subdomain')
        abstract = True


class Subdomain(SubdomainBase):
    class Meta:
        verbose_name_plural = _("Subdomains")
        verbose_name = _("Subdomain")
        unique_together = ('base_domain', 'subdomain')