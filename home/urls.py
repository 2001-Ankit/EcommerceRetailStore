from django.urls import path

from . import views
from .views import *
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('category/<slug>', Categories.as_view(), name='categories'),
    path('search',SearchView.as_view(),name='search'),
    path('product-detail/<slug>',DetailView.as_view(),name='product-detail'),
    path('reviews',views.review,name='reviews'),
    path('signup',views.signup,name='signup'),
    path('logout/',views.logout_view,name='logout'),
    path('add_to_cart/<slug>',views.add_to_cart,name='add_to_cart'),
    path('delete_cart/<slug>',views.delete_cart,name='delete_cart'),
    path('cart/',CartView.as_view(),name='cart'),
    path('remove/<slug>',remove_product,name='remove_product'),
    path('checkout/',CheckoutView.as_view(),name='checkout'),
    path('product-lists',ProductListView.as_view(),name='product-list'),
    path('wishlist/',WishView.as_view(),name='wishlist'),
    path('add_to_wishlist/<slug>',views.add_to_wishlist,name='add_to_wishlist'),
    path('remove_from_wishlist/<slug>',views.remove_form_wishlist,name='remove_from_wishlist')
]

