from django.urls import path
from .views import HomePageView,HomeView

urlpatterns = [
    path('', HomeView, name='home'),
]