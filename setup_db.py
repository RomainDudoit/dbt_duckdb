import duckdb
c = duckdb.connect("lab.duckdb")
c.execute("create schema if not exists jaffle_shop")
c.execute("create or replace table jaffle_shop.orders(id int, user_id int, status varchar, order_date date, amount int)")
c.execute("""insert into jaffle_shop.orders values
 (1,10,'placed','2026-01-01',500),
 (2,11,'','2026-01-02',300),      -- statut vide -> fait échouer not_empty_string
 (3,12,'shipped','2026-01-03',-200) -- montant négatif -> fait échouer assert_amount_positive
""")
print("lab.duckdb prêt")
