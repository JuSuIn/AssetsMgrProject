from django.shortcuts import render
from django.http import JsonResponse
import requests


#KRX open api url
def get_stk_kdx_volume():
    basDd="20241230"
    url = "http://data-dbg.krx.co.kr/svc/sample/apis/idx/kospi_dd_trd?"+f"basDd={ basDd }"
    api_key ="74D1B99DFBF345BBA3FB4476510A4BED4C78D13A"
    
    params = {
       "Authorization": f"Bearer {api_key}"
    }
    
    # get request json data
    response = requests.get(url, params=params)
    print(response.status_code);
    
    # Event processing related to authentication key connection 
    if response.status_code == 401:
        return JsonResponse({"error" : "인증 오류 API키를 확인해주세요"}, status=401)   
    elif response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error" : "Failed to get data"}
    
 # stock KRX return view   
def stk_kdx_volume(request):
    volumn_data = get_stk_kdx_volume()
    
    return JsonResponse(volumn_data)

# View that renders the stock trading volume page
def stock_volume_page(request):
    return render(request,'AsStock/stock_volume.html')
    








