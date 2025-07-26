"""
  test_stockinterest.py
-   사용자 관심 종목 모델 관련 unit test
- 등록이잘되는지
- 삭제도잘이루어지는지

  기본 테스트

 사용되는 곳:
-
"""

import pytest
from django.contrib.auth import get_user_model
from stock.models import StockInfo, StockInterest

User = get_user_model()

#등록
@pytest.mark.django_db
def test_create_stock_interest():
    user = User.objects.create_user(username="interest_user", password="test123")
    stock = StockInfo.objects.create(ticker="GOOGL", name="Google", market="NASDAQ")

    interest = StockInterest.objects.create(
        user=user,
        stock=stock
    )

    assert interest.pk is not None
    assert interest.user == user
    assert interest.stock == stock


#삭제
@pytest.mark.django_db
def test_delete_stock_interest():
    user = User.objects.create_user(username="interest_user3", password="test789")
    stock = StockInfo.objects.create(ticker="NFLX", name="Netflix", market="NASDAQ")
    interest = StockInterest.objects.create(user=user, stock=stock)

    interest_id = interest.pk
    interest.delete()

    with pytest.raises(StockInterest.DoesNotExist):
        StockInterest.objects.get(pk=interest_id)