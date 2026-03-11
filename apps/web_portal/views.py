from django.shortcuts import render


def landing(request):
    return render(request, "web/landing.html")


def docs(request):
    return render(request, "web/docs.html")


def pricing(request):
    return render(request, "web/pricing.html")


def contact(request):
    return render(request, "web/contact.html")
