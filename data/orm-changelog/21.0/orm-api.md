---
version: "21.0"
app: "ORM API"
app_slug: "orm-api"
source_url: "https://www.odoo.com/documentation/master/developer/reference/backend/orm/changelog.html"
item_count: 1
---

# ORM API changelog (21.0)

## `unlink()` processes `ondelete` cascades in the ORM: `@api.ondelete` methods are called on cascade-deleted records too, the new `_delete_extra()` method returns additional records to delete, and only the fields referring to the deleted records are flushed

`Many2oneReference` fields support `ondelete` (`'set null'`, `'restrict'`, `'cascade'`, `'ignore'` or a callable for a subset of models). See [#237614](https://github.com/odoo/odoo/pull/237614) and [#292869](https://github.com/odoo/odoo/pull/292869).
