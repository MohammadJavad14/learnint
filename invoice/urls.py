from cgitb import lookup
from . import views
from django.urls import path, include
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

invoices_router = routers.NestedDefaultRouter(
    router, 'users', lookup='users')
invoices_router.register(
    'invoices', views.InvoiceViewSet, basename='user-invoices')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(invoices_router.urls)),
    path('total_paid_invoices/', views.total_paid_invoices),
    path('average_invoices_price/', views.average_invoices_price),
]
