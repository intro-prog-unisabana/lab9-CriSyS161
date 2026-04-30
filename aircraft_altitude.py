from aircraft import Aircraft
def main():
    model = input("Enter aircraft model:\n")
    my_aircraft = Aircraft(model)
    while True:
        user_input = input("Enter command (A for ascent, D for descent, X to exit):\n")
        parts = user_input.split()
        if not parts:
            continue
        command = parts[0].upper()
        if command == 'X':
            break
        if len(parts) >= 2:
            value = int(parts[1])
            if command == 'A':
                my_aircraft.ascent(value)
            elif command == 'D':
                my_aircraft.descent(value)
    print(f"Final altitude: {my_aircraft.altitude} feet")
if __name__ == "__main__":
    main()