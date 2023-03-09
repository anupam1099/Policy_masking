# DB config
dbConfig = {
    "database": "ackore_policy",
    "username": "postgres",
    "password": "root",
    "host": "localhost",
    "port": "5432",
    "table": "ackore_policy"
}
intermediaryId = "205"
limit = "10000"

# environment
env = {
    "dev": "https://ackodev.com",
    "prod": "https://acko.com"
}

# CONSTANTS
# masked regex
regex_EngineMasked = "X{9}[0-9]{5}"
regex_ChassisMasked = "X{11}[0-9]{5}"
regex_Mobile = "X{6}[0-9]{4}"
regex_Email = "^[\w\.]{1}X[\w]+@([\w-]+\.)+[\w-]{2,4}$"

# unmasked regex
regex_EngineNotMasked = "[A-Z]{2}[0-9]{2}[A-Z]{5}[0-9]{5}"
regex_ChassisNotMasked = "[(A-H|J-N|P|R-Z|0-9)]{17}"
regex_MobileNotMasked = "^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$"
regex_EmailNotMasked = "^[\w\.][^X]+@([\w-]+\.)+[\w-]{2,4}$"
