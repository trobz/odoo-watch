---
version: "19.0"
app: "General"
app_slug: "general"
source_url: "https://www.odoo.com/odoo-19-release-notes#table_of_content_heading_1_76"
item_count: 37
---

# General — Odoo 19.0

## Activities

Activities have been updated with several improvements:

- Simplified activity modal creation
- New filter by due date (tomorrow, this week, or this month) in Activity view
- Create new activities from My Activities (no object required)
- Reschedule activity today, tomorrow, or next week
- Addition of title in the Activity view card for better readability
- Activities are not deleted when marked as done
- Global UX improvements

## Add stage button

A new compact design to add stages has been added to the Kanban view, improving the utilization of the screen width.

## Avatars in custom filters

Users' avatars are displayed in custom search filters.

## Badge notification

Users are notified when they are granted a badge.

## Buttons on mobile

In form view, buttons no longer appear in the action menu; the first button is fully displayed, while the others are stacked under the vertical ellipses icon.

## Customer documents

New sections and sub-sections have been added on customer documents (quotations, sale orders, invoices). Those sections can be easily reorganized, deleted, or duplicated. You can also hide the prices and taxes of the lines within a section, or even completely hide a section's content and all its line on the produced document.

## Dialog design

The design of dialogs has been improved.

## Email recipients

All email recipients are now shown in Odoo and in emails. The email recipient UI and UX has been improved.

## Export wizard

By default, only visible fields are displayed in the export wizard.

## Exports: default fields

In the export screen, the default fields and their display order now match the underlying list view.

## Favorite filters

Easily edit favorite filters from the search panel.

## Follower management

Add or remove followers from mulitiple records at once.

## Gantt view

- Undo changes when rescheduling a record.
- When the Gantt view is grouped, scheduling a record for that group directly pre-filters the data accordingly. For example, when grouping tasks by assignee in the Gantt view and scheduling for a specific user, the dialog now shows only that user’s unplanned tasks.
- When rescheduling dependent records such as tasks and work orders, choose to keep or use the buffer time between them.
- The Gantt view now includes smart zoom based on scale, improved usability, visible start and end dates during drag-and-drop, and more readable labels.
- In Gantt view, fold the off-hours to maximize usable space for scheduling tasks, slots, and bookings.

## Gmail and Outlook account connection

Connect your personal Gmail or Outlook address to send emails via your account.

## Grouped records: list view

- When grouping records in the list view, edit the grouping field using its action menu.
- When records are grouped by default in the list view, create new groups using the link at the bottom of the list (e.g., add new stages from the task list).

## HTML property field type

Create HTML property fields and use AI to fill them.

## Import product variants

When importing products, define a product variant per line and its variant specific data such as the attribute values, the cost, the quantity on hand, and more.

## Import templates

New import templates have been added for the most common records such as contacts, leads, sales orders, purchase orders, accounting entries, tasks, timesheets, etc.

## Kanban cards and stages

- Select Kanban cards to perform mass actions using the ALT + click shortcut on desktops or the long press on mobile devices.
- Easily identify records that have been "rotting" in a Kanban stage, i.e., that have been inactive for a specific amount of time.

## List view

- Drag and drop records between groups in grouped and reorderable lists.
- In list view, double-click a column border to recompute the width of all columns.

## Mobile: date picker

The date picker is opened in a bottom sheet on mobile devices.

## Mobile: select all records

Select all records from a list on mobile devices using a dedicated button.

## Odoo PWA: pull-to-refresh

In Odoo PWA, pull the screen to refresh the data.

## Open link in new tab

Open any link in a new tab using the mouse middle click or the shortcut CTRL + click.

## Out-of-office reply

Users can configure an out-of-office automatic reply to notify senders when they are unavailable.

## Portal users

- Portal users can change their login information from the /my/account page.
- Portal users can manage their addresses from the portal.

## Preview attachments

Preview PDF attachments in the chatter.

## Product access rights

Access rights for product management are now separated from other groups by default.

## Properties

Use property fields' values in email templates.

## Replying to or forwarding specific messages

Reply to a specific message and/or forward it to the desired recipients.

## Rich-text editor

- The rich-text editor supports font families, allowing to customize the text's font.
- The history management system has been improved.
- Insert a file from Documents in the rich-text editor.
- Every heading is now an anchor. Easily navigate and share specific sections.

## Share filters

Share favorite filters with specific users.

## Show records after import

After a successful import, the imported records are shown for better understanding of which records were affected.

## Smaller status bar on mobile

On mobile, the status bar is displayed as a single button indicating whether it represents the first, last, or a middle state.

## Suggested recipients

Customers are no longer added as followers. Instead, the recipients of previous messages are suggested as recipients of future messages.

## Twilio

Twilio integration has been added, allowing you to send SMS directly from Odoo once you have created an account and reserved numbers on Twilio (available from 17.0).

## Warning messages

Blocking messages for products and contacts have been removed. Only warning messages are supported and now appear at the top of the screen instead of as popups.
