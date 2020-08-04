CREATE DATABASE Picto;
USE Picto;


CREATE TABLE Artist (
	ID int NOT NULL AUTO_INCREMENT UNIQUE,
	FirstName varchar(50) NOT NULL,
	LastName varchar (50) NOT NULL,
	SocialCode varchar(10) NOT NULL UNIQUE,
	PhoneNumber varchar(10) NOT NULL UNIQUE,
	Age int CHECK (Age > 0),

	PRIMARY KEY (ID)
);



CREATE TABLE Exhibition (
	ID int NOT NULL AUTO_INCREMENT UNIQUE,
	Name varchar(50) NOT NULL,
	StartDate date NOT NULL,
	EndDate date NOT NULL,

	PRIMARY KEY (ID)
);



CREATE TABLE Auction (
	ID int NOT NULL AUTO_INCREMENT UNIQUE,
	StartDate date NOT NULL,
	ExhibitionID int NOT NULL,

	PRIMARY KEY (ID),

	FOREIGN KEY (ExhibitionID) REFERENCES Exhibition (ID)
);


CREATE TABLE Bidder (
	ID int NOT NULL AUTO_INCREMENT UNIQUE,
	FirstName varchar(50) NOT NULL,
	LastName varchar(50) NOT NULL,
	PhoneNumber varchar(10) NOT NULL UNIQUE,

	PRIMARY KEY (ID)
);



CREATE TABLE ArtPiece (
	ID int NOT NULL AUTO_INCREMENT UNIQUE,
	Name varchar(50) NOT NULL,
	Description varchar(250) NOT NULL,
	Category varchar(9) NOT NULL, #(picture, painting, sculpture)
	OwnerID int NOT NULL,
	ExhibitID int NOT NULL,
	Price int CHECK (Price > 999) NOT NULL, #(Price > 999$)

	PRIMARY KEY (ID),

	FOREIGN KEY (OwnerID) REFERENCES Artist (ID),
	FOREIGN KEY (ExhibitID) REFERENCES Exhibition (ID)
);


CREATE TABLE Invoice (
  ID int NOT NULL AUTO_INCREMENT UNIQUE,
  BidderID int NOT NULL,
  ArtistID int NOT NULL,
  AuctionID int NOT NULL,
  Price int CHECK (Price > 999) NOT NULL,

  PRIMARY KEY (ID),

  FOREIGN KEY (BidderID) REFERENCES Bidder (ID),
  FOREIGN KEY (ArtistID) REFERENCES Artist (ID),
  FOREIGN KEY (AuctionID) REFERENCES Auction (ID)
);