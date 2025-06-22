
# 📤 S4. 자산 전체 내보내기 (CSV 또는 PDF)

> 사용자가 자신의 전체 자산 데이터를 파일로 내보낼 수 있는 기능입니다.  
> PDF 또는 CSV 형식으로 제공되며, 백업 또는 외부 전달용으로 사용됩니다.

---

## 🎯 유즈케이스 목적

- 사용자는 자산 정보를 파일로 저장하거나 공유할 수 있다.
- 선택 포맷(CSV or PDF)에 따라 다운로드 가능하다.

---

## 👥 참여 객체

| 객체 | 설명 |
|------|------|
| User | 내보내기를 요청하는 사용자 |
| React 내보내기 버튼 | PDF/CSV 선택 UI |
| Django API (/api/export/assets) | 파일 생성 요청 API |
| Celery Export Worker | 파일 생성 비동기 처리 |
| ExportService | CSV or PDF 렌더링 |
| PostgreSQL (Assets) | 자산 데이터 저장소 |

---

## 🔄 시나리오 흐름

1. 사용자가 ‘내보내기’ 버튼 클릭 → 포맷 선택 (CSV or PDF)
2. React에서 `POST /api/export/assets` 요청 전송
3. API는 Celery에 작업 큐잉
4. Worker가 자산 데이터 조회 후 ExportService 호출
5. 선택 포맷에 따라 파일 생성
6. 생성된 파일은 저장소(S3 또는 로컬)에 저장
7. 다운로드 링크 생성 → 사용자에게 반환

---

## ✅ 기대 효과

- 사용자 자산 이력 백업 가능
- 다른 시스템으로 이관하거나 외부 제출 자료로 사용 가능
