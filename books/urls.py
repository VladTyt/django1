from django.urls import path, re_path

from . import views

urlpatterns = [
    # post views
    re_path(r'^login/$', views.user_login, name='login'),
    re_path(r'^register/$', views.register, name='register')
]