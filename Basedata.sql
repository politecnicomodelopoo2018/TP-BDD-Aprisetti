-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema TPPYTHON
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `TPPYTHON` ;

-- -----------------------------------------------------
-- Schema TPPYTHON
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `TPPYTHON` DEFAULT CHARACTER SET utf8 ;
USE `TPPYTHON` ;

-- -----------------------------------------------------
-- Table `TPPYTHON`.`Autores`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `TPPYTHON`.`Autores` ;

CREATE TABLE IF NOT EXISTS `TPPYTHON`.`Autores` (
  `idAutor` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `fechaNac` DATE NULL,
  `ratingPromedio` VARCHAR(45) NULL,
  PRIMARY KEY (`idAutor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TPPYTHON`.`Productores`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `TPPYTHON`.`Productores` ;

CREATE TABLE IF NOT EXISTS `TPPYTHON`.`Productores` (
  `idProductor` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `fechaNac` DATE NULL,
  `añosDeExperiencia` INT NULL,
  PRIMARY KEY (`idProductor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TPPYTHON`.`Categorias`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `TPPYTHON`.`Categorias` ;

CREATE TABLE IF NOT EXISTS `TPPYTHON`.`Categorias` (
  `idCategoria` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`idCategoria`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TPPYTHON`.`Peliculas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `TPPYTHON`.`Peliculas` ;

CREATE TABLE IF NOT EXISTS `TPPYTHON`.`Peliculas` (
  `idPelicula` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(45) NULL,
  `duracion` INT NULL,
  `fechaLanzamiento` DATE NULL,
  `presupuesto` INT NULL,
  `ganancia` INT NULL,
  `sinopsis` TEXT NULL,
  `idAutor` INT NOT NULL,
  `idProductor` INT NOT NULL,
  `idCategoria` INT NOT NULL,
  PRIMARY KEY (`idPelicula`),
  INDEX `fk_Peliculas_Autores_idx` (`idAutor` ASC),
  INDEX `fk_Peliculas_Productores1_idx` (`idProductor` ASC),
  INDEX `fk_Peliculas_Categorias1_idx` (`idCategoria` ASC),
  CONSTRAINT `fk_Peliculas_Autores`
    FOREIGN KEY (`idAutor`)
    REFERENCES `TPPYTHON`.`Autores` (`idAutor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Peliculas_Productores1`
    FOREIGN KEY (`idProductor`)
    REFERENCES `TPPYTHON`.`Productores` (`idProductor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Peliculas_Categorias1`
    FOREIGN KEY (`idCategoria`)
    REFERENCES `TPPYTHON`.`Categorias` (`idCategoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TPPYTHON`.`Actores`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `TPPYTHON`.`Actores` ;

CREATE TABLE IF NOT EXISTS `TPPYTHON`.`Actores` (
  `idActor` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `fechaNac` VARCHAR(45) NULL,
  `cantidadDePeliculas` INT NULL,
  PRIMARY KEY (`idActor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TPPYTHON`.`Reviews`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `TPPYTHON`.`Reviews` ;

CREATE TABLE IF NOT EXISTS `TPPYTHON`.`Reviews` (
  `idReview` INT NOT NULL AUTO_INCREMENT,
  `critico` VARCHAR(45) NULL,
  `descripcion` TEXT NULL,
  `puntaje` INT NULL,
  `idPelicula` INT NOT NULL,
  PRIMARY KEY (`idReview`),
  INDEX `fk_Reviews_Peliculas1_idx` (`idPelicula` ASC),
  CONSTRAINT `fk_Reviews_Peliculas1`
    FOREIGN KEY (`idPelicula`)
    REFERENCES `TPPYTHON`.`Peliculas` (`idPelicula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TPPYTHON`.`Peliculas_has_Actores`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `TPPYTHON`.`Peliculas_has_Actores` ;

CREATE TABLE IF NOT EXISTS `TPPYTHON`.`Peliculas_has_Actores` (
  `idPelicula` INT NOT NULL,
  `idActor` INT NOT NULL,
  PRIMARY KEY (`idPelicula`, `idActor`),
  INDEX `fk_Peliculas_has_Actores_Actores1_idx` (`idActor` ASC),
  INDEX `fk_Peliculas_has_Actores_Peliculas1_idx` (`idPelicula` ASC),
  CONSTRAINT `fk_Peliculas_has_Actores_Peliculas1`
    FOREIGN KEY (`idPelicula`)
    REFERENCES `TPPYTHON`.`Peliculas` (`idPelicula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Peliculas_has_Actores_Actores1`
    FOREIGN KEY (`idActor`)
    REFERENCES `TPPYTHON`.`Actores` (`idActor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `TPPYTHON`.`Autores`
-- -----------------------------------------------------
START TRANSACTION;
USE `TPPYTHON`;
INSERT INTO `TPPYTHON`.`Autores` (`idAutor`, `nombre`, `apellido`, `fechaNac`, `ratingPromedio`) VALUES (1, 'Robert', 'Guédiguian', '1953-11-13', 1);
INSERT INTO `TPPYTHON`.`Autores` (`idAutor`, `nombre`, `apellido`, `fechaNac`, `ratingPromedio`) VALUES (DEFAULT, 'Alex', 'Garland', '1970-05-26', 2);
INSERT INTO `TPPYTHON`.`Autores` (`idAutor`, `nombre`, `apellido`, `fechaNac`, `ratingPromedio`) VALUES (DEFAULT, 'Alfred', 'Hitchcock', '1899-08-13', 3);
INSERT INTO `TPPYTHON`.`Autores` (`idAutor`, `nombre`, `apellido`, `fechaNac`, `ratingPromedio`) VALUES (DEFAULT, 'Francis Ford', 'Coppola', '1939-03-07', 20);
INSERT INTO `TPPYTHON`.`Autores` (`idAutor`, `nombre`, `apellido`, `fechaNac`, `ratingPromedio`) VALUES (DEFAULT, 'George', 'Lucas', '1944-05-14', 30);

COMMIT;


-- -----------------------------------------------------
-- Data for table `TPPYTHON`.`Productores`
-- -----------------------------------------------------
START TRANSACTION;
USE `TPPYTHON`;
INSERT INTO `TPPYTHON`.`Productores` (`idProductor`, `nombre`, `apellido`, `fechaNac`, `añosDeExperiencia`) VALUES (DEFAULT, 'Du\'fong', 'Bufon', '1999-06-10', 0);
INSERT INTO `TPPYTHON`.`Productores` (`idProductor`, `nombre`, `apellido`, `fechaNac`, `añosDeExperiencia`) VALUES (DEFAULT, 'Andrew', 'Macdonald', '1981-01-09', 8);
INSERT INTO `TPPYTHON`.`Productores` (`idProductor`, `nombre`, `apellido`, `fechaNac`, `añosDeExperiencia`) VALUES (DEFAULT, 'Albert', 'Roodie', '1900-02-03', 18);
INSERT INTO `TPPYTHON`.`Productores` (`idProductor`, `nombre`, `apellido`, `fechaNac`, `añosDeExperiencia`) VALUES (DEFAULT, 'Alfred', 'Hitchcock', '1899-01-02', 50);
INSERT INTO `TPPYTHON`.`Productores` (`idProductor`, `nombre`, `apellido`, `fechaNac`, `añosDeExperiencia`) VALUES (DEFAULT, 'George', 'Lucas', '1934-08-08', 15);

COMMIT;


-- -----------------------------------------------------
-- Data for table `TPPYTHON`.`Categorias`
-- -----------------------------------------------------
START TRANSACTION;
USE `TPPYTHON`;
INSERT INTO `TPPYTHON`.`Categorias` (`idCategoria`, `nombre`) VALUES (1, 'Drama');
INSERT INTO `TPPYTHON`.`Categorias` (`idCategoria`, `nombre`) VALUES (DEFAULT, 'Sci-fi');
INSERT INTO `TPPYTHON`.`Categorias` (`idCategoria`, `nombre`) VALUES (DEFAULT, 'Pysicological Terror');
INSERT INTO `TPPYTHON`.`Categorias` (`idCategoria`, `nombre`) VALUES (DEFAULT, 'Crime');

COMMIT;


-- -----------------------------------------------------
-- Data for table `TPPYTHON`.`Peliculas`
-- -----------------------------------------------------
START TRANSACTION;
USE `TPPYTHON`;
INSERT INTO `TPPYTHON`.`Peliculas` (`idPelicula`, `titulo`, `duracion`, `fechaLanzamiento`, `presupuesto`, `ganancia`, `sinopsis`, `idAutor`, `idProductor`, `idCategoria`) VALUES (DEFAULT, 'Kilimanjaro', 107, '2011-11-16', 4922786, 4200000, 'A man decides to climb Mt. Kilimanjaro after his relationship ends.', 1, 1, 1);
INSERT INTO `TPPYTHON`.`Peliculas` (`idPelicula`, `titulo`, `duracion`, `fechaLanzamiento`, `presupuesto`, `ganancia`, `sinopsis`, `idAutor`, `idProductor`, `idCategoria`) VALUES (DEFAULT, 'Annihilation', 115, '2018-03-13', 40000000, 42900000, 'A biologist signs up for a dangerous, secret expedition into a mysterious zone where the laws of nature don\'t apply. ', 2, 2, 2);
INSERT INTO `TPPYTHON`.`Peliculas` (`idPelicula`, `titulo`, `duracion`, `fechaLanzamiento`, `presupuesto`, `ganancia`, `sinopsis`, `idAutor`, `idProductor`, `idCategoria`) VALUES (DEFAULT, 'The Godfather', 177, '1972-03-15', 7000000, 250000000, 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son. ', 3, 3, 3);
INSERT INTO `TPPYTHON`.`Peliculas` (`idPelicula`, `titulo`, `duracion`, `fechaLanzamiento`, `presupuesto`, `ganancia`, `sinopsis`, `idAutor`, `idProductor`, `idCategoria`) VALUES (DEFAULT, 'Psycho', 109, '1960-06-16', 806000, 50000000, 'A Phoenix secretary embezzles $40,000 from her employer\'s client, goes on the run, and checks into a remote motel run by a young man under the domination of his mother. ', 4, 4, 4);
INSERT INTO `TPPYTHON`.`Peliculas` (`idPelicula`, `titulo`, `duracion`, `fechaLanzamiento`, `presupuesto`, `ganancia`, `sinopsis`, `idAutor`, `idProductor`, `idCategoria`) VALUES (DEFAULT, 'A New Hope', 121, '1977-05-25', 11000000, 775000000, 'Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empire\'s world-destroying battle-station, while also attempting to rescue Princess Leia from the evil Darth Vader. ', 5, 5, 2);

COMMIT;


-- -----------------------------------------------------
-- Data for table `TPPYTHON`.`Actores`
-- -----------------------------------------------------
START TRANSACTION;
USE `TPPYTHON`;
INSERT INTO `TPPYTHON`.`Actores` (`idActor`, `nombre`, `apellido`, `fechaNac`, `cantidadDePeliculas`) VALUES (DEFAULT, 'Jean', 'Dupoc', '1977-05-07', 1);
INSERT INTO `TPPYTHON`.`Actores` (`idActor`, `nombre`, `apellido`, `fechaNac`, `cantidadDePeliculas`) VALUES (DEFAULT, 'Joseph', 'Stalin', '1898-06-13', 1939);
INSERT INTO `TPPYTHON`.`Actores` (`idActor`, `nombre`, `apellido`, `fechaNac`, `cantidadDePeliculas`) VALUES (DEFAULT, 'Alfredito', 'Fuentes', '1950-07-12', 3);
INSERT INTO `TPPYTHON`.`Actores` (`idActor`, `nombre`, `apellido`, `fechaNac`, `cantidadDePeliculas`) VALUES (DEFAULT, 'Natalie', 'Portman', '1987-04-03', 20);
INSERT INTO `TPPYTHON`.`Actores` (`idActor`, `nombre`, `apellido`, `fechaNac`, `cantidadDePeliculas`) VALUES (DEFAULT, 'Blackie', 'Darks', '1990-09-08', 12);
INSERT INTO `TPPYTHON`.`Actores` (`idActor`, `nombre`, `apellido`, `fechaNac`, `cantidadDePeliculas`) VALUES (DEFAULT, 'Homunculo', 'Homunculin', '2018-08-08', 1);
INSERT INTO `TPPYTHON`.`Actores` (`idActor`, `nombre`, `apellido`, `fechaNac`, `cantidadDePeliculas`) VALUES (DEFAULT, 'Marlon', 'Brando', '1920-12-12', 3);
INSERT INTO `TPPYTHON`.`Actores` (`idActor`, `nombre`, `apellido`, `fechaNac`, `cantidadDePeliculas`) VALUES (DEFAULT, 'Al', 'Pacino', '1937-03-03', 29);
INSERT INTO `TPPYTHON`.`Actores` (`idActor`, `nombre`, `apellido`, `fechaNac`, `cantidadDePeliculas`) VALUES (DEFAULT, 'James', 'Caan', '1940-09-08', 3);
INSERT INTO `TPPYTHON`.`Actores` (`idActor`, `nombre`, `apellido`, `fechaNac`, `cantidadDePeliculas`) VALUES (DEFAULT, 'Anthony', 'Perkins', '1910-10-12', 13);
INSERT INTO `TPPYTHON`.`Actores` (`idActor`, `nombre`, `apellido`, `fechaNac`, `cantidadDePeliculas`) VALUES (DEFAULT, 'Vera', 'Miles', '1912-05-01', 1);
INSERT INTO `TPPYTHON`.`Actores` (`idActor`, `nombre`, `apellido`, `fechaNac`, `cantidadDePeliculas`) VALUES (DEFAULT, 'Janet', 'Leigh', '1909-04-06', 3);
INSERT INTO `TPPYTHON`.`Actores` (`idActor`, `nombre`, `apellido`, `fechaNac`, `cantidadDePeliculas`) VALUES (DEFAULT, 'Mark', 'Hamill', '1956-05-04', 7);
INSERT INTO `TPPYTHON`.`Actores` (`idActor`, `nombre`, `apellido`, `fechaNac`, `cantidadDePeliculas`) VALUES (DEFAULT, 'Harrison', 'Ford', '1942-04-03', 24);
INSERT INTO `TPPYTHON`.`Actores` (`idActor`, `nombre`, `apellido`, `fechaNac`, `cantidadDePeliculas`) VALUES (DEFAULT, 'Carrie', 'Fisher', '1956-07-01', 5);

COMMIT;


-- -----------------------------------------------------
-- Data for table `TPPYTHON`.`Reviews`
-- -----------------------------------------------------
START TRANSACTION;
USE `TPPYTHON`;
INSERT INTO `TPPYTHON`.`Reviews` (`idReview`, `critico`, `descripcion`, `puntaje`, `idPelicula`) VALUES (DEFAULT, 'Josefino Portaño', 'Es una mala pelicula', 3, 1);
INSERT INTO `TPPYTHON`.`Reviews` (`idReview`, `critico`, `descripcion`, `puntaje`, `idPelicula`) VALUES (DEFAULT, 'Ego', 'Sutil drama que no me gusto', 1, 1);
INSERT INTO `TPPYTHON`.`Reviews` (`idReview`, `critico`, `descripcion`, `puntaje`, `idPelicula`) VALUES (DEFAULT, 'Jhon Bain', 'I like it very much 10/10 IGN', 10, 4);
INSERT INTO `TPPYTHON`.`Reviews` (`idReview`, `critico`, `descripcion`, `puntaje`, `idPelicula`) VALUES (DEFAULT, 'Alfred Hitchcock', 'BEST MOVIE EVER', 10, 3);
INSERT INTO `TPPYTHON`.`Reviews` (`idReview`, `critico`, `descripcion`, `puntaje`, `idPelicula`) VALUES (DEFAULT, 'Pepe Botellas', 'Una peli promedio', 5, 5);
INSERT INTO `TPPYTHON`.`Reviews` (`idReview`, `critico`, `descripcion`, `puntaje`, `idPelicula`) VALUES (DEFAULT, 'Aprile', 'Me gusto para ser de ahora', 7, 2);

COMMIT;


-- -----------------------------------------------------
-- Data for table `TPPYTHON`.`Peliculas_has_Actores`
-- -----------------------------------------------------
START TRANSACTION;
USE `TPPYTHON`;
INSERT INTO `TPPYTHON`.`Peliculas_has_Actores` (`idPelicula`, `idActor`) VALUES (1, 1);
INSERT INTO `TPPYTHON`.`Peliculas_has_Actores` (`idPelicula`, `idActor`) VALUES (1, 2);
INSERT INTO `TPPYTHON`.`Peliculas_has_Actores` (`idPelicula`, `idActor`) VALUES (1, 3);
INSERT INTO `TPPYTHON`.`Peliculas_has_Actores` (`idPelicula`, `idActor`) VALUES (2, 4);
INSERT INTO `TPPYTHON`.`Peliculas_has_Actores` (`idPelicula`, `idActor`) VALUES (2, 5);
INSERT INTO `TPPYTHON`.`Peliculas_has_Actores` (`idPelicula`, `idActor`) VALUES (2, 6);
INSERT INTO `TPPYTHON`.`Peliculas_has_Actores` (`idPelicula`, `idActor`) VALUES (3, 7);
INSERT INTO `TPPYTHON`.`Peliculas_has_Actores` (`idPelicula`, `idActor`) VALUES (3, 8);
INSERT INTO `TPPYTHON`.`Peliculas_has_Actores` (`idPelicula`, `idActor`) VALUES (3, 9);
INSERT INTO `TPPYTHON`.`Peliculas_has_Actores` (`idPelicula`, `idActor`) VALUES (4, 10);
INSERT INTO `TPPYTHON`.`Peliculas_has_Actores` (`idPelicula`, `idActor`) VALUES (4, 11);
INSERT INTO `TPPYTHON`.`Peliculas_has_Actores` (`idPelicula`, `idActor`) VALUES (4, 12);
INSERT INTO `TPPYTHON`.`Peliculas_has_Actores` (`idPelicula`, `idActor`) VALUES (5, 13);
INSERT INTO `TPPYTHON`.`Peliculas_has_Actores` (`idPelicula`, `idActor`) VALUES (5, 14);
INSERT INTO `TPPYTHON`.`Peliculas_has_Actores` (`idPelicula`, `idActor`) VALUES (5, 15);

COMMIT;

SELECT * FROM Actores;

