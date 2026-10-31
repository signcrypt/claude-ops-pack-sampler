---
name: gumroad-listing-writer
description: Write a complete Gumroad product listing — name, slug, summary, description with sections, price rationale, Discover category and tags — from a product file or description. Use when publishing or improving a Gumroad listing.
---
# Gumroad listing writer

## Structure
- **Name** (≤ 60 chars): what it is + who it's for + year if it dates (e.g. "Photographer Booking & Shot-List Pack 2026 (Excel)").
- **Slug**: short kebab-case.
- **Summary** (≤ 140 chars): the result the buyer gets.
- **Description** (Markdown-ish, Gumroad supports basic formatting):
  1. One-line promise.
  2. "What's inside" — bullet per file/sheet/module with a concrete detail (counts, formulas, pages).
  3. "Who it's for" / "Not for".
  4. "How to use" — 3 steps.
  5. Compatibility/requirements.
  6. Licence (personal/commercial), updates policy, refund policy.
  7. FAQ (3 Qs).
- **Price**: anchor on comparable listings; explain in one line to the seller why.
- **Discover**: category path + 6–10 tags (Gumroad allows 10): include the format ("excel template"), the audience ("photographer"), the job ("shot list").

## Steps
1. If a product file exists, open it and pull real counts (sheets, formulas, pages, icons) — never invent numbers.
2. Write `listing.md` with the fields above as headed sections so they can be pasted field by field.
3. Add `cover-brief.md`: title text, subtitle, 3 visual elements for a 1280×720 cover.

## Test prompt
"Listing for a 50-skill Claude Code pack at $19." Expect all fields, real counts, 6–10 tags, an FAQ.
