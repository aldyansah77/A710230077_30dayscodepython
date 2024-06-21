#Definisikan kelas Person
class Person:
    def __init__(self, name, age):
        self.name = name   
        self.age = age      

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

#Fungsi utama untuk menjalankan program
def main():
    person1 = Person("dini", 18)
    person2 = Person("tana", 17)

    print("Person 1:")
    person1.display_info()
    print()

    print("Person 2:")
    person2.display_info()

#Memanggil fungsi main untuk menjalankan program
if __name__ == "__main__":
    main()
