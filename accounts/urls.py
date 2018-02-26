from django.urls import path, include

from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('input/', views.input, name='input'),
    path('registration/', views.registration, name='registration'),
    path('<email>/<key>', views.confirm_email, name='confirm_email'),
]