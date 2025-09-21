from django.urls import path

from book import views

urlpatterns = [
    # Category
    path('categories/', views.CategoryListCreate.as_view()),
    path('categories/<int:pk>/', views.CategoryDestroyUpdateRetrieve.as_view()),

    # Printed Book
    path('printed-books/', views.PrintedBookListCreate.as_view()),
    path('printed-books/<int:pk>/', views.PrintedBookDestroyUpdateRetrieve.as_view()),

    # Audio Book
    path('audio-books/', views.AudioBookListCreate.as_view()),
    path('audio-books/<int:pk>/', views.AudioBookDestroyUpdateRetrieve.as_view()),
]
