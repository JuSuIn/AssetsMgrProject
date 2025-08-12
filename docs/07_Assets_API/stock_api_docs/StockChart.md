# 📘 StockChart API 명세서

## 1. 설명
종목별 일/주/월 단위의 시세 차트 데이터를 조회하는 API입니다.

## 2. Endpoint
`/api/stockchart/`

## 3. Method
- GET (쿼리로 조회)

## 4. Request 예시 (Query Parameter)
/api/stockchart/?ticker=005930&interval=day&start=2024-01-01&end=2024-01-31

## 5. Response 예시
```json
[
  {
    "date": "2024-01-02",
    "open": 71000,
    "high": 72000,
    "low": 70500,
    "close": 71800,
    "volume": 1200000
  }
]
```

## 6. Query Parameters
- ticker: 종목 코드 (필수)
- interval: day, week, month
- start, end: 날짜 범위

## 7. 상태 코드 예시
- 200 OK
- 400 Bad Request
