from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('tours/', views.ToursListlView.as_view(), name='tours'),
    path('travel-companies/', views.TravelCompaniesListlView.as_view(), name='travel-companies'),
    path(r'travelcompanies/(<pk>)', views.TravelCompaniesDetailView.as_view(), name='travelcompanies-detail'),
    path(r'tours/(<pk>', views.TourDetailView.as_view(), name='tours-detail'),
]
