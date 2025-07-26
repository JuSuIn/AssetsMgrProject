"""
  test_stockinterest.py
-   사용자 주식 차트 데이터 모델 관련 unit test
- 생성이잘되는지(UUID + 모든 필드 확인)
- 수정이잘되는지(종가 & 거래량 변경)
- 삭제도잘이루어지는지(삭제 후 존재 확인)
- 중복 방지 테스트 (stock, datetime) 중복 시 예외 발생 확인 (unique_together)

  기본 테스트

 사용되는 곳:
-
"""

import pytest
from stock.models import StockInfo,StockChart
from django.utils import timezone
from decimal import Decimal


#등록
#생성이잘되는지(UUID + 모든 필드 확인)
@pytest.mark.django_db
def test_create_stock_chart():
    stock = StockInfo.objects.create(ticker="AAPL", name="Apple Inc.", market="NASDAQ")
    dt = timezone.now()

    chart = StockChart.objects.create(
        stock=stock,
        datetime=dt,
        open_price=Decimal("190.00"),
        high_price=Decimal("195.00"),
        low_price=Decimal("189.00"),
        close_price=Decimal("192.50"),
        volume=10000000
    )

    assert chart.pk is not None
    assert chart.open_price == Decimal("190.00")
    assert chart.volume == 10000000
    assert chart.stock == stock


#수정
# 수정이잘되는지(종가 & 거래량 변경)
@pytest.mark.django_db
def test_update_stock_chart():
    stock = StockInfo.objects.create(ticker="TSLA", name="Tesla", market="NASDAQ")
    dt = timezone.now()

    chart = StockChart.objects.create(
        stock=stock,
        datetime=dt,
        open_price=Decimal("250.00"),
        high_price=Decimal("255.00"),
        low_price=Decimal("245.00"),
        close_price=Decimal("252.00"),
        volume=8000000
    )

    chart.close_price = Decimal("254.00")
    chart.volume = 9000000
    chart.save()

    updated = StockChart.objects.get(pk=chart.pk)
    assert updated.close_price == Decimal("254.00")
    assert updated.volume == 9000000


# 삭제
# 삭제도잘이루어지는지(삭제 후 존재 확인)
@pytest.mark.django_db
def test_delete_stock_chart():
    stock = StockInfo.objects.create(ticker="NVDA", name="NVIDIA", market="NASDAQ")
    dt = timezone.now()

    chart = StockChart.objects.create(
        stock=stock,
        datetime=dt,
        open_price=Decimal("500.00"),
        high_price=Decimal("510.00"),
        low_price=Decimal("490.00"),
        close_price=Decimal("505.00"),
        volume=6000000
    )

    chart_id = chart.pk
    chart.delete()

    with pytest.raises(StockChart.DoesNotExist):
        StockChart.objects.get(pk=chart_id)


#중복방지 테스트
# 중복 방지 테스트 (stock, datetime) 중복 시 예외 발생 확인 (unique_together)
@pytest.mark.django_db
def test_duplicate_stock_chart_prevention():
    stock = StockInfo.objects.create(
        ticker="MSFT",
        name="Microsoft",
        market="NASDAQ"
    )
    dt = timezone.now()

    StockChart.objects.create(
        stock=stock,
        datetime=dt,
        open_price=Decimal("300.00"),
        high_price=Decimal("310.00"),
        low_price=Decimal("295.00"),
        close_price=Decimal("305.00"),
        volume=12000000
    )

    # unique_together로 인해 동일 stock + datetime 조합은 허용되지 않아야 함
    with pytest.raises(Exception):
        StockChart.objects.create(
            stock=stock,
            datetime=dt,
            open_price=Decimal("301.00"),
            high_price=Decimal("311.00"),
            low_price=Decimal("296.00"),
            close_price=Decimal("306.00"),
            volume=13000000
        )


