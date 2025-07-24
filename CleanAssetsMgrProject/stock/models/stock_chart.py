"""
stock_chart.py
- 주식 차트 데이터 (분봉, 캔들, 거래량 등)
- 특정 주식의 시간대별 상세한 가격 변동 정보를 담는다.

사용되는 곳:
- 프론트 차트 표시용, 고빈도 시세 트래킹

모델명:
- StockChart
"""

from django.db import models
from django.utils import timezone
import uuid

class StockChart(models.Model):
    #TODO : 고유식별자ID, 주식종목,시세정보시간,시가,최고가,최저가,종가,거래량,시스템기록
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stock = models.ForeignKey("StockInfo", on_delete=models.CASCADE, related_name="charts")
    datetime = models.DateTimeField(help_text="캔들 시간")
    open_price = models.DecimalField(max_digits=12, decimal_places=2, help_text="시가")
    high_price = models.DecimalField(max_digits=12, decimal_places=2, help_text="고가")
    low_price = models.DecimalField(max_digits=12, decimal_places=2, help_text="저가")
    close_price = models.DecimalField(max_digits=12, decimal_places=2, help_text="종가")
    volume = models.BigIntegerField(help_text="거래량")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('stock', 'datetime')
        ordering = ['-datetime']
        verbose_name = "주식 차트"
        verbose_name_plural = "주식 차트"

    def __str__(self):
        return f"{self.stock.name} - {self.datetime}"
