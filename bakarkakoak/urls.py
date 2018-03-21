from django.urls import path

from . import views

urlpatterns = [
    path('', views.BakarkakoaList.as_view()),
    path('<uuid:pk>/', views.BakarkakoaDetail.as_view()),
]