def main():
    users = ['anna','maria','markus','john', 'me']
    mails = ['anna@no.com','maria@no.com','markus@no.com','john@no.com']
    usr_hash = {}

    for data in zip(users, mails):
        name, mail = data
        usr_hash[name] = mail

    print(usr_hash)

main()