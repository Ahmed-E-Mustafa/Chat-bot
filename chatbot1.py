import random

houses = [
    {
        "title": "Apartment for Rent in F-9",
        "location": "F-9, Islamabad",
        "sector": "F-9",
        "latitude": 33.7041,
        "longitude": 73.0424,
        "rent_or_buy": "rent",
        "price": 70000,
        "beds": 2,
        "baths": 1,
        "area": 1200
    },
    {
        "title": "Bungalow for buy in F-9",
        "location": "F-9, Islamabad",
        "sector": "F-9",
        "latitude": 75.5031,
        "longitude": 83.4133,
        "rent_or_buy": "buy",
        "price": 7000000,
        "beds": 6,
        "baths": 3,
        "area": 5000
    },
    {
        "title": "Bungalow for Sale in G-13",
        "location": "G-13, Islamabad",
        "sector": "G-13",
        "latitude": 33.6471,
        "longitude": 72.9766,
        "rent_or_buy": "buy",
        "price": 15000000,
        "beds": 5,
        "baths": 5,
        "area": 5000
    },
    {
        "title": "Apartment for Rent in H-8",
        "location": "H-8, Islamabad",
        "sector": "H-8",
        "latitude": 33.6917,
        "longitude": 73.0569,
        "rent_or_buy": "rent",
        "price": 55000,
        "beds": 2,
        "baths": 1,
        "area": 1000
    },
    {
        "title": "Bungalow for Sale in G-9",
        "location": "G-9, Islamabad",
        "sector": "G-9",
        "latitude": 33.6939,
        "longitude": 73.0369,
        "rent_or_buy": "buy",
        "price": 8000000,
        "beds": 4,
        "baths": 3,
        "area": 2500
    }
]


def chatbot():
    print("Hi there! I can help you find a house based on your preferences.")
    while True:
        user_input = input("How can I assist you? ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye!")
            break
        elif user_input.lower() in ['find house', 'search house']:
            sector = input("Which sector are you interested in (F-9, G-13, H-8, G-9)? ")
            rentorbuy = input("do you want to buy or rental? ")
            if sector.lower() == 'f-9':
                markaz = input("Do you want to live near a markaz in F-9 sector? (yes/no) ")
            
            beds = int(input("How many bedrooms do you need (1-6)? "))
            area = int(input("What is the minimum required area (in sqft)? "))
            house_type = input("Do you prefer a bungalow or an apartment? ")
            if house_type != 'bungalow' and 'apartment':
                print("I'm sorry, I couldn't find any houses that match your criteria.")
                break
            if sector.lower() == 'f-9' and markaz.lower() == 'yes':
                price_increase = 1.4
            else:
                price_increase = 1.0
            
            filtered_houses = [house for house in houses if house['sector'].lower() == sector.lower() and
                               house['beds'] >= beds and house['area'] >= area and
                               house['title'].lower().startswith(house_type.lower()) and house['rent_or_buy']== rentorbuy ]
            
            if filtered_houses:
                prices = [house['price'] * price_increase for house in filtered_houses]
                price_range = f"Rs. {min(prices):,} to Rs. {max(prices):,}"
            print(f"I found houses that match your criteria in {sector.upper()} sector:")
            for house in filtered_houses:
                print(f"Title: {house['title']}")
                print(f"Location: {house['location']}")
                print(f"Price: {house['price'] * price_increase}")
                print(f"Beds: {house['beds']}")
                print(f"Baths: {house['baths']}")
                print(f"Area: {house['area']}")
                print("========================================")

            user_budget = int(input("How much can you afford to spend on a house? "))
            estimated_price = max(prices)
            if user_budget < estimated_price * 0.5:
                print("I'm sorry, but your budget is too low. You may need to increase your price range.")
            elif user_budget < estimated_price * 0.7:
                print("Based on your budget, I recommend considering the following options:")
                for house in filtered_houses:
                    if house['price'] * price_increase <= user_budget:
                        print(f"Title: {house['title']}")
                        print(f"Location: {house['location']}")
                        print(f"Price: {house['price'] * price_increase}")
                        print(f"Beds: {house['beds']}")
                        print(f"Baths: {house['baths']}")
                        print(f"Area: {house['area']}")
                        print("========================================")
            else:
                print("You have a good budget to explore various options. Consider other options aswell if you wish to save :D")
        else:
            print("I'm sorry, I couldn't find any houses that match your criteria.")
