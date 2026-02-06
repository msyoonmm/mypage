# CLAUDE.md

## Project Overview

A static movie review/rating web application ("내 생애 최고의 영화들" - "The Best Movies of My Life"). This is a learning project from Sparta Coding Club (스파르타코딩클럽) focused on Bootstrap 5 and basic HTML/CSS/JavaScript.

## Tech Stack

- **HTML5** - Single-page static site (`index.html`)
- **Bootstrap 5.0.2** - UI framework (loaded via CDN from jsDelivr)
- **jQuery 3.5.1** - DOM manipulation (loaded via CDN from Google)
- **Google Fonts** - 'Gowun Dodum' Korean font
- **No build tools** - No bundler, transpiler, or package manager

## Project Structure

```
mypage/
├── index.html    # Entire application (HTML + inline CSS + inline JS)
├── CLAUDE.md     # This file
└── .git/         # Git version control
```

This is a single-file project. All markup, styles, and scripts live in `index.html`.

## Code Organization (index.html)

| Section       | Lines   | Description                                    |
|---------------|---------|------------------------------------------------|
| `<head>`      | 1-85    | Meta tags, CDN imports, `<style>`, `<script>`  |
| CDN imports   | 8-13    | Bootstrap CSS/JS, jQuery                        |
| `<style>`     | 16-80   | All custom CSS (inline)                         |
| `<script>`    | 81-84   | JavaScript (currently minimal/placeholder)      |
| `<body>`      | 87-169  | Page content                                    |

### CSS Classes

- `.mytitle` - Hero banner with background image overlay and centered content
- `.mycomment` - Gray-colored comment text
- `.mycards` - 1200px centered card container
- `.mypost` - Centered form container with box shadow (movie submission form)
- `.mybtn` - Flex row for action buttons

### Page Sections

1. **Hero banner** (`.mytitle`) - Title "내 생애 최고의 영화들" with "영화 기록하기" button
2. **Submission form** (`.mypost`) - Movie URL input, star rating (1-3 stars), comment textarea, record/close buttons
3. **Movie cards** (`.mycards`) - Responsive 4-column grid of movie cards using Bootstrap's card component

## Development

### Running Locally

No build step required. Open `index.html` directly in a browser, or serve with any static file server:

```bash
# Python
python3 -m http.server 8000

# Node.js (if npx available)
npx serve .
```

### Making Changes

- All edits go directly to `index.html`
- CSS is in the `<style>` block (lines 16-80)
- JavaScript is in the `<script>` block (lines 81-84)
- HTML body content starts at line 87

### No Build / No Tests

There is no build process, linter, test suite, or CI/CD pipeline. Verify changes by opening `index.html` in a browser.

## Current State & Known Issues

- The `hey()` function referenced by the hero button's `onclick` is **not defined** - clicking the button will throw a ReferenceError
- The "기록하기" (Record) and "닫기" (Close) buttons in the form have **no event handlers**
- Movie card data is **hardcoded** placeholder content (4 identical cards)
- The JavaScript block only contains a test object and `console.log` call
- No backend or API integration exists

## Conventions

- **Language**: UI text is in Korean
- **Styling**: Use Bootstrap utility classes where possible; custom CSS goes in the existing `<style>` block
- **External dependencies**: Loaded via CDN `<script>`/`<link>` tags (no npm)
- **Responsive design**: Uses Bootstrap's `row-cols-1 row-cols-md-4` pattern (1 column on mobile, 4 on desktop)
- **Images**: Movie poster images are loaded from Naver Movie (`movie-phinf.pstatic.net`)

## Git Workflow

- Repository has a single `index.html` file
- Commit messages have historically been brief (e.g., "Update index.html")
- No branch protection or CI checks configured
