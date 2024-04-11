#____________________________________________________________________  PRODUCTS/URLS.PY
from django.urls import path
from . import views

urlpatterns = [
    path('',views.product_list,name='product_list'),
    path('category/<int:category_id>/', views.product_category, name='product_category'),
    path('<int:product_id>/',views.product_detail,name='product_detail'),
    path('add/',views.product_add,name='product_add'),
    path('edit/<int:product_id>/',views.product_edit,name='product_edit'),
    path('delete/<int:product_id>/',views.product_delete,name='product_delete'),
]