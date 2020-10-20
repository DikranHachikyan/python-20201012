## %%
def new_file():
    return 'Create a new file'

# new_file()

def open_file():
    return 'Open a file'

def save_file():
    return 'Save'

# def quit_app():
#     print('Quit Application')
#     quit()

## %%
def main():
    actions = {
        'n':new_file,
        'o':open_file,
        's':save_file,
        'q':quit
    }

    ch = input('Command (n-new, o-open, s-save,q-quit ):')

    if ch in actions:
        result = actions[ch]()
        print(f'action:{result}')
    else:
        print(f'Unknown command:{ch}')

main()