for name in ['Reinout', 'Harry']:
    print(name)

# START_HIGHLIGHT
for i in range(10):
    # END_HIGHLIGHT
    print("Django")

# START_HIGHLIGHT
for index, name in enumerate(['Reinout', 'Harry']):
    # END_HIGHLIGHT
    print(index, name)
    # Prints '0 Reinout' and '1 Harry'

cities = {'Nieuwegein': 'The Netherlands',
          'Utrecht': 'The Netherlands',
          'Ulmen': 'Germany',
          'Toronto': 'Canada'}
for city in cities:
    print(city)
    # Prints the key, so Nieuwegein, Utrecht, etc.

for city in cities.keys():
    print(city)
    # Also the keys.

for country in cities.values():
    print(country)
    # Prints the value, so Germany, Canada, etc.

for city, country in cities.items():
    print(city, country)
    # .items() returns both key and value.
