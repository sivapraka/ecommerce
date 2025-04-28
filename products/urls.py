from django.urls import path
from products import views

urlpatterns = [
    path('hello/', views.hello),
    path('allproducts', views.products_list),
    path('productdetails/<int:id>',views.products_detail),
    path('product',views.products_create),
    path('category', views.category_create),
    path('productcategory',views.products_category),
    path('test',views.test),
    path('error',views.test_error)
]