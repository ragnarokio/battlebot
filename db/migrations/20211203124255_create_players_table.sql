-- migrate:up
create table players (
	-- this is the discord id too
	id text primary key not null,
	character_name text not null,
	unit_ids int[]
);


-- migrate:down
drop table players;


