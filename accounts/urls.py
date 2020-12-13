from django.urls import path

from . import views

urlpatterns = [

    path('',views.register,name='register'),
    # path('homepage',views.loadcontent,name='loadcontent'),
    path('login',views.login,name='login'),
    # path('login/homepage',views.loadhome,name='home'),
    # path('login/assignment',views.status,name='status')
    # path("register", views.register, name="register"),
    # path("login",views.login, name="login"),
    # path("logout",views.logout,name="logout")
]