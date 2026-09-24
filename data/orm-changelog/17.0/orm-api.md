---
version: "17.0"
app: "ORM API"
app_slug: "orm-api"
source_url: "https://www.odoo.com/documentation/master/developer/reference/backend/orm/changelog.html"
item_count: 4
---

# ORM API changelog (17.0)

## Introduce an [`SQL`](../orm.html#odoo.tools.SQL) wrapper object to make SQL composition easier and safer with respect to SQL injections

Methods of the ORM now use it internally. Introduced by [#134677](https://github.com/odoo/odoo/pull/134677).

## Method `name_get()` has been deprecated with [#122085](https://github.com/odoo/odoo/pull/122085)

Read field `display_name` instead.

## Method [`_read_group()`](../orm.html#odoo.models.Model._read_group) has a new signature with [#110737](https://github.com/odoo/odoo/pull/110737)

## Refactor the implementation of searching and reading methods to be able to combine both in a minimal number of SQL queries

We introduce two new methods [`search_fetch()`](../orm.html#odoo.models.Model.search_fetch) and [`fetch()`](../orm.html#odoo.models.Model.fetch) that take advantage of the combination. More details can be found on the pull request [#112126](https://github.com/odoo/odoo/pull/112126).
