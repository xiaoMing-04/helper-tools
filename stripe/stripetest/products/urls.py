from .views import home, success, cancel
from django.urls import path


urlpatterns = [
    path("", home, name="home"),
    path("success/", success, name="success"),
    path("cancel/", cancel, name="cancel"),
]