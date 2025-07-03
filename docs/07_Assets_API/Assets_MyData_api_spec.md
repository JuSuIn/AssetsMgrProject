# 📘 마이데이터 API 명세서 (초안)

---

## 📌 수집 자산 API (MyData Assets)

### 외부 자산 목록 조회
- **Method**: `GET`
- **URL**: `/api/mydata/assets/`
- **설명**: 마이데이터를 통해 수집된 외부 자산 정보를 조회합니다.

---

### 외부 자산 상세 조회
- **Method**: `GET`
- **URL**: `/api/mydata/assets/{id}/`
- **설명**: 특정 외부 자산 항목의 상세 정보를 조회합니다.

---

## 📌 자산 수집 요청 API

### 수집 시작 요청
- **Method**: `POST`
- **URL**: `/api/mydata/collect/`
- **설명**: 사용자의 외부 금융 정보를 수집합니다.

**요청 바디**
```json
{
  "institutions": ["신한은행", "삼성증권"]
}
```

**응답 예시**
```json
{
  "task_id": "ac9f00d1-1234-4e29-baaa-4567123acdef",
  "status": "started"
}
```

---

### 수집 상태 조회
- **Method**: `GET`
- **URL**: `/api/mydata/collect/status/?task_id=...`
- **설명**: 비동기 수집 작업의 상태를 확인합니다.

**응답 예시**
```json
{
  "task_id": "ac9f00d1-1234-4e29-baaa-4567123acdef",
  "status": "completed",
  "collected_count": 23
}
```

---

## 📌 연결 기관 관리 API

### 연결된 기관 목록 조회
- **Method**: `GET`
- **URL**: `/api/mydata/institutions/`
- **설명**: 사용자가 연결한 금융기관 목록을 조회합니다.

---

### 연결 해지
- **Method**: `DELETE`
- **URL**: `/api/mydata/institutions/{id}/`
- **설명**: 특정 기관과의 연결을 해지합니다.

---

## 📌 동의 내역 관리 API

### 데이터 제공 동의서 제출
- **Method**: `POST`
- **URL**: `/api/mydata/consents/`
- **설명**: 사용자 데이터 제공 동의를 등록합니다.

**요청 바디**
```json
{
  "terms_version": "v1.0",
  "agreed_at": "2025-07-01T12:00:00+09:00"
}
```

---

### 현재 동의 상태 조회
- **Method**: `GET`
- **URL**: `/api/mydata/consents/`
- **설명**: 사용자 동의 내역을 조회합니다.

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