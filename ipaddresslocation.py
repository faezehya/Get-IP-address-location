import geoip2.database

# Path to the GeoIP2 database file
db_path = '/path/to/GeoLite2-City.mmdb'

# IP address to lookup
ip_address = '8.8.8.8'

# Open the GeoIP2 database
with geoip2.database.Reader(db_path) as reader:
    # Lookup the IP address
    response = reader.city(ip_address)

    # Print the location information
    print(f'City: {response.city.name}')
    print(f'State: {response.subdivisions.most_specific.name}')
    print(f'Country: {response.country.name}')
    print(f'Latitude: {response.location.latitude}')
    print(f'Longitude: {response.location.longitude}')
