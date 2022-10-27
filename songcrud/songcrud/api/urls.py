from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.SongAPIView.as_view()),
    path('songs/<int:pk>/', views.SongDetailsAPIView.as_view()),
    path('artistes/', views.ArtisteAPIView.as_view()),
    path('lyrics/', views.LyricAPIView.as_view())
]