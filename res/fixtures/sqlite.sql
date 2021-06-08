-- :name get_user :one
select * from users where id = :id

-- :name search_users :many
select * from users where username like :pattern

-- :name update_username :rowcount
update users set username = :username
where id = :id

-- :name count_users :scalar
select count(*) from users

-- :name add_user
-- :lastrowid
insert into users (username) values (:username)

-- :name save_users :void :execute many
insert into users (
    id,
    username,
    firstname,
    lastname,
    email
) values (?, ?, ?, ?, ?)

-- :name create_schema :execute script
create table users (
    id integer,
    username varchar(200),
    firstname varchar(200),
    lastname varchar(200),
    email varchar(200)
);

create table permissions (
    id integer,
    user_id int references users(id),
    permission varchar(200)
);
