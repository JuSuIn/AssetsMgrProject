"""
stock_news.py
- 실시간 주식 관련 뉴스
- 주식 심볼 및 시간과 연결된 뉴스 컨텐츠

사용되는 곳:
- 사용자 뉴스 피드, 종목 정보 탭

모델명:
- StockNews
"""

from django.db import models

class StockNews(models.Model):
    #TODO : field 고유식별자id,주식종목,뉴스제목,뉴스본문,뉴스언론사,URL,언론사실제 게시된 시간,시스템에 처음 저장된 시간
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stock = models.ForeignKey("StockInfo", on_delete=models.CASCADE, related_name="news")
    title = models.CharField(max_length=255, help_text="뉴스 제목")
    content = models.TextField(help_text="뉴스 본문")
    source = models.CharField(max_length=100, help_text="뉴스 제공자")
    url = models.URLField(blank=True, null=True, help_text="뉴스 원문 링크")
    published_at = models.DateTimeField(help_text="기사 작성 시간")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at']
        verbose_name = "주식 뉴스"
        verbose_name_plural = "주식 뉴스"

    def __str__(self):
        return f"[{self.stock.symbol}] {self.title}"
