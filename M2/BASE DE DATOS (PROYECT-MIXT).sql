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

INSERT INTO characters VALUES(1, 'Sir Mirrin y la princesa Minina'),(2, 'Vandal');
INSERT INTO adventure (idAdventure, Name, Description, idCharacter) VALUES
(1, 'La cueva perdida', 'Aria explora una cueva misteriosa llena de secretos.', 1),
(2, 'El bosque oscuro', 'Dario se adentra en un bosque peligroso.', 2);
(3, 'La luz del cometa', 'En el Reino Felinia, la princesa gata Lira y el gato mago Nimbus investigan una luz azulada que cambia el destino del reino.', 1);

-- PASOS DE LAS AVENTURAS
INSERT INTO bystep_adventure (idByStep_Adventure, idAdventure, Description, Final_Step) VALUES
(1, 1, 'Aria entra a la cueva y ve dos caminos.', 0),
(2, 1, 'Aria encuentra un tesoro oculto.', 1),
(3, 2, 'Dario escucha ruidos extraños en el bosque.', 0),
(4, 2, 'Dario derrota a la bestia del bosque.', 1);
(20, 3, 'Inicio: Lira espera a Nimbus. Una luz azulada parpadea en el bosque. ¿Investigar la luz?', 0),
(21, 3, 'Sección A: La luz proviene de un cristal flotante. Nimbus dice que es un Fragmento del Cometa. ¿Tocas el cristal?', 0),
(22, 3, 'A1: Lira toca el cristal. Se abre un portal. Solo quienes tocaron el cristal pueden cruzarlo. ¿Cruzan el portal?', 0),
(23, 3, 'A2: Nimbus toca el cristal y obtiene el Hechizo de Eco Temporal. ¿Cruzan el portal?', 0),
(24, 3, 'B: Camino al festival. El cielo se oscurece y una sombra cubre la luna. ¿Se quedan en el festival o investigan la sombra?', 0),
(25, 3, 'B1: El festival continúa hasta que la sombra desciende y una criatura exige el Fragmento del Cometa.', 0),
(26, 3, 'C: Camino del Portal. Bosque estelar con un árbol de tres sendas brillantes.', 0),
(27, 3, 'C1: Senda plateada. Encuentran un espejo que muestra futuros posibles.', 0),
(28, 3, 'C2: Senda dorada. Un espíritu felino ofrece un pacto: poder a cambio de un recuerdo importante.', 0),
(29, 3, 'C3: Senda violeta (solo si Nimbus tiene el hechizo). Camino oculto hacia la Cámara del Cometa.', 0),
(30, 3, 'D: Investigar la sombra. Umbros, el espíritu felino que absorbe magia del cometa.', 0),
(31, 3, 'E: Lira activa la marca. La Marca crea un escudo lunar y permite purificar a Umbros.', 0),
(32, 3, 'F: Nimbus usa el Hechizo de Eco Temporal y ve la vulnerabilidad de Umbros.', 0),
(33, 3, 'G: El espejo se abre como puerta hacia una torre de luz (si Lira tiene la marca).', 0),
(34, 3, 'H: Pacto del Recuerdo: aceptar implica entregar un recuerdo importante.', 0),
(35, 3, 'I: Cámara del Cometa: obtención del Fragmento Mayor.', 0),
(36, 3, 'J: Batalla Final contra Umbros. Dependiendo de lo que tengan, se llega a distintos finales.', 0),
(37, 3, 'Final Malo 1: Sin herramientas, Umbros domina y Felinia cae en sombra.', 1),
(38, 3, 'Final Malo 2: Capturados por Umbros por no tener nada especial.', 1),
(39, 3, 'Final Neutro 1: Visiones confusas; no obtienen ventaja real.', 1),
(40, 3, 'Final Neutro 2: Rechazan el pacto; se retiran sin poder.', 1),
(41, 3, 'Final Bueno 1: Solo la Marca — Lira purifica y nace un amor tierno entre Lira y Nimbus.', 1),
(42, 3, 'Final Bueno 2: Solo el Hechizo — Nimbus encierra a Umbros; relación fría entre Lira y Nimbus.', 1),
(43, 3, 'Final Verdadero: Fragmento Mayor — Custodia y viaje; vínculo profesional profundo.', 1),
(44, 3, 'Final Épico: Marca + Hechizo — Triunfo y relación apasionada y colaborativa.', 1),
(45, 3, 'Final Supremo: Marca + Hechizo + Fragmento Mayor — Purificación completa; leyenda y era dorada.', 1);

-- RESPUESTAS POR PASO
INSERT INTO answers_bystep_adventure 
(idAnswers_ByStep_Adventure, idByStep_Adventure, Description, Resolution_Anwer, NextStep_Adventure) VALUES
(1, 1, 'Tomar el camino de la izquierda', 'Avanza con cuidado', 2),
(2, 1, 'Tomar el camino de la derecha', 'Encuentra trampas', 2),
(3, 3, 'Investigar el ruido', 'Encuentra a la bestia', 4),
(4, 3, 'Ignorar el ruido', 'La bestia ataca por sorpresa', 4);
(200, 20, 'Sí, investigar la luz', 'Lira y Nimbus van a investigar la luz', 21),
(201, 20, 'No, seguir al festival', 'Deciden ignorar la luz y seguir hacia el festival', 24),

(202, 21, 'Sí, Lira toca el cristal', 'El cristal reacciona y se abre un portal para quien lo tocó', 22),
(203, 21, 'No, Nimbus toca el cristal', 'El cristal absorbe magia; Nimbus obtiene el Hechizo de Eco Temporal', 23),

(204, 22, 'Cruzan el portal', 'Cruzan el portal hacia el bosque estelar', 26),
(205, 22, 'No cruzan; regresan al festival (Lira conserva la Marca)', 'Regresan al camino del festival con la Marca del cristal', 24),

(206, 23, 'Cruzan el portal', 'Cruzan el portal hacia el bosque estelar', 26),
(207, 23, 'No cruzan; regresan al festival (Nimbus conserva el Hechizo)', 'Regresan al camino del festival con el Hechizo desbloqueado', 24),

(208, 24, 'Se quedan en el festival', 'Deciden quedarse en el festival', 25),
(209, 24, 'Investigan la sombra', 'Se dirigen a investigar la sombra', 30),

(210, 25, 'Nadie tocó el cristal', 'Sin herramientas no pueden defenderse', 37),
(211, 25, 'Lira tocó el cristal (activar Marca)', 'Lira puede activar la Marca para proteger', 31),
(212, 25, 'Nimbus obtuvo el Hechizo', 'Nimbus puede usar el Hechizo para ver la debilidad', 32),

(213, 26, 'Elegir senda plateada', 'Se dirigen a la senda plateada', 27),
(214, 26, 'Elegir senda dorada', 'Se dirigen a la senda dorada', 28),
(215, 26, 'Elegir senda violeta', 'Se dirigen a la senda violeta (requiere Hechizo)', 29),

(216, 27, 'Si Lira tiene la Marca, abrir puerta', 'El espejo se abre como puerta hacia la torre de luz', 33),
(217, 27, 'Si no tienen la Marca, solo visiones', 'Solo ven visiones confusas', 39),

(218, 28, 'Aceptar el pacto del espíritu', 'Aceptan entregar un recuerdo a cambio de poder', 34),
(219, 28, 'Rechazar el pacto', 'Rechazan el pacto y se retiran', 40),

(220, 29, 'Seguir hacia la Cámara del Cometa', 'El Hechizo reacciona y abre el camino hacia la Cámara', 35),

(221, 30, 'No tienen nada especial', 'Umbros los captura por falta de herramientas', 38),
(222, 30, 'Lira usa la Marca para repeler', 'Lira repela la sombra con la Marca', 31),
(223, 30, 'Nimbus anticipa ataques con el Hechizo', 'Nimbus usa el Hechizo para anticipar y defender', 32),
(224, 30, 'Tienen el Fragmento Mayor y enfrentan a Umbros', 'Con el Fragmento Mayor pueden enfrentarlo', 36),

(225, 31, 'Ir a la Batalla Final (desde Marca)', 'La Marca permite proteger recuerdos; se avanza a la batalla', 36),
(226, 32, 'Ir a la Batalla Final (desde Hechizo)', 'El Hechizo revela la vulnerabilidad; se avanza a la batalla', 36),
(227, 33, 'Salir de la torre hacia la batalla', 'La visión de la torre guía a la batalla final', 36),

(228, 34, 'Aceptar el pacto y usar el poder', 'El recuerdo alimenta la magia; se avanza a la batalla', 36),
(229, 34, 'Rechazar el pacto y volver', 'Rechazan y se retiran sin ventaja', 40),

(230, 35, 'Obtener el Fragmento Mayor', 'Consiguen el Fragmento Mayor y se preparan para la batalla', 36),

-- Respuestas en la Batalla Final que llevan a cada final según lo que usen
(231, 36, 'Usar solo la Marca', 'Solo la Marca se usa en la batalla', 41),
(232, 36, 'Usar solo el Hechizo', 'Solo el Hechizo se usa en la batalla', 42),
(233, 36, 'Usar el Fragmento Mayor', 'El Fragmento Mayor se usa en la batalla', 43),
(234, 36, 'Combinar Marca y Hechizo', 'Marca y Hechizo combinados en la batalla', 44),
(235, 36, 'Combinar Marca, Hechizo y Fragmento', 'Todos los elementos combinados', 45);

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
