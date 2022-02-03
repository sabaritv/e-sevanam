
from django.urls import path

from manageapp1 import views, admin_views

urlpatterns = [
    path('', views.home,name='home'),
    path('login_view/', views.login_view, name='login_view'),
    path('index', views.index, name="index"),
    path('table', views.table, name="table"),
    path('gov', views.gov, name='gov'),
    path('admin_home', views.index, name='admin_home'),
    path('govregister',admin_views.gov_add,name='govregister'),

]
