-- Create a keyspace
CREATE KEYSPACE IF NOT EXISTS storebooks WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '1' };

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
