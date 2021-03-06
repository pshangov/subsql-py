SubSQL
======

About
-----

SubSQL allows you to manage your SQL queries in text files. It is inspired by and fairly similar to [PugSQL](https://pugsql.org/) and [HugSQL](https://www.hugsql.org/). The main difference from PugSQL is that where PugSQL uses SQLAlchemy to interface with databases, SubSQL uses the native database drivers (e.g. psycopg2 for PostgreSQL), which provides more flexibility at the expense of having to write connectors for each individual driver.

This is alfa-quality software and the interface is likely to change.

Usage
-----

See the `tests` folder for examples.

Drivers
-------

SubSQL comes bundled with a SQLite driver. A PostgreSQL driver is also available as `subsql-pg`.
