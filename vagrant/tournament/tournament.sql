-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;
\c tournament;


DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS players;
create table players
	(id 		SERIAL CONSTRAINT firstkey PRIMARY KEY,
	 name 		varchar(40) not null
	 )
;
create table matches
	(id 		SERIAL UNIQUE,
	 winner		integer references players (id),
	 loser 		integer references players (id)
	 )
;