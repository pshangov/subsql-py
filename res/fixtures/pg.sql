-- :name user_for_id :one
select * from users where user_id = %(user_id)s;

-- :name search_users :many
select * from users where username like %(pattern)s;

-- :name update_username :rowcount
update users set username = %(username)s
where user_id = %(user_id)s;

-- :name get_username :scalar
select username from users where user_id = %(user_id)s;

-- :name add_user
-- :lastrowid
insert into users (username) values (%(username)s);

-- :name save_post :void :execute values
INSERT INTO users (
    username,
    firstname,
    lastname,
    email,
    created
) VALUES %s;

-- :template save_post
(%(username)s, %(firstname)s, %(lastname)s, %(email)s, NOW())

-- :name set_created
update {tablename} set created = NOW();

