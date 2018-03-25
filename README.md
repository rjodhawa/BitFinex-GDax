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

# Accepted Query Pattern Example
- Search for exchange as being either BitFinex or GDax http://localhost:4200/?function={exchange="Bitfinex"} 
- Search for orderBook type as being either ask or bid http://localhost:4200/?function={type="ask"}
- Search by price http://localhost:4200/?function={price>9000}
- Search by amount {amount>200}
- Search by count {count<1}
- Search by pairname {pairname="BTCUSD"} :Currently The value fetched is only of type BTCUSD 

# Disclaimer
All Prices are in USD
