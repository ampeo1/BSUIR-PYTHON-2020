import tempfile
import random
import sys
import os


class Sort:
    def __init__(self, amount, RAM, name_file):
        self.amount = amount
        self.RAM = RAM
        self.name_file = name_file

    def fill_file(self):
        with open(self.name_file, 'w') as f:
            f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(self.amount))

    def split(self):
        arr = []
        files_name = [tempfile.NamedTemporaryFile()]
        with open(self.name_file, 'r') as f:
            for line in f:
                arr.append(line)
                # 0,5 Gb если массив весит больше, то создаём новый файлик
                with open(str(files_name[-1:]), 'a') as file:
                    file.writelines(line)
                if sys.getsizeof(arr) > self.RAM:
                    arr.clear()
                    files_name.append(tempfile.NamedTemporaryFile())
        return files_name

    def sort_files(self, files):
        arr = []
        for index in range(0, len(files)):
            with open(str([files[index]]), 'r') as file:
                for line in file:
                    arr.append(line)
            arr = list(map(int, arr))
            arr.sort()
            with open(str([files[index]]), 'w') as file:
                for arg in arr:
                    file.write(str(arg) + '\n')
            arr.clear()

    def add_elem(self, file_name):
        with open(str([file_name]), 'r') as file:
            elem = file.readline()
            temp = file.readlines()
        with open(str([file_name]), 'w') as file:
            for arg in temp:
                file.write(str(arg))
        return elem

    def check_file(self, file_name):
        with open(str([file_name]), 'r') as file:
            if file.read() == '':
                return 0
            else:
                return 1

    def sort_all(self, files):
        os.remove('Answer')
        arr = []
        for index in range(0, len(files)):
            arr.append(self.add_elem(files[index]))
        for _ in range(0, self.amount):
            arr = list(map(int, arr))
            index_min, min = 0, arr[0]
            for index in range(0, len(arr)):
                if min > arr[index]:
                    min, index_min = arr[index], index
            with open('Answer', 'a') as file:
                file.write(str(min) + '\n')
            arr.pop(index_min)
            if self.check_file(files[index_min]) == 1:
                arr.insert(index_min, self.add_elem(files[index_min]))
            else:
                os.remove(str([files[index_min]]))
                files.pop(index_min)
            if files == []:
                return

    def begin(self):
        self.fill_file()
        files_name = self.split()
        self.sort_files(files_name)
        self.sort_all(files_name)


name_file = 'numbers.txt'
RAM = 1000
amount = 1000

sort = Sort(amount, RAM, name_file)
sort.begin()
