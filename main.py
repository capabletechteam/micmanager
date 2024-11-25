class Microphone:
    def __init__(self, number):
        self.number = number
        self.owner = None

        print(f"Microphone signed in: HH{number}")

    def live(self, owner):
        self.owner = owner
        print(f"Microphone {self.number} is live with {owner}")

    def die(self):
        print(f"Microphone {self.number} returned by {self.owner}")
        self.owner = None

    def __str__(self):
        if self.owner:
            return f"Microphone {self.number} live with {self.owner}"
        else:
            return f"Microphone {self.number} is available"

    def __repr__(self):
        return self.__str__()

mics = []
    
while True:
    inp = input(">")
    match inp.split(" ")[0]:
        case "create":
            mics.append(Microphone(inp.split(" ")[1]))
        case "live":
            mic = mics[int(inp.split(" ")[1])-1]
            mic.live(inp.split(" ")[2])
        case "die":
            mic = mics[int(inp.split(" ")[1])-1]
            mic.die()
        
    print("\n".join([str(mic) for mic in mics]))
