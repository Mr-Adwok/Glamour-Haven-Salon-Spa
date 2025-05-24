from django.urls import path
from . import views


urlpatterns = [
    # path('login/',views.login_page , name = 'login'),
    path('api/sign-up/',views.signup_page, name = 'sign-up')

]