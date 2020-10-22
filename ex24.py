
if __name__ == '__main__':
    
    usr_hash = {
        'anna': 'anna@no.com', 
        'maria': 'maria@no.com',
        'markus': 'markus@no.com', 
        'john': 'john@no.com'
    }

    for data in usr_hash.items():
        name, mail = data
        print(f'name = {name} mail = {mail}')
        
