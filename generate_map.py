#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Polygon as MplPolygon, FancyArrowPatch
import matplotlib.font_manager as fm
import matplotlib.patheffects as pe
import numpy as np

# Force reload fonts and set fallback chain
fm.fontManager.__init__()
plt.rcParams['font.sans-serif'] = ['NanumGothic', 'IPAGothic', 'WenQuanYi Zen Hei', 'DejaVu Sans']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

# ── Figure ──────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(1, 1, figsize=(15, 19))
ax.set_facecolor('#A8D8EA')   # sea
fig.patch.set_facecolor('#F0F4F8')

ax.set_xlim(127.48, 128.52)
ax.set_ylim(26.05, 27.02)
ax.set_aspect('equal')
ax.axis('off')

# ── Okinawa main island outline (approximate, lon=x, lat=y) ────────────────
island = np.array([
    # East coast – north
    [127.68, 26.09],
    [127.76, 26.15],
    [127.81, 26.22],
    [127.85, 26.32],
    [127.88, 26.42],
    [127.91, 26.52],
    [127.96, 26.60],
    [128.01, 26.66],
    [128.05, 26.73],
    [128.10, 26.78],
    [128.18, 26.83],
    [128.26, 26.87],   # Cape Hedo ▲
    # West coast – south
    [128.20, 26.84],
    [128.12, 26.79],
    [128.04, 26.73],
    [127.97, 26.68],
    # Motobu peninsula (bulge to the west)
    [127.94, 26.70],
    [127.91, 26.73],
    [127.88, 26.74],
    [127.86, 26.72],
    [127.85, 26.69],
    [127.87, 26.65],
    [127.90, 26.64],
    [127.92, 26.62],
    # Back to main west coast
    [127.90, 26.57],
    [127.84, 26.49],
    [127.79, 26.40],
    [127.75, 26.33],
    [127.72, 26.25],
    [127.68, 26.15],
    [127.66, 26.09],
])
ax.add_patch(MplPolygon(island, closed=True,
                         facecolor='#C8E6C9', edgecolor='#558B2F',
                         linewidth=2, zorder=2))

# Sesoko Island (small island off Motobu peninsula tip)
sesoko = np.array([
    [127.840, 26.634],
    [127.854, 26.637],
    [127.860, 26.648],
    [127.855, 26.657],
    [127.843, 26.658],
    [127.835, 26.648],
    [127.838, 26.637],
])
ax.add_patch(MplPolygon(sesoko, closed=True,
                          facecolor='#C8E6C9', edgecolor='#558B2F',
                          linewidth=1.5, zorder=2))

# Kouri Island
kouri = np.array([
    [128.006, 26.718],
    [128.022, 26.720],
    [128.030, 26.730],
    [128.025, 26.742],
    [128.010, 26.745],
    [128.001, 26.735],
    [128.003, 26.722],
])
ax.add_patch(MplPolygon(kouri, closed=True,
                          facecolor='#C8E6C9', edgecolor='#558B2F',
                          linewidth=1.5, zorder=2))

# ── Sea labels ───────────────────────────────────────────────────────────────
ax.text(127.55, 26.50, '동중국해', fontsize=11, color='#4A90A4',
        fontstyle='italic', alpha=0.7, zorder=3)
ax.text(128.35, 26.50, '태평양', fontsize=11, color='#4A90A4',
        fontstyle='italic', alpha=0.7, zorder=3)

# ── Kouri Bridge (dashed line) ───────────────────────────────────────────────
ax.plot([127.980, 128.006], [26.699, 26.718],
        color='#8B6914', linewidth=2, linestyle='--', zorder=3, alpha=0.8)
ax.text(127.970, 26.708, '고우리\n대교', fontsize=6.5, color='#8B6914',
        ha='center', zorder=4)

# ── Sesoko Bridge ────────────────────────────────────────────────────────────
ax.plot([127.862, 127.870], [26.648, 26.650],
        color='#8B6914', linewidth=2, linestyle='--', zorder=3, alpha=0.8)

# ── Route arrows ─────────────────────────────────────────────────────────────
# Day1: Naha → Sesoko
ax.annotate('', xy=(127.848, 26.638), xytext=(127.645, 26.195),
            arrowprops=dict(arrowstyle='->', color='#E74C3C',
                            lw=1.5, connectionstyle='arc3,rad=0.25'), zorder=4)

# Day4: Sesoko → American Village → Naha
ax.annotate('', xy=(127.757, 26.321), xytext=(127.848, 26.638),
            arrowprops=dict(arrowstyle='->', color='#E67E22',
                            lw=1.5, connectionstyle='arc3,rad=-0.2'), zorder=4)
ax.annotate('', xy=(127.660, 26.210), xytext=(127.757, 26.321),
            arrowprops=dict(arrowstyle='->', color='#E67E22',
                            lw=1.5, connectionstyle='arc3,rad=0.1'), zorder=4)

# ── Location data ─────────────────────────────────────────────────────────────
# (lon, lat, label_lines, color, text_offset_x, text_offset_y, ha)
locations = [
    # Day 1 / 4 — Red
    (127.645, 26.195,
     ['[출발/귀국] 나하 공항', '那覇空港', 'Day1 도착 · Day4 출발'],
     '#C0392B', -0.11, -0.06, 'right'),

    # Accommodation — Purple
    (127.848, 26.643,
     ['[숙소] 세소코섬 빌라', '(Sesoko Island)  3박'],
     '#7B1FA2', -0.16, 0.04, 'right'),

    # Day 2 — Blue
    (127.878, 26.696,
     ['추라우미 수족관', '(Churaumi Aquarium)', 'Day 2 오전'],
     '#1565C0', 0.06, 0.03, 'left'),

    (127.862, 26.704,
     ['비세 후쿠기 가로수길', '(Bise Fukugi Tree Road)', 'Day 2 오후'],
     '#1565C0', -0.16, 0.05, 'right'),

    (127.954, 26.684,
     ['나키진 성터', '(Nakijin Castle)  유네스코', 'Day 2 오후'],
     '#1565C0', 0.06, 0.01, 'left'),

    # Day 3 — Green
    (128.016, 26.728,
     ['고우리섬', '(Kouri Island)', 'Day 3'],
     '#2E7D32', 0.06, 0.02, 'left'),

    (128.021, 26.738,
     ['티누 해변 (하트 바위)', 'Day 3'],
     '#2E7D32', 0.06, -0.05, 'left'),

    # Day 4 — Orange
    (127.757, 26.321,
     ['아메리칸 빌리지', 'Day 4 오전'],
     '#E65100', 0.07, 0.03, 'left'),

    (127.668, 26.219,
     ['국제거리 · 마키시 시장', 'Day 4 오전'],
     '#E65100', -0.10, -0.07, 'right'),
]

day_colors = {
    'D1': '#C0392B', 'D2': '#1565C0',
    'D3': '#2E7D32', 'D4': '#E65100',
    'Stay': '#7B1FA2',
}

# Draw each location
for lon, lat, lines, color, dx, dy, ha in locations:
    # Marker circle
    circle = plt.Circle((lon, lat), 0.009,
                         facecolor=color, edgecolor='white',
                         linewidth=2.0, zorder=6)
    ax.add_patch(circle)

    # Text box
    label_txt = '\n'.join(lines)
    text_lon = lon + dx
    text_lat = lat + dy

    ax.annotate(
        label_txt,
        xy=(lon, lat),
        xytext=(text_lon, text_lat),
        fontsize=7.5,
        ha=ha,
        va='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                  edgecolor=color, alpha=0.93, linewidth=1.5),
        arrowprops=dict(arrowstyle='-', color=color, lw=1.2),
        zorder=7,
        linespacing=1.4,
    )

# Cape Hedo label
ax.text(128.265, 26.880, '▲ 헤도곶\n(최북단)',
        fontsize=7, ha='center', color='#555', zorder=5,
        bbox=dict(boxstyle='round', facecolor='#FFFDE7', edgecolor='#aaa',
                  alpha=0.85, linewidth=1))

# Sesoko beach marker
ax.text(127.832, 26.660, '~ 세소코\n비치', fontsize=6.5, ha='center', zorder=6,
        color='#0277BD', fontstyle='italic')

# ── Title ─────────────────────────────────────────────────────────────────────
ax.text(0.50, 0.985, '오키나와 3박4일 여행 코스',
        transform=ax.transAxes, fontsize=20, fontweight='bold',
        ha='center', va='top', color='#1A237E',
        path_effects=[pe.withStroke(linewidth=3, foreground='white')])
ax.text(0.50, 0.970, '5월 26일(화) ~ 5월 29일(금)  |  세소코섬 빌라 베이스',
        transform=ax.transAxes, fontsize=11, ha='center', va='top',
        color='#37474F',
        path_effects=[pe.withStroke(linewidth=2, foreground='white')])

# ── Legend ────────────────────────────────────────────────────────────────────
legend_items = [
    mpatches.Patch(facecolor='#C0392B', label='Day 1 (5/26)  도착 · 세소코 정착'),
    mpatches.Patch(facecolor='#1565C0', label='Day 2 (5/27)  북부 관광'),
    mpatches.Patch(facecolor='#2E7D32', label='Day 3 (5/28)  고우리섬 & 액티비티'),
    mpatches.Patch(facecolor='#E65100', label='Day 4 (5/29)  남부 관광 · 귀국'),
    mpatches.Patch(facecolor='#7B1FA2', label='[숙소] 세소코섬 빌라 (3박)'),
]
legend = ax.legend(handles=legend_items, loc='lower left',
                   fontsize=9.5, framealpha=0.95,
                   edgecolor='#90A4AE', fancybox=True,
                   title='■ 일정 범례', title_fontsize=10)
legend.get_frame().set_linewidth(1.5)

# ── North Arrow ──────────────────────────────────────────────────────────────
ax.annotate('', xy=(0.96, 0.20), xytext=(0.96, 0.15),
            xycoords='axes fraction',
            arrowprops=dict(arrowstyle='->', color='#333', lw=2))
ax.text(0.96, 0.21, 'N', transform=ax.transAxes,
        fontsize=12, fontweight='bold', ha='center', color='#333')

# ── Scale bar (rough) ────────────────────────────────────────────────────────
# 0.1° lon ≈ ~9.5 km at 26°N
ax.plot([128.28, 128.38], [26.13, 26.13], color='#333', lw=2.5, zorder=5)
ax.text(128.33, 26.115, '약 10km', fontsize=7.5, ha='center', color='#333', zorder=5)

# ── Border ───────────────────────────────────────────────────────────────────
for spine in ax.spines.values():
    spine.set_visible(False)

fig.tight_layout(pad=1.0)
out = '/home/user/mypage/okinawa_travel_map.png'
fig.savefig(out, dpi=160, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.close()
print(f"Saved: {out}")
