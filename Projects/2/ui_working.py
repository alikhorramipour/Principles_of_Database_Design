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
    global conn
    global cursor
    conn = pymysql.connect(host='localhost', user='root', password='12345678', db='picto')
    cursor = conn.cursor()

#only Artist works!
def create(db_table):
    database()
    if db_table == 'Artist':
        for attr in Artist_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        print(user_input_attributes)
        cursor.execute(
            "INSERT INTO Artist (FirstName, LastName, SocialCode, PhoneNumber, Age) VALUES (%s, %s, %s, %s, %s);"
            , (user_input_attributes[1], user_input_attributes[2],
               user_input_attributes[3],
               user_input_attributes[4], int(user_input_attributes[5])))

    elif db_table == 'Exhibition':
        for attr in Exhibition_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute(
            """INSERT INTO 'Exhibition' VALUES ({0}, {1}, {2}, {3});""".format
            (int(user_input_attributes[0]), str(user_input_attributes[1]), str(user_input_attributes[2]),
             str(user_input_attributes[3])))


    elif db_table == 'Bidder':
        for attr in Bidder_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute(
            """INSERT INTO Bidder VALUES ({0}, {1}, {2});""".format
            (int(user_input_attributes[0]), str(user_input_attributes[1]), str(user_input_attributes[2]),
             int(user_input_attributes[3])))

    elif db_table == 'ArtPiece':
        for attr in ArtPiece_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute(
            """INSERT INTO Bidder VALUES ({0}, {1}, {2});""".format(int(user_input_attributes[0]),
                                                                    str(user_input_attributes[1]),
                                                                    str(user_input_attributes[2]),
                                                                    str(user_input_attributes[3]),
                                                                    int(user_input_attributes[4]),
                                                                    int(user_input_attributes[5]),
                                                                    int(user_input_attributes[6])))

    elif db_table == 'Auction':
        for attr in Auction_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute(
            """INSERT INTO Auction VALUES ({0}, {1}, {2});""".format
            (int(user_input_attributes[0]), str(user_input_attributes[1]),
             int(user_input_attributes[2])))

    elif db_table == 'Invoice':
        for attr in Invoice_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute(
            """INSERT INTO Invoice VALUES ({0}, {1}, {2}, {3}, {4});""".format
            (int(user_input_attributes[0]), int(user_input_attributes[1]), int(user_input_attributes[2]),
             int(user_input_attributes[3]),
             int(user_input_attributes[4])))

    user_input_attributes.clear()
    conn.commit()
    cursor.close()
    conn.close()


def read(db_table):
    database()
    sql = """SELECT * FROM `{0}`;""".format(db_table)
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    conn.commit()
    cursor.close()
    conn.close()


#only Artist works!
def update(db_table, id):
    database()

    if db_table == 'Artist':
        for attr in Artist_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute(
            "UPDATE Artist SET FirstName = %s, LastName = %s, SocialCode = %s, PhoneNumber = %s, Age = %s WHERE ID = %s;",
            (user_input_attributes[0], user_input_attributes[1], user_input_attributes[2],
             user_input_attributes[3], user_input_attributes[4], int(id)))

    elif db_table == 'Exhibition':
        for attr in Exhibition_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute("""UPDATE Exhibition SET {0}, {1}, {2} WHERE id = {3};""".format
                       (str(user_input_attributes[0]), str(user_input_attributes[1]),
                        str(user_input_attributes[2], id)))

    elif db_table == 'Bidder':
        for attr in Bidder_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute(
            """UPDATE Bidder SET {0}, {1}, {2} WHERE ID = {3};""".format
            (str(user_input_attributes[0]), str(user_input_attributes[1]), str(user_input_attributes[2], id)))

    elif db_table == 'ArtPiece':
        for attr in ArtPiece_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute(
            """UPDATE Artpiece SET {0}, {1}, {2}, {3}, {4}, {5} WHERE ID = {6};""".format(
                (str(user_input_attributes[0]), str(user_input_attributes[1]), str(user_input_attributes[2]),
                 int(user_input_attributes[3]), int(user_input_attributes[4]), int(user_input_attributes[5], id))))

    elif db_table == 'Auction':
        for attr in Auction_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute("""UPDATE Auction SET {0}, {1}, {2} WHERE ID = {2};""".format(
            str(user_input_attributes[0]), int(user_input_attributes[1], id)))

    elif db_table == 'Invoice':
        for attr in Invoice_attributes:
            user_input_attributes.append(input('Enter ' + attr + ': '))
        cursor.execute(
            """UPDATE Auction SET {0}, {1}, {2} WHERE ID = {2};""".format(
                (int(user_input_attributes[0]), int(user_input_attributes[1]), int(user_input_attributes[2]),
                 int(user_input_attributes[3], id))))

    user_input_attributes.clear()

    conn.commit()
    cursor.close()
    conn.close()


def delete(db_table, id):
    database()

    if db_table == 'Artist':
        cursor.execute("DELETE FROM Artist WHERE ID = %s;", int(id))

    elif db_table == 'Exhibition':
        cursor.execute("DELETE FROM Exhibition WHERE ID = %s;", int(id))

    elif db_table == 'Bidder':
        cursor.execute("DELETE FROM Bidder WHERE ID = %s;", int(id))

    elif db_table == 'ArtPiece':
        cursor.execute("DELETE FROM ArtPiece WHERE ID = %s;", int(id))

    elif db_table == 'Auction':
        cursor.execute("DELETE FROM Auction WHERE ID = %s;", int(id))

    elif db_table == 'Invoice':
        cursor.execute("DELETE FROM Invoice WHERE ID = %s;", int(id))

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
