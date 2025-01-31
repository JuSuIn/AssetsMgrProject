from django.shortcuts import render
from django.http import JsonResponse
import requests

#KRX open api kospi url
#코스피 시리즈 지수의 시세정보를 제공(일별)에 대해 해당하는 api

def get_stk_kospi_dd_volume():
    basDd="20250107"
    
    # 원래 코드 
    url = "http://data-dbg.krx.co.kr/svc/apis/idx/kospi_dd_trd?"+f"basDd={ basDd }"
    api_key ="30CC14A01CA34602AC741210E107A999C5D167B6"
    
    #url = "http://data-dbg.krx.co.kr/svc/sample/apis/idx/kospi_dd_trd?"+f"basDd={ basDd }"
    #api_key ="74D1B99DFBF345BBA3FB4476510A4BED4C78D13A"
    
    params = {
       "Authorization": f"Bearer {api_key}"
    }
    
    response = requests.get(url, params=params)
    #print(response.status_code)
    
    if response.status_code == 401:
        return JsonResponse({"error" : "인증 오류 API키를 확인해주세요"}, status=401)
    elif response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error" : "Failed to get data"}




    