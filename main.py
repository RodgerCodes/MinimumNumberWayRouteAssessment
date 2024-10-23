from optimizer import FlightRouteOptimizer


if __name__ == "__main__":
    airports = ['DSM', 'ORD', 'BGI', 'LGA', 'JFK', 'HND', 'ICN', 
                'EWR', 'TLV', 'DEL', 'DOH', 'CDG', 'SIN', 'BUD', 
                'SFO', 'SAN', 'EYW', 'LHR']

    routes = [
        ('EWR', 'HND'),
        ('HND', 'ICN'),
        ('ICN', 'JFK'),
        ('JFK', 'LGA'),
        ('TLV', 'DEL'),
        ('DEL', 'CDG'),
        ('DEL', 'DOH'),
        ('CDG', 'SIN'),
        ('CDG', 'BUD'),
        ('SIN', 'JFK'),
        ('SFO', 'SAN'),
        ('SFO', 'DSM'),
        ('SAN', 'EYW'),
        ('EYW', 'LHR'),
        ('LHR', 'SFO'),
        ('DSM', 'ORD'),
        ('ORD', 'BGI'),
        ('BGI', 'LGA')
    ]

    optimizer = FlightRouteOptimizer(routes, airports)
    num_routes, unreachable_airports = optimizer.min_additional_routes('EWR')

    print(f"Starting airport: EWR")
    print(f"Minimum number of additional routes needed: {num_routes}")
    print(f"Unreachable airports: {unreachable_airports}")
    print("\nPossible new routes to add:")
    for airport in unreachable_airports:
        print(f"EWR -> {airport}")