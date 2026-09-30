---
version: "18.0"
app: "ORM API"
app_slug: "orm-api"
source_url: "https://www.odoo.com/documentation/master/developer/reference/backend/orm/changelog.html"
item_count: 8
---

# ORM API changelog (18.0)

## Searching by name is now implemented as `_search_display_name` like all other fields

See [#174967](https://github.com/odoo/odoo/pull/174967).

## New methods to check access rights and rules now combine both access rights and rules: `check_access`, `has_access` and `_filtered_access`

See [#179148](https://github.com/odoo/odoo/pull/179148).

## Translations are made available from the `Environment` with [#174844](https://github.com/odoo/odoo/pull/174844)

## The internal operator `inselect` is removed

The alternative is to use `in` with a Query or SQL object. [#171371](https://github.com/odoo/odoo/pull/171371).

## We can now group by date parts numbers in `read_group`, `_read_group` and domains with [#159528](https://github.com/odoo/odoo/pull/159528)

## The `group_operator` attribute of [`Field`](../orm.html#odoo.fields.Field) is renamed into `aggregator` with [#127353](https://github.com/odoo/odoo/pull/127353)

## We can now group/aggregate/order by related no-store field with [#127353](https://github.com/odoo/odoo/pull/127353)

## Method `_flush_search()` has been deprecated with [#144747](https://github.com/odoo/odoo/pull/144747)

The flushing of fields is now done by [`execute_query()`](../orm.html#odoo.api.Environment.execute_query), and is based on metadata put in the [`SQL`](../orm.html#odoo.tools.SQL) object by `_search()` and other low-level ORM methods that build such objects. Those methods are also responsible for checking the access rights on the fields that are used in the SQL object.
