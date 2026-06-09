from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import copy

# Color palette
DARK_GREEN = RGBColor(0x1A, 0x5C, 0x38)
MID_GREEN = RGBColor(0x2E, 0x86, 0x48)
LIGHT_GREEN = RGBColor(0x6A, 0xB0, 0x4C)
PALE_GREEN = RGBColor(0xE8, 0xF5, 0xE9)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
DARK_GRAY = RGBColor(0x33, 0x33, 0x33)
MID_GRAY = RGBColor(0x66, 0x66, 0x66)
LIGHT_GRAY = RGBColor(0xF5, 0xF5, 0xF5)
ACCENT_ORANGE = RGBColor(0xFF, 0x8C, 0x00)
ACCENT_BLUE = RGBColor(0x1D, 0xA1, 0xF2)

prs = Presentation()
prs.slide_width = Inches(13.33)
prs.slide_height = Inches(7.5)

blank_layout = prs.slide_layouts[6]  # blank


def add_rect(slide, l, t, w, h, color, alpha=None):
    shape = slide.shapes.add_shape(1, Inches(l), Inches(t), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape


def add_textbox(slide, text, l, t, w, h, font_size=14, bold=False, color=DARK_GRAY,
                align=PP_ALIGN.LEFT, italic=False, wrap=True):
    txBox = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    txBox.word_wrap = wrap
    tf = txBox.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return txBox


def add_slide_header(slide, title, subtitle=None):
    # Top bar
    add_rect(slide, 0, 0, 13.33, 1.1, DARK_GREEN)
    # Logo text area
    add_textbox(slide, "천호앤케어", 0.3, 0.05, 2.5, 0.5, font_size=13, bold=True, color=WHITE)
    add_textbox(slide, "Japan Qoo10 마케팅 전략", 0.3, 0.52, 4, 0.45, font_size=10, color=RGBColor(0xA5, 0xD6, 0xA7))
    # Title
    add_textbox(slide, title, 3.5, 0.08, 9.0, 0.6, font_size=22, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    if subtitle:
        add_textbox(slide, subtitle, 3.5, 0.65, 9.0, 0.38, font_size=11, color=RGBColor(0xC8, 0xE6, 0xC9), align=PP_ALIGN.CENTER)
    # Bottom accent line
    add_rect(slide, 0, 7.3, 13.33, 0.2, MID_GREEN)
    # Page indicator bg
    add_rect(slide, 12.5, 7.25, 0.83, 0.25, LIGHT_GREEN)


def add_table_row(slide, cols, l, t, w, h, bg_color, text_color=DARK_GRAY, font_size=11, bold=False):
    col_w = w / len(cols)
    for i, text in enumerate(cols):
        add_rect(slide, l + i * col_w, t, col_w - 0.03, h, bg_color)
        add_textbox(slide, text, l + i * col_w + 0.05, t + 0.03, col_w - 0.13, h - 0.06,
                    font_size=font_size, bold=bold, color=text_color, align=PP_ALIGN.CENTER)


# ─────────────────────────────────────────────
# SLIDE 1: Cover
# ─────────────────────────────────────────────
slide1 = prs.slides.add_slide(blank_layout)

add_rect(slide1, 0, 0, 13.33, 7.5, DARK_GREEN)
add_rect(slide1, 0, 0, 13.33, 7.5, RGBColor(0x0D, 0x3D, 0x20))  # overlay

# Decorative circles
for x, y, sz, op in [(10.5, 1.0, 3.5, 20), (1.0, 5.5, 2.5, 15), (7.0, 5.8, 1.8, 12)]:
    c = slide1.shapes.add_shape(9, Inches(x), Inches(y), Inches(sz), Inches(sz))
    c.fill.solid()
    c.fill.fore_color.rgb = LIGHT_GREEN
    c.line.fill.background()

# Accent bar
add_rect(slide1, 1.0, 2.8, 0.15, 2.0, LIGHT_GREEN)

# Brand name
add_textbox(slide1, "천호앤케어 (ChunHo N Care)", 1.4, 2.7, 10, 0.7, font_size=16, bold=False, color=RGBColor(0xA5, 0xD6, 0xA7))

# Main title
add_textbox(slide1, "일본 Qoo10 마케팅\n예산 운영 제안서", 1.4, 3.3, 10, 1.8, font_size=38, bold=True, color=WHITE)

# Subtitle
add_textbox(slide1, "검색 노출 확대 · 신규 고객 유입 · 브랜드 인지도 구축 · 크루 모집 UGC 전략",
            1.4, 5.1, 10.5, 0.5, font_size=13, color=RGBColor(0xC8, 0xE6, 0xC9))

# Date
add_textbox(slide1, "2026년 6월", 1.4, 6.5, 4, 0.4, font_size=12, color=RGBColor(0x81, 0xC7, 0x84))

# ─────────────────────────────────────────────
# SLIDE 2: 캠페인 목적
# ─────────────────────────────────────────────
slide2 = prs.slides.add_slide(blank_layout)
add_rect(slide2, 0, 0, 13.33, 7.5, WHITE)
add_slide_header(slide2, "캠페인 목적", "Japan Market Entry Strategy")

goals = [
    ("🔍", "검색 노출 확대", "Qoo10 내 키워드 기반 검색 노출 극대화\n상위 랭킹 확보로 브랜드 가시성 향상"),
    ("👥", "신규 고객 유입", "구매 의도가 높은 고객군 타겟팅\n전환율 높은 채널 집중 운영"),
    ("📣", "브랜드 인지도", "SNS 기반 일본 여성 소비자 공략\nInstagram · X 동시 운영"),
    ("🤝", "크루(어필리에이터) 모집", "UGC 콘텐츠 확보\n리뷰 기반 자연 바이럴 확산"),
    ("📈", "자연 유입 확대", "광고 의존도 단계적 축소\n장기적 오가닉 트래픽 구축"),
]

for i, (icon, title, desc) in enumerate(goals):
    col = i % 3
    row = i // 3
    lx = 0.4 + col * 4.3
    ty = 1.4 + row * 2.8

    add_rect(slide2, lx, ty, 4.0, 2.4, PALE_GREEN)
    add_rect(slide2, lx, ty, 4.0, 0.08, MID_GREEN)

    add_textbox(slide2, icon + " " + title, lx + 0.15, ty + 0.15, 3.7, 0.45,
                font_size=13, bold=True, color=DARK_GREEN)
    add_textbox(slide2, desc, lx + 0.15, ty + 0.65, 3.7, 1.5,
                font_size=10.5, color=DARK_GRAY)

# ─────────────────────────────────────────────
# SLIDE 3: Qoo10 광고 – 키워드 플러스
# ─────────────────────────────────────────────
slide3 = prs.slides.add_slide(blank_layout)
add_rect(slide3, 0, 0, 13.33, 7.5, WHITE)
add_slide_header(slide3, "Qoo10 광고 ① 키워드 플러스", "구매 의도 고객 직접 공략 – 가장 높은 전환율")

# Left: 현황
add_rect(slide3, 0.3, 1.25, 5.8, 5.8, PALE_GREEN)
add_rect(slide3, 0.3, 1.25, 5.8, 0.45, DARK_GREEN)
add_textbox(slide3, "현재 현황", 0.45, 1.28, 5.5, 0.38, font_size=13, bold=True, color=WHITE)

stats = [
    ("검색량", "1,008회 / 일"),
    ("입찰 수", "13개"),
    ("예상 노출 순위", "16위"),
]
for i, (k, v) in enumerate(stats):
    ty = 1.85 + i * 0.65
    add_rect(slide3, 0.4, ty, 5.6, 0.55, WHITE)
    add_textbox(slide3, k, 0.55, ty + 0.07, 2.5, 0.4, font_size=11, color=MID_GRAY)
    add_textbox(slide3, v, 3.2, ty + 0.07, 2.6, 0.4, font_size=12, bold=True, color=DARK_GREEN, align=PP_ALIGN.RIGHT)

add_textbox(slide3, "경쟁 입찰가 현황", 0.45, 3.95, 5.5, 0.38, font_size=12, bold=True, color=DARK_GREEN)
bid_rows = [
    ("상위권", "10,000엔", DARK_GREEN, WHITE),
    ("중위권", "6,000 ~ 7,000엔", MID_GREEN, WHITE),
    ("하위권", "1,500 ~ 2,000엔", LIGHT_GREEN, WHITE),
]
for i, (label, price, bg, fg) in enumerate(bid_rows):
    ty = 4.4 + i * 0.62
    add_rect(slide3, 0.4, ty, 5.6, 0.55, bg)
    add_textbox(slide3, label, 0.55, ty + 0.08, 2.5, 0.38, font_size=11, bold=True, color=fg)
    add_textbox(slide3, price, 3.1, ty + 0.08, 2.7, 0.38, font_size=11, bold=True, color=fg, align=PP_ALIGN.RIGHT)

# Right: 추천 키워드
add_rect(slide3, 6.4, 1.25, 6.6, 5.8, LIGHT_GRAY)
add_rect(slide3, 6.4, 1.25, 6.6, 0.45, MID_GREEN)
add_textbox(slide3, "추천 키워드", 6.55, 1.28, 6.3, 0.38, font_size=13, bold=True, color=WHITE)

keywords = [
    ("화이트토마토", "白トマト / 飲む日焼け止め"),
    ("레몬즙", "レモン汁 / レモン水 / デトックス"),
    ("녹차카테킨", "緑茶カテキン / ダイエット / 脂肪対策"),
    ("이너뷰티", "インナービューティー / 紫外線対策"),
]
for i, (ko, jp) in enumerate(keywords):
    ty = 1.85 + i * 0.85
    add_rect(slide3, 6.5, ty, 6.3, 0.75, WHITE)
    add_rect(slide3, 6.5, ty, 0.07, 0.75, MID_GREEN)
    add_textbox(slide3, ko, 6.7, ty + 0.05, 5.9, 0.3, font_size=12, bold=True, color=DARK_GREEN)
    add_textbox(slide3, jp, 6.7, ty + 0.35, 5.9, 0.3, font_size=10, color=MID_GRAY)

# Budget box
add_rect(slide3, 6.4, 5.45, 6.6, 1.5, DARK_GREEN)
add_textbox(slide3, "예상 월 예산", 6.6, 5.5, 6.1, 0.4, font_size=12, bold=True, color=WHITE)
add_textbox(slide3, "20만원 ~ 30만원", 6.6, 5.92, 6.1, 0.6, font_size=26, bold=True, color=ACCENT_ORANGE, align=PP_ALIGN.CENTER)

# ─────────────────────────────────────────────
# SLIDE 4: Qoo10 광고 – 파워 링크업 & 총합
# ─────────────────────────────────────────────
slide4 = prs.slides.add_slide(blank_layout)
add_rect(slide4, 0, 0, 13.33, 7.5, WHITE)
add_slide_header(slide4, "Qoo10 광고 ② 파워 링크업 & 총 예산", "대표 상품 3개 고정 노출로 브랜드 인지도 확보")

# Left: 파워 링크업
add_rect(slide4, 0.3, 1.25, 6.0, 5.8, PALE_GREEN)
add_rect(slide4, 0.3, 1.25, 6.0, 0.45, MID_GREEN)
add_textbox(slide4, "파워 링크업", 0.45, 1.28, 5.7, 0.38, font_size=13, bold=True, color=WHITE)

add_textbox(slide4, "노출 기간별 비용 (엔)", 0.45, 1.85, 5.5, 0.38, font_size=11, bold=True, color=DARK_GREEN)

period_rows = [
    ("30일", "3,000엔"),
    ("60일", "6,000엔"),
    ("90일", "9,000엔"),
]
for i, (p, c) in enumerate(period_rows):
    ty = 2.3 + i * 0.58
    bg = PALE_GREEN if i % 2 == 0 else WHITE
    add_rect(slide4, 0.4, ty, 5.8, 0.52, bg)
    add_textbox(slide4, p, 0.55, ty + 0.08, 2.5, 0.35, font_size=11, color=MID_GRAY)
    add_textbox(slide4, c, 3.5, ty + 0.08, 2.5, 0.35, font_size=12, bold=True, color=DARK_GREEN, align=PP_ALIGN.RIGHT)

add_textbox(slide4, "추천 운영 상품 (3개)", 0.45, 4.1, 5.5, 0.38, font_size=11, bold=True, color=DARK_GREEN)
products = ["화이트토마토 (白トマト)", "레몬즙 (レモン汁)", "녹차카테킨 (緑茶カテキン)"]
for i, p in enumerate(products):
    ty = 4.55 + i * 0.55
    add_rect(slide4, 0.4, ty, 5.8, 0.48, WHITE)
    add_rect(slide4, 0.4, ty, 0.06, 0.48, LIGHT_GREEN)
    add_textbox(slide4, f"  {p}", 0.5, ty + 0.08, 5.6, 0.32, font_size=11, color=DARK_GRAY)

add_rect(slide4, 0.4, 6.25, 5.8, 0.65, MID_GREEN)
add_textbox(slide4, "30일 × 3개 = 9,000엔 → 월 8~10만원", 0.55, 6.3, 5.5, 0.5,
            font_size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

# Right: 총합 테이블
add_rect(slide4, 6.6, 1.25, 6.4, 5.8, LIGHT_GRAY)
add_rect(slide4, 6.6, 1.25, 6.4, 0.45, DARK_GREEN)
add_textbox(slide4, "Qoo10 총 광고비 요약", 6.75, 1.28, 6.1, 0.38, font_size=13, bold=True, color=WHITE)

summary = [
    ("항목", "예산", True, DARK_GREEN, WHITE),
    ("키워드 플러스", "20 ~ 30만원", False, WHITE, DARK_GRAY),
    ("파워 링크업", "8 ~ 10만원", False, PALE_GREEN, DARK_GRAY),
    ("합 계", "30 ~ 40만원", True, MID_GREEN, WHITE),
]
for i, (item, budget, bold, bg, fg) in enumerate(summary):
    ty = 1.85 + i * 0.72
    add_rect(slide4, 6.7, ty, 6.2, 0.65, bg)
    add_textbox(slide4, item, 6.85, ty + 0.12, 3.0, 0.4, font_size=12, bold=bold, color=fg)
    add_textbox(slide4, budget, 9.8, ty + 0.12, 2.9, 0.4, font_size=12, bold=bold, color=fg, align=PP_ALIGN.RIGHT)

# Key message
add_rect(slide4, 6.6, 5.2, 6.4, 1.75, DARK_GREEN)
add_textbox(slide4, "💡 핵심 포인트", 6.8, 5.25, 6.0, 0.38, font_size=12, bold=True, color=ACCENT_ORANGE)
add_textbox(slide4, "구매 의도가 이미 있는 고객이 검색하는 영역\n→ 전환율이 가장 높은 채널\n초기 단계에서 가장 중요한 광고 채널",
            6.8, 5.65, 6.0, 1.2, font_size=10.5, color=WHITE)

# ─────────────────────────────────────────────
# SLIDE 5: Instagram 전략
# ─────────────────────────────────────────────
slide5 = prs.slides.add_slide(blank_layout)
add_rect(slide5, 0, 0, 13.33, 7.5, WHITE)
add_slide_header(slide5, "Instagram 마케팅 전략", "천호앤케어 크루 모집 캠페인 · 일본 여성 타겟")

# Left: 캠페인 구조
add_rect(slide5, 0.3, 1.25, 5.8, 5.8, RGBColor(0xFD, 0xF6, 0xFF))
add_rect(slide5, 0.3, 1.25, 5.8, 0.45, RGBColor(0x83, 0x3A, 0xB4))
add_textbox(slide5, "크루 모집 캠페인 구조", 0.45, 1.28, 5.5, 0.38, font_size=13, bold=True, color=WHITE)

steps = [
    ("STEP 1", "제품 제공", "크루 선발 후 제품 무상 지급"),
    ("STEP 2", "리뷰 작성", "사용 후기 콘텐츠 제작"),
    ("STEP 3", "릴스 업로드", "15~30초 숏폼 영상 게시"),
    ("STEP 4", "스토리 업로드", "제품 태그 & 링크 공유"),
    ("STEP 5", "UGC 확보", "브랜드 자산으로 활용"),
]
for i, (step, title, desc) in enumerate(steps):
    ty = 1.85 + i * 0.98
    add_rect(slide5, 0.4, ty, 5.6, 0.88, WHITE)
    add_rect(slide5, 0.4, ty, 0.8, 0.88, RGBColor(0x83, 0x3A, 0xB4))
    add_textbox(slide5, step, 0.42, ty + 0.2, 0.75, 0.4, font_size=8, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_textbox(slide5, title, 1.3, ty + 0.05, 4.5, 0.35, font_size=12, bold=True, color=RGBColor(0x83, 0x3A, 0xB4))
    add_textbox(slide5, desc, 1.3, ty + 0.42, 4.5, 0.35, font_size=10, color=MID_GRAY)

# Right: 타겟 & 예산
add_rect(slide5, 6.4, 1.25, 6.6, 2.8, LIGHT_GRAY)
add_rect(slide5, 6.4, 1.25, 6.6, 0.45, RGBColor(0x83, 0x3A, 0xB4))
add_textbox(slide5, "Meta 광고 타겟팅", 6.55, 1.28, 6.3, 0.38, font_size=13, bold=True, color=WHITE)

targets = ["일본 여성 20~40대", "뷰티 / 이너뷰티 관심사", "다이어트 / 건강식품 관심사"]
for i, t in enumerate(targets):
    ty = 1.85 + i * 0.62
    add_rect(slide5, 6.5, ty, 6.4, 0.55, WHITE)
    add_rect(slide5, 6.5, ty, 0.06, 0.55, RGBColor(0x83, 0x3A, 0xB4))
    add_textbox(slide5, "  " + t, 6.6, ty + 0.1, 6.2, 0.35, font_size=11, color=DARK_GRAY)

add_rect(slide5, 6.4, 4.2, 6.6, 2.8, RGBColor(0xFD, 0xF6, 0xFF))
add_rect(slide5, 6.4, 4.2, 6.6, 0.45, RGBColor(0x5B, 0x2D, 0x8E))
add_textbox(slide5, "예산 구성", 6.55, 4.23, 6.3, 0.38, font_size=13, bold=True, color=WHITE)

ig_budget = [
    ("항목", "예산", True, RGBColor(0x5B, 0x2D, 0x8E), WHITE),
    ("모집 광고 집행", "20 ~ 30만원", False, WHITE, DARK_GRAY),
    ("제품 제공 비용", "10 ~ 20만원", False, RGBColor(0xFD, 0xF6, 0xFF), DARK_GRAY),
    ("합 계", "30 ~ 50만원", True, RGBColor(0x83, 0x3A, 0xB4), WHITE),
]
for i, (item, budget, bold, bg, fg) in enumerate(ig_budget):
    ty = 4.75 + i * 0.58
    add_rect(slide5, 6.5, ty, 6.4, 0.52, bg)
    add_textbox(slide5, item, 6.65, ty + 0.09, 3.0, 0.35, font_size=11, bold=bold, color=fg)
    add_textbox(slide5, budget, 9.8, ty + 0.09, 2.9, 0.35, font_size=11, bold=bold, color=fg, align=PP_ALIGN.RIGHT)

# ─────────────────────────────────────────────
# SLIDE 6: X (Twitter) 전략
# ─────────────────────────────────────────────
slide6 = prs.slides.add_slide(blank_layout)
add_rect(slide6, 0, 0, 13.33, 7.5, WHITE)
add_slide_header(slide6, "X (구 Twitter) 마케팅 전략", "일본 시장 특화 – 리뷰 확산에 가장 유리한 채널")

# Left
add_rect(slide6, 0.3, 1.25, 5.8, 5.8, RGBColor(0xE8, 0xF4, 0xFD))
add_rect(slide6, 0.3, 1.25, 5.8, 0.45, RGBColor(0x14, 0x71, 0xDA))
add_textbox(slide6, "X 채널 강점", 0.45, 1.28, 5.5, 0.38, font_size=13, bold=True, color=WHITE)

strengths = [
    ("일본 최대 SNS", "인스타그램보다 리뷰 확산 속도 빠름"),
    ("카테고리 반응 우수", "飲む日焼け止め・白トマト\nレモン汁 카테고리 높은 반응"),
    ("RT 바이럴", "팔로우&RT 캠페인으로\n폭발적 확산 가능"),
    ("저비용 고효율", "Premium 구독 + 소규모 광고로\n대형 채널 효과"),
]
for i, (title, desc) in enumerate(strengths):
    ty = 1.85 + i * 1.22
    add_rect(slide6, 0.4, ty, 5.6, 1.12, WHITE)
    add_rect(slide6, 0.4, ty, 0.06, 1.12, RGBColor(0x14, 0x71, 0xDA))
    add_textbox(slide6, title, 0.6, ty + 0.08, 5.2, 0.35, font_size=12, bold=True, color=RGBColor(0x14, 0x71, 0xDA))
    add_textbox(slide6, desc, 0.6, ty + 0.47, 5.2, 0.55, font_size=10, color=DARK_GRAY)

# Right
add_rect(slide6, 6.4, 1.25, 6.6, 2.7, RGBColor(0xE8, 0xF4, 0xFD))
add_rect(slide6, 6.4, 1.25, 6.6, 0.45, RGBColor(0x14, 0x71, 0xDA))
add_textbox(slide6, "캠페인 운영 방식", 6.55, 1.28, 6.3, 0.38, font_size=13, bold=True, color=WHITE)

add_textbox(slide6, "フォロー＆RPキャンペーン", 6.55, 1.85, 6.3, 0.45, font_size=15, bold=True, color=RGBColor(0x14, 0x71, 0xDA))
add_textbox(slide6, "팔로우 + 리트윗 조건 응모\n경품 제공으로 참여 유도\n당선자 UGC 활용",
            6.55, 2.38, 6.3, 1.3, font_size=11, color=DARK_GRAY)

add_rect(slide6, 6.4, 4.1, 6.6, 2.95, LIGHT_GRAY)
add_rect(slide6, 6.4, 4.1, 6.6, 0.45, RGBColor(0x0D, 0x4F, 0x9E))
add_textbox(slide6, "예산 구성", 6.55, 4.13, 6.3, 0.38, font_size=13, bold=True, color=WHITE)

x_budget = [
    ("항목", "예산", True, RGBColor(0x0D, 0x4F, 0x9E), WHITE),
    ("X Premium 구독", "약 1만원/월", False, WHITE, DARK_GRAY),
    ("광고 집행", "5 ~ 10만원", False, RGBColor(0xE8, 0xF4, 0xFD), DARK_GRAY),
    ("경품 비용", "5 ~ 10만원", False, WHITE, DARK_GRAY),
    ("합 계", "10 ~ 20만원", True, RGBColor(0x14, 0x71, 0xDA), WHITE),
]
for i, (item, budget, bold, bg, fg) in enumerate(x_budget):
    ty = 4.65 + i * 0.52
    add_rect(slide6, 6.5, ty, 6.4, 0.46, bg)
    add_textbox(slide6, item, 6.65, ty + 0.07, 3.0, 0.32, font_size=11, bold=bold, color=fg)
    add_textbox(slide6, budget, 9.8, ty + 0.07, 2.9, 0.32, font_size=11, bold=bold, color=fg, align=PP_ALIGN.RIGHT)

# ─────────────────────────────────────────────
# SLIDE 7: 월별 예산안 비교
# ─────────────────────────────────────────────
slide7 = prs.slides.add_slide(blank_layout)
add_rect(slide7, 0, 0, 13.33, 7.5, WHITE)
add_slide_header(slide7, "추천 예산안 비교", "월 100만원 / 150만원 / 200만원 3가지 플랜")

plans = [
    ("BASIC", "월 100만원", [("Qoo10 광고", "40만원"), ("Instagram", "40만원"), ("X", "20만원")], MID_GREEN),
    ("STANDARD", "월 150만원", [("Qoo10 광고", "60만원"), ("Instagram", "55만원"), ("X", "35만원")], DARK_GREEN),
    ("PREMIUM", "월 200만원", [("Qoo10 광고", "80만원"), ("Instagram", "70만원"), ("X", "50만원")], RGBColor(0x0D, 0x3D, 0x20)),
]

for i, (label, total, items, color) in enumerate(plans):
    lx = 0.4 + i * 4.3
    add_rect(slide7, lx, 1.25, 4.0, 5.8, PALE_GREEN)
    add_rect(slide7, lx, 1.25, 4.0, 0.8, color)
    add_textbox(slide7, label, lx + 0.15, 1.28, 3.7, 0.38, font_size=14, bold=True, color=WHITE)
    add_textbox(slide7, total, lx + 0.15, 1.62, 3.7, 0.35, font_size=12, color=RGBColor(0xA5, 0xD6, 0xA7))

    for j, (ch, amt) in enumerate(items):
        ty = 2.2 + j * 0.85
        add_rect(slide7, lx + 0.1, ty, 3.8, 0.75, WHITE)
        # Bar
        bar_w = 3.0
        pct = int(amt.replace("만원", "")) / int(total.replace("월 ", "").replace("만원", ""))
        add_rect(slide7, lx + 0.1, ty + 0.5, 3.8 * pct, 0.18, color)
        add_textbox(slide7, ch, lx + 0.25, ty + 0.05, 2.2, 0.3, font_size=11, color=DARK_GRAY)
        add_textbox(slide7, amt, lx + 2.5, ty + 0.05, 1.2, 0.3, font_size=11, bold=True, color=color, align=PP_ALIGN.RIGHT)

    add_rect(slide7, lx + 0.1, 4.75, 3.8, 0.6, color)
    add_textbox(slide7, "합계: " + total.replace("월 ", ""), lx + 0.25, 4.8, 3.5, 0.45,
                font_size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

    # Description
    desc_map = {
        "BASIC": "초기 시장 진입\n핵심 채널 집중",
        "STANDARD": "균형 잡힌 멀티채널\n크루 모집 본격화",
        "PREMIUM": "공격적 시장 확대\n브랜드 인지도 극대화",
    }
    add_textbox(slide7, desc_map[label], lx + 0.15, 5.45, 3.7, 1.5,
                font_size=10.5, color=DARK_GRAY, align=PP_ALIGN.CENTER)

# ─────────────────────────────────────────────
# SLIDE 8: 채널별 비중 & 시즌 전략
# ─────────────────────────────────────────────
slide8 = prs.slides.add_slide(blank_layout)
add_rect(slide8, 0, 0, 13.33, 7.5, WHITE)
add_slide_header(slide8, "권장 운영 전략", "초기 3개월 채널 비중 배분 & 시즌 전략")

# Left: 비중
add_rect(slide8, 0.3, 1.25, 6.0, 5.8, PALE_GREEN)
add_rect(slide8, 0.3, 1.25, 6.0, 0.45, DARK_GREEN)
add_textbox(slide8, "초기 3개월 채널 비중 (권장)", 0.45, 1.28, 5.7, 0.38, font_size=13, bold=True, color=WHITE)

channels = [
    ("Qoo10 광고", 40, DARK_GREEN, "직접 매출 전환 · 전환율 최우선"),
    ("Instagram", 35, MID_GREEN, "크루 모집 · UGC 콘텐츠 확보"),
    ("X (Twitter)", 25, LIGHT_GREEN, "리뷰 확산 · 바이럴 구축"),
]
for i, (ch, pct, color, desc) in enumerate(channels):
    ty = 1.9 + i * 1.55
    add_textbox(slide8, f"{ch}  {pct}%", 0.45, ty, 5.5, 0.4, font_size=14, bold=True, color=color)
    # bar
    add_rect(slide8, 0.45, ty + 0.45, 5.4, 0.28, RGBColor(0xDD, 0xDD, 0xDD))
    add_rect(slide8, 0.45, ty + 0.45, 5.4 * pct / 100, 0.28, color)
    add_textbox(slide8, desc, 0.45, ty + 0.82, 5.5, 0.3, font_size=10, color=MID_GRAY)

add_rect(slide8, 0.4, 6.45, 5.8, 0.48, DARK_GREEN)
add_textbox(slide8, "Qoo10 40%  →  Instagram 35%  →  X 25%",
            0.5, 6.5, 5.6, 0.38, font_size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

# Right: 시즌 전략
add_rect(slide8, 6.6, 1.25, 6.4, 5.8, LIGHT_GRAY)
add_rect(slide8, 6.6, 1.25, 6.4, 0.45, RGBColor(0xFF, 0x67, 0x00))
add_textbox(slide8, "☀️ 여름 시즌 집중 전략 (6~9월)", 6.75, 1.28, 6.1, 0.38, font_size=13, bold=True, color=WHITE)

add_textbox(slide8, "화이트토마토 (飲む日焼け止め)\n여름 시즌 검색량 급증 카테고리", 6.75, 1.85, 6.1, 0.7,
            font_size=12, bold=True, color=RGBColor(0xFF, 0x67, 0x00))

season_items = [
    ("일반 시즌", "키워드 플러스 예산", "20 ~ 30만원"),
    ("여름 시즌 (6~9월)", "키워드 플러스 예산 확대", "50 ~ 70만원"),
    ("증가 효과", "예산 대비 노출 증가", "+150% 이상"),
]
for i, (period, label, value) in enumerate(season_items):
    ty = 2.75 + i * 0.9
    bg = WHITE if i % 2 == 0 else PALE_GREEN
    add_rect(slide8, 6.7, ty, 6.2, 0.82, bg)
    add_textbox(slide8, period, 6.85, ty + 0.06, 3.0, 0.3, font_size=10, bold=True, color=RGBColor(0xFF, 0x67, 0x00))
    add_textbox(slide8, label, 6.85, ty + 0.39, 3.2, 0.3, font_size=10, color=MID_GRAY)
    add_textbox(slide8, value, 9.8, ty + 0.22, 2.9, 0.35, font_size=13, bold=True, color=DARK_GREEN, align=PP_ALIGN.RIGHT)

add_rect(slide8, 6.7, 5.5, 6.2, 1.4, RGBColor(0xFF, 0x67, 0x00))
add_textbox(slide8, "💡 전략 요약", 6.9, 5.55, 5.8, 0.38, font_size=12, bold=True, color=WHITE)
add_textbox(slide8, "Qoo10은 직접 매출 전환 채널\nInstagram · X는 크루 모집을 통한\nUGC 및 리뷰 콘텐츠 축적 역할",
            6.9, 5.95, 5.8, 0.85, font_size=10.5, color=WHITE)

# ─────────────────────────────────────────────
# SLIDE 9: 실행 로드맵
# ─────────────────────────────────────────────
slide9 = prs.slides.add_slide(blank_layout)
add_rect(slide9, 0, 0, 13.33, 7.5, WHITE)
add_slide_header(slide9, "실행 로드맵", "단계별 마케팅 실행 계획 – 초기 3개월")

months = [
    ("1개월차", "기반 구축", [
        "Qoo10 키워드 플러스 세팅",
        "파워 링크업 3개 상품 등록",
        "Instagram 계정 활성화",
        "X Premium 구독 시작",
        "크루 모집 공고 게시",
    ], DARK_GREEN),
    ("2개월차", "본격 운영", [
        "키워드 플러스 성과 분석 & 최적화",
        "크루 1차 선발 & 제품 발송",
        "Instagram 릴스·스토리 UGC 수집",
        "X フォロー＆RPキャンペーン 실시",
        "Meta 광고 타겟 데이터 분석",
    ], MID_GREEN),
    ("3개월차", "확장 & 최적화", [
        "여름 시즌 대비 예산 증액 검토",
        "UGC 콘텐츠 Qoo10 페이지 활용",
        "크루 2차 확대 모집",
        "자연 검색 유입 지표 확인",
        "다음 분기 예산 재조정",
    ], LIGHT_GREEN),
]

for i, (month, title, tasks, color) in enumerate(months):
    lx = 0.4 + i * 4.3
    add_rect(slide9, lx, 1.25, 4.0, 5.8, PALE_GREEN)
    add_rect(slide9, lx, 1.25, 4.0, 0.9, color)
    add_textbox(slide9, month, lx + 0.15, 1.28, 3.7, 0.4, font_size=11, bold=True, color=WHITE)
    add_textbox(slide9, title, lx + 0.15, 1.65, 3.7, 0.42, font_size=16, bold=True, color=WHITE)

    for j, task in enumerate(tasks):
        ty = 2.3 + j * 0.92
        add_rect(slide9, lx + 0.1, ty, 3.8, 0.82, WHITE)
        add_rect(slide9, lx + 0.1, ty, 0.06, 0.82, color)
        add_textbox(slide9, task, lx + 0.25, ty + 0.18, 3.5, 0.45, font_size=10, color=DARK_GRAY)

# ─────────────────────────────────────────────
# SLIDE 10: 마무리 / 기대 효과
# ─────────────────────────────────────────────
slide10 = prs.slides.add_slide(blank_layout)
add_rect(slide10, 0, 0, 13.33, 7.5, DARK_GREEN)

# Decorative
for x, y, sz in [(10.0, 0.5, 4.0), (0.5, 5.0, 3.0)]:
    c = slide10.shapes.add_shape(9, Inches(x), Inches(y), Inches(sz), Inches(sz))
    c.fill.solid()
    c.fill.fore_color.rgb = MID_GREEN
    c.line.fill.background()

add_rect(slide10, 1.0, 1.0, 0.12, 5.0, LIGHT_GREEN)

add_textbox(slide10, "기대 효과 & 결론", 1.3, 1.0, 10, 0.7, font_size=28, bold=True, color=WHITE)
add_textbox(slide10, "천호앤케어 Japan Qoo10 마케팅 예산 운영 제안", 1.3, 1.7, 10, 0.45,
            font_size=13, color=RGBColor(0xA5, 0xD6, 0xA7))

effects = [
    ("📊", "검색 노출 상승", "키워드 플러스 + 파워 링크업으로\nQoo10 내 상위 노출 확보"),
    ("💬", "UGC 콘텐츠 축적", "크루 모집을 통한 리뷰 자산 확보\n장기적 자연 유입 기반 구축"),
    ("🌸", "일본 여성 팬덤 형성", "Instagram · X 동시 운영으로\n브랜드 인지도 및 충성 고객 확보"),
    ("📉", "광고 의존도 감소", "초기 유료 광고 → 오가닉 전환\n지속 가능한 마케팅 구조 완성"),
]

for i, (icon, title, desc) in enumerate(effects):
    col = i % 2
    row = i // 2
    lx = 1.3 + col * 5.8
    ty = 2.4 + row * 2.3

    add_rect(slide10, lx, ty, 5.2, 2.0, RGBColor(0x1F, 0x6E, 0x45))
    add_rect(slide10, lx, ty, 5.2, 0.06, LIGHT_GREEN)
    add_textbox(slide10, icon + " " + title, lx + 0.2, ty + 0.15, 4.8, 0.42,
                font_size=14, bold=True, color=WHITE)
    add_textbox(slide10, desc, lx + 0.2, ty + 0.65, 4.8, 1.1,
                font_size=11, color=RGBColor(0xC8, 0xE6, 0xC9))

add_textbox(slide10, "문의 · 제안 검토 후 추가 조율 가능합니다",
            1.3, 6.8, 11, 0.45, font_size=12, color=RGBColor(0x81, 0xC7, 0x84), align=PP_ALIGN.CENTER)

# Save
output_path = "/home/user/mypage/천호앤케어_Japan_Qoo10_마케팅제안서.pptx"
prs.save(output_path)
print(f"Saved: {output_path}")
