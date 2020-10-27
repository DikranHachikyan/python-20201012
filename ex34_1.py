
# 1. дефиниция
def show(title, *, width, height=300):
    print(f'positional :title={title}')
    
    print(f'keyword only: width = {width}, height = {height}')


if __name__ == '__main__':
#    2. извикване
    show('Text Editor', width=600)
    show('Text Editor', width=1200, height=400)
    