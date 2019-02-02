def vlag(richting, kleuren):
    uitkomst = ''
    if richting == 'verticaal':

        for i in range(0, len(kleuren)):
           if i == len(kleuren) - 1:
               uitkomst += kleuren[i]
           else:
               uitkomst += kleuren[i] + ' | '

    elif richting == 'horizontaal':

        for i in range(0, len(kleuren)):
           if i == len(kleuren) - 1:
                uitkomst += kleuren[i]

           else:
                uitkomst += kleuren[i] + '\n' + '-' + '\n'
    return uitkomst
print(vlag('horizontaal', ('zwart', 'geel', 'rood')))
print(vlag('verticaal', ('zwart', 'geel', 'rood')))