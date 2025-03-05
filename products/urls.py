from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
  path("", views.product_list, name = "product_list"),
  path("all/", views.product_list, name = "product_list"),
  path("add/", views.add_product, name = "add_product"),

  path("detail/<int:product_id>/", views.product_detail, name = "product_detail"),
  path("filter/<int:category_id>/", views.filter_by_category, name = "filter_by_category"),

]
