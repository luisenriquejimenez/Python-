from pymongo import MongoClient

c = [ {"palabra": "xopa", "significado": "manera de decir como estas"},
        {"palabra": "mopri", "significado":"manera de decir primo de manera invertida"},
        {"palabra": "yalavida", "significado": " interjección de sorpresa o enojo"},
        {"palabra": "Chuleta", "significado": " Exclamacion de sorpresa o admiracion"},
        {"palabra": "Birria", "significado": "Juego muy repetitivo sin espiritu de competencia o finalidad alguna"},
         ]

client = MongoClient('mongodb://3.236.125.65:27017/')

with client:
    db = client.diccionario
    db.diccionario.insert_many(c)
