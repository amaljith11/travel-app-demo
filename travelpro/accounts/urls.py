from . import views
from django.urls import path



urlpatterns = [
    path('register',views.account,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]