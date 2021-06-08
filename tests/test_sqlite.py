import pytest

import sqlite3
from subsql import SubSQL, sqlitedriver

def test_driver():
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    path = './res/fixtures/sqlite.sql'
    subsql = SubSQL(conn, driver=sqlitedriver)
    db = subsql.load(path)

    db.create_schema()

    db.save_users([
        (1, 'foo', 'Foo', 'Fi', 'foo@foo.com'),
        (2, 'bar', 'Bar', 'Baz', 'bar@bar.com')
    ])

    assert db.count_users() == 2

    first_user = db.get_user({'id': 1})
    assert first_user['username'] == 'foo'

    rowcount = db.update_username({'id': 2, 'username': 'baz'})
    assert rowcount == 1

    bar_users = db.search_users({'pattern': 'bar'})
    assert len(bar_users) == 0

    baz_users = db.search_users({'pattern': 'baz'})
    assert baz_users[0]['firstname'] == 'Bar'
