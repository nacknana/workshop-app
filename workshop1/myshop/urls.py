
from django.urls import path
from myshop import views


urlpatterns = [
    path('', views.products, name='products'),
    path('products/<int:pk>/', views.productspk, name='productspk'),
    path('productdetail/<int:pk>/', views.product_detail, name='productdetail'),
    path('categories', views.categories, name='categories'),
    path('contact', views.contact, name='contact'),
    path('login-signup', views.login_or_regis_view, name='signinup'),

    path('logout', views.logout_view, name='logout'),

]
