started = False
while True:
    status = input('>').lower()
    if status=='start':
        if started:
            print('Car is already started!!')
        else:
            started=True
            print('Car started')
    elif status=='stop':
        if not started:
            print('Car is not started so cannot be stopped')
        else:
            print('Car stopped')
            started=False
    elif status=='help':
        print('''start -> car has started
stop -> car has stopped
quit ->  get out of the programe''')
    elif status=='quit':
        break
    else:
        print('Dont understand command')

    
