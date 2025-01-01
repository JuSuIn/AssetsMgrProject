from django.shortcuts import render
from django.http import JsonResponse
import requests
from .Apis.krx_kospi_dd_api import get_stk_kospi_dd_volume
from .Apis.krx_ksq_dd_api   import get_stk_kosdaq_dd_volume


#KRX open api url
# def get_stk_kdx_volume():
#     basDd="20241230"
    
#     # 원래 코드 
#     #url = "http://data-dbg.krx.co.kr/svc/apis/idx/kospi_dd_trd"+f"basDd={ basDd }"
#     #api_key ="30CC14A01CA34602AC741210E107A999C5D167B6"
    
#     url = "http://data-dbg.krx.co.kr/svc/sample/apis/idx/kospi_dd_trd?"+f"basDd={ basDd }"
#     api_key ="74D1B99DFBF345BBA3FB4476510A4BED4C78D13A"
    
#     params = {
#        "Authorization": f"Bearer {api_key}"
#     }
    
#     # get request json data
#     response = requests.get(url, params=params)
#     print(response.status_code);
    
#     # Event processing related to authentication key connection 
#     if response.status_code == 401:
#         return JsonResponse({"error" : "인증 오류 API키를 확인해주세요"}, status=401)   
#     elif response.status_code == 200:
#         data = response.json()
#         return data
#     else:
#         return {"error" : "Failed to get data"}
    
 # stock KRX return view   
# def stk_kdx_volume(request):
#     volumn_data = get_stk_kdx_volume()
    
#     return JsonResponse(volumn_data)

#KRX open api kospi url
#코스피 시리즈 지수의 시세정보를 제공(일별)에 대해 해당하는 api
def stk_kospi_dd_volume(request):
    volumn_data = get_stk_kospi_dd_volume()
    
    return JsonResponse(volumn_data)

#KRX open api Kosdaq url
#코스닥시장에 상장되어 있는 주권의 매매정보 제공 api
def stk_kosdaq_dd_volume(request):
    volume_data= get_stk_kosdaq_dd_volume()
    
    return JsonResponse(volume_data)

# View that renders the stock trading volume page
def stock_volume_page(request):
    return render(request,'AsStock/stock_volume.html')
    








