# 📘 StockNews API 명세서

## 1. 설명
종목별 뉴스 데이터를 수집하고 사용자에게 제공하는 API입니다. 뉴스는 수동 또는 자동 크롤링으로 저장됩니다.

---

## 2. 필드 구조

| 필드명       | 타입     | 설명                 |
|--------------|----------|----------------------|
| id           | integer  | 고유 ID              |
| stock_info   | integer  | 종목 ID (FK)         |
| title        | string   | 뉴스 제목            |
| summary      | string   | 뉴스 요약            |
| url          | string   | 원문 링크            |
| published_at | datetime | 뉴스 게시 일시       |

---

## 3. 기능별 API 명세

### 🔹 뉴스 수동 등록

- **POST** `/api/stocknews/`

```json
{
  "stock_info": 1,
  "title": "삼성전자, 2분기 실적 개선",
  "summary": "영업이익 3조 돌파",
  "url": "https://example.com/news/123",
  "published_at": "2024-07-30T09:00:00Z"
}
```

---

### 🔹 뉴스 리스트 조회

- **GET** `/api/stocknews/?ticker=005930&limit=5`

```json
[
  {
    "title": "삼성전자, 2분기 실적 개선",
    "summary": "영업이익 3조 돌파",
    "published_at": "2024-07-30T09:00:00Z",
    "url": "https://example.com/news/123"
  }
]
```

---

### 🔹 뉴스 상세 조회

- **GET** `/api/stocknews/{id}/`

---

### 🔹 키워드 검색 (예정)

- **GET** `/api/stocknews/search/?keyword=실적`

```json
[
  {
    "title": "삼성전자, 실적 기대감 상승",
    "summary": "...",
    "published_at": "2024-07-29T08:00:00Z"
  }
]
```

---

## 4. 상태 코드

| 코드 | 설명       |
|------|------------|
| 200  | 성공       |
| 201  | 생성 성공  |
| 400  | 요청 오류  |
| 404  | 데이터 없음 |
