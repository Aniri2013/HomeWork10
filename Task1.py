import random as r
import module
drakon_names = ['Ладон', 'Скай', 'Гвинес', 'Флэр', 'Ноздорму', 'Азурегос']
drakon = r.choice(drakon_names)
health_hero = r.randint(40, 50)
health_drakon = r.randint(40, 50)
battle_drakon = r.randint(1, 2)
raund = 0;
print("Бой с драконом!")

hero_name = input("Имя героя - ")
start = True
while start:
    if health_hero <= 0:
        print("\n Победа за драконом!!")
        start = False
        input("")

    if health_drakon <= 0:
        print("\n Победа за вами!")
        start = False
        input("")

    battle_drakon = r.randint(1, 2)
    attack_hero = r.randint(1, 10)
    shield_hero = r.randint(1, 10)
    attack_drakon = r.randint(1, 10)
    shield_drakon = r.randint(1, 10)
    raund += 1
    module.r(raund)

    print('''
    ИТОГИ:
Герой: {}                      Дракон: {}
Здоровья: {}                   Здоровья: {}  
Атака: {}                      Атака: {} 
Защита: {}                     Защита: {}

    '''.format(hero_name,drakon,health_hero,health_drakon,attack_hero,attack_drakon,shield_hero,shield_drakon))
    battle = int(input('''
Выбор хода:
1 - Атака
2 - Защита
'''))

    if (battle == battle_drakon == 1):
        print(" Атака VS Атака")
        if attack_hero == attack_drakon:
            health_hero = health_hero - (attack_drakon // 2)
            health_drakon = health_drakon - (attack_hero // 2)
        elif attack_hero > attack_drakon:
            health_drakon = health_drakon - attack_hero
        elif attack_hero < attack_drakon:
            health_hero = health_hero - attack_drakon
    elif (battle == battle_drakon == 2):
        print("Защита VS Защита")
    elif battle < battle_drakon:
        print("Атака VS Защита")
        if attack_hero > shield_drakon:
            health_drakon = health_drakon - (attack_hero - shield_drakon)
        elif attack_hero <= shield_drakon:
            print("\n Атака Отбита!")
    elif battle > battle_drakon:
        print("Защита VS Атака")
        if attack_drakon < shield_hero:
            health_hero = health_hero - (attack_drakon - shield_hero)
        elif attack_drakon <= shield_hero:
            print("\nАтака Отбита!")