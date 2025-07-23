"""
 stock_info.py
- 종목 기본 정보 모델 정의 (StockInfo)
- 종목 코드, 회사명, 시장, 업종 등 메타 정보 포함

 사용되는 곳:
- 관심 종목, 보유 종목, 가격 이력, 차트 데이터 등 모든 주식 도메인의 기준점 역할
- API, Celery 작업, 프론트 종목 리스트 조회 등에 활용됨

 모델명:
- StockInfo
"""
from django.db import models

class StockInfo(models.Model):
    #TODO : field 추후 정의
    pass

