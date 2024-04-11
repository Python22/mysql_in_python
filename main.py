import pymysql


def create_database():
    try:
        db_name = input("insert a name: ")
        query = f"""CREATE DATABASE IF NOT EXISTS {db_name}"""
        cursor.execute(query)
        connection.commit()
        print("Done.")
        if input("Would you change current database to this new database(yes or no): ").lower() in ("yes", "y"):
            query = f"""USE {db_name}"""
            cursor.execute(query)
            print(f"Now you are using {db_name} database.")
    except:
        print("Something wrong. Operation is not completed.")


def change_database():
    try:
        query = f"""USE {input("insert a name: ")}"""
        cursor.execute(query)
        print("Done.")
    except:
        print("Something wrong. Operation is not completed.")


def create_table():
    try:
        table_name = input("Name of table: ")
        first_column_name = input("first column name: ")
        second_column_name = input("second column name: ")
        query = f"""CREATE TABLE IF NOT EXISTS {table_name} ({first_column_name} INT PRIMARY KEY, {second_column_name} VARCHAR(255))"""
        cursor.execute(query)
        connection.commit()
    except:
        print("Something wrong. Operation is not completed.")


def insert_info_to_table():
    show_all_tables()
    table = input("Name of table: ")
    try:
        query = f"""SHOW COLUMNS FROM {table}"""
        cursor.execute(query)
        print("All columns:")
        for column in cursor:
            print(*column)
        match table:
            case "teachers":
                query = """INSERT INTO teachers (first_name, second_name, age) VALUES (%s, %s, %s)"""
                values = (
                    input("Insert a firstname: "),
                    input("Insert a second name: "),
                    int(input("Insert an age: "))
                )
                cursor.execute(query, values)
                connection.commit()
            case "groups":
                query = """INSERT INTO groups (name, auditory) VALUES (%s, %s)"""
                values = (
                    input("Insert a name: "),
                    input("Insert an auditory: ")
                )
                cursor.execute(query, values)
                connection.commit()
            case "teachers_and_groups":
                query = f"""SELECT * FROM TEACHERS"""
                cursor.execute(query)
                for teacher in cursor:
                    print(f"id: {teacher[0]}; firstname: {teacher[1]}; lastname: {teacher[2]}")
                teacher_id = int(input("Insert teacher id: "))

                query = f"""SELECT * FROM GROUPS"""
                cursor.execute(query)
                for group in cursor:
                    print(f"id: {group[0]}; name: {group[1]}; auditory: {group[2]}")
                group_id = int(input("Insert group id: "))

                query = """INSERT INTO teachers (teacher_id, groups_id) VALUES (%s, %s)"""
                values = (teacher_id, group_id)
                cursor.execute(query, values)
                connection.commit()
    except:
        print("Something wrong. Operation is not completed.")


def delete_info_from_table():
    show_all_tables()
    table = input("Table name: ")

    query = f"""SELECT * FROM {table}"""
    cursor.execute(query)
    print("All columns:")
    for column in cursor:
        print(*column)


    value = int(input("enter id where need to delete: "))

    query = f"""DELETE FROM {table} WHERE id = %s"""

    cursor.execute(query, value)
    connection.commit()


def update_info_in_table():
    teacher_id = int(input("teacher_id: "))
    query = f"""UPDATE teachers SET first_name = %s, second_name = %s, age = %s WHERE id = {teacher_id}"""
    values = (
        input("firstname: "),
        input("second name: "),
        int(input("age: "))
    )
    cursor.execute(query, values)
    connection.commit()



def show_some_info():
    print("\n\n")
    print("-" * 100)
    print("1. Show all databases.")
    print("2. Show all tables in current database.")
    print("3. Show all columns in some table.")
    print("4. Show all data in some table.")
    print("5. Show others info.")
    print("0. Back.")
    try:
        user_choice = input("Your choice: ")
        match user_choice:
            case "1": show_all_databases()
            case "2": show_all_tables()
            case "3": show_table_columns()
            case "4": show_all_data_in_table()
            case "5": pass
            case "0": return
            case _: show_all_databases()
    except:
        print("Something wrong. Operation is not completed.")


def show_all_databases():
    try:
        cursor.execute("SHOW DATABASES")
        print("All databases:")
        for db in cursor:
            print(*db)
    except:
        print("Something wrong. Operation is not completed.")


def show_all_tables():
    try:
        print("All tables in this database:")
        cursor.execute("SHOW TABLES")
        for db in cursor:
            print(*db)
    except:
        print("Something wrong. Operation is not completed.")


def show_table_columns():
    try:
        table_name = input("Table name: ")
        query = f"""SHOW COLUMNS FROM {table_name}"""
        cursor.execute(query)
        for db in cursor:
            print(*db)
    except:
        print("Something wrong. Operation is not completed.")


def show_all_data_in_table():
    try:
        table_name = input("Table name: ")
        query = f"""SELECT * FROM {table_name}"""
        cursor.execute(query)
        for db in cursor:
            print(*db)
    except:
        print("Something wrong. Operation is not completed.")


try:
    with pymysql.connect(host="localhost", port=3307, user="root", password="") as connection:
        print(connection, "OK")
        with connection.cursor() as cursor:

            cursor.execute("USE ACADEMY")

            while True:
                print("\n\n")
                print("-" * 100)
                print("1. Create database.")
                print("2. Change database.")
                print("3. Create table in database.")
                print("4. Insert info in to a table.")
                print("5. Delete info from a table.")
                print("6. Update info in a table.")
                print("7. Show some info.")
                print("0. Quit.")
                user_choice = input("Your choice: ")
                match user_choice:
                    case "1": create_database()
                    case "2": change_database()
                    case "3": create_table()
                    case "4": insert_info_to_table()
                    case "5": delete_info_from_table()
                    case "6": update_info_in_table()
                    case "7": show_some_info()
                    case "0": quit()
                    case _: print("Unknown command. Try again.")


except pymysql.Error as e:
    print(e)











# cursor.execute("SHOW DATABASES")
            # for db in cursor:
            #     print(db)
            #
            # cursor.execute("CREATE DATABASE IF NOT EXISTS TESTIK")
            #
            # print("-------------")
            # cursor.execute("SHOW DATABASES")
            # for db in cursor:
            #     print(db)
            #
            #
            #
            # cursor.execute("CREATE DATABASE IF NOT EXISTS ACADEMY")
            # cursor.execute("USE ACADEMY")
            #
            #
            # cursor.execute("SHOW DATABASES")
            # for db in cursor:
            #     print(db)
            #
            # cursor.execute(
            # """
            # CREATE TABLE IF NOT EXISTS teachers (
            #     id INT AUTO_INCREMENT PRIMARY KEY,
            #     first_name VARCHAR(100),
            #     second_name VARCHAR(100),
            #     age INT
            # )
            # """
            # )
            # cursor.execute(
            #     """
            #     CREATE TABLE IF NOT EXISTS groups (
            #         id INT AUTO_INCREMENT PRIMARY KEY,
            #         name VARCHAR(100),
            #         auditory VARCHAR(10)
            #     )
            #     """
            # )
            # cursor.execute(
            #     """
            #     CREATE TABLE IF NOT EXISTS teachers_and_groups (
            #         teacher_id INT,
            #         group_id INT,
            #         PRIMARY KEY(teacher_id, group_id),
            #         FOREIGN KEY (teacher_id) REFERENCES teachers(id),
            #         FOREIGN KEY (group_id) REFERENCES groups(id)
            #     )
            #     """
            # )

            # cursor.execute("USE ACADEMY")
            # cursor.execute(
            #     """INSERT INTO teachers (first_name, second_name, age)  VALUES ('vasya', 'vasin', 50)"""
            # )
            # connection.commit()

            # cursor.execute("SELECT * FROM teachers")
            # for line in cursor:
            #     print(line)




