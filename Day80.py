T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    alice_count = {}
    store_count = {}

    for animal_type in A:
        store_count[animal_type] = store_count.get(animal_type, 0) + 1

    for animal_type in store_count:
        alice_count[animal_type] = alice_count.get(animal_type, 0) + store_count[animal_type]

    for animal_type in alice_count:
        if alice_count[animal_type] != store_count.get(animal_type, 0):
            print("NO")
            break
    else:
        print("YES")
