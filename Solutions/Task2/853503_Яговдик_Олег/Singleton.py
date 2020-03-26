class Singleton(type):
    state = None

    def __call__(self, *args, **kwargs):
        if self.state == None:
            self.state = super().__call__(*args, **kwargs)
        return self.state


class Universities(metaclass=Singleton):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


univer1 = Universities("ПТУИР")
univer2 = Universities("БГУИР")
univer3 = Universities("БНТУ")

print(univer1)
print(univer2)
print(univer3)
