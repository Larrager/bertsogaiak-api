from django.urls import path

from . import views

urlpatterns = [
    path('', views.OfizioaList.as_view(), name='ofizioak'),
    path('<uuid:pk>/', views.OfizioaDetail.as_view()),
]