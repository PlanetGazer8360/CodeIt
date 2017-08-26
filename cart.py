from string import Template

class MyTemplate(Template):
    delimiter = '#'

def main():
    cart = []
    cart.append(dict(item="Coke", price = 8, qty= 2))
    cart.append(dict(item="Cake", price=3, qty=1))
    cart.append(dict(item="Juice", price=5,qty=4))
    t = MyTemplate("#item x #qty = #price")
    total = 0
    print("Cart:")
    for data in cart:
        print(t.substitute(data))
        total += data["price"]
        print("Total: " + str(total))

main()