# 📘 자산관리 API 명세서 (초안)

---

## 📌 사용자(User) API

### 회원가입 - 사용자 계정 생성
- **Method**: `POST`
- **URL**: `/api/signup/`
- **설명**: 새로운 사용자 계정을 생성합니다.

#### ✅ 요청 Request

**헤더**
```http
Content-Type: application/json
```

**바디**
```json
{
  "email": "user@example.com",
  "password": "1234abcd",
  "name": "홍길동"
}
```

**필드 설명**

| 필드명 | 타입 | 필수 | 설명 |
|--------|------|------|------|
| email | string | ✅ | 사용자 이메일 |
| password | string | ✅ | 비밀번호 |
| name | string | ✅ | 사용자 이름 |

#### ✅ 응답 Response

```json
{
  "id": 1,
  "email": "user@example.com",
  "name": "홍길동"
}
```

---

### 로그인 - JWT 토큰 발급
- **Method**: `POST`
- **URL**: `/api/login/`
- **설명**: 로그인 후 access/refresh 토큰을 반환합니다.

**요청 바디**
```json
{
  "email": "user@example.com",
  "password": "1234abcd"
}
```

**응답 바디**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOi...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOi..."
}
```

---

### 내 정보 조회
- **Method**: `GET`
- **URL**: `/api/me/`
- **설명**: 로그인된 사용자의 정보를 조회합니다.

---

## 📌 자산 그룹(AssetGroup) API

### 자산 그룹 목록 조회
- **Method**: `GET`
- **URL**: `/api/asset-groups/`

---

### 자산 그룹 생성
- **Method**: `POST`
- **URL**: `/api/asset-groups/`

**요청 바디**
```json
{
  "name": "현금성 자산"
}
```

---

### 자산 그룹 수정
- **Method**: `PATCH`
- **URL**: `/api/asset-groups/{id}/`

**요청 바디**
```json
{
  "name": "투자 자산"
}
```

---

### 자산 그룹 삭제
- **Method**: `DELETE`
- **URL**: `/api/asset-groups/{id}/`

---

## 📌 자산(Asset) API

### 자산 목록 조회
- **Method**: `GET`
- **URL**: `/api/assets/`
- **설명**: 로그인한 사용자의 자산 목록 전체 조회

---

### 자산 등록
- **Method**: `POST`
- **URL**: `/api/assets/`

**요청 바디**
```json
{
  "group_id": 2,
  "name": "삼성증권 CMA",
  "amount": 1500000,
  "asset_type": "현금",
  "institution_name": "삼성증권",
  "product_name": "CMA RP형"
}
```

---

### 자산 수정
- **Method**: `PATCH`
- **URL**: `/api/assets/{id}/`

---

### 자산 삭제
- **Method**: `DELETE`
- **URL**: `/api/assets/{id}/`

---

## 📌 목표(Goal) API

### 목표 목록 조회
- **Method**: `GET`
- **URL**: `/api/goals/`

---

### 목표 생성
- **Method**: `POST`
- **URL**: `/api/goals/`

**요청 바디**
```json
{
  "name": "전세자금 마련",
  "target_amount": 100000000,
  "due_date": "2027-01-01",
  "related_asset_ids": [1, 3]
}
```

---

### 목표 수정
- **Method**: `PATCH`
- **URL**: `/api/goals/{id}/`

---

### 목표 삭제
- **Method**: `DELETE`
- **URL**: `/api/goals/{id}/`

---

## 📌 대시보드(Dashboard) API

### 대시보드 조회
- **Method**: `GET`
- **URL**: `/api/dashboard/`
- **설명**: 자산 총합, 그룹별 구성, 목표 달성률 등을 조회합니다.

#### ✅ 응답 예시
```json
{
  "total_assets": 60000000,
  "by_group": {
    "현금성": 20000000,
    "투자": 40000000
  },
  "goals": [
    {
      "name": "비상금",
      "target": 5000000,
      "current": 3500000,
      "rate": 0.7
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