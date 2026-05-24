#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Polygon as MplPolygon
import matplotlib.font_manager as fm
import matplotlib.patheffects as pe
import numpy as np

fm.fontManager.__init__()
plt.rcParams['font.sans-serif'] = ['NanumGothic', 'IPAGothic', 'WenQuanYi Zen Hei', 'DejaVu Sans']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

# ── Figure: map (top) + legend strip (bottom) ─────────────────────────────
fig = plt.figure(figsize=(15, 22))
fig.patch.set_facecolor('#F0F4F8')

# Map axes: leaves room for legend panel at bottom
ax = fig.add_axes([0.02, 0.16, 0.96, 0.82])
ax.set_facecolor('#A8D8EA')
ax.set_xlim(127.45, 128.55)
ax.set_ylim(26.04, 27.02)
ax.set_aspect('equal')
ax.axis('off')

# Legend axes below map (taller)
ax_leg = fig.add_axes([0.02, 0.01, 0.96, 0.14])
ax_leg.axis('off')
ax_leg.set_facecolor('#EEF2F7')
ax_leg.add_patch(plt.Rectangle((0, 0), 1, 1, transform=ax_leg.transAxes,
                                facecolor='#EEF2F7', edgecolor='#90A4AE',
                                linewidth=1.5, zorder=0))

# ── Okinawa main island ────────────────────────────────────────────────────
island = np.array([
    [127.68, 26.09], [127.76, 26.15], [127.81, 26.22],
    [127.85, 26.32], [127.88, 26.42], [127.91, 26.52],
    [127.96, 26.60], [128.01, 26.66], [128.05, 26.73],
    [128.10, 26.78], [128.18, 26.83], [128.26, 26.87],
    [128.20, 26.84], [128.12, 26.79], [128.04, 26.73],
    [127.97, 26.68],
    [127.94, 26.70], [127.91, 26.73], [127.88, 26.74],
    [127.86, 26.72], [127.85, 26.69], [127.87, 26.65],
    [127.90, 26.64], [127.92, 26.62],
    [127.90, 26.57], [127.84, 26.49], [127.79, 26.40],
    [127.75, 26.33], [127.72, 26.25], [127.68, 26.15],
    [127.66, 26.09],
])
ax.add_patch(MplPolygon(island, closed=True,
                         facecolor='#C8E6C9', edgecolor='#558B2F',
                         linewidth=2, zorder=2))

# Sesoko Island
sesoko = np.array([
    [127.840, 26.634], [127.854, 26.637], [127.860, 26.648],
    [127.855, 26.657], [127.843, 26.658], [127.835, 26.648],
    [127.838, 26.637],
])
ax.add_patch(MplPolygon(sesoko, closed=True,
                          facecolor='#C8E6C9', edgecolor='#558B2F',
                          linewidth=1.5, zorder=2))

# Kouri Island
kouri = np.array([
    [128.006, 26.718], [128.022, 26.720], [128.030, 26.730],
    [128.025, 26.742], [128.010, 26.745], [128.001, 26.735],
    [128.003, 26.722],
])
ax.add_patch(MplPolygon(kouri, closed=True,
                          facecolor='#C8E6C9', edgecolor='#558B2F',
                          linewidth=1.5, zorder=2))

# ── Sea labels ────────────────────────────────────────────────────────────
ax.text(127.53, 26.52, '동중국해', fontsize=11, color='#4A90A4',
        fontstyle='italic', alpha=0.75, zorder=3)
ax.text(128.38, 26.50, '태평양', fontsize=11, color='#4A90A4',
        fontstyle='italic', alpha=0.75, zorder=3)

# ── Bridges ───────────────────────────────────────────────────────────────
ax.plot([127.980, 128.006], [26.699, 26.718],
        color='#8B6914', linewidth=2, linestyle='--', zorder=3, alpha=0.8)
ax.text(127.968, 26.707, '고우리대교', fontsize=6.5, color='#8B6914',
        ha='center', zorder=4)
ax.plot([127.862, 127.870], [26.648, 26.650],
        color='#8B6914', linewidth=2, linestyle='--', zorder=3, alpha=0.8)

# ── Route arrows ──────────────────────────────────────────────────────────
# Day 1: 공항 → 세소코
ax.annotate('', xy=(127.848, 26.638), xytext=(127.645, 26.195),
            arrowprops=dict(arrowstyle='->', color='#C0392B',
                            lw=1.8, connectionstyle='arc3,rad=0.28'), zorder=4)
# Day 3: 고우리섬 → 아메리칸 빌리지 (북→남)
ax.annotate('', xy=(127.757, 26.321), xytext=(128.016, 26.728),
            arrowprops=dict(arrowstyle='->', color='#2E7D32',
                            lw=1.8, connectionstyle='arc3,rad=0.30'), zorder=4)
# Day 4: 세소코 → 국제거리/공항
ax.annotate('', xy=(127.668, 26.219), xytext=(127.848, 26.638),
            arrowprops=dict(arrowstyle='->', color='#E65100',
                            lw=1.8, connectionstyle='arc3,rad=-0.15'), zorder=4)
# Day 4: 국제거리 → 공항
ax.annotate('', xy=(127.645, 26.195), xytext=(127.668, 26.219),
            arrowprops=dict(arrowstyle='->', color='#E65100',
                            lw=1.5, connectionstyle='arc3,rad=0.0'), zorder=4)

# ── Locations ─────────────────────────────────────────────────────────────
# (lon, lat, label_lines, dot_color, text_x, text_y, ha, va)
locations = [
    # Day 1/4 — 나하 공항 (라벨을 왼쪽 아래로 멀리)
    (127.645, 26.195,
     ['나하 공항', 'Day1 도착 / Day4 출발'],
     '#C0392B', 127.510, 26.115, 'left', 'center'),

    # 숙소 — 세소코섬
    (127.848, 26.643,
     ['세소코섬 빌라', '(숙소 · 3박)'],
     '#7B1FA2', 127.680, 26.660, 'right', 'center'),

    # Day 2 — 추라우미 수족관
    (127.878, 26.696,
     ['추라우미 수족관', 'Day 2 오전'],
     '#1565C0', 127.960, 26.715, 'left', 'center'),

    # Day 2 — 비세 후쿠기 가로수길
    (127.862, 26.704,
     ['비세 후쿠기 가로수길', 'Day 2 오후'],
     '#1565C0', 127.690, 26.745, 'right', 'center'),

    # Day 2 — 나키진 성터
    (127.954, 26.684,
     ['나키진 성터 (유네스코)', 'Day 2 오후'],
     '#1565C0', 128.060, 26.665, 'left', 'center'),

    # Day 3 — 고우리섬
    (128.016, 26.728,
     ['고우리섬', 'Day 3 오전'],
     '#2E7D32', 128.130, 26.740, 'left', 'center'),

    # Day 3 — 티누 해변
    (128.021, 26.738,
     ['티누 해변 (하트 바위)', 'Day 3 오전'],
     '#2E7D32', 128.130, 26.770, 'left', 'center'),

    # Day 3 — 아메리칸 빌리지 (오후 이동)
    (127.757, 26.321,
     ['아메리칸 빌리지 쇼핑몰', 'Day 3 오후'],
     '#2E7D32', 127.870, 26.330, 'left', 'center'),

    # Day 4 — 국제거리 (나하 공항과 분리: 오른쪽 위로)
    (127.668, 26.219,
     ['국제거리 · 마키시 시장', 'Day 4 오전'],
     '#E65100', 127.820, 26.255, 'left', 'center'),
]

for lon, lat, lines, color, tx, ty, ha, va in locations:
    ax.add_patch(plt.Circle((lon, lat), 0.010,
                             facecolor=color, edgecolor='white',
                             linewidth=2.2, zorder=6))
    ax.annotate(
        '\n'.join(lines),
        xy=(lon, lat), xytext=(tx, ty),
        fontsize=8.5, ha=ha, va=va,
        bbox=dict(boxstyle='round,pad=0.45', facecolor='white',
                  edgecolor=color, alpha=0.95, linewidth=1.8),
        arrowprops=dict(arrowstyle='-', color=color, lw=1.3),
        zorder=8,
        linespacing=1.5,
    )

# ── Extra map decorations ─────────────────────────────────────────────────
ax.text(128.265, 26.883, '▲ 헤도곶 (최북단)',
        fontsize=7.5, ha='center', color='#444', zorder=5,
        bbox=dict(boxstyle='round', facecolor='#FFFDE7',
                  edgecolor='#aaa', alpha=0.88, linewidth=1))

ax.text(127.828, 26.665, '세소코\n비치', fontsize=6.5, ha='center',
        color='#0277BD', fontstyle='italic', zorder=5)

# ── Title ─────────────────────────────────────────────────────────────────
ax.text(0.50, 0.993, '오키나와 3박4일 여행 코스',
        transform=ax.transAxes, fontsize=21, fontweight='bold',
        ha='center', va='top', color='#1A237E',
        path_effects=[pe.withStroke(linewidth=4, foreground='white')])
ax.text(0.50, 0.977, '5월 26일(화) ~ 5월 29일(금)  |  세소코섬 빌라 베이스',
        transform=ax.transAxes, fontsize=11.5, ha='center', va='top',
        color='#37474F',
        path_effects=[pe.withStroke(linewidth=2, foreground='white')])

# ── North arrow ────────────────────────────────────────────────────────────
ax.annotate('', xy=(0.965, 0.17), xytext=(0.965, 0.12),
            xycoords='axes fraction',
            arrowprops=dict(arrowstyle='->', color='#333', lw=2.2))
ax.text(0.965, 0.18, 'N', transform=ax.transAxes,
        fontsize=13, fontweight='bold', ha='center', color='#333')

# ── Scale bar ──────────────────────────────────────────────────────────────
ax.plot([128.30, 128.40], [26.100, 26.100], color='#333', lw=3, zorder=5)
ax.text(128.35, 26.082, '약 10km', fontsize=8, ha='center', color='#333', zorder=5)

# ── Legend panel — 2행 3열 그리드 ────────────────────────────────────────
# 행 1: Day1, Day2, Day3  /  행 2: Day4, 숙소
legend_data = [
    ('#C0392B', 'Day 1  (5/26)', '나하 도착 → 세소코 정착'),
    ('#1565C0', 'Day 2  (5/27)', '추라우미 수족관 · 비세 가로수길 · 나키진 성터'),
    ('#2E7D32', 'Day 3  (5/28)', '고우리섬 · 티누 해변 → 아메리칸 빌리지 쇼핑'),
    ('#E65100', 'Day 4  (5/29)', '국제거리 · 마키시 시장 → 귀국'),
    ('#7B1FA2', '숙소',          '세소코섬 빌라 (3박 4일)'),
]

# 타이틀
ax_leg.text(0.50, 0.97, '■ 일정 범례',
            transform=ax_leg.transAxes, fontsize=10.5, fontweight='bold',
            ha='center', va='top', color='#1A237E')

# 그리드: 3열 × 2행
cols = 3
rows = 2
cell_w = 1.0 / cols
cell_h = 0.42   # 전체 높이에서 각 행이 차지하는 비율

rect_w  = 0.022   # 색상 박스 너비 (axes fraction)
rect_h  = 0.28    # 색상 박스 높이
pad_l   = 0.015   # 셀 왼쪽 여백
txt_gap = 0.030   # 박스~텍스트 간격

for i, (color, day_lbl, detail_lbl) in enumerate(legend_data):
    col = i % cols
    row = i // cols

    x0 = col * cell_w + pad_l
    y0 = 0.72 - row * cell_h   # 첫 행 y 중심

    # 색상 박스
    ax_leg.add_patch(plt.Rectangle(
        (x0, y0 - rect_h / 2), rect_w, rect_h,
        transform=ax_leg.transAxes,
        facecolor=color, edgecolor='white', linewidth=1.2, zorder=2,
    ))

    # 굵은 날짜 라벨
    ax_leg.text(x0 + rect_w + txt_gap, y0 + 0.05, day_lbl,
                transform=ax_leg.transAxes,
                fontsize=9, fontweight='bold', va='center', color=color)

    # 일반 설명
    ax_leg.text(x0 + rect_w + txt_gap, y0 - 0.13, detail_lbl,
                transform=ax_leg.transAxes,
                fontsize=8, va='center', color='#444')

fig.savefig('/home/user/mypage/okinawa_travel_map.png',
            dpi=160, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.close()
print("Saved.")
