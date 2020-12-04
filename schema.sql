drop table if exists users;
drop table if exists transactions;

create table users (
    username text primary key unique not null,
    amount float not null,
    publickey BLOB unique not null
);

create table transactions (
    id integer primary key autoincrement,
    amount float not null,
    time TEXT DEFAULT CURRENT_TIMESTAMP,
    user1 integer not null,
    user2 integer not null,
    hash TEXT not null,
    FOREIGN KEY (user1) REFERENCES users (username),
    FOREIGN KEY (user2) REFERENCES users (username)
);




