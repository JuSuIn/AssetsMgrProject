"""
 stock_history.py

 모델 개요:
    - 주식 가격 이력 데이터를 저장하는 모델
    - 일별 시세 (시가, 종가, 고가, 저가, 거래량 등)를 기록

️ 사용 목적:
    - 특정 종목의 과거 시세 분석 및 차트 데이터 제공
    - 주식 정보(StockInfo)와 연결되어 종목별 이력 관리

 사용되는 곳 (예정):
    - 자산 대시보드 그래프
    - 종목 상세 페이지 (과거 시세 탭)
    - 백테스트용 데이터 분석

 연관 모델:
    - StockInfo (ForeignKey)

 모델명:
    - StockHistory

️ 제약 조건:
    - 같은 날짜에 같은 종목으로 중복 기록 불가 (unique_together)
    - 최신 날짜 기준으로 정렬 (Meta.ordering)
"""

from django.db import models
import uuid
from .stock_info import StockInfo

class StockHistory(models.Model):

    # 고유 식별자 (UUID 사용)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # TODO : field  : 관련 주식 정보,거래 날짜, 시가, 종가 , 고가 , 저가, 거래량

    # 관련 주식 정보 (StockInfo와의 외래키 관계)
    stock = models.ForeignKey(
        StockInfo,
        on_delete=models.CASCADE,
        related_name='histories',
        help_text="해당 히스토리가 속한 주식"
    )

    # 거래 날짜
    date = models.DateField(
        db_index=True,
        help_text="해당 거래 날짜"
    )
    # 시가
    open_price = models.DecimalField(
        max_digits=12, decimal_places=2,
        help_text="해당 날짜의 시가",
        default=0,
    )

    # 종가
    close_price = models.DecimalField(
        max_digits=12, decimal_places=2,
        help_text="해당 날짜의 종가",
        default=0,
    )

    # 고가
    high_price = models.DecimalField(
        max_digits=12, decimal_places=2,
        help_text="해당 날짜의 고가",
        default=0,
    )

    # 저가
    low_price = models.DecimalField(
        max_digits=12, decimal_places=2,
        help_text="해당 날짜의 저가",
        default=0,
    )

    # 거래량
    volume = models.BigIntegerField(
        help_text="해당 날짜의 거래량",
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="데이터 생성 일시"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="데이터 수정 일시"
    )

    class Meta:
        #  같은 주식에 대해 날짜 중복 방지
        unique_together = ('stock', 'date')
        ordering = ['date'] # 최신데이터가 먼저

    def __str__(self):
        return f"{self.stock.ticker} - {self.date}"

