from . import views
from django.urls import path
from . import api


urlpatterns = [
    path('', api.materials, name="materials"),
    path('<slug:slug>/', api.material, name="material"),
    path('materials/<slug:slug>/snippets/', api.snippets, name="snippets"),
]