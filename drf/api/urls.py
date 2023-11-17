from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_urls, name="api_urls"),
    path('listing/', views.listing, name='listing'),
    path('Details/<str:pk>/', views.Details,name="Details"),
    path('create/', views.create, name="create"),
    path('update/<str:pk>/', views.update, name="update"),
    path('delete/<str:pk>/',views.delete, name="delete")
]

