from django.urls import path
from .views import HomePageView,HomeView,togaraklarsingle_View

urlpatterns = [
    path('', HomeView, name='home'),
    path('togaraklar/<str:slug>/',togaraklarsingle_View, name='togaraklarsingle' ),
]