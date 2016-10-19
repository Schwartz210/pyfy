__author__ = 'Avi Schwartz - Schwartz210@gmail.com'
from sqlite3 import connect
DATABASE = 'test.db'

def create_table():
    sql_request = 'CREATE TABLE Stocks(ID INTEGER PRIMARY KEY AUTOINCREMENT, Open Decimal(15,15), Date DATE, Close Decimal(15,15), Low Decimal(15,15), Symbol VARCHAR(5), Adj_Close Decimal(15,15), Volume Integer, High Decimal(15,15))'
    execute_sql(sql_request)

def execute_sql(SQL_request):
    '''
    Alter database. Does not query data.
    '''
    conn = connect(DATABASE)
    c = conn.cursor()
    c.execute(SQL_request)
    conn.commit()
    conn.close()

def execute_multiple_sql(SQL_requests):
    conn = connect(DATABASE)
    c = conn.cursor()
    for SQL_request in SQL_requests:
        c.execute(SQL_request)
    conn.commit()
    conn.close()

def pull_data(SQL_request):
    '''
    Inputs SQL_request, outputs records
    '''
    conn = connect(DATABASE)
    c = conn.cursor()
    try:
        list_of_tuples = list(c.execute(SQL_request))
        list_of_lists = [list(elem) for elem in list_of_tuples]
        conn.commit()
        conn.close()
        return list_of_lists
    except:
        raise Exception('Not able to fulfill request')

def add_record(record):
    sql_request = 'INSERT INTO Stocks VALUES(NULL, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (record['Open'], record['Date'], record['Close'], record['Low'], record['Symbol'], record['Adj_Close'], record['Volume'], record['High'])
    return sql_request

def convert_list_of_lists_to_list(list_of_lists):
    new_list = []
    for lst in list_of_lists:
        item = lst[0]
        new_list.append(item)
    return new_list

def get_ticker_list():
    messy_data = pull_data('SELECT DISTINCT Symbol FROM Stocks')
    data = convert_list_of_lists_to_list(messy_data)
    return data

def get_date_close(symbol):
    sql_request = 'SELECT Date, Close FROM Stocks WHERE Symbol="%s" LIMIT 10' % (symbol)
    data = pull_data(sql_request)
    dates = [record[0] for record in data]
    close_amounts = [record[1] for record in data]
    series = [dates, close_amounts]
    return series

