import oracledb
def connect(user,password,wallet_password):
    connection = oracledb.connect(
        config_dir = "C:\ORACLE",
        user = user,
        password = password ,
        dsn = "databaseduoc_medium",
        wallet_location = "C:\ORACLE",
        wallet_password = wallet_password)
    return connection