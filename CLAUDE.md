# Brow Loft - Project Guidelines

## Project Overview
Static HTML beauty salon website for Brow Loft with locations in Langley and Burnaby, Vancouver, Canada. No build system — served as plain HTML/CSS/JS.

## Page Structure (Must Match Across All Pages)
Every page must follow this structure (use langley-location.html as the reference template):

1. **Head**: Same stylesheets in same order, favicon `assets/images/favicon.png`
2. **Preloader**: `loader-wrap` with "B" and "L" spinner
3. **Search Popup**: `#search-popup` section
4. **Header**: `main-header header-overlay` with:
   - `header-upper`: logo + tagline "Luxury Brows. Timeless Beauty."
   - `header-lower`: navigation menu
   - `sticky-header`: empty nav (populated by JS)
5. **Mobile Menu**: `mobile-menu` with `menu-outer` containing JS comment `<!--Here Menu Will Come Automatically Via Javascript / Same Menu as in Header-->`
6. **Page Title/Banner**: `page-title centred` with background image (no text overlay)
7. **Page Content**: wrapped in `service-details sec-pad` with `service-booking-section` and `section-heading`
8. **Footer**: `main-footer` with `footer-top--redesign` layout (Contact + Services columns)
9. **Scroll To Top**: SVG-based `scroll-top` div
10. **Scripts**: Same JS files in same order

## Navigation Menu
All pages must have the same nav structure:
```html
<ul class="navigation clearfix">
    <li><a href="index.html">Home</a></li>
    <li class="dropdown"><a>Services</a>
        <ul>
            <li><a href="langley-location.html">Langley Location</a></li>
            <li><a href="burnaby-location.html">Burnaby Location</a></li>
        </ul>
    </li>
    <li class="dropdown"><a>About</a>
        <ul>
            <li><a href="about.html">About Us</a></li>
            <li><a href="policies.html">Policies</a></li>
            <li><a href="faq.html">FAQ</a></li>
            <li><a href="after-care.html">After Care</a></li>
        </ul>
    </li>
    <li><a href="index.html#enquiry">Contact</a></li>
</ul>
```
- Add `class="current dropdown"` to the About `<li>` on about, policies, faq, and after-care pages
- Nav changes must be applied to ALL pages: index.html, about.html, policies.html, faq.html, after-care.html, langley-location.html, burnaby-location.html, booking.html

## Active Pages
- `index.html` — Homepage
- `about.html` — About Us page (content TBD)
- `policies.html` — Policies page (cancellation, parking/payment, service safety)
- `faq.html` — FAQ page (threading, tinting, lash lift questions)
- `after-care.html` — After Care page (threading, tint, lash lift, facial aftercare)
- `langley-location.html` — Langley services with desktop + mobile dual layouts
- `burnaby-location.html` — Burnaby services with desktop + mobile dual layouts
- `booking.html` — Booking page

## Service Pages (Langley & Burnaby)
- Desktop and mobile service lists must stay in sync
- `data-service` attributes on list items must match `id` attributes on detail panels
- `service-duration` class shows timings (not prices) for add-ons, packages, and facial add-ons
- `service-meta` in detail panels shows timing or price info

## Design Tokens

### Light Theme (Service pages, Policies, FAQ)
- Card background: `#fff` with border `#e0e0e0` and `box-shadow: 0 2px 10px rgb(0 0 0 / 8%)`
- Highlight/accent background: `#f9f9f9`
- Heading text: `#1e1e1e`
- Body text: `#333`
- Meta/muted text: `#666`
- Accent gold: `#b08a61`
- Gold border-left on highlights: `3px solid #b08a61`

### Dark Theme (Footer only)
- Footer background: `#2f2825`
- Text light: `#f2f2f2`, `#bdb7ab`
- Text muted: `#9a9490`

### Shared
- Accent gold: `#b08a61`
- Fonts: Jost (body), Mrs Saint Delafield (decorative)

## CSS Architecture
- Main styles: `assets/css/style.css`
- Content wrapper: `.service-details.sec-pad` → `.service-booking-section` → `.section-heading` (gold, centered, letter-spaced)
- Policy cards: `.policy-card` (white bg, light shadow), `.policy-highlight` (`#f9f9f9` bg, gold left border), `.policy-location`, `.payment-chip`
- Policies grid: `.policies-page__grid` (max-width: 90%, flex column, gap 40px)
- Policy text uses light theme colors: headings `#1e1e1e`, body `#333`, muted `#666`, accent `#b08a61`
- FAQ accordion: `.faq-item` (white card, light shadow), `.faq-question` (clickable header, uppercase h4), `.faq-answer` (collapsible via `.open` class), `.faq-toggle` (chevron rotates on open)
- FAQ grid: `.faq-grid` (max-width: 90%, flex column, gap 16px)
- FAQ uses same light theme as policies; only one item open at a time (accordion behavior via inline JS)
- Banner: `.page-title.centred` with inline background-image style

## Important Conventions
- Each About sub-section is a SEPARATE page (not sections on one page)
- Service rename: "Velvet Touch" is now "Signature Area Threading"
- "Luxe Brows & Velvet Touch" is now "Luxe Brows & Signature One Area Threading"
- Added: "Luxe Brows & Signature Two Area's Threading"
- Add-ons, packages, and facial add-ons show durations (not prices)
