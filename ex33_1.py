
# 1. дефиниция
def show(title, n=1, *args, **kwargs):
    print(f'positional :title={title}')
    print(f'positional default:n={n}')

    print('list of args:' + ','.join(map(str, args)))

    print('Keyword Arguments:')
    kw_params = {
        'path': kwargs.get('path', '/tmp'),
        'log' : kwargs.get('log', '/var/log/messages') 
    }

    print(f'{kw_params}')

if __name__ == '__main__':
#    2. извикване
    
    # show('Text Editor')

    # show('Text Editor',11, 22, 33,44)

    # show('Text Editor',11, 22, 33,44, log = '/var/log/editor.log', path = './')
    show('Text Editor', log = '/var/log/editor.log', path = './')

    app_config = {
        'log':'/var/log/editor.log',
        # 'path':'./app',
        'max_mem':4096
    }
    show('Text Editor', 100,9,5,3, **app_config)