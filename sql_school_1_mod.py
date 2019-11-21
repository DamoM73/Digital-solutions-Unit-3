import sqlite3

def run_sql_statement(dbfile,sql_statement):
    # connect to database and initalise cursor
    with sqlite3.connect(dbfile) as database:
        cursor = database.cursor()

        #execute sqlstatement
        cursor.execute(sql_statement)

        # return list of results
        return cursor.fetchall()

query = """SELECT student.stname, AVG(results.percent)
            FROM student
            JOIN results
            ON student.stnumb = results.stnumb
            WHERE student.grade = 7
            GROUP BY student.stnumb;
        """
database_file = "school.db"

result = run_sql_statement(database_file,query)

for row in result:
    print(f"{row[0]} has an average grade of {row[1]}")