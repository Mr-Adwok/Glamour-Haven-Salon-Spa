from django.urls import path
from . import views


urlpatterns = [
    path('book-appointment/',views.book_appointment),
    path('all_appointment/',views.all_appoinment)
]