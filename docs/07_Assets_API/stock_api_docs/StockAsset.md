# 📘 StockAsset API 명세서

## 1. 설명
사용자가 보유 중인 주식 자산을 관리하는 API입니다. 종목별 수량, 평균 매수가 등을 저장하고, 보유 종목 목록과 수익률 등을 계산할 수 있습니다.

---

## 2. 필드 구조

| 필드명         | 타입     | 설명                     |
|----------------|----------|--------------------------|
| id             | integer  | 고유 ID                  |
| user           | integer  | 사용자 ID                |
| stock_info     | integer  | 종목 ID (FK: StockInfo)  |
| quantity       | float    | 보유 수량                |
| avg_buy_price  | float    | 평균 매수가              |

---

## 3. 기능별 API 명세

### 🔹 자산 등록

- **POST** `/api/stockasset/`

```json
{
  "user": 1,
  "stock_info": 3,
  "quantity": 10.5,
  "avg_buy_price": 73500
}
```

- 응답:

```json
{
  "id": 1,
  "user": 1,
  "stock_info": 3,
  "quantity": 10.5,
  "avg_buy_price": 73500
}
```

---

### 🔹 자산 목록 조회

- **GET** `/api/stockasset/?user=1`

- 응답:

```json
[
  {
    "id": 1,
    "stock_info": {
      "ticker": "005930",
      "name": "삼성전자"
    },
    "quantity": 10.5,
    "avg_buy_price": 73500
  }
]
```

---

### 🔹 자산 수정

- **PUT** `/api/stockasset/{id}/`

```json
{
  "quantity": 20,
  "avg_buy_price": 72000
}
```

---

### 🔹 자산 삭제

- **DELETE** `/api/stockasset/{id}/`

---

### 🔹 수익률 계산 (예정)

- **GET** `/api/stockasset/{id}/profit/`

- 응답:

```json
{
  "current_price": 74500,
  "avg_buy_price": 72000,
  "quantity": 10,
  "profit": 2500,
  "rate": 0.035
}
```

