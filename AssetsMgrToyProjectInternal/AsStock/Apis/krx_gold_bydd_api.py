#KRX open api gold url
import requests
from django.http import JsonResponse

# 금시장 일별매매정보  대해 해당하는 api

def get_krx_gold_bydd_volume():
    basDd = "20250107"
    #원래코드
    #url = ""
    #api_key = ""

    #sample
    url = "http://data-dbg.krx.co.kr/svc/sample/apis/gen/gold_bydd_trd?"+f"basDd={ basDd }"
    api_key ="74D1B99DFBF345BBA3FB4476510A4BED4C78D13A"

    params = {
       "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(url, params=params)

    if response.status_code == 401:
        return JsonResponse({"error" : "인증 오류 API키를 확인해주세요"}, status=401)
    elif response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error" : "Failed to get data"}

