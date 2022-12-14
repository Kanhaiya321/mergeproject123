from django.urls import path
from . import views
from django.contrib import admin
from django.views.generic.base import TemplateView
# from core.views import SignUpView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('signup/',views.signup,name='signup'),
    path('login/', views.login_view, name='login'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
]