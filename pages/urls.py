from django.contrib import admin
from django.urls import path, include
from .views import promocode, profile, main, ex_product

app_name = 'pages'

urlpatterns = [
    path('', main, name='main'),
    path('promocode/', promocode, name='promocode'),
    path('profile/', profile, name='profile'),
    path('<int:prod_id>/', ex_product, name='ex_product'),
]
