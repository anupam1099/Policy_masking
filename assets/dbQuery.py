import psycopg2
from assets.constants import dbConfig, intermediaryId, limit
from assets.utils import printError


# Generating SQL Query
def makeQuery(dbConfig, intermediaryId, limit):
    sqlQuery = "SELECT * FROM public." + \
        dbConfig["table"] + " where intermediary_id=" + \
        intermediaryId + " ORDER BY id DESC LIMIT " + limit

    # psqlQuery = "SELECT * FROM public." + \
    #     dbConfig["table"] + " where intermediary_id=" + \
    #     intermediaryId + " ORDER BY updated_on DESC LIMIT " + limit
    return sqlQuery


# DB connection and SQL query Execution
def policyList():
    QUERY = makeQuery(dbConfig, intermediaryId, limit)
    try:
        connection = psycopg2.connect(
            database=dbConfig['database'],
            user=dbConfig['username'],
            password=dbConfig['password'],
            host=dbConfig['host'],
            port=dbConfig['port']
        )
    except psycopg2.Error as e:
        printError(e)
        return None
    cursor = connection.cursor()
    try:
        cursor.execute(QUERY)
    except psycopg2.Error as e:
        printError(e)
        return None
    return cursor.fetchall()
