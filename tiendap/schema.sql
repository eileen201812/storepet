CREATE TABLE contacto (
	codigo bigserial,
	run numeric(13),
	dv varchar(1),
	nombres varchar(80),
	apellido_paterno varchar(80),
	apellido_materno varchar(80),
	email varchar(80),
	telefono varchar(16),
	asunto varchar(250),
	primary key (codigo)
);

CREATE TABLE registrodeusuario (
	codigo bigserial,
	nombres varchar(80),
	apellido_paterno varchar(80),
	apellido_materno varchar(80),
	email varchar(80),
	primary key (codigo)
);