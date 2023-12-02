from django.urls import path

from . import views

app_name='web'

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login_usuario,name='loginusuario'),
    path('logout',views.logout_usuario,name='logoutusuario')
]