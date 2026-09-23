---
version: "16.0"
app: "ORM API"
app_slug: "orm-api"
source_url: "https://www.odoo.com/documentation/master/developer/reference/backend/orm/changelog.html"
item_count: 13
---

# ORM API changelog (16.0)

## Translations for translated fields are stored as JSONB values with [#97692](https://github.com/odoo/odoo/pull/97692) and [#101115](https://github.com/odoo/odoo/pull/101115)

Code translations are no longer stored into the database. They become static and are extracted from the PO files when needed.

## [`search_count()`](../orm.html#odoo.models.Model.search_count) takes the `limit` argument into account with [#95589](https://github.com/odoo/odoo/pull/95589)

It limits the number of records to count, improving performance when a partial result is acceptable.

## New API for flushing to the database and invalidating the cache with [#87527](https://github.com/odoo/odoo/pull/87527)

New methods have been added to `odoo.models.Model` and `odoo.api.Environment`, and are less confusing about what is actually done in each case. See the section [SQL Execution](../orm.html#reference-orm-sql).

## The argument `args` is renamed to `domain` for [`search()`](../orm.html#odoo.models.Model.search), [`search_count()`](../orm.html#odoo.models.Model.search_count) and `_search()`

[#83687](https://github.com/odoo/odoo/pull/83687)

## [`filtered_domain()`](../orm.html#odoo.models.Model.filtered_domain) conserves the order of the current recordset

[#83687](https://github.com/odoo/odoo/pull/83687)

## [`browse()`](../orm.html#odoo.models.Model.browse) does not accept [`str`](https://docs.python.org/3/library/stdtypes.html#str) as `ids`

[#83687](https://github.com/odoo/odoo/pull/83687)

## The methods `fields_get_keys()` and `get_xml_id()` on [`Model`](../orm.html#odoo.models.Model) are deprecated

[#83687](https://github.com/odoo/odoo/pull/83687)

## The method `_mapped_cache()` is removed

[#83687](https://github.com/odoo/odoo/pull/83687)

## Remove the `limit` attribute of [`One2many`](../orm.html#odoo.fields.One2many) and [`Many2many`](../orm.html#odoo.fields.Many2many)

[#83687](https://github.com/odoo/odoo/pull/83687)

## Specific index types on fields: With [#83274](https://github.com/odoo/odoo/pull/83274) and [#83015](https://github.com/odoo/odoo/pull/83015), developers can now define what type of indexes can be used on fields by PostgreSQL

See the [index property](../orm.html#reference-fields) of `odoo.fields.Field`.

## The `_sequence` attribute of [`Model`](../orm.html#odoo.models.Model) is removed

Odoo lets PostgreSQL use the default sequence of the primary key. [#82727](https://github.com/odoo/odoo/pull/82727)

## The method `_write()` does not raise an error for non-existing records

[#82727](https://github.com/odoo/odoo/pull/82727)

## The `column_format` and `deprecated` attributes of [`Field`](../orm.html#odoo.fields.Field) are removed

[#82727](https://github.com/odoo/odoo/pull/82727)
