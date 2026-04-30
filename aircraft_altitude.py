from aircraft import Aircraft
def main():
    model = input("Enter aircraft model:\n")
    my_aircraft = Aircraft(model)
    while True:
        pilot_input = input("Enter command (A for ascent, D for descent, X to exit):\n")
        parts = pilot_input.split()
        command = parts[0].upper()
        if command == 'X':
            break
        if len(parts) < 2:
            print("Please provide the number of feet.")
            continue
        feet = int(parts[1])
        if command == 'A':
            my_aircraft.ascend(feet)
        elif command == 'D':
            my_aircraft.descend(feet)
        else:
            print("Invalid command.")
    print(f"Final altitude: {my_aircraft.altitude}")
if __name__ == "__main__":
    main()