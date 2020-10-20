def main():
    users = ['anna','maria','markus','john', 'me']
    mails = ['anna@no.com','maria@no.com','markus@no.com','john@no.com']

    for data in zip(users, mails):
        name, mail = data
        print(f'<a href="mailto:{mail}">{name}</a>')

main()