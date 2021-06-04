from django.urls import path , include
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/',views.About.as_view(), name="about"),
    path('profile/',views.CustomerProfile.as_view(),name="profile_detail"),
    path('profile/<int:pk>/', views.CustomerProfileUpdate.as_view(),
         name="profile_update"),
    path('profile/<int:pk>/subscribe/', views.CustomerSubscribeUpdate.as_view(),
         name="profile_subscribe"),
    path('profile/<int:pk>/delete',
         views.CustomerProfileDelete.as_view(), name="profile_delete"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('profile/<int:pk>/order/new',
         views.OrderCreate.as_view(), name="order_create"),
    path('order/<int:pk>',
         views.OrderDetail.as_view(), name="order_detail"),
    path('order/<int:pk>/update/',
         views.OrderUpdate.as_view(), name="order_update"),
     
]
