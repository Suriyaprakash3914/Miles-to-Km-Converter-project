logo = '''
     $$$$         $$$$
   $$$$$$$$     $$$$$$$$
 $$$$$$$$$$$$ $$$$$$$$$$$$                     
$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$
        ┈╱▔▔▔▔▔▔▔▔╲┈┈┈┈ 
        ╱▔▔▔▔▔▔▔▔╲╱┈┈┈┈
        ▏┳╱╭╮┓┏┏┓▕╱▔▔╲┈
        ▏┃╱┃┃┃┃┣▏▕▔▔╲╱▏
        ▏┻┛╰╯╰╯┗┛▕▕▉▕╱╲
        ▇▇▇▇▇▇▇▇▇▇▔▔▔╲▕
        ▇▇╱▔╲▇▇▇▇▇╱▔╲▕╱
        ┈┈╲▂╱┈┈┈┈┈╲▂╱▔┈
 $$$$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$
          $$$$$$$
            $$$
             $
'''
user_password = {'suriya': 'mahi@2321', 'jayashri': 'mahi@2002'}
user_pin = {'suriya': 1425, 'jayashri': 2024}
user_amt = {'suriya': 590, 'jayashri': 245}
print('\t\t\t\t\t\tWELCOME TO MAHI LOVE BANK')
u_i = input('enter login/signup: ').lower()
print(logo)
if u_i == 'login':
    user_name = input('Enter your user_name:')
    if user_name in user_password:
        password = input('Enter your password: ')
        if password == user_password[user_name]:
            print('1.deposit\n2.withdraw\n3.balance check')
            operation = input('Enter the operation to perform: ').lower()
            if operation == 'deposit':
                u_pin = int(input('Enter the pin: '))
                if u_pin == user_pin[user_name]:
                    amt = int(input('Enter the amount: '))
                    user_amt[user_name] += amt
                    print(f'Amount Credited Successfully Available Balance is {user_amt[user_name]}')
                else:
                    print('Invalid pin')
            elif operation == 'withdraw':
                u_pin = int(input('Enter the pin: '))
                if u_pin == user_pin[user_name]:
                    amt = int(input('Enter the amount: '))
                    if amt <= user_amt[user_name]:
                        user_amt[user_name] -= amt
                        print(f'Amount Debited Successfully Available Balance is {user_amt[user_name]}')
                    else:
                        print('insufficient balance...')
            elif operation == 'balance check':
                u_pin = int(input('Enter the pin: '))
                if u_pin == user_pin[user_name]:
                    print(f'Available Balance is {user_amt[user_name]}')
