from django.urls import path

from apps.api_public.views import ApiRootView

urlpatterns = [
    path("", ApiRootView.as_view(), name="api-root"),
]
