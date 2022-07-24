from django.urls import path
from .views import (
  FiscaliaListView,
  FiscaliaDetailView,
)

urlpatterns = [
  path('', FiscaliaListView.as_view(), name = 'fiscalia-list'),
  path('<int:pk>', FiscaliaDetailView.as_view(), name = 'fiscalia-detail'),
]