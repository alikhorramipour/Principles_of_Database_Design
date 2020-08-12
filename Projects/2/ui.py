import pymysql

database_tables = ['Artist', 'Exhibition', 'Bidder', 'ArtPiece', 'Auction', 'Invoice']

Artist_attributes = ['ID', 'First Name', 'Last Name', 'Social Code', 'Phone Number', 'Age']
Exhibition_attributes = ['ID', 'Name', 'Start Date', 'End Date']
Bidder_attributes = ['ID', 'Bidder First Name', 'Bidder Last Name', 'Phone Number']
ArtPiece_attributes = ['ID', 'Art Piece Name', 'Description', 'Category', 'OwnerID', 'ExhibitID', 'Price']
Auction_attributes = ['ID', 'Start Date', 'ExhibitionID']
Invoice_attributes = ['ID', 'BidderID', 'ArtistID', 'AuctionID', 'Placed Price']

user_input_attributes = []


def database():
    global conn, cursor
    conn = pymysql.connect(host='localhost', user='user', password='password', db='picto')
    cursor = conn.cursor()


def create(db_table):
    if db_table == 'Artist':
        for attr in Artist_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute(
            "INSERT INTO Artist VALUES (ID = %d, 'First Name' = %s, 'Last Name' = %s, 'Social Code' = %s,  'Phone Number' = %s,  'Age' = %d)",
            (int(user_input_attributes[0]), str(user_input_attributes[1]), str(user_input_attributes[2]),
             str(user_input_attributes[3]),
             str(user_input_attributes[4]), int(user_input_attributes[5])))

    elif db_table == 'Exhibition':
        for attr in Exhibition_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute("INSERT INTO Exhibition VALUES (ID = %d, 'Name' = %s, 'Start Date' = %s, 'End Date' = %s)",
                       (int(user_input_attributes[0]), str(user_input_attributes[1]), str(user_input_attributes[2]),
                        str(user_input_attributes[3])))

    elif db_table == 'Bidder':
        for attr in Bidder_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute(
            "INSERT INTO Bidder VALUES (ID = %d, 'Bidder First Name' = %s, 'Bidder Last Name' = %s, 'Phone Number' = %s)",
            (int(user_input_attributes[0]), str(user_input_attributes[1]), str(user_input_attributes[2]),
             str(user_input_attributes[3])))

    elif db_table == 'ArtPiece':
        for attr in ArtPiece_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute(
            "INSERT INTO ArtPiece VALUES (ID = %d, 'Art Piece Name' = %s, 'Description' = %s, 'Category' = %s,  'OwnerID' = %d, 'ExhibitID' = %d, 'Price' = %d)",
            (int(user_input_attributes[0]), str(user_input_attributes[1]), str(user_input_attributes[2]),
             str(user_input_attributes[3]),
             int(user_input_attributes[4]), int(user_input_attributes[5]), int(user_input_attributes[6])))

    elif db_table == 'Auction':
        for attr in Auction_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute("INSERT INTO Auction VALUES (ID = %d, 'Start Date' = %s, 'ExhibitionID' = %d)",
                       (int(user_input_attributes[0]), str(user_input_attributes[1]), int(user_input_attributes[2])))

    elif db_table == 'Invoice':
        for attr in Invoice_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute(
            "INSERT INTO Invoice VALUES (ID = %d, 'BidderID' = %d, 'ArtistID' = %d, 'AuctionID' = %d,  'Placed Price' = %d)",
            (int(user_input_attributes[0]), int(user_input_attributes[1]), int(user_input_attributes[2]),
             int(user_input_attributes[3]),
             int(user_input_attributes[4])))

    user_input_attributes.clear()
    conn.commit()
    cursor.close()
    conn.close()


def read(db_table):
    database()
    cursor.execute("SELECT * FROM 'db_table' = %s", db_table)
    conn.commit()
    cursor.close()
    conn.close()


def update(db_table, id):
    database()

    if db_table == 'Artist':
        for attr in Artist_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute(
            "UPDATE Artist SET 'First Name' = %s, 'Last Name' = %s, 'Social Code' = %s,  'Phone Number' = %s,  'Age' = %d WHERE ID = %d",
            (str(user_input_attributes[0]), str(user_input_attributes[1]), str(user_input_attributes[2]),
             str(user_input_attributes[3]), int(user_input_attributes[4], id)))

    elif db_table == 'Exhibition':
        for attr in Exhibition_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute("UPDATE Exhibit SET 'Name' = %s, 'Start Date' = %s, 'End Date' = %s WHERE ID = %d",
                       (
                       str(user_input_attributes[0]), str(user_input_attributes[1]), str(user_input_attributes[2], ID)))

    elif db_table == 'Bidder':
        for attr in Bidder_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute(
            "UPDATE Bidder SET 'Bidder First Name' = %s, 'Bidder Last Name' = %s, 'Phone Number' = %s WHERE ID = %d",
            (str(user_input_attributes[0]), str(user_input_attributes[1]), str(user_input_attributes[2], ID)))

    elif db_table == 'ArtPiece':
        for attr in ArtPiece_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute(
            "UPDATE ArtPiec SET 'Art Piece Name' = %s, 'Description' = %s, 'Category' = %s,  'OwnerID' = %d, 'ExhibitID' = %d, 'Price' = %d WHERE ID = %d",
            (str(user_input_attributes[0]), str(user_input_attributes[1]), str(user_input_attributes[2]),
             int(user_input_attributes[3]), int(user_input_attributes[4]), int(user_input_attributes[5], ID)))

    elif db_table == 'Auction':
        for attr in Auction_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute("UPDATE Auction SET 'Start Date' = %s, 'ExhibitionID' = %d WHERE ID = %d",
                       (str(user_input_attributes[0]), int(user_input_attributes[1], ID)))

    elif db_table == 'Invoice':
        for attr in Invoice_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute(
            "UPDATE Invoice SET 'BidderID' = %d, 'ArtistID' = %d, 'AuctionID' = %d,  'Placed Price' = %d WHERE ID = %d",
            (int(user_input_attributes[0]), int(user_input_attributes[1]), int(user_input_attributes[2]),
             int(user_input_attributes[3], ID)))

    user_input_attributes.clear()

    conn.commit()
    cursor.close()
    conn.close()


def delete(db_table, ID):
    database()
    cursor.execute("DELETE FROM db_table WHERE ID = %d", ID)
    conn.commit()
    cursor.close()
    conn.close()


def get_input_table():
    user_input_table = input('Select a table [Artist, Exhibition, Bidder, ArtPiece, Auction, Invoice]: ')

    if database_tables.count(user_input_table) == 0:
        print('Wrong input!')
        get_input_table()
    else:
        return user_input_table


if __name__ == '__main__':
    user_input_option = int()

    while 1:
        user_input_option = int(input('Choose an option [Read(1), Create(2), Update(3), Delete(4), Exit(5)]: '))
        if user_input_option == 1:
            read(get_input_table())

        elif user_input_option == 2:
            create(get_input_table())

        elif user_input_option == 3:
            update(get_input_table(), input('Enter the ID: '))

        elif user_input_option == 4:
            delete(get_input_table(), input('Enter the ID: '))

        elif user_input_option == 5:
            break

        else:
            print('Wrong input!')
