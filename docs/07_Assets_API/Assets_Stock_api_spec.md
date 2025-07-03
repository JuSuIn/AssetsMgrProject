# 📘 주식 도메인 API 명세서 (초안)

---

## 📌 종목 정보 API

### 종목 목록 조회
- **Method**: `GET`
- **URL**: `/api/stocks/`
- **설명**: 전체 주식 종목(국내/해외 포함) 리스트를 조회합니다.

---

### 종목 상세 조회
- **Method**: `GET`
- **URL**: `/api/stocks/{ticker}/`
- **설명**: 특정 종목의 상세 정보 및 차트 데이터 조회

---

### 종목 검색
- **Method**: `GET`
- **URL**: `/api/stocks/search/?keyword=삼성`
- **설명**: 종목명 또는 티커(symbol)로 검색

---

## 📌 관심 종목 API

### 관심 종목 등록
- **Method**: `POST`
- **URL**: `/api/stocks/watchlist/`

**요청 바디**
```json
{
  "ticker": "005930"
}
```

---

### 관심 종목 삭제
- **Method**: `DELETE`
- **URL**: `/api/stocks/watchlist/{id}/`

---

### 관심 종목 목록 조회
- **Method**: `GET`
- **URL**: `/api/stocks/watchlist/`

---

## 📌 주식 투자 기록 API

### 보유 주식 등록
- **Method**: `POST`
- **URL**: `/api/stocks/holdings/`

**요청 바디**
```json
{
  "ticker": "AAPL",
  "quantity": 10,
  "average_price": 185.23,
  "purchase_date": "2024-12-01"
}
```

---

### 보유 주식 수정
- **Method**: `PATCH`
- **URL**: `/api/stocks/holdings/{id}/`

---

### 보유 주식 삭제
- **Method**: `DELETE`
- **URL**: `/api/stocks/holdings/{id}/`

---

### 보유 종목 목록 조회
- **Method**: `GET`
- **URL**: `/api/stocks/holdings/`

---

## 📌 실시간 데이터/차트 API

### 실시간 가격 조회
- **Method**: `GET`
- **URL**: `/api/stocks/{ticker}/price/`

---

### 종목 차트 데이터 조회
- **Method**: `GET`
- **URL**: `/api/stocks/{ticker}/chart/?range=1w`
- **설명**: 분봉/일봉/주봉 등 기간별 차트 데이터 제공

---

## 📌 공통 에러 코드

| HTTP 상태코드 | 설명 |
|---------------|------|
| 400 Bad Request | 잘못된 요청 (필드 누락, 타입 오류 등) |
| 401 Unauthorized | 인증 실패 (로그인 필요) |
| 403 Forbidden | 권한 없음 |
| 404 Not Found | 해당 리소스를 찾을 수 없음 |
| 500 Internal Server Error | 서버 오류 |

---