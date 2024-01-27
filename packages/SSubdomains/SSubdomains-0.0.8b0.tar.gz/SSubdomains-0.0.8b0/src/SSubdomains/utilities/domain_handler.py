from SSubdomains.domain import Domain


def domain_handler(request):
    host = request.META.get('HTTP_HOST', '').split(':')
    if len(host) > 0:
        host = host[0]
    else:
        host = 'localhost'
    domain = Domain(full_domain=host)
    request.domain = domain
    return request