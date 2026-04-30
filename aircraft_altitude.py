from aircraft import Aircraft
def main():
    model = input("Enter aircraft model:\n")
    my_aircraft = Aircraft(model)
    while True:
        pilot_input = input("Enter command (A for ascent, D for descent, X to exit):\n")
        parts = pilot_input.split()
        if not parts:
            continue
        command = parts[0].upper()
        if command == 'X':
            break
        if command == 'A' and len(parts) > 1:
            feet = int(parts[1])
            my_aircraft.ascent(feet)
        elif command == 'D' and len(parts) > 1:
            feet = int(parts[1])
            my_aircraft.descent(feet)
    print(f"Final altitude: {my_aircraft.altitude} feet")
if __name__ == "__main__":
    main()