import oracledb
def connect(user,password,wallet_password):
    connection = oracledb.connect(
        config_dir = "C:\Oracle\OracleCloud\DATABASEDUOC",
        user = user,
        password = password ,
        dsn = "databaseduoc_medium",
        wallet_location = "C:\Oracle\OracleCloud\DATABASEDUOC",
        wallet_password = wallet_password)
    return connection