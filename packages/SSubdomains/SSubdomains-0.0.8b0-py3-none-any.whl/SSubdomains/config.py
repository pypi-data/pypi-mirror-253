from django.conf import settings

SSUBDOMAINS_CONFIG = {

    "SUBDOMAIN_URLCONFS": {
        'www': 'Root.urls.www',
        '1.1': 'Root.subdomains1',
        '2': 'Root.subdomains2',
        # '2': 'Root.urls.subdomain2',
    },
    "ROLE_FIELD": "role",
    "ALLOWED_SUBDOMAINS_BY_ROLE": {
        "eee": ["1.1", "2"],
    },
    "DISABLED_SUBDOMAINS_BY_ROLE": {
        "admin": ["2"],
        "guest,none": ["2"],
    },
    #     number parts will exclude from subdomain
    "USE_MODEL": True,
    "MODEL": "SSubdomains.Subdomain",

}

for key in SSUBDOMAINS_CONFIG:
    if key not in settings.SSUBDOMAINS_CONFIG:
        SSUBDOMAINS_CONFIG[key] = settings.SSUBDOMAINS_CONFIG[key]
