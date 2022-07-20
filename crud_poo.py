import os

def clearConsole():
    os.system('cls')

class Student:
    users = []
        
    def createUser(self, cc, name, age, ocupation):
        user = {
            'cc': cc,
            'name': name,
            'age': age,
            'ocupation': ocupation,
        }
        
        self.users.append(user)
    
    def showUsers(self):
        for user in range(len(self.users)):
            print(f'cc: {self.users[user]["cc"]}\nNombre: {self.users[user]["name"]}\nEdad: {self.users[user]["age"]}\nOcupacion: {self.users[user]["ocupation"]}\n')
    
    def deleteUser(self, cc):
        no_exist = True;
        
        for user in range(len(self.users)):
            if(self.users[user]['cc'] == cc):
                delUser = self.users.pop(user)
                no_exist = False
                print('Usuario eliminado => ')
                input(delUser)

        if(no_exist):
            print(f'El usuario con la cedula {cc} no existe')
            input(' ')

def validation(phrase, typeVal):
    if(typeVal == 1):
        while True:
            var = int(input(phrase))
            if(var):
                return var
    elif(typeVal == 2):
        while True:
            var = (input(phrase))
            if(var):
                return var

def creatingUser(nameClass):
    cc = validation('Ingrese la cedula => ', 1)
    name = validation('Ingrese el nombre => ', 2)
    age = validation('Ingrese la edad => ', 1)
    ocupation = validation('Ingrese la ocupacion => ', 2)

    nameClass.createUser(cc, name, age, ocupation)
    
    clearConsole()

def showingUsers(nameClass):
    nameClass.showUsers()
    input('Estos son todos los usuarios')
    clearConsole()

def deletingUser(nameClass):
    cc = validation('Ingresa la cedula del usuario a eliminar => ', 1)
    nameClass.deleteUser(cc)
    clearConsole()

def menu():
    try:
        print('Estas en el menu, que quieres hacer?')
        print('1. registar usuario')
        print('2. mostrar usuarios')
        print('3. eliminar usuario')
        print('4. salir\n')
        
        while True:
            op = int(input('=> '))
            if(op):
                return op
            
    except :
        print('Ingresa un opcion valida')

def main():
    school = Student()
    while True:
        op = menu()
        if(op == 1):
            creatingUser(school)
        elif(op == 2):
            showingUsers(school)
        elif(op == 3):
            deletingUser(school)
        elif(op == 4):
            break

main()



