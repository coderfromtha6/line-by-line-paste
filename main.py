import pyperclip, time, keyboard
with open('input.txt') as f:
    lines = f.readlines()

if lines == []:
    print('input.txt is empty. Exiting...')
    exit()
else:
    print('running...')
    for line in lines:
        pyperclip.copy(line)
        keyboard.wait('ctrl+v')
        print('Line Pasted: ' + line)
        time.sleep(0.05)
    print('No more lines to copy. Exiting...')   