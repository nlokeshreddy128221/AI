def reflex_agent(room):
    if room == "Dirty":
        return "Clean"
    else:
        return "Move to next room"


# Toy environment
rooms = {
    "A": "Dirty",
    "B": "Clean",
    "C": "Dirty"
}

print("Initial Rooms:", rooms)

for room in rooms:
    print("\nRobot is in Room", room)
    print("Room status:", rooms[room])

    action = reflex_agent(rooms[room])
    print("Action:", action)

    if action == "Clean":
        rooms[room] = "Clean"

print("\nFinal Rooms:", rooms)
