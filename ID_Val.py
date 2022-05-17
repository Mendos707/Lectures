

def start_body():
    global user_input
    user_input = None
    while True:
        if not user_input:
            while True:
                user_input = input('Enter id:')
                try:
                    int(user_input)
                    if len(user_input) != 11:
                        raise UserWarning
                except ValueError   :
                    print('Code is not numeric')
                except UserWarning:
                    if len(user_input) > 11:
                        print('Code is too long')
                    else:
                        print('Code is too short')
                else:
                    print(user_input)
                    main_body()
                    return user_input
                    break
def main_body():
    while True:
        user_choice = input('Please choose:\n'
                            '1.Get gender\n'
                            '2.Get date of birth\n'
                            '3.Get region of bith\n'
                            '4.Validate ID\n'
                            '5.Change ID\n'
                            '0.Exit\n'
                            '--> ')
        if user_choice == '1':
            split_num = [int(a) for a in user_input]
            if split_num[0] == 1:
                gender = 'Male 1800 — 1899 year of birth'
                century = 18
            elif split_num[0] == 2:
                gender = 'Female 1800 — 1899 year of birth'
                century = 18
            elif split_num[0] == 3:
                gender = 'Male 1900 — 1999 year of birth'
                century = 19
            elif split_num[0] == 4:
                gender = 'Female 1900 — 1999 year of birth'
                century = 19
            elif split_num[0] == 5:
                gender = 'Male 2000 — 2099 year of birth'
                century = 20
            elif split_num[0] == 6:
                gender = 'Female 2000 — 2099 year of birth'
                century = 20
            elif split_num[0] == 7:
                gender = 'Male 2100 — 2199 year of birth'
                century = 21
            elif split_num[0] == 8:
                gender = 'Female 2100 — 2199 year of birth'
                century = 21
            print(f'Your gender and century: {gender}')


        elif user_choice == '2':
            if user_input[0] == '3' or user_input[0] == '4':
                x = '19'
            elif user_input[0] == '5' or user_input[0] == '6':
                x = '20'
            print(f'Date of birth: {user_input[5]}{user_input[6]}.{user_input[3]}{user_input[4]}.{x}{user_input[1]}{user_input[2]}')
        elif user_choice == '3':
            if int(user_input[7:10]) in range(1,11):
                hospital = 'Kuressaare haigla'
            elif int(user_input[7:10]) in range(11,20):
                hospital = 'Tartu Ülikooli Naistekliinik'
            elif int(user_input[7:10]) in range(21,151):
                hospital = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
            elif int(user_input[7:10]) in range(151,161):
                hospital = 'Keila haigla'
            elif int(user_input[7:10]) in range(161,221):
                hospital = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
            elif int(user_input[7:10]) in range(221,271):
                hospital = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
            elif int(user_input[7:10]) in range(271,370):
                hospital = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
            elif int(user_input[7:10]) in range(371,421):
                hospital = 'Narva haigla'
            elif int(user_input[7:10]) in range(421,471):
                hospital = 'Pärnu haigla'
            elif int(user_input[7:10]) in range(471,491):
                hospital = 'Haapsalu haigla'
            elif int(user_input[7:10]) in range(491,521):
                hospital = 'Järvamaa haigla (Paide)'
            elif int(user_input[7:10]) in range(521,571):
                hospital = 'Rakvere haigla, Tapa haigla'
            elif int(user_input[7:10]) in range(571,600):
                hospital = 'Valga haigla'
            elif int(user_input[7:10]) in range(601,651):
                hospital = 'Viljandi haigla'
            elif int(user_input[7:10]) in range(651,701):
                hospital = 'Lõuna-Eesti haigla (Võru), Põlva haigla'

            print(f'Maternity hospital: {hospital}')
        elif user_choice == '4':
            control1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
            control2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
            point = 0
            point2 = 0
            control_code = 0
            control_code2 = 0
            for i in control1:
                control_code += i * int(user_input[point])
                point += 1
            control_code %= 11
            if control_code < 10:
                print(f'Check digit: {control_code % 11}')
            elif control_code >= 10:
                for h in control2:
                    control_code2 += h * int(user_input[point2])
                    point2 += 1
                control_code2 %= 11
                if control_code2 < 10:
                    print(f'Check digit: {control_code2 % 11}')
                elif control_code2 >= 10:
                    print('Check digit: 0')

        elif user_choice == '5':
            print('You can enter your ID again!')
            start_body()
        elif user_choice == '0':
            exit()
        else:
            print('Choice is out of range')

user_input = None
start_body()