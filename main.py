from optimizer import FlightRoutesOptimizer

if __name__ == "__main__":
    # Sample data from the diagram
    airports = ['DSM', 'ORD', 'BGI', 'LGA', 'JFK', 'HND', 'ICN', 
                'EWR', 'TLV', 'DEL', 'DOH', 'CDG', 'SIN', 'BUD', 
                'SFO', 'SAN', 'EYW', 'LHR']

    routes = [
        ('DSM', 'ORD'), ('ORD', 'BGI'), ('BGI', 'LGA'), ('JFK', 'LGA'),
        ('JFK', 'ICN'), ('HND', 'ICN'), ('TLV', 'DEL'), ('DEL', 'DOH'),
        ('DEL', 'CDG'), ('CDG', 'BUD'), ('CDG', 'SIN'), ('SIN', 'JFK'),
        ('SFO', 'SAN'), ('SFO', 'DSM'), ('EYW', 'LHR'), ('SAN', 'EYW'),
        ('LHR', 'SFO'), ('EWR', 'HND')
    ]

    optimizer = FlightRoutesOptimizer(routes, airports)
    result = optimizer.min_additional_routes('DSM')
    print(f"Minimum additional routes needed: {result}")
