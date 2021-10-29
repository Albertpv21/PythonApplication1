import random
a=['камень', 'ножницы', 'бумага']
while True:
    a=player1_input = input('камень, ножницы или бумага?\n')
    player1 = a.index(player1_input)
    player2_input = random.randint(0,2)
    player2 = a[player2_input]
    print('Компьютер выбрал: ' + player2)
    difference = player1-player2_input
    if difference == -1 or difference == 2:
        print('Вы выиграли')
    elif player1== player2_input:
        print('ничья')
    else:
        print('Вы проиграли')
        N=input("Хочешь продолжить игру? Y/N")
        Y= 1
        if N == "Y":
            print("Продолжаем")
        elif N == "N":
            print("Жалко тебя")
