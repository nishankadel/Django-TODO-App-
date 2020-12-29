from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('profile/', views.profile, name='profile'),
    path('list_todo/', views.list_todo, name='list_todo'),
    path('delete_todo/<int:id>', views.delete_todo, name='delete_todo'),
    path('update_todo/<int:id>', views.update_todo, name='update_todo'),
    path('search_todo/', views.search_todo, name='search_todo'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='todo/logout.html'), name='logout'),

]
