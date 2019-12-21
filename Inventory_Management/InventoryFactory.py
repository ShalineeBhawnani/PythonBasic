import json
class Command:
    def execute(self): pass

class Rice(Command):
    def execute(self):
        print("You're a loony.")
    
class Pulses(Command):
    def execute(self):
        print("You might even need a new brain.")

class Wheats(Command):
    def execute(self):
        print("I couldn't Wheats a whole new brain.")

def factory_method(product_type):
    if product_type == 'Rice':
        return Rice()
    elif product_type == 'Pulses':
        return Pulses()
    elif product_type == 'Wheats':
        return Wheats()
    else:
        raise ValueError(format(product_type))
def main():
    for product_type in ('Rice', 'Pulses','Wheats'):
        product = factory_method(product_type)
        print(str(product))
        
if __name__ == '__main__':
    main()