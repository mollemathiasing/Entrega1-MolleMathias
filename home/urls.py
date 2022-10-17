from django.urls import path
from home import views

urlpatterns = [
    path ('', views.index, name = 'index'),
    path('view_user/', views.view_user, name = 'view_user'),
    path('input_user', views.input_user, name = 'input_user'),
]
