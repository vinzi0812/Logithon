from django.urls import path
from .views import  RouteView, CostView, DurationView, CarbonEmissionView

urlpatterns = [
    path('routes/', RouteView.as_view(), name='routes'),
    path('cost/', CostView.as_view(), name='cost'),
    path('duration/', DurationView.as_view(), name='duration'),
    path('emission/', CarbonEmissionView.as_view(), name='carbon-emission'),
]