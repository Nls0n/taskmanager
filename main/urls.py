from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('aboutme', views.about, name='about'),
    path('create', views.create, name='create')
]
