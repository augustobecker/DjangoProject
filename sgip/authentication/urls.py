from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("new-product/", views.new_product, name="new-product"),
	path("products/", views.display_products, name="products")
]