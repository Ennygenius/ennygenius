from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('portfolio.html', views.portfolio, name='portfolio'),
    path('home.html', views.home, name='home'),

]