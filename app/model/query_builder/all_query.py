class AllQuery:
    def insert( table, fields):
        _list = list()
        _list.append(""" insert into {} (""".format( table))
        _list.append(", ".join(""" {} """.format(key) for key, value in fields.items()))
        _list.append(", created_at ) VALUES (")
        _list.append(", ".join(""" '{}' """.format(value) for key, value in fields.items()))
        _list.append(", NOW() );")
        return "".join(_list)

    def update(table, fields, condition):
        _list = list()
        _list.append("""update {} set """.format( table))
        _list.append(", ".join(""" {} = '{}'""".format(key, value) for key, value in fields.items()))
        _list.append("".join(""" where {} = {}""".format(key, value) for key, value in condition.items()))
        _list.append(";")
        return "".join(_list)

    def find_all(table):
        _list = list()
        _list.append("""SELECT * FROM {} """.format(table))
        _list.append(";")
        return "".join(_list)

    def find_where(table, fields):
        _list = list()
        _list.append("""SELECT * FROM {} WHERE """.format(table))
        _list.append(" and ".join(""" {} = '{}' """.format(key, value) for key, value in fields.items()))
        _list.append(";")
        return "".join(_list)

    def delete(table, fields):
        _list = list()
        _list.append("""DELETE FROM {} WHERE """.format(table))
        _list.append(" and ".join(""" {} = '{}' """.format(key, value) for key, value in fields.items()))
        _list.append(";")
        return "".join(_list)