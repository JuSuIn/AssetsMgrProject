"""
  test_stocknews.py
  실시간 주식 관련 뉴스  주식 심볼 및 시간과 연결된 뉴스 컨텐츠 모델 모델 관련 unit test
- 생성이잘되는지(기본 필드 + URL optional 필드 포함 생성 확인)
- 수정이잘되는지(제목과 본문 수정 후 저장 확인)
- 삭제도잘이루어지는지(	삭제 후 .get() 시 DoesNotExist 예외 확인)
- 중복 URL 테스트 제거 unique=True가 제거되었으므로 중복 저장 허용됨

  기본 테스트

 사용되는 곳:
-
"""

import pytest
from stock.models import StockInfo, StockNews
from django.utils import timezone

# 생성
# (기본 필드 + URL optional 필드 포함 생성 확인)
@pytest.mark.django_db
def test_create_stock_news():
    stock = StockInfo.objects.create(ticker="AAPL", name="Apple", market="NASDAQ")

    news = StockNews.objects.create(
        stock=stock,
        title="Apple launches M4 chip",
        content="Apple released the M4 chip with major performance boosts.",
        source="Bloomberg",
        url="https://news.example.com/apple-m4-launch",
        published_at=timezone.now()
    )

    assert news.pk is not None
    assert news.title.startswith("Apple")
    assert news.stock == stock
    assert news.source == "Bloomberg"


#수정
# 제목과 본문 수정 후 저장 확인
@pytest.mark.django_db
def test_update_stock_news():
    stock = StockInfo.objects.create(ticker="TSLA", name="Tesla", market="NASDAQ")

    news = StockNews.objects.create(
        stock=stock,
        title="Tesla reveals new EV",
        content="Tesla has revealed its latest electric vehicle model.",
        source="Reuters",
        url=None,
        published_at=timezone.now()
    )

    news.title = "Tesla EV launch delayed"
    news.content += " Launch postponed to Q4."
    news.save()

    updated = StockNews.objects.get(pk=news.pk)
    assert "delayed" in updated.title
    assert "Q4" in updated.content


#삭제
# (	삭제 후 .get() 시 DoesNotExist 예외 확인)
@pytest.mark.django_db
def test_delete_stock_news():
    stock = StockInfo.objects.create(ticker="GOOGL", name="Google", market="NASDAQ")

    news = StockNews.objects.create(
        stock=stock,
        title="Google acquires startup",
        content="Google expands AI capabilities via acquisition.",
        source="TechCrunch",
        url="https://news.example.com/google-acquire",
        published_at=timezone.now()
    )

    news_id = news.pk
    news.delete()

    with pytest.raises(StockNews.DoesNotExist):
        StockNews.objects.get(pk=news_id)