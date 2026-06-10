def ft_count_harvest_recursive(days = None, current = None):
    if days == None:
        days = int(input('Days until harvest: '))
        current = 1
    if current > days: 
        print('Harvest time!')
        return
    print('Day ' + str(current))
    ft_count_harvest_recursive(days, current +1)


# ft_count_harvest_recursive()

# ----- NOTES -----