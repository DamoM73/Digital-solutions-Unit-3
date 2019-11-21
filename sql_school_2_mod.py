import sqlite3

def run_sql_statement(dbfile,sql_statement):
    # connect to database and initalise cursor
    with sqlite3.connect(dbfile) as database:
        cursor = database.cursor()

        #execute sqlstatement
        cursor.execute(sql_statement)

        # return list of results
        return cursor.fetchall()

query = """SELECT subjname
            FROM subject
            WHERE tname IN (
                SELECT tname
                FROM teacher
                WHERE room = 'A2'
            );
        """
database_file = "school.db"

result = run_sql_statement(database_file,query)

for row in result:
    print(f"The subject taught in A2 is {row[0]}.")