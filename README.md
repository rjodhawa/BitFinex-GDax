# Preliminary
You will be connecting to two Websocket channels via their APIs: one from Bitfinex and one from Coinbase. These channels relay information about those companies’ Order Books. Upon connection, they each send a snapshot of their respective order books and then send any subsequent updates.

# Steps
1.  Create Websocket connections to both exchanges’ order books.
2.  Create a new consolidated order book that contains information from both exchanges, which is aggregated from the snapshots that come from the Bitfinex/Gdax Websocket APIs as well as the updates they each emit.
3.  Upon receiving the snapshot, store it into a MySQL database using SQLAlchemy.
4.	Create a Websocket API that returns the consolidated order book 
5.  The user it able to connect to it and receive order book and subsequent snapshots.
6.  Create a REST endpoint with the ability to take query parameters for filtering the order book.

# Work in progress
1.  Creating a Angular 4 app that connects to back-end API
2.  Display the order book and update the view in real-time with any updates that come from Websocket connection.
3.  Building a form (Reactive Form) for filtering the snapshot of the order book.

# BitFinex-GDax
Relay Bitcoin information of orderBooks from BitFinex and GDax
Make sure that your machine has Python3 installed

Download the following packages for python
1. tornado 4.5.3 (Web Socket API for python)
2. SimpleJSON 3.13.2 (Reading and parsing data received from BitFinex and GDax)
3. sqlalchemy 1.2.5 (For storage, retrieval and performing query on Data)

Steps To launch the program:
1. Launch  NobleWebSocket.py
2. Launch WebAPI.py
3. Open Browser and perform operations

# NobleWebSocket
This program continously adds data to SQLLITE database from the time it is started, until we close the program. It fetches data from BitFinex and Gdax parse it and stores it in DB continously.

# WebAPI
Listens at port 4200 and displays results of the query on web browser.

# Warning:
You would have to stop and rerun the WebAPI.py everytime a new query is requested.

# View OrderBooks
- Run both the python program in sequence and then go to http://localhost:4200/noble-markets-order-book-snapshot
- To View Snapshot updates to order Books http://localhost:4200/noble-markets-order-book-snapshot

# Accepted Query Pattern Example
- Search for exchange as being either BitFinex or GDax http://localhost:4200/?function={exchange="Bitfinex"} 
- Search for orderBook type as being either ask or bid http://localhost:4200/?function={type="ask"}
- Search by price http://localhost:4200/?function={price>9000}
- Search by amount {amount>200}
- Search by count {count<1}
- Search by pairname {pairname="BTCUSD"} :Currently The value fetched is only of type BTCUSD 

# Disclaimer
All Prices are in USD
