create DATABASE Whatsapp
USE Whatsapp;
SHOW TABLES;

USE Whatsapp;
select * from USUARIOS;

create TABLE USUARIOS (
  ID INT AUTO_INCREMENT PRIMARY KEY,       -- Reemplaza IDENTITY por AUTO_INCREMENT
  CELULAR VARCHAR(100) UNIQUE NOT NULL,
  NOMBRE VARCHAR(100) NOT NULL,
  ESTADO VARCHAR(1),
  Usuario_Creacion INT,
  ID_Creacion VARCHAR(20),
  Fecha_Creacion DATETIME,
  Usuario_Modificacion INT,
  ID_Modificacion VARCHAR(20),
  Fecha_Modificacion DATETIME
)

USE Whatsapp;
select * from ESTADOS;

create TABLE ESTADOS (
  ID INT AUTO_INCREMENT,   
  ID_USUARIO INT,-- Solo ID debe ser AUTO_INCREMENT
  CONTENIDO VARCHAR(100),
  Usuario_Creacion INT,
  ID_Creacion VARCHAR(20),
  Fecha_Creacion DATETIME,
  Usuario_Modificacion INT,
  ID_Modificacion VARCHAR(20),
  Fecha_Modificacion DATETIME,
  FOREIGN KEY (ID_USUARIO) REFERENCES USUARIOS(ID),
  PRIMARY KEY (ID)            
);

ALTER TABLE ESTADOS CHANGE COLUMN ID_USUARIO id_usuario_id INT;

