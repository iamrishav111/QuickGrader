from django.urls import path

from assign_db import views

urlpatterns = [
    path('',views.loadhome,name='loadhome'),
    path('/submit',views.submit,name='submit'),
    path('/all',views.showsubmissions,name='showsubmissions')
    # path('login/homepage',views.loadhome,name='home')
    # path("register", views.register, name="register"),
    # path("login",views.login, name="login"),
    # path("logout",views.logout,name="logout")
]