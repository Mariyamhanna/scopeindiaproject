from .views import *
from django.urls import path  # type: ignore 
urlpatterns = [
    path('home',home),
    path('courses',courses),
    path('about',about),
    path('faq',faq),
    path('contact',contact),
    path('register',register_page, name='register'),
    path('thankyou',thankyou, name='thankyou'),
    path('login',login, name='login'),
    path('profile',profile, name='profile'),
    path('delete-profile', delete_profile, name='delete_profile'),
    path('logout/',logout_view, name='logout'),
    path('logout', logout, name='logout')

]
