def reconstruct_itinerary(N, cards):
    graph = {}
    for card in cards:
        A, B, C = card.split()
        graph[A] = (B, int(C))

    itinerary = []
    current_city = next(iter(graph))

    for _ in range(N-1):
        next_city, cost = graph[current_city]
        itinerary.append(f"{current_city} {next_city} {cost}")
        current_city = next_city

    total_cost = sum(cost for _, _, cost in itinerary)
    return itinerary, total_cost


# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the number of cities
    N = int(input())

    cards = []
    for _ in range(N-1):
        card = input()
        cards.append(card)

    # Reconstruct the itinerary and calculate the total cost
    itinerary, total_cost = reconstruct_itinerary(N, cards)

    # Print the reconstructed itinerary
    for card in itinerary:
        print(card)

    # Print the total cost
    print(total_cost)
