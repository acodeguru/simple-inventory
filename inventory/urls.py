from django.urls import path

from inventory import views_page
from . import views

urlpatterns = [
    path('api/', views.InventroyOverview, name="inventory-overview"),
    path('api/inventory/', views.inventoryList, name="inventory-api-list"),
    path('api/inventory/<str:pk>/', views.inventoryDetail, name="inventory-api-detail"),
    path('api/inventory-update/<str:pk>/', views.inventoryUpdate, name="inventory-api-update"),
    path('api/inventory-delete/', views.inventoryDelete, name="inventory-api-delete"),
    path('api/inventory-create/', views.inventoryCreate, name="inventory-api-create"),
    
    path('inventory/', views_page.inventoryList, name="inventory-page-list"),
    path('inventory/<str:pk>/', views_page.inventoryDetail, name="inventory-page-detail"),

  ]