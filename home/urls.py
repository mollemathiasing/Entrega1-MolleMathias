from django.urls import path
from home import views

urlpatterns = [
    path ('', views.index, name = 'index'),
    path('view_user/', views.ViewUser.as_view(), name = 'view_user'),
    path('input_user/', views.InputUser.as_view(), name = 'input_user')
]
