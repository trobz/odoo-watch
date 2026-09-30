---
version: "20.0"
app: "ORM API"
app_slug: "orm-api"
source_url: "https://www.odoo.com/documentation/master/developer/reference/backend/orm/changelog.html"
item_count: 21
---

# ORM API changelog (20.0)

## Adding `BinaryValue.filename` and updating the RPC format for binary fields

See [#266082](https://github.com/odoo/odoo/pull/266082).

## Removing `Model._table_query` in [#281202](https://github.com/odoo/odoo/pull/281202)

## Simplifying translation manipulation

Fields have now a copy function and it defaults to a function that adds “(copy)” for char fields named “name”. See [#272177](https://github.com/odoo/odoo/pull/272177) and [#284881](https://github.com/odoo/odoo/pull/284881).

## New `populate` script to generate fake data for testing

## Storing manifest terms in modules’ own translation files instead of `base`

See [#264363](https://github.com/odoo/odoo/pull/264363).

## `ir.access` that merges ACLs and record rules

See [#166359](https://github.com/odoo/odoo/pull/166359).

## Field updates and inverse execution are now consistently ordered by `(field.write_sequence, field_index)` in both `create()` and `write()`

See [#265469](https://github.com/odoo/odoo/pull/265469).

## New HTTP server based on h11

See [#247162](https://github.com/odoo/odoo/pull/247162).

## Removing `request` from the code of models and adding `env.website`

See [#252766](https://github.com/odoo/odoo/pull/252766).

## Thread-safe ormcache and automatic signaling

See [#255059](https://github.com/odoo/odoo/pull/255059) and [#261736](https://github.com/odoo/odoo/pull/261736).

## Modularize reporting engines and prepare paper-muncher

See respectively [#259626](https://github.com/odoo/odoo/pull/259626). and [#264068](https://github.com/odoo/odoo/pull/264068).

## The type of Binary fields is now a BinaryValue

We no longer encode using base64 all over the data flow, just use the new object. See [#244421](https://github.com/odoo/odoo/pull/244421).

## Fixing cache pollution for x2many fields

Accessing such a field returns only the accessible records. See [#254944](https://github.com/odoo/odoo/pull/254944).

## Custom access permissions implemented using domains

A domain operator “access” can check explicitly the permissions of the comodel easing writing access rules. See [#254381](https://github.com/odoo/odoo/pull/254381) and [#239862](https://github.com/odoo/odoo/pull/239862).

## Simpler `Model.concat` and `Model.union` API

See [#249731](https://github.com/odoo/odoo/pull/249731).

## Write multiple translations in one write

See [#246357](https://github.com/odoo/odoo/pull/246357).

## Binary fields store only binary data in raw format

See [#235832](https://github.com/odoo/odoo/pull/235832) and [#238513](https://github.com/odoo/odoo/pull/238513).

## Various qweb improvements

See [#232539](https://github.com/odoo/odoo/pull/232539) and [#244092](https://github.com/odoo/odoo/pull/244092).

## New API for ir.config_parameter

See [#223180](https://github.com/odoo/odoo/pull/223180).

## New API to build SQL

See [#234156](https://github.com/odoo/odoo/pull/234156).

## `Field.compute_sql` allows to define a way to produce SQL for computed fields

Once done, we can group by and sort using computed fields. See [#221544](https://github.com/odoo/odoo/pull/221544).
