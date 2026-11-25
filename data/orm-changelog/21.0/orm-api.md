---
version: "21.0"
app: "ORM API"
app_slug: "orm-api"
source_url: "https://www.odoo.com/documentation/master/developer/reference/backend/orm/changelog.html"
item_count: 5
---

# ORM API changelog (21.0)

## `unlink()` processes `ondelete` cascades in the ORM: `@api.ondelete` methods are called on cascade-deleted records too, the new `_delete_extra()` method returns additional records to delete, and only the fields referring to the deleted records are flushed

`Many2oneReference` fields support `ondelete` (`'set null'`, `'restrict'`, `'cascade'`, `'ignore'` or a callable for a subset of models). See [#237614](https://github.com/odoo/odoo/pull/237614) and [#292869](https://github.com/odoo/odoo/pull/292869).

## New `Model.partitioned()` to split a recordset by predicates

See [#293366](https://github.com/odoo/odoo/pull/293366).

## New field attributes `ui_readonly`, `ui_required` and `ui_domain`

See [#302515](https://github.com/odoo/odoo/pull/302515) and [#292770](https://github.com/odoo/odoo/pull/292770).

## Shared test data companies and users (`--with-test-data`)

See [#284989](https://github.com/odoo/odoo/pull/284989).

## Persistent signed file cache of compiled QWeb code

See [#302905](https://github.com/odoo/odoo/pull/302905).
