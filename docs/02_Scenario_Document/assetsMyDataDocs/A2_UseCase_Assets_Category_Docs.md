
## 📊 A2. 자산 카테고리별 흐름 분석

### 🎯 목적
사용자의 자산 변동 추이를 카테고리별로 분석하여 시각화된 데이터로 제공한다.

### 👥 참여 객체
| 객체 | 설명 |
|------|------|
| User | 자산 흐름을 조회하는 사용자 |
| React App | 대시보드 차트 컴포넌트 |
| Django API (/api/assets/flow) | 자산 변화량 API |
| AssetService | 월별 변동량 계산 로직 |
| PostgreSQL | 자산 기록 테이블 |

### 🔄 시나리오 흐름
1. 사용자가 대시보드 접속 → 자산 흐름 차트 확인 요청
2. React는 GET /api/assets/flow 요청 전송
3. API는 DB에서 최근 6개월 자산 데이터를 카테고리별 조회
4. AssetService에서 월별 변화율 계산
5. JSON 응답으로 전송 (month, category, amount)
6. React에서 차트(Pie/Line)로 시각화 표시