"""
 stock_interest.py
-  사용자 관심 종목 (stockInterest)

사용자 관심 종목 모델
    - 특정 사용자가 관심 등록한 종목

 사용되는 곳:
-
 모델명: StockInterest
-
"""
import uuid
from django.db import models
from django.conf import settings
from .stock_info import StockInfo

class StockInterest(models.Model):

    """
      사용자 관심 종목 모델
      - 특정 사용자가 관심 등록한 종목
     """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    #TODO : user, stock
    user= models.ForeignKey(
        settings.AUTH_USER_MODEL, # 사용자 모델 참조 방식
        on_delete=models.CASCADE,
        related_name="interestsed_stocks",
        null=True
    )

    stock = models.ForeignKey(
        StockInfo,
        on_delete=models.CASCADE,
        related_name="interested_by_users",
        null=True
    )

    added_at = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        db_table = "stock_interest"
        verbose_name="관심 종목"
        verbose_name_plural = "관심 종목 목록"
        unique_together = ("user", "stock") #같은 사용자가 같은 종목을 중복 등록할 수 없습니다.

    def __str__(self):
        return f"{self.user} 관심종목 : {self.stock}"