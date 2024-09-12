# --------------------------------------------------
# # Simple Chatbot using lists
# --------------------------------------------------

def chatbot():
    # List of 20 countries and tourist information
    countries = [
        "france", "italy", "japan", "egypt", "usa", "brazil", "australia", 
        "canada", "china", "india", "germany", "spain", "greece", "thailand", 
        "turkey", "mexico", "south africa", "russia", "argentina", "uk"
    ]
    
    tourist_info = [
        "France is home to the Eiffel Tower and the historic Palace of Versailles.",
        "Italy boasts the Colosseum in Rome and the beautiful canals of Venice.",
        "Japan offers the serene Mount Fuji and the bustling city of Tokyo.",
        "Egypt is famous for the ancient Pyramids of Giza and the Sphinx.",
        "The USA is known for the Grand Canyon and the Statue of Liberty.",
        "Brazil is famous for the Christ the Redeemer statue and the Amazon Rainforest.",
        "Australia is home to the Sydney Opera House and the Great Barrier Reef.",
        "Canada is known for the stunning Niagara Falls and the Rocky Mountains.",
        "China offers the Great Wall of China and the Terracotta Army.",
        "India is known for the Taj Mahal and the palaces of Rajasthan.",
        "Germany boasts the Brandenburg Gate and the Black Forest.",
        "Spain is famous for the Sagrada Familia in Barcelona and the Alhambra in Granada.",
        "Greece is known for the Parthenon in Athens and the islands of Santorini.",
        "Thailand offers the temples of Bangkok and the beaches of Phuket.",
        "Turkey is famous for Hagia Sophia in Istanbul and the fairy chimneys of Cappadocia.",
        "Mexico boasts the ancient pyramids of Teotihuacan and the beaches of Cancun.",
        "South Africa is known for Kruger National Park and Table Mountain.",
        "Russia offers the Kremlin and Red Square in Moscow and the Hermitage Museum in St. Petersburg.",
        "Argentina is famous for the stunning Iguazu Falls and the tango culture of Buenos Aires.",
        "The UK is known for Big Ben in London and the historic Edinburgh Castle in Scotland."
    ]
    
    country = input("What's your favorite destination country? ").lower()

    print("\n\n")

    # Check if the country is in the list
    if country in countries:
        index = countries.index(country)
        print(f"Great choice! {tourist_info[index]}")
        print("\n\n")
    else:
        print("Sorry, I don't have information about that country yet.")

chatbot()
