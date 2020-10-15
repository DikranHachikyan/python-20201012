# %%
dc = dict(port=3306,host='localhost',db='northwind')
# %%
dc['host']
# %%
dc['port']
# %%
user = {
    'fname':'Anna',
    'lname':'Smith',
    'age': 30
}
# %%
user['fname']
# %%
user.keys()
# %%
user.values()
# %%
user.items()
# %%
user['email']
# %%
'email' in user
# %%
'age' in user
# %%
user.get('email', 'no@no.com')
# %%
