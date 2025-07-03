# 📘 금융 도메인 API 명세서 (초안)

---

## 📌 금융상품 목록 API

### 금융상품 전체 조회
- **Method**: `GET`
- **URL**: `/api/finance/products/`
- **설명**: 전체 금융상품(예적금, 펀드, 보험 등) 리스트를 조회합니다.

---

### 금융상품 상세 조회
- **Method**: `GET`
- **URL**: `/api/finance/products/{id}/`
- **설명**: 특정 금융상품의 상세 정보를 조회합니다.

---

### 금융상품 검색
- **Method**: `GET`
- **URL**: `/api/finance/products/search/?keyword=`
- **설명**: 상품명 또는 기관명으로 검색합니다.

---

## 📌 금융상품 즐겨찾기 API

### 즐겨찾기 등록
- **Method**: `POST`
- **URL**: `/api/finance/favorites/`

**요청 바디**
```json
{
  "product_id": 5
}
```

---

### 즐겨찾기 해제
- **Method**: `DELETE`
- **URL**: `/api/finance/favorites/{id}/`

---

### 즐겨찾기 목록 조회
- **Method**: `GET`
- **URL**: `/api/finance/favorites/`

---

## 📌 금융기관 API

### 금융기관 목록 조회
- **Method**: `GET`
- **URL**: `/api/finance/institutions/`

---

### 금융기관 상세 조회
- **Method**: `GET`
- **URL**: `/api/finance/institutions/{id}/`

---

## 📌 금융상품 추천 API

### 사용자 자산 기반 금융상품 추천
- **Method**: `GET`
- **URL**: `/api/finance/products/recommendation/`
- **설명**: 사용자의 자산과 투자성향에 기반한 금융상품을 추천합니다.

**응답 예시**
```json
{
  "recommended_products": [
    {
      "id": 10,
      "name": "신한 알뜰 정기예금",
      "type": "예금",
      "interest_rate": 3.5
    },
    {
      "id": 22,
      "name": "미래에셋 글로벌 ETF",
      "type": "펀드",
      "expected_return": 7.8
    }
  ]
}
```

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