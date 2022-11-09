import psycopg2
import datetime
import psycopg2.extras


hostname = 'localhost'
database ='debts'
username ='postgres'
pwd ='prajituri420'
port_id = 5432
conn = None
cur = None

try:

    conn = psycopg2.connect(
            host=hostname,
            dbname = database,
            user=username,
            password=pwd,
            port=port_id)



    '''date= datetime.date(2022,2,12)
    date2= datetime.date(2022,3,23)'''
    

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('DROP TABLE IF EXISTS debtss')


    create_script=''' CREATE TABLE IF NOT EXISTS debtss (
                         id            int PRIMARY KEY,
                         person        varchar(40) NOT NULL,
                         debt_value    int,
                         data_scadenta varchar(40))'''
    
    cur.execute(create_script)

    insert_script = 'INSERT INTO debtss (id, person, debt_value, data_scadenta) VALUES (%s,%s,%s,%s)'
    insert_value = [(1,'AS',200,'2022-11-10'),(2,'John',3200,'2022-03-12')]

    for record in insert_value:
        cur.execute(insert_script, record)
    
    ''' update_script = 'UPDATE debtss SET debt_value= debt_value - 50'
    cur.execute(update_script)'''
    '''
    delete_script = 'DELETE FROM debtss WHERE person=%s'
    delete_record=('Gigel',)
    cur.execute(delete_script,delete_record)
    '''

    cur.execute('SELECT * FROM DEBTSS')
    for record in cur.fetchall():
        print(record['person'], record['debt_value'],record['data_scadenta'])


    

    conn.commit()
   


except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()