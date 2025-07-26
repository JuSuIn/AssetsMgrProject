"""
  test_stockinfo.py
-   사용자 보유 종목 모델 관련 unit test
- 등록이잘되는지
- 수정이잘되는지
- 삭제도잘이루어지는지

  기본 테스트

 사용되는 곳:
-
"""

import pytest
from django.contrib.auth import get_user_model
from stock.models import StockInfo, StockAsset

# 유저 모델 불러옴
User = get_user_model()

# 등록
# StockAsset이 잘 생성되고 관련 필드(FK 포함)가 올바르게 연결됨
@pytest.mark.django_db
def test_create_stock_asset():
    user = User.objects.create_user(username="testuser", password="pass1234")
    stock = StockInfo.objects.create(ticker="AAPL", name="Apple", market="NASDAQ")

    asset=StockAsset.objects.create(user=user,
                                    stock=stock,
                                    quantity=10,
                                    avg_buy_price=180.50
                                    )

    assert asset.pk is not None
    assert asset.quantity == 10
    assert asset.avg_buy_price == 180.50
    assert asset.user == user
    assert asset.stock == stock

#수정
# quantity, avg_buy_price를 수정하고 DB에 반영되는지 확인
@pytest.mark.django_db
def test_update_stock_asset():
    user = User.objects.create_user(username="updateuser", password="pass5678")
    stock = StockInfo.objects.create(ticker="TSLA", name="Tesla", market="NASDAQ")

    asset=StockAsset.objects.create(user=user,
                                    stock=stock,
                                    quantity=5,
                                    avg_buy_price=300.00
                                    )
    asset.quantity=20
    asset.avg_buy_price =310.00
    asset.save()

    updated = StockAsset.objects.get(pk=asset.pk)
    #성공
    assert updated.quantity== 20
    #실패
    #assert updated.quantity == 10

    assert updated.avg_buy_price == 310.00

#삭제
# 삭제 후 .get() 시 DoesNotExist 예외 발생 확인
@pytest.mark.django_db
def test_delete_stock_asset():
    user = User.objects.create_user(username="deleteuser", password="pass9999")
    stock = StockInfo.objects.create(ticker="NVDA", name="NVIDIA", market="NASDAQ")
    asset = StockAsset.objects.create(user=user, stock=stock, quantity=20, avg_buy_price=500.00)

    asset_id = asset.pk
    asset.delete()

    #삭제 관련
    with pytest.raises(StockAsset.DoesNotExist):
        StockAsset.objects.get(pk=asset_id)
