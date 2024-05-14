-- MySQL Workbench Forward Engineering
 
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
 
-- -----------------------------------------------------
-- Schema goDutch
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `goDutch` DEFAULT CHARACTER SET utf8mb3 ;
USE `goDutch` ;
 
-- -----------------------------------------------------
-- Table `goDutch`.`Adres`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `goDutch`.`Adressen` (
  `adresID` INT NOT NULL AUTO_INCREMENT,
  `postcode` VARCHAR(6) NOT NULL,
  `huisnummer` VARCHAR(6) NOT NULL,
  `straat` VARCHAR(45) NOT NULL,
  `plaats` VARCHAR(45) NOT NULL,
  `catagorie` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`adresID`),
  UNIQUE INDEX `adresID_UNIQUE` (`adresID` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;
 
 
-- -----------------------------------------------------
-- Table `goDutch`.`Klant`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `goDutch`.`Klanten` (
  `klantID` INT NOT NULL AUTO_INCREMENT,
  `voornaam` VARCHAR(45) NOT NULL,
  `tussenvoegsel` VARCHAR(45) NULL DEFAULT NULL,
  `achternaam` VARCHAR(45) NOT NULL,
  `bankrekeningnummer` VARCHAR(45) NOT NULL,
  `k_adresID` INT NOT NULL,
  PRIMARY KEY (`klantID`),
  INDEX `fk_Klant_Adres1_idx` (`k_adresID` ASC) VISIBLE,
  UNIQUE INDEX `klantID_UNIQUE` (`klantID` ASC) VISIBLE,
  CONSTRAINT `fk_Klant_Adres1`
    FOREIGN KEY (`k_adresID`)
    REFERENCES `goDutch`.`Adres` (`adresID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;
 
 
-- -----------------------------------------------------
-- Table `goDutch`.`Bedrijf`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `goDutch`.`Bedrijven` (
  `KVKnummer` INT NOT NULL,
  `BTWnummer` INT NOT NULL,
  `b_adresID` INT NOT NULL,
  `b_klantID` INT NOT NULL,
  PRIMARY KEY (`KVKnummer`),
  INDEX `fk_Bedrijf_Adres1_idx` (`b_adresID` ASC) VISIBLE,
  INDEX `fk_Bedrijf_Klant1_idx` (`b_klantID` ASC) VISIBLE,
  CONSTRAINT `fk_Bedrijf_Adres1`
    FOREIGN KEY (`b_adresID`)
    REFERENCES `goDutch`.`Adres` (`adresID`),
  CONSTRAINT `fk_Bedrijf_Klant1`
    FOREIGN KEY (`b_klantID`)
    REFERENCES `goDutch`.`klant` (`klantID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;
 
 
-- -----------------------------------------------------
-- Table `goDutch`.`Contract`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `goDutch`.`Contracten` (
  `contractNummer` INT NOT NULL AUTO_INCREMENT,
  `datum` VARCHAR(45) NOT NULL,
  `c_klantID` INT NOT NULL,
  PRIMARY KEY (`contractNummer`),
  INDEX `fk_Contracten_Klant1_idx` (`c_klantID` ASC) VISIBLE,
  UNIQUE INDEX `ContractNummer_UNIQUE` (`contractNummer` ASC) VISIBLE,
  CONSTRAINT `fk_Contracten_Klant1`
    FOREIGN KEY (`c_klantID`)
    REFERENCES `goDutch`.`klant` (`klantID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;
 
 
-- -----------------------------------------------------
-- Table `goDutch`.`Vestiging`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `goDutch`.`Vestigingen` (
  `vestegingsID` INT NOT NULL AUTO_INCREMENT,
  `vestegingsnaam` VARCHAR(45) NOT NULL,
  `v_adresID` INT NOT NULL,
  PRIMARY KEY (`vestegingsID`),
  INDEX `fk_Vesteging_Adres1_idx` (`v_adresID` ASC) VISIBLE,
  UNIQUE INDEX `VestegingsID_UNIQUE` (`vestegingsID` ASC) VISIBLE,
  CONSTRAINT `fk_Vesteging_Adres1`
    FOREIGN KEY (`v_adresID`)
    REFERENCES `goDutch`.`Adres` (`adresID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;
 
 
-- -----------------------------------------------------
-- Table `goDutch`.`Fiets`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `goDutch`.`Fietsen` (
  `fietsnummer` INT NOT NULL AUTO_INCREMENT,
  `Merk` VARCHAR(45) NOT NULL,
  `model` VARCHAR(45) NOT NULL,
  `fietstype` VARCHAR(45) NOT NULL,
  `elektrisch` VARCHAR(15) NOT NULL,
  `dagprijs` FLOAT NOT NULL,
  `Aankoopdatum` DATE NOT NULL,
  `f_vestegingsID` INT NOT NULL,
  PRIMARY KEY (`fietsnummer`),
  INDEX `fk_Fiets_Vesteging1_idx` (`f_vestegingsID` ASC) VISIBLE,
  UNIQUE INDEX `fietsnummer_UNIQUE` (`fietsnummer` ASC) VISIBLE,
  CONSTRAINT `fk_Fiets_Vesteging1`
    FOREIGN KEY (`f_vestegingsID`)
    REFERENCES `goDutch`.`Vestiging` (`vestegingsID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;
 
 
-- -----------------------------------------------------
-- Table `goDutch`.`Huur`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `goDutch`.`Huren` (
  `Contracten_ContractNummer` INT NOT NULL,
  `Fiets_Fietsnummer` INT NOT NULL,
  `startdatum` DATE NOT NULL,
  `inleverdatum` DATE NOT NULL,
  PRIMARY KEY (`Contracten_ContractNummer`, `Fiets_Fietsnummer`),
  INDEX `fk_Contracten_has_Fiets_Fiets1_idx` (`Fiets_Fietsnummer` ASC) VISIBLE,
  INDEX `fk_Contracten_has_Fiets_Contracten1_idx` (`Contracten_ContractNummer` ASC) VISIBLE,
  UNIQUE INDEX `iuk_fiets_contract` (`Fiets_Fietsnummer` ASC, `Contracten_ContractNummer` ASC) INVISIBLE,
  INDEX `huurperiode` (`startdatum` ASC, `inleverdatum` ASC) INVISIBLE,
  CONSTRAINT `fk_contractNummer`
    FOREIGN KEY (`Contracten_ContractNummer`)
    REFERENCES `goDutch`.`Contract` (`contractNummer`),
  CONSTRAINT `fk_fietsNummer`
    FOREIGN KEY (`Fiets_Fietsnummer`)
    REFERENCES `goDutch`.`Fiets` (`fietsnummer`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;
 
 
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;