def badge_maker(name):
    return "Hello, my name is " + name + "."

def batch_badge_creator(names):
    return [(f"Hello, my name is {name}.") for name in names]

def assign_rooms(names):
    msgs = []
    num = 1
    for name in names:
        msg = f"Hello, {name}! You'll be assigned to room {num}!"
        msgs.append(msg)
        num += 1
        
    return msgs
        

def printer(names):
    batchs = batch_badge_creator(names)
    for batch in batchs:
        print(batch)
    rooms = assign_rooms(names)
    for room in rooms:
        print(room)
