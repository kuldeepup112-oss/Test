
print('My New University Welcomes You to SRMU')
print('*' * 60)

print('Hello! Welcome to the BCA Department.')
Us = input('Are you a BCA student? (yes/no): ').lower()

print('*' * 30)

print('B7 Block - Your Room Number is 201')
print('*' * 30)

print('May I come in, Sir/Madam?')
print('*' * 30)

Name_Roll_number = {
    'shiva': 201,
    'sai': 202,
    'kumar': 203,
    'sandeep': 204,
    'suresh': 205,
    'ramesh': 206,
    'rajesh': 207,
    'vijay': 208,
    'ajay': 209,
    'arjun': 210
}

if Us == 'yes':
    print('Please enter your name:')
    user_name = input().strip().lower()

    if user_name in Name_Roll_number:
        print('*' * 30)
        print('Welcome to SRMU!')
        print('Your name is:', user_name.capitalize())
        print('Your roll number is:',
              Name_Roll_number[user_name])
        print('Your room number is: 201')
    else:
        print('Sorry! Your name is not registered.')

else:
    print('Please contact the BCA Department.')

print('*' * 60)
print('Thank you for visiting SRMU!')
