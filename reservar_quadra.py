import mysql.connector


# def main():
#     verify_availability(1, 2, '2019-05-12 08:00:00', '2019-05-12 09:30:00')


def start_db():
    my_db = mysql.connector.connect(
      host="thh2lzgakldp794r.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",
      user="cqvqzm2i3e1a7v11",
      password="fw6q0gex6nwfxie4",
      database="opu1ysh7dog4b9k3"
    )

    return my_db


def verify_availability(grupo, quadra, dataInicio, dataFim):
    my_db = start_db()
    my_cursor = my_db.cursor()

    sql = "SELECT * FROM Agendamento WHERE DataFim > %s AND DataInicio < %s AND IdQuadra = %s"
    val = (dataInicio, dataFim, quadra)
    my_cursor.execute(sql, val)

    agendado = my_cursor.fetchall()

    if not agendado:
        sql = "INSERT INTO Agendamento(IdQuadra, IdGrupo, DataInicio, DataFim) VALUES(%s,%s,%s,%s)"
        val = (quadra, grupo, dataInicio, dataFim)
        my_cursor.execute(sql, val)
        # print("Horário agendado!")
        my_db.commit()
        status = True
    else:
        # print("Horário já agendado!")
        status = False

    my_db.close()
    my_cursor.close()

    return status
