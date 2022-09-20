import random
import telebot
from telebot import types

bot=telebot.TeleBot('5141905547:AAGaUm3F5lGzlnsDGMLdKHisN-4-c-N3ljY')


# _______________________________________________________________________________________________________________

def randCard():
    global card_pool
    current_card = random.choice(card_pool)
    temp_pool = []
    for key in card_pool:
        index = card_pool.index(key)
        if key != current_card:
            temp_pool.append(key)
    card_pool = temp_pool   
    return current_card

def check(current_card):
    card = ''

    try:
        if current_card:
            card = int(current_card)
            return card
 
    except:
        temp = {
            'Валет': 2,
            'Дама': 3,
            'Король': 4,
            'Туз': 11
            
        }
        if current_card in temp:
            card = int(temp[current_card])
            return card
        else:
            print('CHEK CARD ERROR')

def cardstat():
    print(f'Сумма ваших карт: {card_sum}')
    print(f'Сумма карт бота: {card_sum_bot}\n')
    print('Ваши карты:')
    q=1
    for i in card_user_pool:
        print(f"{q}) {i[0]}, масть '{i[1]}' ")
        q += 1
    print('Карты бота:\n')
    q=1
    for i in card_bot_pool:
        print(f"{q}) {i[0]}, масть '{i[1]}' ")
        q += 1


def botAI():
    global card_sum_bot
    global card_bot_pool
    global card_counter_bot
    while card_counter_bot < 6:
        current_card_bot = randCard()
        card_int_bot = check(current_card_bot[0])
        try_int = card_int_bot + card_sum_bot
        if try_int < 21:
            card_bot_pool.append(current_card_bot)
            card_sum_bot = try_int
            card_counter_bot += 1
        else:
            return card_sum_bot
    return card_sum_bot



def game():
    global card_counter
    global card_sum
    global card_sum_bot
    card_sum_bot = botAI()
    
    print(f"\n \nВыпали: {card_int1[0]} с мастью {card_int1[1]}, {card_int2[0]} с мастью {card_int2[1]}")
    while card_counter < 6:  
        if card_counter == 5:
            if card_sum > card_sum_bot:
                print("You Won!")
                cardstat()
            elif card_sum_bot == card_sum:
                print("У вас одинаковые карты 0_-")
                cardstat()
            else:
                print("\n\nBot won.. again")
                cardstat()
                print('try harder looser')
            break
        else:
            print(f"\nСумма карт: {card_sum}\n Ваши карты:")
            q=1
            for i in card_user_pool:
                print(f"{q}) {i[0]}, масть '{i[1]}'")
                q += 1
            answer = input("\nБудем брать еще? \nОтвет: Да/Нет \n")
            if answer in ('Да', 'yes', 'д','y','1'):
                card_counter += 1
                current_card = randCard()
                card_int = check(current_card[0])
                card_sum += card_int
                card_user_pool.append(current_card)
                if card_sum > 21:
                    q = 1
                    print(f'\nGame Over c====3 У тебя перебор\n Сумма карт: {card_sum}')
                    for i in card_user_pool:
                        print(f"{q}){i[0]}, масть '{i[1]}' ")
                        q += 1
                    break
            else:
                if card_sum > card_sum_bot:
                    print("\n\nYou Won!")
                    cardstat()
                elif card_sum_bot == card_sum:
                    print("У вас одинаковые карты 0_-")
                    cardstat()
                else:
                    print("\n\nBot won.. again")
                    cardstat()
                    print('try harder looser')
                break   
    else:
        print(f'\nGame Over c====3 У тебя перебор\n Сумма карт: {card_sum}')   



all_card = [6,7,8,9,10,'Валет','Дама','Король','Туз']
all_mast = ['Пики','Червы', 'Бубны', 'Трефы']
card_counter = 2
card_counter_bot = 2
card_sum = 0
card_sum_bot = 0
card_pool = [[x,y] for x in all_card for y in all_mast] #[[6,tref],[dama,pik]]

card_int1, card_int2 = randCard(), randCard()
card_sum = int(check(card_int1[0])) + int(check(card_int2[0]))
card_user_pool = [card_int1, card_int2]
        
        
card_int1, card_int2 = randCard(), randCard()
card_sum_bot = int(check(card_int1[0])) + int(check(card_int2[0]))
card_bot_pool = [card_int1,card_int2]

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет ✌️ ")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["Давай"]
    keyboard.add(*buttons)
    message.answer_dice(emoji="🎰")
    bot.send_message(message.chat.id,'Приветствую тебя в игрe black jack!')
    bot.send_message(message.chat.id,'Сыграем?',reply_markup=keyboard)





bot.infinity_polling()
 
