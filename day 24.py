# Definisi kelas pertama (superclass)
class A:
    def __init__(self, a):
        self.a = a

    def methodA(self):
        return f'Method dari kelas A dengan nilai a = {self.a}'

# Definisi kelas kedua (superclass)
class B:
    def __init__(self, b):
        self.b = b

    def methodB(self):
        return f'Method dari kelas B dengan nilai b = {self.b}'

# Definisi kelas turunan (subclass) yang mewarisi kelas A dan B
class C(A, B):
    def __init__(self, a, b, c):
        super().__init__(a)  # Memanggil konstruktor kelas A
        B.__init__(self, b)  # Memanggil konstruktor kelas B
        self.c = c

    def methodC(self):
        return f'Method dari kelas C dengan nilai c = {self.c}'

# Contoh penggunaan kelas-kelas yang sudah didefinisikan
if __name__ == "__main__":
    obj = C(10, 20, 30)

    print(obj.methodA())  # Output: Method dari kelas A dengan nilai a = 10
    print(obj.methodB())  # Output: Method dari kelas B dengan nilai b = 20
    print(obj.methodC())  # Output: Method dari kelas C dengan nilai c = 30
