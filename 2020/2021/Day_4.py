from collections import Counter
import re


class Passport:
    
    valid_eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    hair_color_regex = re.compile('^#+[0-9a-f]{6}$')
    passport_id_regex = re.compile('^[0-9]{9}$')

    def is_valid_birth_date(birthday):
        return int(birthday) >= 1920 and int(birthday) <= 2002

    def is_valid_passport_id(passport_id):
        return Passport.passport_id_regex.match(passport_id) is not None

    def is_valid_hair_color(hair_color):
        return Passport.hair_color_regex.match(hair_color) is not None

    def is_valid_issue_date(issue_date):
        return int(issue_date) >= 2010 and \
        int(issue_date) <= 2020 

    def is_valid_expiration_date(expiration_date):
        return int(expiration_date) >= 2020 and \
        int(expiration_date) <= 2030

    def is_valid_height(height):
        try:
            metric = height[-2:]
            if metric == 'cm':
                height_in_cm = int(height[0:-2])
                return height_in_cm >= 150 and height_in_cm <= 193
            elif metric == 'in':
                height_in_inches = int(height[0:-2])
                return height_in_inches >= 59 and height_in_inches <= 76
            else:
                return False
        except:
            return False

    def is_valid_eye_color(color):
        return color in Passport.valid_eye_colors
    
    validity_map = {
        'byr': is_valid_birth_date,
        'iyr': is_valid_issue_date,
        'eyr': is_valid_expiration_date,
        'hgt': is_valid_height,
        'ecl': is_valid_eye_color,
        'hcl': is_valid_hair_color,
        'pid': is_valid_passport_id,
    }

    def __init__(self):
        self.attributes = {}

    def add_attributes(self, attributes):
        for attribute in attributes:
            key, value = attribute.split(':')
            self.attributes[key] = value
    
    def get_validity(self):
        try:
            for attribute, validity_check in Passport.validity_map.items():
                if not validity_check(self.attributes[attribute]):
                    return attribute
            return True

        except KeyError as e:
            return False

def parse_passports(lines):
    passports = []
    
    start = 0
    end = 1
    # find end
    while end < len(lines):
        while end < len(lines):
            if lines[end] == '\n':
               break;
            end += 1

        passport = Passport()
        for i in range(start, end):
            attributes_to_add = lines[i].rstrip('\n').split(' ')
            passport.add_attributes(attributes_to_add)

        passports.append(passport)
        end += 1
        start = end
    return passports

def count_valid_passports(passports):
    valid_passport_count = 0
    invalidity_reason_map = Counter()
    total = 0
    for passport in passports:
        total += 1
        reason = passport.get_validity()

        if isinstance(reason, str):
            invalidity_reason_map[reason] += 1
        elif reason:
            valid_passport_count += 1
        else:
            pass
    return valid_passport_count

def test():
    print('Start testing height')
    assert Passport.is_valid_height('60in'), 'hgt should be valid'
    assert Passport.is_valid_height('190cm'), 'hgt should be valid'
    assert not Passport.is_valid_height('190in'), 'hgt should be valid'
    assert not Passport.is_valid_height('190'), 'hgt should be valid'
    print('End testing height')

if __name__ == '__main__':
    test()
    with open(
        'Day_4_input.txt', 
        mode='r', 
        encoding='utf8', 
    ) as f:
        lines = f.readlines()
        passports = parse_passports(lines)
        print('Look at me i did it', count_valid_passports(passports))

