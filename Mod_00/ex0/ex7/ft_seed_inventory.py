def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    ending = ''
    if unit == 'packets': 
        ending = f'{quantity} {unit} available'
    if unit == 'grams': 
        ending = f'{quantity} {unit} total'
    if unit == 'area': 
        ending = f'covers {quantity} square meters'
    print(f'{seed_type.capitalize()} seeds: {ending}')
    
    
ft_seed_inventory('tomato', 15, 'packets')
ft_seed_inventory('carrot', 8, 'grams')
ft_seed_inventory('lettuce', 12, 'area')