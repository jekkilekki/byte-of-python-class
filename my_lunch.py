lunch = {
    'hamburger': ['cheese', 'chicken', 'onion', 'tomato'],
    'gukbap': ['pork', 'sundae', 'organs', 'dubu'],
    'sundae': ['minari', 'goguma', 'kimchi', 'water'],
    'pizza': ['pepperoni', 'shrimp', 'pineapple', 'pizza'],
    'bap': ['egg', 'spam', 'JJBBB', 'kanjang']
}

msg = "Lunch choice: 1. Hamburger, 2. Gukbap, 3. Sundae, 4. Pizza, 5. Bap"
msg += "\nWhat do you want? "
my_lunch = input(msg) # String
my_lunch = int(my_lunch)

if my_lunch == 1:
    print("Mmmmm, hamburger....")
    choice = 'hamburger'
if my_lunch == 2:
    print("Are you drunk?")
    choice = 'gukbap'
if my_lunch == 3:
    print("Are you a vampire?")
    choice = 'sundae'
if my_lunch == 4:
    print("Thick or thin?")
    choice = 'pizza'
if my_lunch == 5:
    print("No money?")
    choice = 'bap'

menu = "Your lunch will have "
for side in lunch[choice]:
    menu += side
    menu += ", "

print(menu)

def hello(name):
    """
    A simple function to print hello to someone.

    Parameters:
        name (string): The person to say hello to.
    """
    print(f"Hello {name}!")

hello()  