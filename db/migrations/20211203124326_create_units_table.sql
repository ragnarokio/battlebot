-- migrate:up
create table units(
	id serial primary key,
	player_id text not null,
	name text not null,
	life int not null,
	damage int not null,
	tags text[]
);


-- migrate:down
drop table units;

