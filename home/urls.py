from django.urls import path
from home import views

urlpatterns = [
    path ('', views.index, name = 'index'),
    path ('about/', views.acerca_de_mi, name = 'acerca_de_mi'),
    path('view_servs/', views.ViewServs.as_view(), name = 'view_servs'),
    path('input_servs/', views.InputServs.as_view(), name = 'input_servs'),
    path('edit_servs/<int:pk>', views.EditServs.as_view(), name = 'edit_servs'),    
    path('delete_servs/<int:pk>', views.DeleteServs.as_view(), name = 'delete_servs'),
    path('view_serv/<int:pk>', views.ViewServ.as_view(), name = 'view_serv'),                      
]
