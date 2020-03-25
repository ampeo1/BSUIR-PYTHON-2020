def cached(func):
    data = {}

    def wrapper(self):
        if data != {}:
            for key, value in data.items():
                if key == self.__str__():
                    return value
        data[self.__str__()] = func(self)
        return data.get(self.__str__())

    return wrapper


class Vector:
    def __init__(self, vector):
        self.vector = list(vector)

    def __iter__(self):
        # return self.iteration ??
        self.iteration = 0
        return self

    def __next__(self):
        if self.iteration < self.__len__():
            self.iteration += 1
            return self.iteration - 1
        else:
            raise StopIteration

    def __len__(self):
        return len(self.vector)

    def __getitem__(self, item):
        return self.vector[item]

    def sum(self, vec2):
        if len(self.vector) != len(vec2):
            print("Bad input!")
            return
        for index in range(0, len(self.vector)):
            self.vector[index] += vec2[index]
        return self.__str__()

    def sub(self, vec2):
        if len(self.vector) != len(vec2):
            print("Bad input!")
            return
        for index in range(0, len(self.vector)):
            self.vector[index] -= vec2[index]
        return self.__str__()

    def mul_const(self, const):
        for index in range(0, len(self.vector)):
            self.vector[index] *= const
        return self.__str__()

    def mul_scal(self, vec2):
        if len(self.vector) != len(vec2):
            print("Bad input!")
            return
        result = 0
        for index in range(0, len(self.vector)):
            result += vec2[index] * self.vector[index]
        return result

    def compare(self, vec2):
        if len(self.vector) != len(vec2):
            print("Bad input!")
            return
        for index in range(0, len(self.vector)):
            if self.vector[index] != vec2[index]:
                return False
        return True


    @cached
    def len(self):
        result = 0
        for arg in self.vector:
            result += arg ** 2
        return result ** (1 / 2)

    def __str__(self):
        string = ""
        for arg in self.vector:
            string += str(arg) + ", "
        return string[:-2]
