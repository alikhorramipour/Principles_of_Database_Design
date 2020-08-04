SELECT * FROM NikShop.Users User WHERE User.City = 'Tehran';


SELECT * FROM NikShop.Users User WHERE User.Cellphone LIKE '912%';


SELECT Mrch.* FROM NikShop.Merch Mrch JOIN NikShop.Producers Pro ON Pro.ID = Mrch.Producer AND Pro.NationalNumber = '1234567890';


SELECT Mrc.MerchID, Mrch.* FROM NikShop.Merch Mrch, NikShop.BillDetails Mrc WHERE Mrc.MerchID = Mrch.ID GROUP BY Mrc.MerchID HAVING (AVG(Mrc.UserScore) BETWEEN 3 AND 4);


UPDATE NikShop.Merch SET SellingPrice = 1.1 * SellingPrice;
SELECT * NikShop.Merch ORDER BY SellingPrice DESC;


SELECT Mrc.MerchID, Mrch.* FROM NikShop.BillDetails Mrc JOIN NikShop.Merch Mrch ON Mrch.ID = Mrc.MerchID AND ProducerID IN (SELECT ID FROM NikShop.Producers Pro WHERE Pro.FirstName = 'PFN1' ) GROUP BY MerchID HAVING AVG(UserScore) > 3;


SELECT Bill.* FROM NikShop.Bills Bill JOIN NikShop.Users User ON User.ID = Bill.BuyerID AND User.NationalNumber='1122334455';


SELECT Pro.* FROM NikShop.Producers Pro JOIN NikShop.Merch Mrch ON Mrch.ProducerID = Pro.ID AND MRCH.ID IN (SELECT Mrc.MerchID FROM NikShop.BillDetails Mrc JOIN NikShop.Bills Bill ON Mrc.BillID = Bill.ID AND Bill.BuyerID IN (SELECT User.ID FROM NikShop.Users User WHERE User.NationalNumber='1122334455'));


SELECT DISTINCT Mrch.* FROM NikShop.Merch Mrch JOIN NikShop.BillDetails Mrc ON Mrc.MerchID = Mrch.ID AND Mrc.BillID IN (SELECT Bill.ID FROM NikShop.Bills Bill WHERE RecordDate > '2020-1-1');


SELECT * FROM NikShop.Merch WHERE SellingPrice > BoughtAtPrice + 2000;


SELECT DISTINCT User.FirstName FROM NikShop.Users User JOIN NikShop.Bills Bill ON Bill.BuyerID = User.ID AND Bill.ID IN (SELECT Mrc.BillID FROM NikShop.BillDetails Mrc JOIN NikShop.Merch Mrch ON Mrch.ID = Mrc.MerchID AND Mrch.Name = 'M4');


SELECT MerchID, Mrch.* FROM NikShop.BillDetails Mrc JOIN NikShop.Merch Mrch ON Mrch.ID = Mrc.MerchID GROUP BY Mrc.MerchID HAVING AVG(Mrc.UserScore) > (SELECT AVG(Mrc2.UserScore) FROM NikShop.BillDetails Mrc2);


SELECT MerchID, Mrch.* FROM NikShop.BillDetails Mrc JOIN NikShop.Merch Mrch ON Mrch.ID = Mrc.MerchID GROUP BY Mrc.MerchID ORDER BY AVG(Mrc.UserScore) DESC LIMIT 1;


SELECT MerchID, Mrch.* ,SUM(Quantity) * Mrch.SellingPrice FROM NikShop.BillDetails Mrc JOIN NikShop.Merch Mrch ON Mrch.ID = Mrc.MerchID GROUP BY Mrc.MerchID ORDER BY SUM(Quantity) * Mrch.SellingPrice;


SELECT DISTINCT User.* FROM NikShop.Users User WHERE User.ID IN (SELECT Bill.BuyerID FROM NikShop.BillDetails Mrc JOIN NikShop.Bills Bill ON Mrc.BillID = Bill.ID GROUP BY Mrc.MerchID, Bill.BuyerID HAVING COUNT(*) > 1);


SELECT DISTINCT Mrch.* FROM NikShop.Merch Mrch WHERE Mrch.ID IN (SELECT Mrc.MerchID FROM NikShop.BillDetails Mrc JOIN NikShop.Bills Bill ON Mrc.BillID = Bill.ID GROUP BY Mrc.MerchID, Bill.BuyerID HAVING COUNT(*) > 1);


SELECT Pro.FirstName, Pro.LastName, COUNT(*) FROM NikShop.Producers Pro JOIN NikShop.Merch Mrch ON Mrch.ProducerID = Pro.ID JOIN NikShop.BillDetails Mrc ON Mrc.MerchID = Mrch.ID JOIN NikShop.Bills Bill ON Mrc.BillID = Bill.ID AND Bill.RecordDate > '2020-01-01' GROUP BY Pro.ID ORDER BY COUNT(*) DESC;


SELECT Bill.*, SUM(Mrc.Quantity * Mrch.SellingPrice) FROM NikShop.Bills Bill JOIN NikShop.BillDetails Mrc ON Mrc.BillID = Bill.ID JOIN NikShop.Merch Mrch ON Mrch.ID = Mrc.MerchID GROUP BY Bill.ID ORDER BY SUM(Mrc.Quantity * Mrch.SellingPrice) DESC;


SELECT Bill.*, SUM(Mrc.Quantity * (Mrch.SellingPrice - Mrch.BoughtAtPrice)) FROM NikShop.Bills Bill JOIN NikShop.BillDetails Mrc ON Mrc.BillID = Bill.ID JOIN NikShop.Merch Mrch ON Mrch.ID = Mrc.MerchID GROUP BY Bill.ID ORDER BY SUM(Mrc.Quantity * (Mrch.SellingPrice - Mrch.BoughtAtPrice)) DESC;





CREATE VIEW NikShop.MerchDetails AS SELECT Mrch.Name AS Merch_Name, Pro.FirstName AS Producer_FirstName, Pro.LastName AS Producer_LastName, COUNT(*) AS Buyers_Count FROM NikShop.BillDetails Mrc JOIN NikShop.Merch Mrch ON Mrch.ID = Mrc.MerchID JOIN NikShop.Producers Pro ON Pro.ID = Mrch.ProducerID GROUP BY Mrc.MerchID;


CREATE VIEW NikShop.ProducersDetails AS SELECT ProducerID, Pro.FirstName AS Producer_name, Pro.NationalNumber FROM NikShop.Merch Mrch JOIN NikShop.Producers Pro ON Pro.ID = Mrch.ProducerID GROUP BY ProducerID HAVING COUNT(*) > 1;