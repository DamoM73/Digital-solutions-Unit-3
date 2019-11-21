import sqlite3

def run_sql_statement(dbfile,sql_statement):
    # connect to database and initalise cursor
    with sqlite3.connect(dbfile) as database:
        cursor = database.cursor()

        #execute sqlstatement
        cursor.execute(sql_statement)

        # return list of results
        return cursor.fetchall()

query = """SELECT subject.tname, AVG(results.percent)
            FROM subject
            JOIN results
            ON subject.subjnumb = results.subjnumb
            GROUP BY subject.tname
            ;
        """
database_file = "school.db"

result = run_sql_statement(database_file,query)

for row in result:
    print(f"The average results for students of {row[0]} is {row[1]}")
