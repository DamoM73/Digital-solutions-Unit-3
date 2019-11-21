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
                    WHERE subjname = 'language'
                ) AND percent > 50
            ) AND (grade = 4 OR grade = 5)
            ;
        """
database_file = "school.db"

result = run_sql_statement(database_file,query)

for row in result:
    print(f"Student {row[0]} scored ovcer 50% for Language.")
