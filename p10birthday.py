with open('pi.txt') as file_object:
    lines = file_object.readlines()
pi_digits = ''
answer = ''
for line in lines:
    pi_digits += line.strip()
answer = input('Хотите проверить вашу дату рождения? ')
pi_digits = pi_digits[2:]
answer = answer.strip().title()
while True:
    i = 1
    k = 1
    if answer == 'Да':
        birthday = input('Введите дату рождения, в формате ДДММГГ: ')
        birthday = birthday.strip()
        print('Вы ввели: ' + birthday)
        try:
            int(birthday) == int(birthday)
        except ValueError:
            print('Вы ввели не число!')
        else:
            if len(birthday) != 6 or int(birthday) < 0:
                print('Ваша дата не соответсвует формату ДДММГГ!')
                continue
            else:
                if birthday in pi_digits:
                    print('Дата вашего рождения есть в числе pi.')
                    print('Вычисляем место...')
                    print('...')
                    while True:
                        if birthday not in pi_digits[(i - 1) * 100:(i + 1) * 100]:
                            i += 1
                            continue
                        else:
                            while True:
                                if birthday not in pi_digits[(i - 1) * 100:((i - 1) * 100) + k]:
                                    k += 1
                                    continue
                                break
                        break
                    j = (int(i - 1) * 100) + (int(k) - 6)
                    print('Дата вашего рождения в числе pi находится на '
                          + str(j) + ' месте, после запятой.')
                    print('3.141...' + pi_digits[j - 6:j + 12] + '...')
                    answer = input('Проверить еще дату? ')
                    answer = answer.title().strip()
                else:
                    print('Даты вашего рождения нет в числе pi.')
                    answer = input('Проверить еще дату? ')
                    answer = answer.title().strip()
    elif answer == 'Нет':
        break
    else:
        answer = input("Введите 'да'/'нет' ")
        answer = answer.title().strip()
print('Спасибо за использование программы.')