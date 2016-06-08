"""urlviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from createviewapp.views import index_view
from createviewapp.views import portfolio_view
from createviewapp.views import summers_page
from createviewapp.views import summers_birthday_photos
from createviewapp.views import summers_blowing_out_candles



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view),
    url(r'^portfolio$', portfolio_view),
    url(r'^portfolio/summer$', summers_page),
    url(r'^portfolio/summer/birthday$', summers_birthday_photos),
    url(r'^portfolio/summer/birthday/cake$', summers_blowing_out_candles)






]
