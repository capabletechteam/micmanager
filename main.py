class Microphone:
    def __init__(self, number, mictype):
        # Initialize a microphone object with a unique number and type
        self.number = number  # Microphone number
        self.owner = None  # Current owner (default is None)
        self.type = mictype  # Type of microphone

        # Print a message when a microphone is signed in
        print(f"{mictype} signed in: HH{number}")

    def live(self, owner):
        # Set the microphone as live and assign an owner
        self.owner = owner
        # Print a message indicating the microphone is live
        print(f"{self.number} ({self.type}) is live with {owner}")

    def die(self):
        # Mark the microphone as returned and clear the owner
        print(f"{self.number} ({self.type}) returned by {self.owner}")
        self.owner = None  # Reset owner to None

    def __str__(self):
        # Return a string representation of the microphone's status
        if self.owner:
            # If the microphone has an owner, indicate it's live
            return f"{self.number} ({self.type}) live with {self.owner}"
        else:
            # If no owner, indicate it's available
            return f"{self.number} ({self.type}) is available"

    def __repr__(self):
        # Use the same string representation for object representation
        return self.__str__()

# List to store all created microphone objects
mics = []

print("Welcome to the Microphone Management System!")
print("Commands:")
print("- create <number> <type>: Create a new microphone.")
print("- live <number> <owner>: Set a microphone as live.")
print("- die <number>: Mark a microphone as returned.")
print("- exit: Quit the program.")

while True:
    # Get user input from the command line
    inp = input("> ").strip()
    if inp.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break
    
    # Split the input into parts
    parts = inp.split(" ")
    command = parts[0].lower()

    try:
        match command:
            case "create":
                if len(parts) != 3:
                    print("Error: 'create' requires two arguments: <number> <type>")
                    continue

                number = parts[1]
                mictype = parts[2]

                if not number.isdigit():
                    print("Error: Microphone number must be a numeric value.")
                    continue

                # Create a new Microphone and add it to the list
                mics.append(Microphone(number, mictype))
                print(f"Microphone {number} of type '{mictype}' created successfully.")

            case "live":
                if len(parts) != 3:
                    print("Error: 'live' requires two arguments: <number> <owner>")
                    continue

                mic_index = int(parts[1]) - 1
                owner = parts[2]

                if mic_index < 0 or mic_index >= len(mics):
                    print(f"Error: Microphone {parts[1]} does not exist.")
                    continue

                mic = mics[mic_index]
                mic.live(owner)
                print(f"Microphone {mic.number} is now live with {owner}.")

            case "die":
                if len(parts) != 2:
                    print("Error: 'die' requires one argument: <number>")
                    continue

                mic_index = int(parts[1]) - 1

                if mic_index < 0 or mic_index >= len(mics):
                    print(f"Error: Microphone {parts[1]} does not exist.")
                    continue

                mic = mics[mic_index]
                mic.die()
                print(f"Microphone {mic.number} has been returned.")

            case _:
                print("Error: Unknown command. Please use 'create', 'live', 'die', or 'exit'.")
                continue

        # Print the status of all microphones in the list
        print("\nCurrent Microphones:")
        print("\n".join([str(mic) for mic in mics]))

    except ValueError:
        print("Error: Invalid input. Please try again.")
    except Exception as e:
        print(f"Unexpected error: {e}")
