# 📘 StockInfo API 명세서

## 1. 설명
주식 종목 기본 정보를 관리하는 API입니다.  
종목 코드(ticker), 이름(name), 산업군(sector), 거래소(market) 정보를 등록, 조회, 수정, 삭제할 수 있습니다.

---

## 2. 필드 구조 및 설명

| 필드명   | 타입     | 설명                          |
|----------|----------|-------------------------------|
| id       | integer  | 고유 ID                       |
| ticker   | string   | 종목 코드 (예: 005930)         |
| name     | string   | 종목 이름                     |
| sector   | string   | 산업군 (예: 전자, 바이오 등)  |
| market   | string   | 거래소 (예: KOSPI, KOSDAQ 등) |

---

## 3. Endpoint 및 기능

### 🔹 3-1. 종목 목록 조회

- **Method**: GET  
- **Endpoint**: `/api/stockinfo/`

#### ✅ 예시 응답

```json
[
  {
    "id": 1,
    "ticker": "005930",
    "name": "삼성전자",
    "sector": "전자",
    "market": "KOSPI"
  }
]
```

#### 🔍 Query Parameters
| 이름 | 설명 |
|------|------|
| sector | 산업군 필터링 |
| market | 거래소 필터링 |
| search | 종목명 또는 ticker 검색 |

---

### 🔹 3-2. 종목 상세 조회

- **Method**: GET  
- **Endpoint**: `/api/stockinfo/{id}/`

#### ✅ 예시 응답

```json
{
  "id": 1,
  "ticker": "005930",
  "name": "삼성전자",
  "sector": "전자",
  "market": "KOSPI"
}
```

---

### 🔹 3-3. 종목 등록

- **Method**: POST  
- **Endpoint**: `/api/stockinfo/`

#### ✅ Request Body

```json
{
  "ticker": "005930",
  "name": "삼성전자",
  "sector": "전자",
  "market": "KOSPI"
}
```

#### ✅ Response (201 Created)

```json
{
  "id": 1,
  "ticker": "005930",
  "name": "삼성전자",
  "sector": "전자",
  "market": "KOSPI"
}
```

#### ❌ 에러 응답 (400 Bad Request)

```json
{
  "ticker": ["이미 존재하는 종목 코드입니다."]
}
```

---

### 🔹 3-4. 종목 수정

- **Method**: PUT/PATCH  
- **Endpoint**: `/api/stockinfo/{id}/`

#### ✅ Request Body

```json
{
  "name": "삼성전자우",
  "sector": "전자",
  "market": "KOSPI"
}
```

---

### 🔹 3-5. 종목 삭제

- **Method**: DELETE  
- **Endpoint**: `/api/stockinfo/{id}/`

#### ✅ 응답
- 상태 코드: 204 No Content

---

### 🔹 3-6. 종목 코드로 검색

- **Method**: GET  
- **Endpoint**: `/api/stockinfo/search/`
- **Query Parameters**: `?ticker=005930`

#### ✅ 예시 응답

```json
{
  "id": 1,
  "ticker": "005930",
  "name": "삼성전자",
  "sector": "전자",
  "market": "KOSPI"
}
```

---

## 4. 상태 코드 정의

| 코드 | 설명 |
|------|------|
| 200 | 성공 조회 |
| 201 | 생성 성공 |
| 204 | 삭제 성공 |
| 400 | 잘못된 요청 |
| 404 | 데이터 없음 |

---

## 5. 예외 처리 예시

### 🔸 종목 코드 중복 등록 시

```json
{
  "ticker": ["이미 존재하는 종목 코드입니다."]
}
```

### 🔸 유효하지 않은 필드 입력 시

```json
{
  "market": ["'KOSP'는 유효한 선택이 아닙니다."]
}
```
