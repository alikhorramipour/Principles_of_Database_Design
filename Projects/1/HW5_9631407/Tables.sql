CREATE DATABASE 'NikShop';
USE 'NikShop';

CREATE TABLE 'Users'(
	'ID' int NOT NULL UNIQUE,
	'FirstName' varchar(50) NOT NULL,
	'LastName' varchar(50) NOT NULL,
	'NationalNumber' varchar(10) NOT NULL UNIQUE,
	'Cellphone' varchar(10) NOT NULL UNIQUE,
	'City' varchar(50) NOT NULL,
	'HomeAddress' varchar(50) NOT NULL UNIQUE,

	PRIMARY KEY ('ID')
);

CREATE TABLE 'Merch'(
	'ID' int NOT NULL UNIQUE,
	'Name' varchar(50) NOT NULL UNIQUE,
	'Remaining' int NOT NULL,
	'SellingPrice' float NOT NULL,
	'BoughtAtPrice' float NOT NULL,
	'ProducerID' int NOT NULL,

	PRIMARY KEY ('ID'),

	FOREIGN KEY ('ID') REFERENCES 'Producers' ('ID')
);

CREATE TABLE 'Bills'(
	'ID' int NOT NULL UNIQUE,
	'BuyerID' int NOT NULL,
	'RecordDate' DATE NOT NULL,

	PRIMARY KEY ('ID'),

	FOREIGN KEY ('BuyerID') REFERENCES 'Users' ('ID')
);

CREATE TABLE 'BillDetails'(
	'ID' int NOT NULL UNIQUE,
	'MerchID' int NOT NULL,
	'Quantity' int NOT NULL,
	'BillID' int NOT NULL,
	'UserScore' int NOT NULL DEFAULT 1,

	PRIMARY KEY ('ID'),

	FOREIGN KEY ('MerchID') REFERENCES 'Merch' ('ID'),
	FOREIGN KEY ('BillID') REFERENCES 'Bills' ('ID')
);

CREATE TABLE 'Producers'(
	'ID' int NOT NULL UNIQUE,
	'NationalNumber' varchar(10) NOT NULL UNIQUE,
	'FirstName' varchar(50) NOT NULL,
	'LastName' varchar(50) NOT NULL,
	'Cellphone' varchar(10) NOT NULL UNIQUE,

	PRIMARY KEY ('ID')
);