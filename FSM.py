class FSM:
    
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, handler, end_state=0):
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name

    def run(self, cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            print("no")
    
        while True:
            (newState, cargo) = handler(cargo)
            if newState in self.endStates:
                print("reached ", newState)
                break 
            else:
                handler = self.handlers[newState]    

unlock_code = ["eight"]

# 1 4 7 2 5 8 

def start_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word == "one":
        newState = "one_state"
    else:
        newState = "error_state"
    return (newState, txt)

def hashtag_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word == "#":
        newState = "Start"
    return (newState, txt)

def zero_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word == "zero":
        newState = "error_state"
    return (newState, txt)

def one_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word == "four":
        newState = "four_state"
    else:
        newState = "error_state"
    return (newState, txt)

def two_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word == "five":
        newState = "five_state"
    else:
        newState = "error_state"
    return (newState, txt)

def three_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word == "three":
        newState = "error_state"
    return (newState, txt)
  
def four_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word == "seven":
        newState = "seven_state"
    else:
        newState = "error_state"
    return (newState, txt)

def five_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word in unlock_code:
        newState = "unlocked_state"
    else:
        newState = "error_state"
    return (newState, txt)

def six_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word == "six":
        newState = "error_state"
    return (newState, txt)

def seven_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word == "two":
        newState = "two_state"
    else:
        newState = "error_state"
    return (newState, txt)


def nine_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word == "nine":
        newState = "error_state"
    return (newState, txt)

## 1 4 7 2 5 8

m = FSM()
m.add_state("Start", start_transitions)
m.add_state("one_state", one_state_transitions)
m.add_state("four_state", four_state_transitions)
m.add_state("seven_state", seven_state_transitions)
m.add_state("two_state", two_state_transitions)
m.add_state("five_state", five_state_transitions)
m.add_state("unlocked_state", None, end_state=1)
m.add_state("three_state", three_state_transitions)
m.add_state("six_state", six_state_transitions)
m.add_state("nine_state", nine_state_transitions)
m.add_state("error_state", None, end_state=1)
m.set_start("Start")
m.run("one four seven two five eight");
#m.run("one four nine # one four seven two five eight")

