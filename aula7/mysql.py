import MySQLdb

try:
    con = MySQLdb.connect(
        host="172.25.0.3",
        user="root",
        passwd="123456",
        db="projetos"
    )

    cur = con.cursor()

    ### INSERT
    cur.execute("INSERT INTO clientes(nome,endereco) \
                 VALUES('mariana', 'mariana@4linux.com.br')"
    )

    ### UPDATE
    cur.execute("UPDATE clientes SET endereco='gabriel@gabriel' \
                WHERE nome='gabriel'")

    ## DELETE
    # cur.execute("DELETE FROM alunos WHERE nome='mariana'")

    con.commit()

except Exception as e:
    print(e)
    con.rollback()
    cur.close()
    con.close()