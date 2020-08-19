"""needy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

from api.views import Offers, Viewpost

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("api.urls")),
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("login", TemplateView.as_view(template_name="login.html"), name="login"),
    path("offers", Offers.as_view(), name="offers"),
    path("post", TemplateView.as_view(template_name="post.html"), name="post"),
    path("profile", TemplateView.as_view(template_name="profile.html"), name="profile"),
    path("register", TemplateView.as_view(template_name="register.html"), name="register"),
    path("viewpost", Viewpost.as_view(), name="viewpost"),
    path("viewpost/<int:id>", Viewpost.as_view(), name="viewpost"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
