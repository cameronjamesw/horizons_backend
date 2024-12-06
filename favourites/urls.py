from django.urls import path
from favourites import views

urlpatterns = [
    path('favourites/', views.FavouriteList.as_view()),
]