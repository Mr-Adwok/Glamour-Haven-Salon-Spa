from django.urls import path
from . import views


urlpatterns = [
    # path('login/',views.login_page , name = 'login'),
    path('api/sign-up/',views.signup_page, name = 'sign-up'),
    path('api/get-all-user/',views.get_all_user),
    path('api/get-user/<int:user_id>/',views.get_one_user)

]