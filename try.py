shop = {
    'Products': {
        'Lemon': 0,
        'Orange': 0
    }
}

text = 'Магазин:\n'

for product in shop['Products'].items():
    text += f'    {product[0]}: {product[1]}\n'

print(text)

