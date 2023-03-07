import psycopg2


def makeQuery(dbConfig, intermediaryId, limit):
    psqlQuery = "SELECT * FROM public." + \
        dbConfig["table"] + " where intermediary_id=" + \
        intermediaryId + " ORDER BY id DESC LIMIT " + limit

    return psqlQuery


def policyList(dbConfig, intermediaryId, limit,):
    QUERY = makeQuery(dbConfig, intermediaryId, limit)
    try:
        connection = psycopg2.connect(
            database=dbConfig['database'],
            user=dbConfig['username'],
            password=dbConfig['password'],
            host=dbConfig['host'],
            port=dbConfig['port']
        )
    except psycopg2.DatabaseError as e:
        print("ERROR ==> ", e)
        return None
    cursor_obj = connection.cursor()
    cursor_obj.execute(QUERY)
    result = cursor_obj.fetchall()
    return result