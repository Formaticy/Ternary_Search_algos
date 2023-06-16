from django.urls import path

from .views import element_search_d, extremum_search, first_page

urlpatterns = [
    path('first/', first_page),
    path('element_search/', element_search_d, name='element_search'),
    path('extremum_search/', extremum_search, name='extremum_search'),
]