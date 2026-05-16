# InnerG Intel Creative Follow-Up Tracker

An installable Codex skill for graphic designers and creative freelancers who need to keep leads, replies, paid customers, invoices, and project next steps organized.

This is Skill 05 in the InnerG Intel creative sales toolkit. It closes the loop after finding leads, writing outreach, auditing brands, and building offers.

## What It Tracks

- Lead stage
- Priority
- Last touch
- Next action
- Follow-up due date
- Next message
- Offer or package
- Amount and payment status
- Project status
- Notes

## Use In Codex

Paste this into Codex:

```text
Use Creative Follow-Up Tracker.

Organize these leads, replies, paid customers, and project notes into a follow-up tracker.
Include stage, priority, next action, due date, next message, payment status, project status, and notes.

Notes:
[paste notes here]
```

More examples:

```text
Use Creative Follow-Up Tracker on these DM replies and paid customer notes. Give me a tracker sorted by priority.
```

```text
Use Creative Follow-Up Tracker for customers who paid already but have not sent project info yet. Write the exact follow-up message.
```

## Install

```bash
bash scripts/install.sh
```

Or manually:

```bash
mkdir -p ~/.codex/skills
cp -R skill/creative-follow-up-tracker ~/.codex/skills/
```

## Example Prompt

```text
Use Creative Follow-Up Tracker on these DM replies and paid customer notes. Give me a tracker sorted by priority.
```

## CSV Helper

```bash
python3 skill/creative-follow-up-tracker/scripts/update_tracker.py examples/leads.csv /tmp/followups.csv
```

Expected input can include:

```text
business_name,contact_name,channel,last_touch,reply,offer,amount,payment_status,project_status,notes
```

## InnerG Intel Ecosystem

1. Creative Client Finder
2. Creative Outreach Writer
3. Brand Audit Snapshot
4. Creative Offer Builder
5. Creative Follow-Up Tracker
