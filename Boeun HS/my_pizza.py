# my_pizza.py

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    
    print(f"\nMaking a {size}cm pizza with: ")
    
    for t in toppings:
        if t.lower() == 'myulchi' or t.lower() == 'pineapple' or t.lower() == 'gochu':
            print(f"- NO {t}!")
        else:
            print(f"- {t}")

make_pizza(12, "pepperoni", "cheese")
make_pizza(12, "pepperoni", "cheese", "GOGUMA", "pineapple", "pickles", "mushrooms", "tomatoes", "ham", "sausage", "chicken", "gochu", "myulchi")