import psycopg2
import psycopg2.extras


hostname = 'localhost'
database ='debts'
username ='postgres'
pwd ='prajituri420'
port_id = 5432
conn = None

def trying():
    try:

        with psycopg2.connect(
                host=hostname,
                dbname = database,
                user=username,
                password=pwd,
                port=port_id) as conn:

            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            ##  cur.execute('DROP TABLE IF EXISTS debtss')


                ##create_script=''' CREATE TABLE IF NOT EXISTS debtss (
                ##                    id            SERIAL PRIMARY KEY,
                ##                    person        varchar(40) NOT NULL,
                ##                    debt_value    int,
                ##                    data_scadenta varchar(40))'''
                
                ## cur.execute(create_script)

                insert_script = 'INSERT INTO debtss (person, debt_value, data_scadenta) VALUES (%s,%s,%s)'
                insert_value = [("xuesc",23,"2022-23-1")]

                for record in insert_value:
                    cur.execute(insert_script, record)
                
            ##    update_script = 'UPDATE debtss SET debt_value= debt_value - 50'
            ##    cur.execute(update_script)
                
            ##    delete_script = 'DELETE FROM debtss WHERE person=%s'
            ##    delete_record=('ion',)
            ##    cur.execute(delete_script,delete_record)
                

                cur.execute('SELECT * FROM DEBTSS')
                for record in cur.fetchall():
                    print(record['person'], record['debt_value'],record['data_scadenta'])



    except Exception as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()