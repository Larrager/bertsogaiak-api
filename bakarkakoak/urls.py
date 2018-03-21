from django.urls import path

from . import views

urlpatterns = [
    path('', views.BakarkakoaList.as_view(), name='bakarkakoak'),
    path('<uuid:pk>/', views.BakarkakoaDetail.as_view()),
]