from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    # path('categories/', views.categories_view, name="categories"),
    # path('check-out/', views.check_out_view, name="check-out"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('product/<slug>/', views.ProductDetailView.as_view(), name="product"),
    # path('cart/', views.cart_view, name='cart'),
    
]
