

# function which reads data from text file which contains detail of store
def store_details():
    laptops = {}
    with open('main.txt', 'r') as file:
        for line in file:
            name, brand, price, quantity, processor, graphics = line.strip().split(', ')
            laptops[name.upper()] = {'brand': brand, 'price': float(price.strip('$')), 'quantity': int(quantity), 'processor': processor, 'graphics': graphics}
            # print(line)
    return laptops