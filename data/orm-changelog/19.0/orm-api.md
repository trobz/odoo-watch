---
version: "19.0"
app: "ORM API"
app_slug: "orm-api"
source_url: "https://www.odoo.com/documentation/master/developer/reference/backend/orm/changelog.html"
item_count: 15
---

# ORM API changelog (19.0)

## Add support for `GROUPING SETS` for pivot views

See [#194413](https://github.com/odoo/odoo/pull/194413).

## Adding support for dynamic dates in domains

See [#216665](https://github.com/odoo/odoo/pull/216665).

## Deprecated `odoo.osv` in [#217708](https://github.com/odoo/odoo/pull/217708)

## Deprecated `record._cr`, `record._context`, `record._uid` in [#193636](https://github.com/odoo/odoo/pull/193636)

## The `reinit` option is added to the CLI to reinitialize modules

See [#206408](https://github.com/odoo/odoo/pull/206408).

## Possibility to write and combine custom domains for injecting arbitrary SQL

See [#205208](https://github.com/odoo/odoo/pull/205208).

## Domain optimization is applied before executing `Fields.search` methods

All equalities are handled consistently: `=` is equivalent to `in`. See [#191549](https://github.com/odoo/odoo/pull/191549).

## New cron API for notifying progress with batch commits

See [#197781](https://github.com/odoo/odoo/pull/197781).

## Demo data no longer loaded by default

See [#194585](https://github.com/odoo/odoo/pull/194585).

## `read_group` has been deprecated in favor of `_read_group` for backend usage and of `formatted_read_group` as formatted public API

See [#163300](https://github.com/odoo/odoo/pull/163300).

## `@api.private` is added to distinguish public Python methods from methods exposed for RPC calls

See [#195402](https://github.com/odoo/odoo/pull/195402).

## Native namespaces for `odoo` module [PEP-420](https://peps.python.org/pep-0420/)

See [#195664](https://github.com/odoo/odoo/pull/195664).

## New `odoo.domain` and `odoo.Domain` API for domain manipulation

See [#170009](https://github.com/odoo/odoo/pull/170009).

## Declare constraints and indexes as model attributes with [#175783](https://github.com/odoo/odoo/pull/175783)

## The `json` controllers have been renamed to `jsonrpc`

They are called the same, only the `type` in the python files changed. See [#183636](https://github.com/odoo/odoo/pull/183636).
