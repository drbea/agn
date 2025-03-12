from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
  path("", views.product_list, name = "product_list"),
  path("all/", views.product_list, name = "product_list"),
  path("add/", views.add_product, name = "add_product"),
  path("detail/<int:product_id>/", views.product_detail, name = "product_detail"),
  path("filter/<int:category_id>/", views.filter_by_category, name = "filter_by_category"),
  path("add_to_cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
  # path("remove_from_cart/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
  path("cart/", views.cart_view, name="panier"),

  path('update_cart/', views.update_cart, name='update_cart'),
  path('remove_item_ajax/', views.remove_item_ajax, name='remove_item_ajax'),

  path("checkout/", views.checkout, name="checkout"),
  path("order_confirmation/", views.order_confirmation, name="order_confirmation"),


  path('payment/process/', views.process_payment, name='process_payment'),
  path('payment/payment_selection/', views.payment_selection, name='payment_selection'),

]
