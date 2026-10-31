---
name: cold-email-from-url
description: Write a personalised cold email (and a WhatsApp version) to a business from its website URL: find a specific gap, show a quick win, make one small ask. Use for outreach to local businesses or prospects.
---
# Cold email from URL

## Steps
1. Fetch the site. Note: business name, what they sell, city, 1 thing that's good, 1 concrete gap (no mobile layout, no booking button, 2019 copyright, no Google reviews linked, slow images).
2. Email ≤ 110 words: subject (≤ 6 words, specific), first line about *them* (the good thing), the gap in one sentence, what you'd do and the result, a tiny ask (reply "yes" / a 10-min call / "want me to send the demo?"), sign-off with name and one link.
3. WhatsApp version ≤ 50 words, no links in the first message.
4. If a demo page exists (see `github-pages-deploy`), reference it by URL.
5. Output `outreach-<domain>.md`. Batch mode: CSV of URLs → one file each + `outreach.csv` with subject/body columns.

## Rules
No flattery padding, no "I hope this finds you well", no bullet lists in the email.

## Test prompt
"Cold email for https://example-studio.id offering a booking page." Expect a specific gap observed on the site and one small ask.
