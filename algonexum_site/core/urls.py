
from os import path
from .views import home
from algonexum_site.core import views

urlpatterns = [
    path('', home, name='home'),
    path('contact',views.contact, name ='contact'),
    path('about',views.about,name='about'),
    path('login',views.login, name='login'),
    path('register',views.register,name='register'),
    
]
