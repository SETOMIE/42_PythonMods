def ft_garden_intro():
    print('=== Welcome to My Garden ===')
    print('Plant: Rose')
    print('Height: 25cm')
    print('Age: 30 days')
    print('')
    print('=== End of Program ===')


if __name__ == '__main__':
    ft_garden_intro()


# ----- NOTES -----

# Python auto sets __name__ to '__main__' when directly running file.
# __name__ makes py. files flexible and reusable

# if file imported -> __name__ will be set to imported file, will not run '__main__'.
# once mod is imported, all code within will be executed (funct, code) without being called.
# importing specific functionality of module does not save resources, will still run whole script but returns functionality.
# [__name__ explanaition](https://www.youtube.com/watch?v=hZ9rsHdcxtY&list=TLPQMDEwNjIwMjZv__TCQx3nLw&index=18)