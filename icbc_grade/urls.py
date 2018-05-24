"""icbc_grade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from judge import views as jud
from pub import views as p
from django.views.generic.base import RedirectView

urlpatterns = [

    url(r'^$', p.index, name='index'),
    url(r'^admin', admin.site.urls),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'static/favicon.ico')),
    url(r'ajax_submit', jud.ajax_submit),
    url(r'ajax_reload', jud.ajax_reload),

    url(r'^judge/$', jud.index, name='judge'),

    url(r'^login', jud.login, name='login'),
    url(r'^logout', jud.logout, name='logout'),
    # 展示
    url(r'^showgrade/(\d+)', p.showgrade, name='showgrade'),
    # 查看数据
    url(r'^showgrade/ajax_search', p.ajax_search, name='ajax_search'),
    url(r'^showgrade/ajax_ave', p.ajax_ave, name='ajax_ave'),
    url(r'^list', p.list, name='list'),
    url(r'^sort', p.sort, name='sort'),
    # 测试母版url
    url(r'^base', p.base, name='base'),
    # url(r'start_server_script/$', jud.start_server_script)

]
