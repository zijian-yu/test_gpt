from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.gene_search, name='gene_search'),
    path('gene/<str:gene_id>/', views.gene_detail, name='gene_detail'),
    path('portal/<str:portal_name>/', views.portal, name='portal'),
]
