class Microphone:
    def __init__(self, number, mictype):
        self.number = number
        self.owner = None
        self.type = mictype

        print(f"{mictype} signed in: HH{number}")

    def live(self, owner):
        self.owner = owner
        print(f"{self.number} ({self.type}) is live with {owner}")

    def die(self):
        print(f"{self.number} ({self.type}) returned by {self.owner}")
        self.owner = None

    def __str__(self):
        if self.owner:
            return f"{self.number} ({self.type}) live with {self.owner}"
        else:
            return f"{self.number} ({self.type}) is available"

    def __repr__(self):
        return self.__str__()

mics = []
    
while True:
    inp = input(">")
    match inp.split(" ")[0]:
        case "create":
            mics.append(Microphone(inp.split(" ")[1], inp.split(" ")[2]))
        case "live":
            mic = mics[int(inp.split(" ")[1])-1]
            mic.live(inp.split(" ")[2])
        case "die":
            mic = mics[int(inp.split(" ")[1])-1]
            mic.die()
        
    print("\n".join([str(mic) for mic in mics]))
