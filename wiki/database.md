# Database

<h2>Table of contents</h2>

- [What is a database](#what-is-a-database)
- [Database server](#database-server)
- [`PostgreSQL`](#postgresql)
- [`pgAdmin`](#pgadmin)
- [`SQL`](#sql)
- [Database schema](#database-schema)
- [Database table](#database-table)
- [Database row](#database-row)
- [Database modeling](#database-modeling)

## What is a database

A database is an organized collection of data that can be accessed, managed, and updated.

Databases store data in structures such as tables (rows and columns).

## Database server

A database server is software that manages one or more databases and handles queries from clients (applications).

Examples of database servers: [`PostgreSQL`](./postgresql.md#postgresql-server), `MySQL`, `SQLite`.

## `PostgreSQL`

See [`PostgreSQL`](./postgresql.md#what-is-postgresql).

## `pgAdmin`

See [`pgAdmin`](./pgadmin.md#what-is-pgadmin).

## `SQL`

See [`SQL`](./sql.md#what-is-sql).

## Database schema

The database schema defines the structure of the database: tables, columns, data types, and constraints.

You can [inspect columns](./pgadmin.md#browse-columns-in-the-table) of a table in [`pgAdmin`](./pgadmin.md#what-is-pgadmin).

> [!NOTE]
> The column names in the database must match the field names in the [`Python`](./python.md#what-is-python) code.
> If they don't match, the application will fail to read data from the database.

## Database table

A database table is a collection of related data organized into rows and columns.

Each table represents one entity type (e.g., `users`, `todos`). The columns of a table are defined by the [database schema](#database-schema).

## Database row

A database row (also called a record) is a single entry in a [database table](#database-table).

Each row represents one instance of the entity and contains a value for each column.

## Database modeling

See [Database modeling](./database-modeling.md#what-is-database-modeling).
