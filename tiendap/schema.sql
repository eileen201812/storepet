
create table category (
	id BIGSERIAL PRIMARY KEY,
	category_name varchar(100),	
	category_description varchar(200)
);







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
	run numeric(13),
	dv varchar(1),
	nombres varchar(80),
	apellido_paterno varchar(80),
	apellido_materno varchar(80),
	email varchar(80),
	primary key (codigo)
);



create table product (
	id BIGSERIAL PRIMARY KEY,
	name varchar(150),
	product_description varchar(200),
		
	category_code BIGINT,
    img_url varchar(250),
   	
   	CONSTRAINT fk_product_category_id
    	FOREIGN KEY(category_code) 
	 	REFERENCES category(id)	
);