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
    #TODO : field 정의
    #종목코드,회사명,시장구분,업종,산업군,상장일,현재거래여부

    ticker = models.CharField(max_length=20,unique=True,help_text="종목 코드 (예: AAPL, 005930)")
    name = models.CharField(max_length=200, help_text="회사명")
    market = models.CharField(max_length=50, help_text="시장 (KOSPI, KOSDAQ, NASDAQ 등)")
    sector = models.CharField(max_length=150, null=True, blank=True, help_text="업종")
    industry = models.CharField(max_length=150, null=True, blank=True, help_text="산업군")
    listed_at = models.DateField(null=True, blank=True, help_text="상장일")
    is_active = models.BooleanField(default=True, help_text="현재 거래 여부")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name ="종목 기본 정보"
        verbose_name_plural = "종목 기본 정보 목록"

    def __str__(self):
        return f"{self.name} ({self.ticker})"

