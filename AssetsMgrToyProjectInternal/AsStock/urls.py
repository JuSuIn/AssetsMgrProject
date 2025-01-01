from django.urls import path
from . import views

urlpatterns = [
    # path('stk-kdx-volume/',views.stk_kdx_volume,name='stk_kdx_volume'), #  kdx open api url
    path('stk_kospi_dd_volume/',views.stk_kospi_dd_volume,name='stk_kospi_dd_volume'),#KRX open api kospi url
    path('stk_kosdaq_dd_volume/',views.stk_kosdaq_dd_volume,name='stk_kosdaq_dd_volume'), #KRX open api Kosdaq url
    #path('stock-volume-page/',views.stock_volume_page,name='stock_volume_page'), # stock trading volume page
]