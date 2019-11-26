from pymongo import MongoClient
client = MongoClient('127.0.0.1', 27017)
client.drop_database('food')
db = client['food']

comments = db['comments']
comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Chilis", "rating":"4"})
comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Chilis", "rating":"5"})
comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Chilis", "rating":"5"})

comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Galaxy", "rating":"5"})
comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Galaxy", "rating":"5"})

comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Brik Oven", "rating":"3"})
comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Brik Oven", "rating":"5"})
comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Brik Oven", "rating":"4"})

comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Indian Kitchen", "rating":"4"})

comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Mainland China", "rating":"4"})
comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Mainland China", "rating":"3"})

comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Onesta", "rating":"4"})
comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Onesta", "rating":"4"})
comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Onesta", "rating":"4"})

comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Punjab Grill", "rating":"4"})

comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "The Art Cafe", "rating":"4"})
comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "The Art Cafe", "rating":"4"})
comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "The Art Cafe", "rating":"4"})
comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "The Art Cafe", "rating":"4"})

comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Toscano", "rating":"4"})
comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Toscano", "rating":"4"})

comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Tiamo", "rating":"5"})
comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Tiamo", "rating":"5"})
comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Tiamo", "rating":"5"})
comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Tiamo", "rating":"5"})
comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Tiamo", "rating":"5"})

comments.insert_one({"id" : "1574340699989","name":"Dweepa3", "message": "So cool", "rest" : "Hoot", "rating":"5"})







restaurants = db['restaurants']
db.restaurants.insert_one({ "rest": "Chilis", "description": "Family-friendly chain serving classic Tex-Mex & American fare in a Southwestern-style setting", "image": "chilis.jpeg"  })

db.restaurants.insert_one({ "rest": "Galaxy", "description": "Housed inside the Samsung Opera House, a luxury restaurant that satisfies your every craving from Indian food all the way to American", "image": "galaxy.jpeg"  })

db.restaurants.insert_one({ "rest": "Brik Oven", "description": "Located in the heart of the City on Church Street, is known as one of the best pizza places in Bangalore. This small and cozy place is a lunch favorite.", "image": "brikoven.jpg"  })

db.restaurants.insert_one({ "rest": "Indian Kitchen", "description": "As the name suggests, is an overload of Indian cuisine, ranging from North Indian to South Indian all of which is impeccably prepared", "image": "inidankitchen.jpeg"  })

db.restaurants.insert_one({ "rest": "Mainland China", "description": "This place takes you right to the heart of China, with noodles and ramen served along with fried vegetarian as well as non-vegetarian food", "image": "mainlandchina.jpeg"  })

db.restaurants.insert_one({ "rest": "Onesta", "description": "Slowly but surely becoming one of the most go-to places for pizza in town, and is available at numerous locations in order for you to fulfill your hunger", "image": "onesta.jpg"  })

db.restaurants.insert_one({ "rest": "Punjab Grill", "description": "If you're a North Indian, you are going to love this place. The spicy chicken is off the charts, and takes you to a place none other than the heart of Punjab.", "image": "punjabgrill.jpeg"  })

db.restaurants.insert_one({ "rest": "The Art Cafe", "description": "As the name suggests, the place is decorated by magnificent art works, and is a common hangout place for writers and artists alike. Coffee here is a must have, and bodes well for journalists to mingle.", "image": "theartcafe.jpeg"  })

db.restaurants.insert_one({ "rest": "Toscano", "description": "A hip new pizza cafe, Savor delicious new offerings, along with classic favorites!", "image": "toscano.jpeg"  })

db.restaurants.insert_one({ "rest": "Tiamo", "description": "One of Bangalore's favorite luxury restaurants, located in Conrad Bengaluru, is famous for its rendition of the dish Ratatouille. Your pocket is going to hurt here, but it is worth the experience for a date.", "image": "tiamo.jpg"  })

db.restaurants.insert_one({ "rest": "Hoot", "description": "Located on Sarjapur road this classic place has live music performances and great tasting food", "image": "hoot.jpg"  })
