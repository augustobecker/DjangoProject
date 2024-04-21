from django.urls import path, re_path
from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("products/", views.display_products, name="list-products"),
	re_path(r'^(?P<category>[^/]+)/new-product/$', views.new_product, name='new_product'),
	re_path(r'^(?P<category>[^/]+)/(?P<subcategory>[^/]+)/new-product/$', views.new_product, name='new_product_with_subcategory')
]
