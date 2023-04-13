from django.urls import path
#from myapp.views import Login,Signup, logout, Index, Home ,Post,songrecomm
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]