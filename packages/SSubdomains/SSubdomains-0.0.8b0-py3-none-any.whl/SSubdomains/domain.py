from django.conf import settings


class Domain(object):
    #     create two fields full_domain,subdomain
    def __init__(self, full_domain: str):
        self.full_domain = full_domain
        #        check if the domain is localhost for testing or when running locally for production but use proxy

        if full_domain.endswith("localhost"):
            self.base_domain = "localhost"
            if len(full_domain.split(".")) > 1:
                self.subdomain = full_domain.replace(".localhost", "")
            else:
                self.subdomain = None

        #         when the domain is not localhost
        else:

            # exclude the last two parts of the domain
            self.subdomain = ".".join(
                full_domain.split(".")[:settings.SSUBDOMAINS_CONFIG["MAIN_DOMAIN_PARTS"] * -1])
            self.base_domain = ".".join(
                full_domain.split(".")[-1 * settings.SSUBDOMAINS_CONFIG["MAIN_DOMAIN_PARTS"]:])

        # base domain
