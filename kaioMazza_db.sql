create database kaioMazza_db

create table usuario(
    userid int not null auto_increment,
    nome text,
    telefone text,
    email text,
    usuario text,
    senha text,
    primary key (userid)    
);