from django.http import HttpResponse

def indexSubdomain1(request):
    return HttpResponse("Subdomain 1")

def indexSubdomain2(request):
    return HttpResponse("Subdomain 2")
