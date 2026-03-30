import sqlite3

succesfully_created = False

def create_table(conn):
    print("Creating LTO tapes table")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS fitas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            diretorio TEXT NOT NULL,
            tipo_fita TEXT NOT NULL,
            numero_fita INTEGER NOT NULL
            )''')
    conn.commit()
    return True 

def filling_data(conn):
        with open('files_data/teste 2.txt', 'r') as file:
                for line in file:
                        print(line)
                        tipo_fita, numero_fita, diretorio = line.strip().split(';')
                        print(f"Dir: {diretorio}, Tipo: {tipo_fita}, Numero: {numero_fita}")
                        c = conn.cursor()
                        c.execute("INSERT INTO fitas (diretorio, tipo_fita, numero_fita) VALUES (?, ?, ?)",
                                  (diretorio, tipo_fita, int(numero_fita)))

def main_local_db():
        print("Creating local database")
        print(30 * "=")

        print("creating local.db")
        conn = sqlite3.connect('database/local.db')
        
        if not create_table(conn):
                print("Failed to create table... Exiting")
                conn.close()
                return 0
        
        print("Table created successfully")
        print("Filling data into table...")
        
        if not filling_data(conn):
                print("Failed to fill data into table... Exiting")
                conn.close()
                return 0
        
        print("Data filled successfully")
        
        conn.close()
        return succesfully_created == True      




if __name__ == "__main__":
    main_local_db()