from pygame.event import get

button_dict = {i: ord(i) for i in "abcdefghijklmnopqrstuvwxyz"}
button_dict["down"] = 768
button_dict["mouse"] = 1025

def event_get():
    return get()