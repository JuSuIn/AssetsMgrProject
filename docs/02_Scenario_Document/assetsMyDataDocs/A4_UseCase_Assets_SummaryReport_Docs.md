
## 📂 A4. 전체 자산 요약 리포트(PDF) 생성

### 🎯 목적
사용자의 자산 상태를 정리하여 PDF 형태로 저장/다운로드할 수 있게 한다.

### 👥 참여 객체
| 객체 | 설명 |
|------|------|
| User | 리포트를 요청하는 사용자 |
| React App | 리포트 요청 버튼 |
| Django API | 리포트 생성 요청 수신 |
| Celery Worker | PDF 생성 처리 |
| ReportRenderer | WeasyPrint/ReportLab 등 |
| PostgreSQL | 자산, 목표, 통계 데이터 |

### 🔄 시나리오 흐름
1. 사용자가 리포트 생성 클릭
2. API는 Celery로 작업 큐잉
3. Worker가 자산/목표 데이터 집계
4. 템플릿 렌더링 후 PDF 생성
5. 파일 저장 or 다운로드 URL 반환
6. 사용자는 결과 PDF 열람
