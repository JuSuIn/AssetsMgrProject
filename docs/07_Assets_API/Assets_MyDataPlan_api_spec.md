# 📘 마이데이터 계획 API 명세서 (초안)

---

## 📌 목표 기반 자산 계획 API

### 사용자 계획 목록 조회
- **Method**: `GET`
- **URL**: `/api/mydata/plans/`
- **설명**: 사용자가 등록한 재무 계획 목록을 조회합니다.

---

### 계획 상세 조회
- **Method**: `GET`
- **URL**: `/api/mydata/plans/{id}/`
- **설명**: 특정 재무 계획 상세 조회

---

### 계획 생성
- **Method**: `POST`
- **URL**: `/api/mydata/plans/`
- **설명**: 사용자의 재무 목표 및 자산 계획을 생성합니다.

**요청 바디**
```json
{
  "goal_name": "3년 안에 전세자금 1억 모으기",
  "target_amount": 100000000,
  "target_date": "2028-01-01",
  "monthly_budget": 500000,
  "linked_asset_ids": [1, 2]
}
```

---

### 계획 수정
- **Method**: `PATCH`
- **URL**: `/api/mydata/plans/{id}/`

---

### 계획 삭제
- **Method**: `DELETE`
- **URL**: `/api/mydata/plans/{id}/`

---

## 📌 목표 추천 API

### 사용자 자산 기반 목표 추천
- **Method**: `GET`
- **URL**: `/api/mydata/plans/recommendation/`
- **설명**: 현재 자산 현황을 기반으로 추천 가능한 재무 목표를 제시합니다.

**응답 예시**
```json
{
  "recommended_goals": [
    {
      "name": "비상금 마련",
      "target_amount": 3000000,
      "suggested_monthly_budget": 250000
    },
    {
      "name": "노후 준비",
      "target_amount": 50000000,
      "suggested_monthly_budget": 400000
    }
  ]
}
```

---

## 📌 계획 달성 분석 API

### 계획 진행 상황 요약 조회
- **Method**: `GET`
- **URL**: `/api/mydata/plans/{id}/progress/`
- **설명**: 특정 계획에 대한 현재 달성률과 진행 분석을 반환합니다.

**응답 예시**
```json
{
  "goal_name": "3년 안에 전세자금 1억 모으기",
  "target_amount": 100000000,
  "current_amount": 23000000,
  "achieved_rate": 0.23,
  "expected_finish_date": "2028-02-15"
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