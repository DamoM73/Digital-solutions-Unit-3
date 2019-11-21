import sqlite3

def run_sql_statement(dbfile,sql_statement):
    # connect to database and initalise cursor
    with sqlite3.connect(dbfile) as database:
        cursor = database.cursor()

        #execute sqlstatement
        cursor.execute(sql_statement)

        # return list of results
        return cursor.fetchall()

query = """SELECT student.stname
            FROM student
            JOIN results
            ON student.stnumb = results.stnumb
            JOIN subject
            ON results.subjnumb = subject.subjnumb
            WHERE subject.tname LIKE "Simms%"
            ;
        """
database_file = "school.db"

result = run_sql_statement(database_file,query)

for row in result:
    print(f"{row[0]} is taught by Simms")
