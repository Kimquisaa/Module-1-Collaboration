from sqlalchemy import create_engine, MetaData, Table, select
engine = create_engine("sqlite:///books.db")
connection = engine.connect()
metadata = MetaData()
metadata.reflect(bind=engine)
book_table = metadata.tables['book']
query = select(book_table.c.title).order_by(book_table.c.title)
results = connection.execute(query)
for row in results:
 print(row.title)