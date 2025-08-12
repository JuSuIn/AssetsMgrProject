# 📘 StockInterest API 명세서

## 1. 설명
사용자가 관심 종목으로 등록한 주식을 조회, 등록, 삭제할 수 있는 API입니다. 중복 등록 방지, 현재 관심 여부 확인 기능 포함.

---

## 2. 필드 구조

| 필드명     | 타입     | 설명                      |
|------------|----------|---------------------------|
| id         | integer  | 고유 ID                   |
| user       | integer  | 사용자 ID                 |
| stock_info | integer  | 관심 종목 ID (FK)         |

---

## 3. 기능별 API 명세

### 🔹 관심 종목 등록

- **POST** `/api/stockinterest/`

```json
{
  "user": 1,
  "stock_info": 2
}
```

- 응답:

```json
{
  "id": 10,
  "user": 1,
  "stock_info": 2
}
```

- 중복 등록 시 에러:

```json
{
  "detail": "이미 등록된 관심 종목입니다."
}
```

---

### 🔹 관심 종목 목록 조회

- **GET** `/api/stockinterest/?user=1`

```json
[
  {
    "id": 10,
    "stock_info": {
      "ticker": "005930",
      "name": "삼성전자"
    }
  }
]
```

---

### 🔹 관심 종목 삭제

- **DELETE** `/api/stockinterest/{id}/`

---

### 🔹 관심 여부 확인

- **GET** `/api/stockinterest/check/?user=1&ticker=005930`

```json
{
  "is_interested": true
}
```

---

## 4. 상태 코드

| 코드 | 설명 |
|------|------|
| 200  | 성공 |
| 201  | 생성 성공 |
| 400  | 요청 오류 |
| 404  | 데이터 없음 |
