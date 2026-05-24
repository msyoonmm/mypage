#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe

fm.fontManager.__init__()
plt.rcParams['font.sans-serif'] = ['NanumGothic', 'IPAGothic', 'DejaVu Sans']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

# ── A4 사이즈 (가로 21cm × 세로 29.7cm, 100dpi 기준 약 8.27×11.69인치) ──
fig, ax = plt.subplots(figsize=(8.27, 11.69))
fig.patch.set_facecolor('#FFFFFF')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# ── 색상 팔레트 ────────────────────────────────────────────────────────────
C = {
    'd1': '#C0392B', 'd2': '#1565C0', 'd3': '#2E7D32',
    'd4': '#E65100', 'stay': '#7B1FA2',
    'bg': '#F8F9FC', 'hdr': '#1A237E', 'sub': '#37474F',
    'line': '#CFD8DC',
}

def box(x, y, w, h, fc, ec='none', lw=0, radius=1.5, zorder=1):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle=f'round,pad=0,rounding_size={radius}',
                                facecolor=fc, edgecolor=ec, linewidth=lw, zorder=zorder))

def txt(x, y, s, fs=9, fw='normal', color='#222', ha='left', va='center', z=5):
    ax.text(x, y, s, fontsize=fs, fontweight=fw, color=color,
            ha=ha, va=va, zorder=z)

# ── 배경 ───────────────────────────────────────────────────────────────────
box(0, 0, 100, 100, C['bg'], zorder=0)

# ── 헤더 ───────────────────────────────────────────────────────────────────
box(0, 88, 100, 12, C['hdr'], radius=0, zorder=1)
txt(50, 95.5, '오키나와 3박4일 여행 일정표', fs=22, fw='bold', color='white', ha='center')
txt(50, 91,   '5월 26일(화) ~ 5월 29일(금)  |  세소코섬 빌라 베이스  |  Eastar Jet ZE631/632',
    fs=10, fw='bold', color='#B3C8F0', ha='center')

# ── 항공 정보 배너 ─────────────────────────────────────────────────────────
box(2, 84.5, 96, 3.0, '#E3F2FD', ec='#90CAF9', lw=1, radius=1, zorder=2)
txt(3.5, 86.0, '출발  5/26(화)  ICN → OKA  11:30 - 14:00  ZE631', fs=9.5, fw='bold', color='#1565C0')
txt(55,  86.0, '귀국  5/29(금)  OKA → ICN  15:00 - 17:35  ZE632', fs=9.5, fw='bold', color='#C0392B')
txt(50,  86.0, '|', fs=9.5, color='#90CAF9', ha='center')

# ── 일정 데이터 ────────────────────────────────────────────────────────────
schedule = [
    {
        'day': 'Day 1', 'date': '5월 26일 (화)', 'title': '나하 도착 → 세소코 정착',
        'color': C['d1'],
        'items': [
            ('14:00', '나하 공항 도착 / 렌터카 수령'),
            ('14:30', '오키나와 자동차도로 북상 (약 1시간 30분)'),
            ('16:30', '세소코섬 빌라 체크인'),
            ('17:30', '세소코 비치 산책 & 석양 감상'),
            ('19:00', '모토부 현지 식당 저녁 (오키나와 소바 추천)'),
        ]
    },
    {
        'day': 'Day 2', 'date': '5월 27일 (수)', 'title': '북부 핵심 관광',
        'color': C['d2'],
        'items': [
            ('08:30', '추라우미 수족관 (세계 최대급, 빌라에서 10분)'),
            ('11:00', '오션 엑스포 공원 관람'),
            ('13:00', '비세 후쿠기 가로수길 근처 카페 점심'),
            ('14:00', '비세 후쿠기 가로수길 (수백 년 나무 터널)'),
            ('15:30', '나키진 성터 (유네스코 세계문화유산, 바다 전망)'),
            ('18:00', '세소코 귀환 / 해산물 저녁'),
        ]
    },
    {
        'day': 'Day 3', 'date': '5월 28일 (목)', 'title': '고우리섬 & 아메리칸 빌리지 쇼핑',
        'color': C['d3'],
        'items': [
            ('09:00', '고우리 대교 드라이브 (에메랄드 바다 위 2km 다리)'),
            ('09:30', '티누 해변 (하트 바위 포토스팟)'),
            ('11:00', '고우리섬 점심 (고우리 새우 요리)'),
            ('13:00', '아메리칸 빌리지 쇼핑몰 이동 (약 1시간 30분)'),
            ('14:30', '아메리칸 빌리지 쇼핑 & 포토스팟'),
            ('18:00', '세소코 귀환'),
        ]
    },
    {
        'day': 'Day 4', 'date': '5월 29일 (금)', 'title': '국제거리 관광 → 귀국',
        'color': C['d4'],
        'items': [
            ('08:00', '세소코 빌라 체크아웃 / 남하'),
            ('10:00', '국제거리 쇼핑 (기념품)'),
            ('11:00', '마키시 공설시장 점심 (2층 해산물 정식)'),
            ('12:45', '렌터카 반납 & 나하 공항 이동'),
            ('13:00', '나하 공항 도착 / 탑승 수속'),
            ('15:00', 'OKA 출발 → ICN 17:35 도착'),
        ]
    },
]

# ── 각 Day 카드 배치 ────────────────────────────────────────────────────────
card_h   = 18.5      # 카드 높이
card_gap = 1.5       # 카드 간격
y_start  = 82.5      # 첫 카드 상단 y

for di, day in enumerate(schedule):
    y_top = y_start - di * (card_h + card_gap)
    color = day['color']

    # 카드 배경
    box(2, y_top - card_h, 96, card_h, 'white', ec=color, lw=1.2, radius=1.5, zorder=2)

    # 좌측 색상 바
    box(2, y_top - card_h, 3.5, card_h, color, radius=1.5, zorder=3)

    # Day 라벨 (세로 중앙, 세로 쓰기 느낌으로 두 줄)
    txt(3.75, y_top - card_h * 0.38, day['day'],
        fs=11, fw='bold', color='white', ha='center', va='center', z=4)
    txt(3.75, y_top - card_h * 0.62, day['date'][:5],  # "5월 26"
        fs=7.5, fw='bold', color='#FFD0CC' if color == C['d1'] else
                           '#B3C8F0' if color == C['d2'] else
                           '#A5D6A7' if color == C['d3'] else '#FFCCBC',
        ha='center', va='center', z=4)

    # 제목 줄
    box(5.5, y_top - 4.2, 92.5, 4.0, color, radius=0, zorder=3)
    # 날짜
    txt(7, y_top - 2.2, day['date'], fs=9, fw='bold', color=(1, 1, 1, 0.75),
        ha='left', va='center', z=4)
    # 제목
    txt(23, y_top - 2.2, day['title'], fs=12, fw='bold', color='white',
        ha='left', va='center', z=4)

    # 일정 항목
    row_h = (card_h - 4.5) / len(day['items'])
    for ri, (time_s, desc) in enumerate(day['items']):
        ry = y_top - 4.5 - ri * row_h - row_h * 0.5

        # 홀짝 줄 배경
        if ri % 2 == 0:
            box(5.5, y_top - 4.5 - ri * row_h - row_h, 92.5, row_h,
                '#F5F5F5', radius=0, zorder=2)

        # 시간 뱃지
        box(6.5, ry - 1.1, 9, 2.2, color + '22', radius=0.8, zorder=3)
        txt(11, ry, time_s, fs=9, fw='bold', color=color, ha='center', va='center', z=4)

        # 설명
        txt(17.5, ry, desc, fs=9.5, fw='bold', color='#222', ha='left', va='center', z=4)

# ── 숙소 정보 배너 ─────────────────────────────────────────────────────────
y_stay = y_start - 4 * (card_h + card_gap) + 0.5
box(2, y_stay - 4.5, 96, 4.5, '#F3E5F5', ec=C['stay'], lw=1.2, radius=1.5, zorder=2)
box(2, y_stay - 4.5, 3.5, 4.5, C['stay'], radius=1.5, zorder=3)
txt(3.75, y_stay - 2.25, '숙소', fs=9, fw='bold', color='white', ha='center', z=4)
txt(7, y_stay - 1.5, '세소코섬 빌라  (3박)',
    fs=11, fw='bold', color=C['stay'], ha='left', z=4)
txt(7, y_stay - 3.3,
    '주소: Okinawa, Motobu-cho, Sesoko 498-3  |  렌터카 필수 (세소코섬은 다리로 연결)',
    fs=9, fw='bold', color='#555', ha='left', z=4)

# ── 하단 Tips 박스 ─────────────────────────────────────────────────────────
y_tip = y_stay - 5.5
box(2, y_tip - 5.2, 96, 5.0, '#FFFDE7', ec='#F9A825', lw=1.2, radius=1.5, zorder=2)
txt(50, y_tip - 0.9, '여행 꿀팁', fs=11, fw='bold', color='#F57F17', ha='center', z=4)
tips = [
    '렌터카: 나하 공항 도착 즉시 수령 (북부는 대중교통 불편)',
    '날씨: 5월 말은 장마 초입 — 우비/우산 필수, 맑은 날 스노클링 최고',
    '추라우미 수족관: 오전 일찍 입장 추천 (오후 혼잡)',
    '고우리 새우: 고우리섬 내 양식장 식당에서 갓잡은 신선 새우 추천',
]
for ti, tip in enumerate(tips):
    txt(4, y_tip - 2.0 - ti * 0.95, f'• {tip}', fs=8.5, fw='bold', color='#555', z=4)

# ── 하단 여백 ──────────────────────────────────────────────────────────────
txt(50, 0.6, '예약번호: VFZ8ME  |  Eastar Jet ZE631 / ZE632',
    fs=8.5, fw='bold', color='#999', ha='center', z=4)

fig.tight_layout(pad=0)
out_pdf = '/home/user/mypage/okinawa_schedule.pdf'
out_png = '/home/user/mypage/okinawa_schedule.png'
fig.savefig(out_pdf, dpi=200, bbox_inches='tight', facecolor='white')
fig.savefig(out_png, dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Saved: {out_pdf}, {out_png}")
