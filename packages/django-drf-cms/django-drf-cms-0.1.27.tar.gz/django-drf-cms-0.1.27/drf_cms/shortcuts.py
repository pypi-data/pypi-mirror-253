from django.contrib.sites.models import Site

def get_current_site(request):
    return Site.objects.filter(domain=request.META.get('HTTP_ORIGIN')).first()