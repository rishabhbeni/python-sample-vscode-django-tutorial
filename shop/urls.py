from django.urls import path
from .views import product_list
from .views import product_detail

app_name = 'shop'


urlpatterns = [
 path('', product_list, name='product_list'),
 path('<slug:category_slug>/', product_list,name='product_list_by_category'),
 path('<int:id>/<slug:slug>/', product_detail,name='product_detail'),


]
