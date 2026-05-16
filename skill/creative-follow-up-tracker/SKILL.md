---
name: creative-follow-up-tracker
description: Use when organizing creative freelance leads, outreach replies, paid customer intake, proposals, invoices, follow-up timing, and client next actions. Converts lead lists, DM replies, emails, customer notes, payment status, and project status into a follow-up tracker with priority, stage, next message, due date, owner action, and CSV-style output.
---

# Creative Follow-Up Tracker

Use this skill to keep creative leads and clients from getting lost after discovery, outreach, payment, or proposal.

## Workflow

1. Classify each contact into a stage:
   - `new_lead`
   - `contacted`
   - `replied`
   - `proposal_needed`
   - `invoice_needed`
   - `paid_needs_info`
   - `active_project`
   - `follow_up`
   - `won`
   - `lost`
2. Extract or infer the next action:
   - Send first DM
   - Send audit snapshot
   - Send offer
   - Send invoice/payment link
   - Collect intake details
   - Confirm deadline
   - Start project
   - Follow up
3. Set priority:
   - `High`: paid, replied positively, deadline/urgent need, or clear buyer signal.
   - `Medium`: good fit but no reply or needs education.
   - `Low`: weak fit, vague contact, or low urgency.
4. Write the next message in the right format: DM, SMS, email, or internal note.
5. Output a tracker table or CSV row.

## Output Format

For chat output, use:

- Contact / business
- Stage
- Priority
- Reason
- Next action
- Next message
- Due date
- Notes

For CSV output, use:

```text
business_name,contact_name,channel,stage,priority,last_touch,next_action,due_date,next_message,offer,amount,payment_status,project_status,notes
```

## Follow-Up Timing

Use these defaults unless the user gives dates:

- No reply after first outreach: follow up in 2 business days.
- Warm reply but no decision: follow up in 1 business day.
- Proposal sent: follow up in 2 business days.
- Invoice sent: follow up in 1 business day.
- Paid but missing details: same day follow-up, then next day.
- Active project waiting on client: follow up in 1 business day.

When today’s date matters, use the current local date and return absolute dates.

## Message Rules

- Keep messages short and specific.
- Reference the exact need, offer, or paid status.
- Avoid guilt, pressure, or fake urgency.
- For paid clients, be direct: collect the missing information and confirm the next step.
- For cold leads, lead with one useful observation or quick win.

## Bundled Resources

- Use `scripts/update_tracker.py` to normalize lead/client rows into a tracker CSV.
- Read `references/stages.md` when deciding stage, priority, due date, and next message.
