import threading

from tornado import web
from tornado.ioloop import IOLoop
from sqlalchemy import create_engine
import time

class queryHandler(web.RequestHandler):

    #@web.asynchronous
    def get(self, *args):
        func = self.get_argument("function")
        print(str(func))
        func = func[1:-1]
        eng = create_engine("sqlite:///mydb.db")
        conn = eng.connect()
        rows = conn.execute("SELECT COUNT(*) FROM orderBooks")
        rows = str(rows.first())
        rows = rows[1:-2]
        count = int(rows)
        count_old = 0
        for i in range(0, count):
            conn = eng.connect()
            results = conn.execute("SELECT type, price, amount, count, exchange, pairname FROM orderBooks WHERE " + func +" AND ROWID <" + str(count) + " AND ROWID >="+ str(count_old))
            for rows in results:
                self.write(str(rows)+ "<BR>")
                time.sleep(0.1)
                self.flush(str(rows))
            rows = conn.execute("SELECT COUNT(*) FROM orderBooks")
            rows = str(rows.first())
            rows = rows[1:-2]
            count_old = count
            count = int(rows)

        # price > 40 http://localhost:8888/?function={price%3E40}
        # exchange = 'Bitfinex' http://localhost:8888/?function={exchange="Bitfinex"}
        # pair = BTCUSD http://localhost:8888/?function={pairname="BTCUSD"}

class displayOrderBook(web.RequestHandler):

    @web.asynchronous
    def get(self, *args):
        eng = create_engine("sqlite:///mydb.db")
        conn = eng.connect()
        rows = conn.execute("SELECT * FROM orderBooks")
        for row in rows:
            self.write(str(row) + "<BR>")
            time.sleep(0.1)
            self.flush(str(row))
        self.finish()

class snapshotOrderBook(web.RequestHandler):

    @web.asynchronous
    def get(self, *args):
        eng = create_engine("sqlite:///mydb.db")
        conn = eng.connect()
        rows = conn.execute("SELECT COUNT(*) FROM orderBooks")
        rows = str(rows.first())
        rows = rows[1:-2]
        initialcount = int(rows)
        count =initialcount + 100
        for i in range(0, count):
            conn = eng.connect()
            results = conn.execute("SELECT type, price, amount, count, exchange, pairname FROM orderBooks WHERE ROWID <" + str(count) + " AND ROWID >="+ str(initialcount))
            for rows in results:
                self.write(str(rows) + "<BR>")
                time.sleep(0.1)
                self.flush(str(rows))
            rows = conn.execute("SELECT COUNT(*) FROM orderBooks")
            rows = str(rows.first())
            rows = rows[1:-2]
            initialcount = count
            count = int(rows)
        self.finish()

app = web.Application([
    (r'/noble-markets-realtime-order-book',  displayOrderBook),
    (r'/noble-markets-order-book-snapshot', snapshotOrderBook),
    (r'/', queryHandler),
])

if __name__ == '__main__':
    app.listen(4200)
    IOLoop.instance().start()