
## 🔔 A3. 이상자산 감지 및 알림

### 🎯 목적
자산이 급감하거나 특정 임계치를 벗어날 경우 사용자에게 즉시 알림을 전송한다.

### 👥 참여 객체
| 객체 | 설명 |
|------|------|
| Celery Scheduler | 정기 자산 감지 작업 |
| Django API | 알림 로직 |
| PostgreSQL | 자산/알림 테이블 |
| User | 자산 상태를 확인하는 사용자 |
| Email Service | 이메일/화면 알림 전송 |

### 🔄 시나리오 흐름
1. 스케줄러가 하루 1회 Celery 작업 수행
2. 자산 변화 비교 (전일 대비)
3. 변동률이 임계값 초과 시 알림 저장
4. 이메일 또는 프론트 알림 트리거
5. 사용자는 로그인 후 알림 확인