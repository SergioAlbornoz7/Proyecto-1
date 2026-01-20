DROP DATABASE IF EXISTS ProyectoMX;
CREATE DATABASE ProyectoMX CHARACTER SET utf8mb4;
USE ProyectoMX;

CREATE TABLE characters (
  idCharacter INT primary key,
  CharacterName VARCHAR(45)
);
CREATE TABLE adventure (
  idAdventure INT primary key,
  Name Varchar(45),
  Description Varchar(4000),
  idCharacter INT,
  foreign key (idCharacter) references characters(idCharacter)
);
CREATE TABLE bystep_adventure (
  idByStep_Adventure INT primary key,
  idAdventure int,
  Description Varchar(4000),
  Final_Step TINYINT,
  FOREIGN KEY (idAdventure) REFERENCES adventure(idAdventure)

);
CREATE TABLE answers_bystep_adventure (
  idAnswers_ByStep_Adventure INT primary key,
  idByStep_Adventure int,
  Description Varchar(2000),
  Resolution_Anwer Varchar(200),
  NextStep_Adventure INT,
  foreign key(idByStep_Adventure) references bystep_adventure(idByStep_Adventure),
  foreign key(NextStep_Adventure) references bystep_adventure(idByStep_Adventure)
);
CREATE TABLE user (
  idUser INT auto_increment primary key,
  Username Varchar(10),
  Password Varchar(45)
);
CREATE TABLE game (
  idGame INT auto_increment primary key,
  idUser int,
  idCharacter INT,
  idAdventure INT,
  Date Datetime,
  foreign key (idUser) references user(idUser),
  foreign key (idAdventure) references adventure(idAdventure),
  foreign key (idCharacter) references characters(idCharacter)
);
CREATE TABLE choices (
  idGame INT,
  idByStep_Adventure int,
  idAnswers_ByStep_Adventure INT,
  foreign key (idGame)references game(idGame),
  foreign key (idByStep_Adventure)references bystep_adventure(idByStep_Adventure),
  foreign key(idAnswers_ByStep_Adventure)references answers_bystep_adventure(idAnswers_ByStep_Adventure),
  PRIMARY KEY (idGame, idByStep_Adventure)
);

INSERT INTO characters VALUES(1, 'Aria la Exploradora'),(2, 'Dario el Guerrero');
INSERT INTO adventure (idAdventure, Name, Description, idCharacter) VALUES
(1, 'La cueva perdida', 'Aria explora una cueva misteriosa llena de secretos.', 1),
(2, 'El bosque oscuro', 'Dario se adentra en un bosque peligroso.', 2);

-- PASOS DE LAS AVENTURAS
INSERT INTO bystep_adventure (idByStep_Adventure, idAdventure, Description, Final_Step) VALUES
(1, 1, 'Aria entra a la cueva y ve dos caminos.', 0),
(2, 1, 'Aria encuentra un tesoro oculto.', 1),
(3, 2, 'Dario escucha ruidos extraños en el bosque.', 0),
(4, 2, 'Dario derrota a la bestia del bosque.', 1);

-- RESPUESTAS POR PASO
INSERT INTO answers_bystep_adventure 
(idAnswers_ByStep_Adventure, idByStep_Adventure, Description, Resolution_Anwer, NextStep_Adventure) VALUES
(1, 1, 'Tomar el camino de la izquierda', 'Avanza con cuidado', 2),
(2, 1, 'Tomar el camino de la derecha', 'Encuentra trampas', 2),
(3, 3, 'Investigar el ruido', 'Encuentra a la bestia', 4),
(4, 3, 'Ignorar el ruido', 'La bestia ataca por sorpresa', 4);

-- USUARIO
INSERT INTO user VALUES(1, 'player1', '1234'),(2, 'player2', '123');

-- JUEGOS (uno por personaje)
INSERT INTO game (idGame, idUser, idCharacter, idAdventure, Date) VALUES
(1, 1, 1, 1, NOW()),
(2, 1, 2, 2, NOW());

-- ELECCIONES REALIZADAS
INSERT INTO choices (idGame, idByStep_Adventure, idAnswers_ByStep_Adventure) VALUES
(1, 1, 1),
(2, 3, 3);
