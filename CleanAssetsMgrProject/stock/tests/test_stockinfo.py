"""
  test_stockinfo.py
-   종목 기본 정보 모델 정의 관련 unit test

 사용되는 곳:
-
"""

import pytest
from stock.models import StockInfo

@pytest.mark.django_db
def test_create_stock_info():
    stock = StockInfo.objects.create(
        ticker="AAPL",
        name="Apple Inc.",
        market="NASDAQ"
    )

    assert stock.ticker == "AAPL"
    assert stock.name == "Apple Inc."
    assert stock.market == "NASDAQ"
    #assert str(stock) == "AAPL - Apple Inc." # 일부러 이름 에러냄
    #assert str(stock) == "Apple Inc. (AAPL)" # 이름 에러가 안나는경우

@pytest.mark.django_db
def test_stock_info_unique_ticker():
    StockInfo.objects.create(ticker="GOOGL",
                             name="Google",
                             market="NASDAQ")

    with pytest.raises(Exception): # 일부로 IntegrityError 발생 시킴
        StockInfo.objects.create(ticker="GOOGL",name="Duplicate", market="NASDAQ")
