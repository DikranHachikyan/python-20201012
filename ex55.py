
class DictionaryKeyError(Exception):
    pass

def find_key(key, **kwargs):
    if key in kwargs:
        print(f'{key}=>{kwargs[key]}')
    else:
        raise DictionaryKeyError(f'Key {key} not found')

if __name__ == '__main__':
    conn = {
        'host':'lcalhost',
        'port': 3306,
        'service':'mysql'
    }

    try:
        find_key('ip',**conn)
        find_key('host',**conn)
    except DictionaryKeyError as e:
        print(e)