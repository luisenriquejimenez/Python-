import sqlalchemy as db

engine = db.create_engine('sqlite:///slangpanameño.db')
conn = engine.connect()
metadata = db.MetaData()
slangpanameño = db.Table('slangpanameño', metadata, autoload=True, autoload_with=engine)

print(slangpanameño.columns.keys())
print(repr(metadata.tables['slangpanameño']))

query = db.select([slangpanameño])
resultado = conn.execute(query).fetchall()
print(resultado)


slangpanameño.drop(engine)
