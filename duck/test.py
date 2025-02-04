
import duckdb

duckdb.sql("SELECT 42").show()

r1 = duckdb.sql("SELECT 42 AS i")
duckdb.sql("SELECT i * 2 AS k FROM r1").show()


conn = duckdb.connect('my_first_db.db')