import sqlite3

def run_sql_statement(dbfile,sql_statement):
    # connect to database and initalise cursor
    with sqlite3.connect(dbfile) as database:
        cursor = database.cursor()

        #execute sqlstatement
        cursor.execute(sql_statement)

        # return list of results
        return cursor.fetchall()

query = """SELECT stname
            FROM student
            WHERE stnumb IN (
                SELECT stnumb
                FROM results
                WHERE subjnumb IN (
                    SELECT subjnumb
                    FROM subject
                    WHERE subjname = 'science'
                )
            );
        """
database_file = "school.db"

result = run_sql_statement(database_file,query)

for row in result:
    print(f"{row[0]} studies science.")
