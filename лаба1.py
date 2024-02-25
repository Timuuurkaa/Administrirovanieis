from peewee import *
import argparse

db = SqliteDatabase("база1.db")


class CLIENTS(Model):
    NAME = CharField()
    CITY = CharField()
    ADDRESS = CharField()

    class Meta:
        database = db
        table_name = "Clients"


class ORDERS(Model):
    CLIENT = ForeignKeyField(CLIENTS)
    DATE = DateField()
    AMOUNT = IntegerField()
    DESCRIPTION = CharField()

    class Meta:
        database = db
        table_name = "Orders"


clients_data = [
    {"NAME": "Иван Иванов", "CITY": "Москва", "ADDRESS": "ул. Ленина, д. 123"},
    {
        "NAME": "Мария Смирнова",
        "CITY": "Санкт-Петербург",
        "ADDRESS": "пр. Невский, д. 456",
    },
    {
        "NAME": "Александр Попов",
        "CITY": "Новосибирск",
        "ADDRESS": "ул. Красная, д. 789",
    },
    {"NAME": "Елена Иванова", "CITY": "Екатеринбург", "ADDRESS": "пр. Ленина, д. 101"},
    {"NAME": "Сергей Козлов", "CITY": "Казань", "ADDRESS": "ул. Баумана, д. 543"},
    {"NAME": "Анна Петрова", "CITY": "Челябинск", "ADDRESS": "пр. Победы, д. 222"},
    {"NAME": "Дмитрий Соколов", "CITY": "Омск", "ADDRESS": "ул. Пушкина, д. 333"},
    {"NAME": "Татьяна Иванова", "CITY": "Самара", "ADDRESS": "пр. Кирова, д. 444"},
    {
        "NAME": "Артем Федоров",
        "CITY": "Ростов-на-Дону",
        "ADDRESS": "ул. Гагарина, д. 555",
    },
    {"NAME": "Ольга Морозова", "CITY": "Уфа", "ADDRESS": "пр. Октября, д. 666"},
]

orders_data = [
    {
        "CLIENT": None,
        "DATE": "2024-02-21",
        "AMOUNT": 100,
        "DESCRIPTION": "Описание заказа 1",
    },
    {
        "CLIENT": None,
        "DATE": "2024-02-22",
        "AMOUNT": 200,
        "DESCRIPTION": "Описание заказа 2",
    },
    {
        "CLIENT": None,
        "DATE": "2024-02-23",
        "AMOUNT": 150,
        "DESCRIPTION": "Описание заказа 3",
    },
    {
        "CLIENT": None,
        "DATE": "2024-02-24",
        "AMOUNT": 300,
        "DESCRIPTION": "Описание заказа 4",
    },
    {
        "CLIENT": None,
        "DATE": "2024-02-25",
        "AMOUNT": 180,
        "DESCRIPTION": "Описание заказа 5",
    },
    {
        "CLIENT": None,
        "DATE": "2024-02-26",
        "AMOUNT": 250,
        "DESCRIPTION": "Описание заказа 6",
    },
    {
        "CLIENT": None,
        "DATE": "2024-02-27",
        "AMOUNT": 120,
        "DESCRIPTION": "Описание заказа 7",
    },
    {
        "CLIENT": None,
        "DATE": "2024-02-28",
        "AMOUNT": 220,
        "DESCRIPTION": "Описание заказа 8",
    },
    {
        "CLIENT": None,
        "DATE": "2024-02-29",
        "AMOUNT": 170,
        "DESCRIPTION": "Описание заказа 9",
    },
    {
        "CLIENT": None,
        "DATE": "2024-03-01",
        "AMOUNT": 280,
        "DESCRIPTION": "Описание заказа 10",
    },
]


def pretty_print(*args, FIRST=False):
    MAX = 12
    data = []
    for arg in args:
        if len(arg) > MAX:
            data.append(arg[:MAX])
        else:
            data.append(arg + (" " * (MAX - len(arg))))
    print(" | ".join(data))
    if FIRST:
        print("_" * ((MAX + 3) * len(args)))


def init():
    if db.get_tables():
        db.drop_tables([CLIENTS, ORDERS])
    db.create_tables([CLIENTS, ORDERS])


def fill():
    for i in range(10):
        order_data = orders_data[i].copy()
        order_data["CLIENT"] = CLIENTS.create(**clients_data[i])
        ORDERS.create(**order_data)


def show(tablename):
    table = {"orders": ORDERS, "clients": CLIENTS}[tablename]
    pretty_print(*table._meta.sorted_field_names, FIRST=True)
    for i in table.select():
        # print(f"{i.CLIENT} | {i.DATE} | {i.AMOUNT} | {i.DESCRIPTION}")
        pretty_print(
            *tuple(str(getattr(i, field)) for field in table._meta.sorted_field_names)
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("parametr", help="Параметр, что необходимо сделать, возможные значения: init, fill, show")
    parser.add_argument("tablename", nargs="?", default="")
    args = parser.parse_args()
    parametr = args.parametr.lower()
    tablename = args.tablename.lower()
    if parametr not in ("init", "fill", "show"):
        parser.error("Возможные значения parametr: init, fill, show")
    if parametr == "show" and tablename not in ("orders", "clients"):
        parser.error("show требует название таблицы, возможные значения: orders, clients")
    args = [tablename] if tablename else []
    db.connect()
    try:
        {"init": init, "fill": fill, "show": show}[parametr](*args)
    finally:
        db.close()
