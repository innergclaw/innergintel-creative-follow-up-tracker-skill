#!/usr/bin/env python3
import csv
import sys
from datetime import date, timedelta


FIELDS = [
    "business_name",
    "contact_name",
    "channel",
    "stage",
    "priority",
    "last_touch",
    "next_action",
    "due_date",
    "next_message",
    "offer",
    "amount",
    "payment_status",
    "project_status",
    "notes",
]


def value(row, *keys):
    for key in keys:
        if row.get(key):
            return row[key].strip()
    return ""


def add_business_days(start, days):
    current = start
    added = 0
    while added < days:
        current += timedelta(days=1)
        if current.weekday() < 5:
            added += 1
    return current


def infer(row):
    business = value(row, "business_name", "name") or "Lead"
    contact = value(row, "contact_name", "name")
    channel = value(row, "channel") or ("email" if value(row, "email") else "dm")
    payment = value(row, "payment_status", "paid_status").lower()
    is_paid = payment in {"paid", "payment received", "complete", "completed", "confirmed"}
    reply = value(row, "reply", "latest_reply", "notes").lower()
    offer = value(row, "offer", "suggested_offer", "offer_name")
    amount = value(row, "amount", "price", "amount_paid")
    today = date.today()

    if is_paid and "missing" in reply:
        stage, priority, days = "paid_needs_info", "High", 0
        action = "Collect project details"
        message = "I received the payment. Send me the brand name, deadline, colors/style, wording, and reference links so I can move it into the queue."
    elif is_paid:
        stage, priority, days = "active_project", "High", 1
        action = "Confirm next project milestone"
        message = f"Payment is confirmed for {offer or 'the project'}. I am checking the next details and will confirm the next step."
    elif "invoice" in reply or "payment" in reply or "price" in reply:
        stage, priority, days = "invoice_needed", "High", 1
        action = "Send invoice or payment link"
        message = f"Based on this, I can send the invoice for {offer or 'the package'} and then collect the project details."
    elif "yes" in reply or "interested" in reply or "send" in reply:
        stage, priority, days = "proposal_needed", "High", 1
        action = "Send offer"
        message = f"The best fit is {offer or 'a starter creative package'}. Want me to send the package details and next step?"
    elif value(row, "last_touch"):
        stage, priority, days = "contacted", "Medium", 2
        action = "Follow up"
        message = f"Following up on this. I can help {business} with {offer or 'a cleaner creative presence'} if you want me to send the quick package."
    else:
        stage, priority, days = "new_lead", "Medium", 0
        action = "Send first outreach"
        message = f"I noticed {business} could use {offer or 'a cleaner design presence'}. Want me to send a quick option?"

    return {
        "business_name": business,
        "contact_name": contact,
        "channel": channel,
        "stage": stage,
        "priority": priority,
        "last_touch": value(row, "last_touch"),
        "next_action": action,
        "due_date": add_business_days(today, days).isoformat(),
        "next_message": message,
        "offer": offer,
        "amount": amount,
        "payment_status": value(row, "payment_status", "paid_status"),
        "project_status": value(row, "project_status"),
        "notes": value(row, "notes", "evidence", "design_need"),
    }


def main():
    if len(sys.argv) != 3:
        print("Usage: update_tracker.py input.csv output.csv", file=sys.stderr)
        return 2

    with open(sys.argv[1], newline="", encoding="utf-8") as src:
        rows = list(csv.DictReader(src))

    with open(sys.argv[2], "w", newline="", encoding="utf-8") as dst:
        writer = csv.DictWriter(dst, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow(infer(row))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
