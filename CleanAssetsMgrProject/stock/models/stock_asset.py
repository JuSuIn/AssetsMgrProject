"""
 stock_asset.py
-  사용자 보유 종목 (stockAsset)
- 사용자가 보유 중인 종목 정보 저장 모델 (StockAsset)
- 종목, 수량, 평균 매입 단가, 보유 일자 등을 관리

 사용되는 곳:
- 자산 대시보드, 수익률 계산, 종목별 분석 등
 모델명:
- StockAsset
"""

from django.db import models
from django.conf import settings
from .stock_info import StockInfo

class StockAsset(models.Model):
    # 보유자 (Django User FK)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        # migrateion 확정 후에는 주석 처리( 외래키임 )
        # null = True,
        # blank = True,
        related_name='stock_assets'
    )
    # 어떤 종목인지(StockInfo FK)
    stock = models.ForeignKey(
        StockInfo,
        on_delete=models.CASCADE,
        # migrateion 확정 후에는 주석 처리( 외래키임 )
        # null=True,
        # blank=True,
        related_name='owned_assets'
    )

    #TODO : 보유 수량, 평균 매수단가, 최초 매수일, 비고/메모
    quantity = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        help_text="보유 수량",
        default=0
    )
    avg_buy_price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        help_text="평균 매수 단가",
        default=0
    )
    buy_date = models.DateField(
        null=True,
        blank=True,
        help_text="최초 매수일"
    )
    note = models.TextField(
        null=True,
        blank=True,
        help_text="비고 / 메모"
    )

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = ('user', 'stock')
        verbose_name = "보유 종목"
        verbose_name_plural = "보유 종목 목록"

    def __str__(self):
        return f"{self.user.username} - {self.stock.ticker} ({self.quantity})"