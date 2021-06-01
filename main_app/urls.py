from django.urls import path , include
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/',views.About.as_view(), name="about"),
    path('profile/',views.CustomerProfile.as_view(),name="profile_detail"),
    path('profile/<int:pk>/', views.CustomerProfileUpdate.as_view(),
         name="profile_update"),
    path('profile/<int:pk>/delete',
         views.CustomerProfileDelete.as_view(), name="profile_delete"),
]
