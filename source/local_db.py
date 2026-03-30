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
        try:
                with open('files_data/teste 2.txt', 'r') as file:
                        for line in file:
                                #print(line)
                                #print(f"Dir: {diretorio}, Tipo: {tipo_fita}, Numero: {numero_fita}")
                                tipo_fita, numero_fita, diretorio = line.strip().split(';')
                                c = conn.cursor()
                                c.execute("SELECT * FROM fitas WHERE diretorio=? AND tipo_fita=? AND numero_fita=?", (diretorio, tipo_fita, int(numero_fita)))
                                result = c.fetchone()
                                if result[1] == diretorio and result[3] == int(numero_fita):
                                        print(f"Data {diretorio}, {tipo_fita} {numero_fita} already exists in the database. Skipping insertion.")
                                       
                                
                                #c.execute("INSERT INTO fitas (diretorio, tipo_fita, numero_fita) VALUES (?, ?, ?)",
                                #        (diretorio, tipo_fita, int(numero_fita)))
                conn.commit()
                return True
        
        except Exception as e:
                print(f"Error occurred while filling data: {e}")
                return False

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