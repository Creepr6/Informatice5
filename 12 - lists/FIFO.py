
invoer = input('invoer: ')
lijst = []

while invoer != 'STOP':

    if invoer != '?':
        lijst.append(invoer)

    elif len(lijst) > 0:
        print(lijst.pop(0))

    invoer = input('invoer')