class ConnectedThings():
    def hello_word(self):
        return "hello_world"

connected_things = ConnectedThings()
        
def hello_word(**kwargs):
    res = connected_things.hello_word(**kwargs)
    return res