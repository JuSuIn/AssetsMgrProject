"""
  test_stockhistory.py
-  주식 가격 이력 데이터를 저장하는 모델 모델 관련 unit test
- 생성이잘되는지(종목별 일자별 시세 데이터 생성 확인)
- 수정이잘되는지(종가, 거래량 변경 후 저장 확인)
- 삭제도잘이루어지는지(삭제 후 .get() 시 DoesNotExist 발생 확인)
- 중복 방지 테스트 동일 종목 + 날짜 등록 시 unique_together 위반 확인


  기본 테스트

 사용되는 곳:
-
"""

import pytest
from stock.models import StockInfo, StockHistory
from decimal import Decimal
from datetime import date

@pytest.mark.django_db
def test_create_stock_history():
    stock = StockInfo.objects.create(ticker="AAPL", name="Apple", market="NASDAQ")

    history = StockHistory.objects.create(
        stock=stock,
        date=date(2024, 7, 26),
        open_price=Decimal("190.00"),
        close_price=Decimal("195.00"),
        high_price=Decimal("196.00"),
        low_price=Decimal("188.00"),
        volume=10000000
    )

    assert history.pk is not None
    assert history.stock == stock
    assert history.date == date(2024, 7, 26)
    assert history.open_price == Decimal("190.00")
    assert history.volume == 10000000


@pytest.mark.django_db
def test_update_stock_history():
    stock = StockInfo.objects.create(ticker="TSLA", name="Tesla", market="NASDAQ")
    history = StockHistory.objects.create(
        stock=stock,
        date=date(2024, 7, 25),
        open_price=Decimal("250.00"),
        close_price=Decimal("260.00"),
        high_price=Decimal("265.00"),
        low_price=Decimal("240.00"),
        volume=5000000
    )

    history.close_price = Decimal("262.00")
    history.volume = 6000000
    history.save()

    updated = StockHistory.objects.get(pk=history.pk)
    assert updated.close_price == Decimal("262.00")
    assert updated.volume == 6000000


@pytest.mark.django_db
def test_delete_stock_history():
    stock = StockInfo.objects.create(ticker="NVDA", name="NVIDIA", market="NASDAQ")
    history = StockHistory.objects.create(
        stock=stock,
        date=date(2024, 7, 24),
        open_price=Decimal("450.00"),
        close_price=Decimal("460.00"),
        high_price=Decimal("470.00"),
        low_price=Decimal("440.00"),
        volume=3000000
    )

    history_id = history.pk
    history.delete()

    with pytest.raises(StockHistory.DoesNotExist):
        StockHistory.objects.get(pk=history_id)


@pytest.mark.django_db
def test_duplicate_stock_history_prevention():
    stock = StockInfo.objects.create(ticker="MSFT", name="Microsoft", market="NASDAQ")
    history_date = date(2024, 7, 23)

    StockHistory.objects.create(
        stock=stock,
        date=history_date,
        open_price=Decimal("300.00"),
        close_price=Decimal("310.00"),
        high_price=Decimal("312.00"),
        low_price=Decimal("295.00"),
        volume=1200000
    )

    # 중복 저장 시도 → unique_together 제약 위반 발생
    with pytest.raises(Exception):
        StockHistory.objects.create(
            stock=stock,
            date=history_date,  # 동일 날짜
            open_price=Decimal("305.00"),
            close_price=Decimal("315.00"),
            high_price=Decimal("317.00"),
            low_price=Decimal("300.00"),
            volume=1400000
        )