def calculate_handshakes(num_people):
    handshakes = (num_people * (num_people - 1)) // 2
    return handshakes

num_people = int(input("Enter the number of people in the room: "))

max_handshakes = calculate_handshakes(num_people)

print(max_handshakes)
