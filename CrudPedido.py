import mysql.connector
#import datetime


db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='104604_Md',
    database='crud',
)

cursor = db.cursor()

def create_pedido (nome_cliente, item, quant, valor_item):
    sql = """INSERT INTO pedido (
          nome_cliente,
          item,
          quant,
          valor_item)
          VALUES ({}.format(nome_cliente),{}.format(item), %s, %s)"""
    values = input("Digite os valores separados por virgulas:")
    tupla= tuple(values.split(","))
    cursor.execute(sql, tupla)
    db.commit()
    print("Novo pedido criado!")
    
print(create_pedido)

def read_pedido ():
    sql = "SELECT * FROM pedido"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
        
def delete_pedido ():
    sql = "DELETE FROM vendas WHERE nome_cliente = %s"
    values(nome_cliente)
    cursor.execute(sql, values)
    db.commit()
    print("Pedido excluído!")
             
cursor.close()
db.close()




