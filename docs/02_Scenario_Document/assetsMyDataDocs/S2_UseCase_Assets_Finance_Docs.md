
# 🧭 S2. 금융상품 리스트 조회 + 즐겨찾기 추가

> 사용자가 금융상품을 탐색하고, 원하는 상품을 즐겨찾기할 수 있는 흐름입니다.  
> 리스트 조회는 정렬/필터링을 포함하고, 즐겨찾기는 사용자 기준으로 개별 저장됩니다.

---

## 🎯 유즈케이스 목적

- 사용자는 예금, 적금, 펀드 등의 금융상품을 조회할 수 있다.
- 이자율, 기간, 종류 등으로 정렬/필터링하여 탐색 가능하다.
- 관심 있는 상품을 즐겨찾기에 추가하여 따로 관리할 수 있다.

---

## 👥 참여 객체

| 객체 | 설명 |
|------|------|
| User | 상품을 조회하고 즐겨찾기하는 사용자 |
| React 금융상품 뷰 | 리스트 UI 및 즐겨찾기 버튼 |
| Django API (GET /api/finance/products) | 상품 조회 API |
| Django API (POST /api/finance/favorites) | 즐겨찾기 등록 API |
| FinanceService | 상품 조회 및 즐겨찾기 비즈니스 로직 처리 |
| PostgreSQL (Products, Favorites) | 상품 및 즐겨찾기 저장소 |

---

## 🔄 시나리오 흐름

### [1] 금융상품 리스트 조회

1. 사용자가 금융상품 메뉴로 이동한다.
2. React에서 `GET /api/finance/products?sort=interest_rate` 요청을 전송한다.
3. Django API에서 `FinanceService`를 통해 정렬 조건에 맞게 상품을 조회한다.
4. DB에서 상품 정보를 SELECT하여 가져온다.
5. 응답 데이터를 JSON 형태로 반환한다.
6. React는 리스트를 화면에 표시한다.

### [2] 즐겨찾기 추가

1. 사용자가 관심 있는 상품의 ‘★’ 아이콘을 클릭한다.
2. `POST /api/finance/favorites` API 요청이 전송된다 (payload: product_id).
3. API에서 `FinanceService`를 호출하여 즐겨찾기 등록 로직 실행
4. DB에 `INSERT INTO favorites(user_id, product_id)` 실행
5. 성공 시 OK 응답을 반환
6. React는 즐겨찾기 UI를 반영한다 (색 변경 등)

---

## 📌 예외 흐름

- 상품이 존재하지 않으면 404 응답
- 이미 즐겨찾기한 상품은 중복 방지 처리
- 비로그인 상태에서는 즐겨찾기 기능 제한

---

## 🔗 관련 API 명세 (간략)

### 1. 상품 리스트 조회

```
GET /api/finance/products?sort=interest_rate

응답:
[
  {
    "id": 1,
    "name": "KB 예금 3.2%",
    "type": "예금",
    "interest_rate": 3.2,
    "duration_months": 12
  },
  ...
]
```

### 2. 즐겨찾기 등록

```
POST /api/finance/favorites

요청:
{
  "product_id": 1
}

응답:
{
  "success": true,
  "message": "즐겨찾기에 추가되었습니다."
}
```

---

## ✅ 기대 효과

- 다양한 상품을 탐색하고 비교할 수 있는 사용자 경험 강화
- 즐겨찾기 기능을 통해 자주 확인할 상품을 효율적으로 관리 가능
