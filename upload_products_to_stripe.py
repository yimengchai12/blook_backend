from sqlalchemy import create_engine, Table, MetaData
import stripe

stripe.api_key = "sk_test_51MqXdHE3thje2p8MDiPdiAf9rL1wQHZirFYfmKIetPDBkvyX2avd9BtxfIJ1BpThFRSTyoBSGBbk48BQygVYXkWo00kAK2chaW"
# create a connection to the database
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/activity')

# create a metadata object and reflect the database schema
metadata = MetaData()
metadata.reflect(bind=engine)

# get a reference to the table you want to iterate over
my_table = Table('activity', metadata, autoload=True, autoload_with=engine)

# create a select statement to retrieve all rows from the table
stmt = my_table.select()

# execute the select statement and retrieve the result set
with engine.connect() as conn:
    result_set = conn.execute(stmt)

    # iterate over the rows in the result set
    for row in result_set:
        # process each row as needed
        try:
            stripe.Product.create(
                id=row[0],
                name=row[1],
                default_price_data={
                    "unit_amount": int(row[3]*100),
                    "currency": "sgd",
                },
                expand=["default_price"],
            )
        except:
            pass
