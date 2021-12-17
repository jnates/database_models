-- Create a keyspace
CREATE KEYSPACE IF NOT EXISTS storebooks WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '1' };

-- Create a table
CREATE TABLE IF NOT EXISTS storebooks.books (
bookid text,
title text,
author text,
content_short text,
publisher text,
publisher_date text,
pages text,
lan text,
primary key(bookid, publisher_date, author, title )
)WITH CLUSTERING ORDER BY (publisher_date DESC, author ASC, title ASC);

CREATE TABLE IF NOT EXISTS storebooks.author_book (
authorid text,
author text,
book text,
publisher text,
publisher_date text,
pages text,
lan text,
primary key((authorid, author), book )
);


authorid,author,book,publisher,publisher_date,pages,lan,
insert into storebooks.author(bookid,title,content_short,publisher,publisher_date,pages,lan) values