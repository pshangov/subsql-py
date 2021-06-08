import pytest

from subsql import sqlitedriver, SQLiteCommand
from subsql.parser import ParserError

def test_commands():
    path = './res/fixtures/sqlite.sql'
    errors, commands = sqlitedriver.parse(path)

    assert len(errors) == 0
    assert len(commands) == 7

    assert type(commands[0]) == SQLiteCommand
    assert commands[0].name == 'get_user'
    assert commands[0].query == 'select * from users where id = :id'
    assert commands[0].returns == 'one'
    assert commands[0].execute == None

    assert type(commands[1]) == SQLiteCommand
    assert commands[1].name == 'search_users'
    assert commands[1].query == 'select * from users where username like :pattern'
    assert commands[1].returns == 'many'
    assert commands[1].execute == None

    assert type(commands[2]) == SQLiteCommand
    assert commands[2].name == 'update_username'
    assert commands[2].query == 'update users set username = :username\nwhere id = :id'
    assert commands[2].returns == 'rowcount'
    assert commands[2].execute == None

    assert type(commands[3]) == SQLiteCommand
    assert commands[3].name == 'count_users'
    assert commands[3].query == 'select count(*) from users'
    assert commands[3].returns == 'scalar'
    assert commands[3].execute == None

    assert type(commands[4]) == SQLiteCommand
    assert commands[4].name == 'add_user'
    assert commands[4].query == 'insert into users (username) values (:username)'
    assert commands[4].returns == 'lastrowid'
    assert commands[4].execute == None

    assert type(commands[5]) == SQLiteCommand
    assert commands[5].name == 'save_users'
    assert commands[5].query == 'insert into users (\n    id,\n    username,\n    firstname,\n    lastname,\n    email\n) values (?, ?, ?, ?, ?)'
    assert commands[5].returns == 'void'
    assert commands[5].execute == 'many'

    assert type(commands[6]) == SQLiteCommand
    assert commands[6].name == 'create_schema'
    assert commands[6].returns == 'void'
    assert commands[6].execute == 'script'
    assert 'create table users' in commands[6].query
    assert 'create table permissions' in commands[6].query

def test_errors():
    path = './res/fixtures/errors.sql'
    errors, commands = sqlitedriver.parse(path)

    assert len(errors) == 7
    assert len(commands) == 1

    assert type(commands[0]) == SQLiteCommand
    assert commands[0].name == 'get_user'
    assert commands[0].query == 'select * from users where user_id = :user_id'
    assert commands[0].returns == 'one'
    assert commands[0].execute == None

    assert type(errors[0]) == ParserError
    assert errors[0].message == "Command get_user already exists"
    assert errors[0].file == './res/fixtures/errors.sql'
    assert errors[0].lineno == 5

    assert type(errors[1]) == ParserError
    assert errors[1].message == "Snippet doesn't have a name"
    assert errors[1].file == './res/fixtures/errors.sql'
    assert errors[1].lineno == 9

    assert type(errors[2]) == ParserError
    assert errors[2].message == "Found duplicate option many"
    assert errors[2].file == './res/fixtures/errors.sql'
    assert errors[2].lineno == 13

    assert type(errors[3]) == ParserError
    assert errors[3].message == "Unsupported option affected"
    assert errors[3].file == './res/fixtures/errors.sql'
    assert errors[3].lineno == 17

    assert type(errors[4]) == ParserError
    assert errors[4].message == "Multiple returns types (scalar, one) specified for command get_username"
    assert errors[4].file == './res/fixtures/errors.sql'
    assert errors[4].lineno == 21

    assert type(errors[5]) == ParserError
    assert errors[5].message == "Parameter to :execute must be 'many' or 'script', not 'batch'"
    assert errors[5].file == './res/fixtures/errors.sql'
    assert errors[5].lineno == 25

    assert type(errors[6]) == ParserError
    assert errors[6].message == "No query found for command find_users"
    assert errors[6].file == './res/fixtures/errors.sql'
    assert errors[6].lineno == 29

