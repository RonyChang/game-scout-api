from django.urls import path

from apps.web_portal import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("docs/", views.docs, name="docs"),
    path("pricing/", views.pricing, name="pricing"),
    path("contact/", views.contact, name="contact"),
]
