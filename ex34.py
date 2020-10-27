
# 1. дефиниция
def show(title, n=1, *args, width, height=300, **kwargs):
    print(f'positional :title={title}')
    print(f'positional default:n={n}')
    
    print(f'keyword only: width = {width}, height = {height}')


if __name__ == '__main__':
#    2. извикване
    show('Text Editor', width=600, path='./')
    show('Text Editor', 1,*(11, 22, 33), width=1200, height=400, path='./')
    