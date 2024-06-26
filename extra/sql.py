


def sql_add_data(table_name, data, conn, cursor):
    try:
        for entry in data:
            cursor.execute(f"INSERT INTO {table_name} (Image_Path) VALUES (?)", (entry))
            conn.commit()
        print(f'Successfully added paths to the {table_name} table')
    except:
        print(f"Couldn't add images to {table_name} table")
    conn.close   

