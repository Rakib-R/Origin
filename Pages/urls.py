from django.urls import path 
from .views import PostListView ,PostDetailView
from . import views

urlpatterns = [
    path('', views.index ,name="index"),
    path('about', views.about, name="about" ),
    path('listing/<int:listing_id>' , PostListView.as_view(),name='listing')
]
