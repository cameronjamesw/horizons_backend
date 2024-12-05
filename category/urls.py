from django.urls import path
from category import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
]