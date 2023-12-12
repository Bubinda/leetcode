flights = [
    ['Chennai', 'Bangalore'], 
    ['Bombay', 'Delhi'], 
    ['Goa', 'Chennai'], 
    ['Delhi', 'Goa'], 
    ['Bangalore', 'Beijing']
]


def plan_trip(flights: list) -> list:
    set_departure, set_arrival = set(), set()
    flight_map = {}

    # first we need to fid our start city by getting all departures and arivals into sets and then find the difference between them which has to be the start city
    # also we are building our flights map where the start is the key and the arival is the value
    for i in flights:
        set_departure.add(i[0])
        set_arrival.add(i[1])
        if i[0] not in flight_map:
            flight_map[i[0]] = i[1]
        else:
            pass
    
    start_city = list(set_departure - set_arrival)[0]
    print(start_city)

    sorted_trip = []

    for i in range(len(flight_map.items())):
        sorted_trip.append([start_city,flight_map[start_city]])
        start_city = flight_map[start_city]

    return sorted_trip


print(plan_trip(flights))



#smae function but with more clear varibale names

def plan_trip_2(flights):
    # Build a directed graph from the given flights
    graph = {}
    start_cities = set()
    end_cities = set()

    for flight in flights:
        start_city, end_city = flight
        start_cities.add(start_city)
        end_cities.add(end_city)
        graph[start_city] = end_city

    # Find the starting city (the one in start_cities but not in end_cities)
    start_city = (start_cities - end_cities).pop()

    # Reconstruct the path
    path = []
    current_city = start_city

    while current_city in graph:
        next_city = graph[current_city]
        path.append([current_city, next_city])
        current_city = next_city

    return path


print(plan_trip_2(flights))


# still not working
#allow to visit cities multiples times:

def plan_trip_multiple_visits(flights):
    # Build a directed graph from the given flights
    graph = {}

    for flight in flights:
        start_city, end_city = flight
        if start_city not in graph:
            graph[start_city] = []
        graph[start_city].append(end_city)

    # Reconstruct the path
    path = []
    stack = [flights[0][0]]  # Start with the first departure city

    while stack:
        current_city = stack[-1]

        if current_city in graph and graph[current_city]:
            next_city = graph[current_city].pop(0)
            stack.append(next_city)
            path.append([current_city, next_city])
        else:
            stack.pop()

    return path

flights_multi = [
    ['Chennai', 'Bangalore'], 
    ['Bombay', 'Delhi'], 
    ['Goa', 'Chennai'], 
    ['Delhi', 'Goa'], 
    ['Bangalore', 'Beijing']
]

print(plan_trip_multiple_visits(flights_multi))