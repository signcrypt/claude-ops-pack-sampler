# Claude Code Ops Pack — free sampler (3 of 50 skills)

Three skills from the [Claude Code Ops Pack](https://libertybound0.gumroad.com/l/claude-ops-pack), free, MIT-licensed:

- `invoice-generator` — real .xlsx invoice with formulas (IDR/USD, PPN, PPh 23). Uses `scripts/xlsx_helpers.py`.
- `gumroad-listing-writer` — name, slug, summary, sectioned description, price rationale, Discover tags.
- `cold-email-from-url` — personalised ≤110-word outreach email from a business's website, plus a WhatsApp version.

## Install
```bash
git clone https://github.com/signcrypt/claude-ops-pack-sampler
cp -r claude-ops-pack-sampler/skills/* ~/.claude/skills/
```
Then: *"Make me an invoice for Acme, 10 h at $80, due in 14 days."*

## Try the invoice script directly
```bash
python3 scripts/xlsx_helpers.py   # writes /tmp/demo-invoice.xlsx and prints the formula count
```

The full pack has 50 skills in three clusters (business ops, dev ops, marketing), four helper scripts and a validator — the same skills that built two live Gumroad products. $19: https://libertybound0.gumroad.com/l/claude-ops-pack
