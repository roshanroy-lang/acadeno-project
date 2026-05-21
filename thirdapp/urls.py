from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='home'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/',views.logout_page,name='logout'),
    path('delete/<int:id>/',views.delete_task,name='delete'),
    path('update/<int:id>/',views.update_task,name='update')


]

