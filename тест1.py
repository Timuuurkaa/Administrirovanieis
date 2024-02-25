from лаба1 import init, fill, show, db

def test_init():
    db.connect()
    init()
    db.close()

def test_init_second_time():
    db.connect()
    init()
    db.close()

def test_show_empty():
    db.connect()
    for tablename in ("clients", "orders"):
        show(tablename)
    db.close()

def test_fill():
    db.connect()
    for i in range(25):
        fill()
    db.close()

def test_show():
    db.connect()
    for tablename in ("clients", "orders"):
        show(tablename)
    db.close()
