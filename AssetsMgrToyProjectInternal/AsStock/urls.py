from django.urls import path
from . import views

urlpatterns = [
    path('stk-kdx-volume/',views.stk_kdx_volume,name='stk_kdx_volume'), #  kdx open api url
    path('stock-volume-page/',views.stock_volume_page,name='stock_volume_page'), # stock trading volume page
]