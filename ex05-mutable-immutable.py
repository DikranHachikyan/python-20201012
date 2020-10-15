# %%
age = 35
id(age)

# %%
x = 35
id(x)
# %%
age = 25
id(age)
# %%
class Point:
    def __init__(self, x):
        self.x = x

# %%
p1 = Point(x = 10)
# %%
id(p1)
# %%
p2 = Point(x = 10)
id(p2)
# %%
id(p1.x)
# %%
id(p2.x)
# %%
s1 = 'python'
s2 = 'python'
# %%
id(s1) == id(s2)
# %%
s3 = 'hello ' * 3
# %%
s1 = 'python' * 10_000
s2 = 'python' * 10_000
id(s1) == id(s2)
# %%
