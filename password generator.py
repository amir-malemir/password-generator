import random
import string
import os
setting = {
    'lower': True,
    'upper': True,
    'symbol': True,
    'number': True,
    'space': False,
    'length': 10
}
MIN_PASSWORD_LENGTH = 4
MAX_PASSWORD_LENGTH = 30
def clear_screen():
    os.system('cls')
    
def get_user_password_length(option, default,min_pass = MIN_PASSWORD_LENGTH,max_pass = MAX_PASSWORD_LENGTH):
    while True:
        user_input = input(f'enter password length. (default is {default}. enter: default) :')
        if user_input == '':
            return default
        if user_input.isdigit():
            user_password_length = int(user_input)
            if min_pass <= user_password_length <= max_pass:
                return int(user_input)
            print('invalid input')
            print(f'password length should be between {min_pass} and {max_pass}')
        else:
            print('plz neter number')
        print('try again')

def get_yes_or_no_for_setting(option,default):
    while True:
        user_input = input(f'include {option}? , defaults is {default}, (y:yes,n:no): ')
        if user_input == '':
            return default
        if user_input in ['y','n']:
            return user_input == 'y'
        print('invalid input, plz try again')
    
def get_setting_from_user(setting):
    for option, default in setting.items():
        if option != 'length':
            user_choice = get_yes_or_no_for_setting(option,default)
            setting[option] = user_choice
        else:
            user_password_length = get_user_password_length(option,default)
            setting[option] = user_password_length
            
def ask_if_change_settings(setting):
        while True:
            ask_user_for_setting = input(' do ypu want to change settings? (y: yes, n: no, enter: yes): ')
            if ask_user_for_setting in ['y','n','']:
                if ask_user_for_setting in ['y','']:
                    print('-'*5, 'change settings' , '-'*5)
                    get_setting_from_user(setting)
                break
            else:
                print('invalid input. (choose from: y: yes, n: no, enter: yes).')
                print('please try again.')

        
def get_random_lower_case():
    return random.choice(string.ascii_lowercase)

def get_random_upper_case():
    return random.choice(string.ascii_uppercase)

def get_random_symbol_case():
    return random.choice("""~`!@#$%^&*()_-+={[}]|:;"'<,>.?/""")

def get_random_number():
    return random.choice('0123456789')
            
def generate_random_char(choices):
    choice = random.choice(choices)

    if choice == 'lower':
        return get_random_lower_case()
    if choice == 'upper':
        return get_random_upper_case()
    if choice == 'symbol':
        return get_random_symbol_case()
    if choice == 'number':
        return get_random_number()
    if choice == 'space':
        return ' '
    
def ask_user_to_generate_another_password():
    while True:
            wants_another_password = input(' Regenerate? (y: yes, n: no, enter: yes): ')
            if wants_another_password in ['y','n','']:
                if wants_another_password == 'n':
                    return False
                return True
            else:
                print('invalid input. (choose from: y: yes, n: no, enter: yes).')
                print('please try again.')
    
def password_generation(setting):
    final_password = ''
    password_length = setting['length']
    choices = list(filter(lambda x: setting[x], ['lower','upper','symbol','space','number'])) 
    for i in range(password_length):
        final_password += generate_random_char(choices)
    return final_password

def password_generation_loop(setting):
    while True:
        print('-'*20)
        print(f'Generated password: {password_generation(setting)}')
        print('-'*20)
        if ask_user_to_generate_another_password() == False:
            print('thanks for choosing us. :)')
            break

def run():
    clear_screen()
    ask_if_change_settings(setting)
    password_generation_loop(setting)
run()