from django.urls import path
from .import views


urlpatterns = [
    path('', views.MoviesView.as_view(), name='home'),
    path('<slug:slug>/', views.MovieDatailView.as_view(), name='detail' ),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>/', views.ActorView.as_view(), name='actor_detail'),
]