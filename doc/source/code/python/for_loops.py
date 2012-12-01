for name in ['Reinout', 'Maurits']:
    print(name)

for i in range(10):
    print("Django")

for index, name in enumerate(['Reinout', 'Maurits']):
    print(index, name)
    # Prints '0 Reinout' and '1 Maurits'

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
