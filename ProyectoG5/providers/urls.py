from django.urls import path
from providers.views import list_providers
urlpatterns = [
    path ("", list_providers, name = "list_providers")

]