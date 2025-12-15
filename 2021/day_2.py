class Password:
    def __init__(self, line):
        info = line.split(' ')
        limits = info[0].split('-')
        self.min = int(limits[0])
        self.max = int(limits[1])
        self.character = info[1][0]
        self.password = info[2]

    def __str__(self):
        return f'''
min: {self.min}
max: {self.max}
char: {self.character}
password: {self.password}
        '''
def countValidPasswords(passwords):
    result = 0
    for password in passwords:
        char_count = 0
        for char in password.password:
            if char == password.character:
                char_count += 1
        if char_count <= password.max \
            and char_count >= password.min:
            result += 1
    return result

def countValidPasswordsPart2(passwords):
    result = 0
    for password in passwords:
        try:
            first_check = password.password[password.min - 1] == password.character 
            second_check = password.password[password.max - 1] == password.character 
            if first_check ^ second_check:
                result += 1
        except IndexError:
            print('first', first_check)
            print('second', second_check)
            print(password)
    return result

if __name__ == '__main__':
    with open('2_input.txt') as f:
        lines = f.readlines()
        passwords = list(map(Password, lines))
        print(countValidPasswords(passwords))

        print(countValidPasswordsPart2(passwords))
