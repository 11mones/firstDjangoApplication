from django.urls import path
from .views import HomeView,Aboutview

urlpatterns = [
    path('', HomeView.as_view(),name = 'home'),
    path('aboutus', Aboutview.as_view(),name = 'aboutus'),
]