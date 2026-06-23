import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
ws = wb.active
ws.title = 'K뷰티 팝업 이벤트 아이디어'

# ── 스타일 헬퍼 ──────────────────────────────────────────
def make_fill(hex_color):
    return PatternFill(start_color=hex_color, end_color=hex_color, fill_type='solid')

def make_border(color='CCCCCC', style='thin'):
    s = Side(style=style, color=color)
    return Border(left=s, right=s, top=s, bottom=s)

def align(h='left', v='center', wrap=True):
    return Alignment(horizontal=h, vertical=v, wrap_text=wrap)

HEADER_BG = '1A1A2E'
TITLE_BG  = '16213E'
HEADER_FG = 'FFFFFF'
ACCENT    = 'E63946'
GREEN     = '2D6A4F'
PURPLE    = '6A0572'

IDEA_BG = [
    'FFF0F5','FFF5E6','F0FFF4','EEF2FF','FFF8F0',
    'F5F0FF','F0FFFF','FFFAF0','F5FFF5','EFF6FF','FFF0F0'
]

thin  = make_border('DDDDDD','thin')

# ── 데이터 ───────────────────────────────────────────────
ideas = [
    {
        'no': 1,
        'en': 'K-Beauty Lucky Spin',
        'kr': '팝업 입장 즉시 룰렛',
        'feature': '룰렛 + QR 코드 + LINE 소셜 커플링',
        'scenario': (
            '① 팝업 입구 QR 코드 스캔\n'
            '② 브랜드 LINE 공식 계정 친구 추가\n'
            '③ 즉시 룰렛 1회 제공\n'
            '④ 당첨: 샘플 / 할인 쿠폰 / 한정 굿즈\n'
            '   (꽝 없음, 최소 샘플 보장)'
        ),
        'reward': '샘플 키트 / 10~20% 할인 쿠폰 / 한정 굿즈',
        'kpi': 'LINE 친구 추가 수 / 룰렛 참여율 / 현장 체류 시간',
        'target': 'ISNTREE, BOJ, ooznary 등\n팔로워 1만 이하 소규모 브랜드',
        'effect': (
            '· LINE 팔로워 단기 폭증 (오프라인→디지털 자산화)\n'
            '· 현장 체류 시간 증가\n'
            '· 입장 대기 시간 활용 가능\n'
            '· 팝업 종료 후 리타겟팅 마케팅 가능'
        ),
        'timing': '팝업 전 기간 (입장 즉시)',
    },
    {
        'no': 2,
        'en': 'Beauty Zone Bingo',
        'kr': '팝업 존 탐방 빙고',
        'feature': '빙고 + QR 인증 + 단계형 리워드',
        'scenario': (
            '① 팝업 내 존 구성\n'
            '   (스킨케어 / 메이크업 / 포토존 / 체험존)\n'
            '② 각 존 체험 후 QR 인증 → 3x3 빙고 카드\n'
            '③ 1줄 완성: 샘플 키트\n'
            '④ 2줄 완성: 정품 미니어처\n'
            '⑤ 풀 빙고: 한정 굿즈 or 추첨권'
        ),
        'reward': '1줄: 샘플키트 / 2줄: 미니어처 / 풀빙고: 한정 굿즈·추첨권',
        'kpi': '존별 방문율 / 빙고 완성율 / 평균 체류 시간',
        'target': 'Wonjungyo x CipiCipi x muice\n합동 팝업 (각 브랜드 부스 = 빙고 칸)',
        'effect': (
            '· 팝업 전 공간 골고루 탐방 유도\n'
            '· 체류 시간 극대화 → 자연스러운 추가 구매\n'
            '· 소규모 브랜드 노출 강제화 효과\n'
            '· 합동 팝업 브랜드 간 공평한 트래픽 분배'
        ),
        'timing': '팝업 전 기간',
    },
    {
        'no': 3,
        'en': 'Buy More, Win More',
        'kr': '구매 인증 더블업 챌린지',
        'feature': 'Double or Nothing + 레시트 인증 + 단계형 리워드',
        'scenario': (
            '① 제품 구매 후 영수증 QR 인증\n'
            '   → 1단계 기본 쿠폰 즉시 획득\n'
            '② 추가 제품 구매 인증 → 리워드 2배\n'
            '③ 총 3종 구매 인증 → 최고 리워드\n'
            '   (한정 굿즈 / 풀키트)\n'
            '④ 실패해도 이전 단계 리워드 유지'
        ),
        'reward': '1단계: 5% 쿠폰 / 2단계: 10% 쿠폰 / 3단계: 한정 풀키트',
        'kpi': '객단가 변화 / 단계별 전환율 / 영수증 인증 건수',
        'target': 'TIRTIR, 롬앤, 데이지크\n멀티 SKU 보유 브랜드',
        'effect': (
            '· 객단가 자연스럽게 상승\n'
            '· "손해 없다"는 심리로 참여율 폭증\n'
            '· 구매 데이터 기반 고객 행동 분석 가능\n'
            '· 재고 소진 가속화 효과'
        ),
        'timing': '팝업 전 기간 (구매 즉시)',
    },
    {
        'no': 4,
        'en': 'K-Beauty Stamp Tour',
        'kr': 'K뷰티 멀티브랜드 스탬프 랠리',
        'feature': '디지털 스탬프 랠리 + 위치 기반 정밀 타겟팅',
        'scenario': (
            '① 멀티 브랜드 팝업 환경에서 운영\n'
            '   (무신사 도쿄, 합동 팝업 등)\n'
            '② 각 브랜드 부스 QR 스캔 → 스탬프 적립\n'
            '③ 3개 방문: 공통 쿠폰\n'
            '④ 5개 방문: 굿즈 키트\n'
            '⑤ 전체 방문: 특별 추첨 응모\n'
            '   (스탬프 보드가 지도 형태로 표시)'
        ),
        'reward': '3개: 공통 쿠폰 / 5개: 굿즈 키트 / 전체: 특별 추첨 응모',
        'kpi': '브랜드별 부스 방문율 / 스탬프 완주율 / 동선 데이터',
        'target': '무신사 도쿄 팝업, 9브랜드 합동 팝업\n등 멀티 브랜드 행사',
        'effect': (
            '· 소규모 브랜드 인지도 자연 상승\n'
            '· 단일 브랜드 고착 동선 탈피\n'
            '· 전체 이벤트 체류 시간 증가\n'
            '· 위치 데이터 기반 방문 패턴 분석 가능'
        ),
        'timing': '팝업 전 기간',
    },
    {
        'no': 5,
        'en': 'Morning Glow / Night Glow',
        'kr': '타임시프트 이벤트',
        'feature': '타임시프트 자동 전환 + 시간대별 다른 이벤트 화면',
        'scenario': (
            '① 오픈 직후(AM): "얼리버드 스크래치"\n'
            '   → 선착순 방문객 특별 쿠폰\n'
            '② 오후 골든타임: "피크 룰렛"\n'
            '   → 최고 리워드 당첨 확률 상승\n'
            '③ 마감 1시간 전: "라스트 찬스 더블업"\n'
            '   → 미구매자 대상 파격 혜택\n'
            '④ 화면·카피·리워드 시간대별 자동 전환'
        ),
        'reward': '얼리버드: 한정 샘플 / 피크: 대형 리워드 / 마감: 추가 할인',
        'kpi': '시간대별 방문자 수 / 구매 전환율 / 재방문율',
        'target': 'LANEIGE, VT Cosmetics\n일별 방문 데이터 중요 브랜드',
        'effect': (
            '· 특정 시간 방문 집중 현상 분산\n'
            '· "마감 전 혜택" 메시지로 재방문 유도\n'
            '· 시간대별 마케팅 최적화 데이터 수집\n'
            '· 운영자 코딩 없이 실시간 변경 가능'
        ),
        'timing': '팝업 운영 시간 전체 (시간대 자동 분리)',
    },
    {
        'no': 6,
        'en': 'Post & Win',
        'kr': 'SNS 인증 미션',
        'feature': '참여형 미션 + QR 인증 + 1st Party 데이터 수집',
        'scenario': (
            '① 팝업 포토존에서 제품 들고 촬영\n'
            '② Instagram / X에 지정 해시태그 업로드\n'
            '③ 업로드 URL 이벤트 페이지에 제출\n'
            '   → 즉시 인증 쿠폰 발급\n'
            '④ 베스트 포스트 선정\n'
            '   → 공식 SNS 리그램 + 추가 경품 증정'
        ),
        'reward': '즉시 쿠폰 / 베스트 포스트 선정 시 추가 경품',
        'kpi': '해시태그 게시물 수 / SNS 도달 수 / 인증 완료율',
        'target': '전 브랜드 공통\n특히 SNS 팔로워 적은 소규모 브랜드',
        'effect': (
            '· 브랜드 SNS 팔로워 유기적 증가\n'
            '· 팝업 현장 바이럴 확산 → 미방문자 유입 전환\n'
            '· SNS 계정 수집 = 향후 정밀 타겟팅 자산\n'
            '· UGC(사용자 생성 콘텐츠) 자동 확보'
        ),
        'timing': '팝업 전 기간 (상시)',
    },
    {
        'no': 7,
        'en': 'K-Beauty Lucky Raffle',
        'kr': '구매액 연동 라플 추첨',
        'feature': '라플(복권형 추첨) + 구매 실적 연동 응모권 누적',
        'scenario': (
            '① 1,000엔 구매 시 응모권 1장 자동 적립\n'
            '② 많이 살수록 당첨 확률 기하급수적 상승\n'
            '③ 팝업 마지막 날 라이브 추첨\n'
            '   (X / Instagram 라이브 연동)\n'
            '④ 1등: 한국 왕복 항공권 or 브랜드 풀키트\n'
            '⑤ 2~5등: 한정 세트 / 6~10등: 대용량 제품'
        ),
        'reward': '1등: 항공권·풀키트 / 2~5등: 한정세트 / 6~10등: 대용량 제품',
        'kpi': '총 구매 금액 / 평균 구매 단가 / 재방문율 / 라이브 시청자 수',
        'target': '롬앤, 마녀공장, COSRX\n단가 높은 세트 판매 브랜드',
        'effect': (
            '· 팝업 기간 내 재방문 + 추가 구매 강력 유도\n'
            '· 마지막 날 라이브로 SNS 화제성 극대화\n'
            '· 응모 과정 연락처 수집 = 1st Party 데이터 자산\n'
            '· "더 사면 더 유리하다" 심리로 객단가 자연 상승'
        ),
        'timing': '팝업 전 기간 누적 + 마지막 날 라이브 추첨',
    },
    {
        'no': 8,
        'en': 'Skin Type Advisor',
        'kr': 'AI 피부 타입 진단 & 맞춤 추천',
        'feature': 'AI 연동 + 퀴즈/설문 + 1st Party 데이터 수집',
        'scenario': (
            '① QR 진입 → 피부 타입 진단 설문\n'
            '   (건성 / 지성 / 복합 / 민감)\n'
            '② AI가 피부 타입에 맞는 제품 3가지 추천\n'
            '③ 진단 완료 시 추천 제품 전용 10% 쿠폰 발급\n'
            '④ 입력 데이터(피부 타입·고민·연령대)\n'
            '   브랜드 자산으로 안전 수집'
        ),
        'reward': '맞춤 제품 전용 10% 쿠폰 + 피부 타입별 샘플 증정',
        'kpi': '설문 완료율 / 추천 제품 구매 전환율 / 수집 데이터 건수',
        'target': 'Torriden, ISNTREE, Round Lab, manyo\n스킨케어 특화 브랜드',
        'effect': (
            '· "나를 위한 추천" → 구매 결정 허들 감소\n'
            '· 피부 타입 데이터 → 리타겟팅 광고 직결\n'
            '· 성분·제품 자연스럽게 교육\n'
            '· 고객 1인당 가장 많은 데이터 수집 가능'
        ),
        'timing': '팝업 입장 후 (자유 참여)',
    },
    {
        'no': 9,
        'en': 'K-Beauty Quiz Challenge',
        'kr': 'K뷰티 지식 퀴즈 이벤트',
        'feature': '퀴즈 게임 + 즉시 리워드 + 브랜드 콘텐츠 노출',
        'scenario': (
            '① 브랜드 관련 퀴즈 5문항 출제\n'
            '   (성분 효과, 제품 특징 등)\n'
            '② 전문 지식 없이도 도전 가능한 난이도\n'
            '③ 3개 정답: 샘플 증정\n'
            '④ 5개 전부: 풀사이즈 제품 쿠폰 발급\n'
            '⑤ 오답 시 "정답 해설 + 제품 정보" 자동 노출'
        ),
        'reward': '3개 정답: 샘플 / 5개 전부: 풀사이즈 제품 쿠폰',
        'kpi': '퀴즈 참여율 / 평균 정답률 / 퀴즈 후 제품 탐색율',
        'target': 'Beauty of Joseon(한방), COSRX(저자극),\nmanyo(갈락) 성분 스토리 강한 브랜드',
        'effect': (
            '· 브랜드 성분·철학 자연스럽게 교육\n'
            '· 오답 시 제품 정보 재노출 → 구매 관심 제고\n'
            '· 퀴즈 결과 SNS 공유 유도 → 바이럴 확산\n'
            '· 콘텐츠 제작 비용 최소화'
        ),
        'timing': '팝업 전 기간 (상시)',
    },
    {
        'no': 10,
        'en': 'Brand Hopping Reward',
        'kr': '합동 팝업 크로스 브랜드 챌린지',
        'feature': 'Double or Nothing + 스탬프 랠리\n+ LINE 소셜 커플링 복합 활용',
        'scenario': (
            '① 합동 팝업 (원정요 x CipiCipi x muice 등)\n'
            '② A브랜드 구매 인증\n'
            '   → 기본 리워드 + B브랜드 도전권\n'
            '③ B브랜드 구매 인증\n'
            '   → 리워드 2배 + C브랜드 도전권\n'
            '④ 전 브랜드 완료 → 그랜드 마스터 굿즈\n'
            '⑤ 각 브랜드 LINE 친구 추가 시 응모권 추가'
        ),
        'reward': 'A완료: 기본쿠폰 / AB: 2배쿠폰 / 전브랜드: 그랜드 마스터 굿즈',
        'kpi': '브랜드 간 크로스 구매율 / 전체 매출 / LINE 팔로워 증가',
        'target': '합동 팝업 전 브랜드\n(원정요·CipiCipi·muice·fwee 등)',
        'effect': (
            '· 단일 브랜드에서 다수 브랜드로 자연스러운 동선\n'
            '· 브랜드 간 크로스 셀링 매출 동시 견인\n'
            '· 소규모 브랜드 트래픽 대형 브랜드 후광 흡수\n'
            '· 공동 마케팅 비용 절감'
        ),
        'timing': '팝업 전 기간',
    },
    {
        'no': 11,
        'en': 'Limited Drop Queue',
        'kr': '한정 드랍 x 가상 대기실',
        'feature': '가상 대기실(Virtual Waiting Room)\n+ 트래픽 제어 + YouTube 삽입',
        'scenario': (
            '① 팝업 한정 제품을 특정 시간 드랍\n'
            '② 디프로모션 가상 대기실로 입장 순서 관리\n'
            '   → 공정한 구매 기회 보장\n'
            '③ 대기 중 브랜드 스토리 영상 노출\n'
            '   (YouTube 삽입 기능 활용)\n'
            '④ 대기 번호 SNS 공유 시\n'
            '   우선순위 소폭 상승 → 바이럴 유도'
        ),
        'reward': '한정 제품 구매 기회 (대기 번호순) + 대기 완료 쿠폰',
        'kpi': '대기 참여자 수 / 실제 구매 전환율 / SNS 공유 수',
        'target': 'TIRTIR(쿠션), LANEIGE(립세트)\n인기 한정품 보유 브랜드',
        'effect': (
            '· 한정품 드랍 → SNS 화제성 극대화\n'
            '· "줄 서는 브랜드" 이미지 → 희소성·프리미엄 구축\n'
            '· 대기 과정 자체가 SNS 콘텐츠화\n'
            '· 서버 다운 없이 안정적 트래픽 처리'
        ),
        'timing': '팝업 특정 시간 (드랍 이벤트)',
    },
]

# ── 열 정의 ───────────────────────────────────────────────
cols = [
    ('No',            4),
    ('이벤트명(영문)', 22),
    ('이벤트명(한글)', 20),
    ('활용 기능\n(디프로모션)', 26),
    ('이벤트 시나리오', 46),
    ('리워드 구성',    34),
    ('KPI 지표',       32),
    ('추천 브랜드',    28),
    ('기대 효과',      44),
    ('운영 타이밍',    26),
]

# ── 행 1: 메인 타이틀 ────────────────────────────────────
ws.merge_cells('A1:J1')
c = ws['A1']
c.value = '디프로모션 x K뷰티 팝업 이벤트 아이디어  |  총 11개'
c.font  = Font(name='Malgun Gothic', bold=True, size=14, color=HEADER_FG)
c.fill  = make_fill(HEADER_BG)
c.alignment = align('center', 'center')
c.border = thin
ws.row_dimensions[1].height = 36

# ── 행 2: 헤더 ──────────────────────────────────────────
for ci, (name, width) in enumerate(cols, 1):
    c = ws.cell(row=2, column=ci, value=name)
    c.font      = Font(name='Malgun Gothic', bold=True, size=10, color=HEADER_FG)
    c.fill      = make_fill(TITLE_BG)
    c.alignment = align('center', 'center')
    c.border    = thin
    ws.column_dimensions[get_column_letter(ci)].width = width
ws.row_dimensions[2].height = 34

# ── 행 3~: 데이터 ────────────────────────────────────────
for i, idea in enumerate(ideas):
    r = i + 3
    bg = make_fill(IDEA_BG[i % len(IDEA_BG)])

    vals = [
        idea['no'],
        idea['en'],
        idea['kr'],
        idea['feature'],
        idea['scenario'],
        idea['reward'],
        idea['kpi'],
        idea['target'],
        idea['effect'],
        idea['timing'],
    ]

    for ci, val in enumerate(vals, 1):
        c = ws.cell(row=r, column=ci, value=val)
        c.fill   = bg
        c.border = thin

        if ci == 1:   # No
            c.font      = Font(name='Malgun Gothic', bold=True, size=13, color=ACCENT)
            c.alignment = align('center', 'center')
        elif ci == 2: # 영문명
            c.font      = Font(name='Malgun Gothic', bold=True, size=10, color='1A1A2E')
            c.alignment = align('center', 'center')
        elif ci == 3: # 한글명
            c.font      = Font(name='Malgun Gothic', bold=True, size=10, color=GREEN)
            c.alignment = align('center', 'center')
        elif ci == 4: # 기능
            c.font      = Font(name='Malgun Gothic', size=9, color=PURPLE)
            c.alignment = align('center', 'center')
        else:
            c.font      = Font(name='Malgun Gothic', size=9, color='333333')
            c.alignment = align('left', 'top')

    ws.row_dimensions[r].height = 110

# ── 상단 고정 + 자동 필터 ────────────────────────────────
ws.freeze_panes = 'A3'
ws.auto_filter.ref = 'A2:J13'

# ── 인쇄 설정 ─────────────────────────────────────────────
ws.page_setup.orientation = 'landscape'
ws.page_setup.fitToPage   = True
ws.page_setup.fitToWidth  = 1
ws.print_title_rows = '1:2'

out = '/home/user/mypage/kbeauty_popup_events.xlsx'
wb.save(out)
print('saved:', out)
