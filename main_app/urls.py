from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('crystals/', views.crystals_index, name='index'),
    path('crystals/<int:crystal_id>/', views.crystals_detail, name='detail'),
    path('cats/<int:crystal_id>/add_cleansing/', views.add_cleansing, name='add_cleansing'),
    path('crystals/<int:crystal_id>/assoc_energy/<int:energy_id>/',views.assoc_energy, name='assoc_energy'),
    path('crystals/create/', views.CrystalCreate.as_view(), name='crystals_create'),
    path('crystals/<int:pk>/update/', views.CrystalUpdate.as_view(), name='crystals_update'),
    path('crystals/<int:pk>/delete/', views.CrystalDelete.as_view(), name='crystals_delete'),
    path('energys/', views.EnergyList.as_view(), name='energys_index'),
    path('energys/<int:pk>/', views.EnergyDetail.as_view(), name='energys_detail'),
    path('energys/<int:pk>/update/', views.EnergyUpdate.as_view(), name='energys_update'),
    path('energys/<int:pk>/delete/', views.EnergyDelete.as_view(), name='energys_delete'),
    path('energys/create/', views.EnergyCreate.as_view(), name='energys_create'),
    
    ]