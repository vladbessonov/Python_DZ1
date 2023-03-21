'''
Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.
'''
NumberTicket = int(input('введите номер билета: '))
list_1=[]
if NumberTicket < 100000 or NumberTicket >= 1000000:
    print(f'введенное число {NumberTicket} не является номером билета')
else:
    while NumberTicket > 0:
        k = NumberTicket % 10
        NumberTicket=NumberTicket//10 
        list_1.append(k)
        sum1 = list_1[0]+list_1[1]+list_1[2]
        sum2 = list_1[3]+list_1[4]+list_1[5]
        if sum2 == sum1:
            print('У вас в руках счастливый билет!')
            print('Загадайте желание!')
        else:
            print('К сожалению счастливый билет достался другому пассажиру.')
            print('Купите еще билет. Он наверняка будет счастливым!')
