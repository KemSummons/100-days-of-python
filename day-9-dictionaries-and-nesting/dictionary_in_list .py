travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country, visits, cities):
    new_dictionary = {}
    if country != '':
        new_dictionary['country'] = country
    if visits != '':
        new_dictionary['visits'] = visits
    if cities != '':
        new_dictionary['cities'] = cities
    travel_log.append(new_dictionary)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
