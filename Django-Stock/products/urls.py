from django.urls import path
from . import views

urlpatterns = [
    path("", views.products_index, name="products_index"),
    path('create', views.products_create, name='products_create'),
    path('edit/<int:pk>', views.products_update, name='products_edit'),
    path('deleted', views.deleted, name='product_deleted'),
    path('delete/<int:pk>', views.products_delete, name='products_delete'),
]
