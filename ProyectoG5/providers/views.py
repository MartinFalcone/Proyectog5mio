from django.shortcuts import render
from providers.models import Provider

# Create your views here.

def list_providers(request):
    list_providers = Provider.objects.all()
    context = {"list_providers":list_providers}
    return render(request, "list_providers.html", context = context)