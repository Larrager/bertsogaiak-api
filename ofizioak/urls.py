from django.urls import path

from . import views

urlpatterns = [
    path('', views.OfizioaList.as_view()),
    path('<uuid:pk>/', views.OfizioaDetail.as_view()),
]