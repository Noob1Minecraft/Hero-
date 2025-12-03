from random import randint
from time import sleep

class Hero:
    """Базовый класс героя"""
    
    def __init__(self, name, hp, armor, power, weapon):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.power = power
        self.weapon = weapon
    
    def attack(self, enemy):
        print(f"{self.name} атакует {enemy.name}!")
        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.hp += enemy.armor
            enemy.armor = 0
    
    def info(self):
        print(f"Имя: {self.name}")
        print(f"Здоровье: {self.hp}")
        print(f"Броня: {self.armor}")
        print(f"Сила: {self.power}")
        print(f"Оружие: {self.weapon}")


class Warrior(Hero):
    """Воин - сильный боец с мечом"""
    
    def __init__(self, name, hp, armor, power):
        Hero.__init__(self, name, hp, armor, power, "Меч")
    
    def hello(self):
        print(f"Я {self.name}, могучий воин! Кто посмел потревожить мой покой?")
    
    def attack(self, enemy):
        print(f"[ВОИН] {self.name} взмахивает мечом и наносит мощный удар по {enemy.name}!")
        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.hp += enemy.armor
            enemy.armor = 0


class Mage(Hero):
    """Маг - использует магию"""
    
    def __init__(self, name, hp, armor, power):
        Hero.__init__(self, name, hp, armor, power, "Посох")
    
    def hello(self):
        print(f"Приветствую, путник. Я {self.name}, хранитель древних знаний.")
    
    def attack(self, enemy):
        print(f"[МАГ] {self.name} направляет посох на {enemy.name} и запускает огненный шар!")
        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.hp += enemy.armor
            enemy.armor = 0


class Rogue(Hero):
    """Разбойник - быстрый и ловкий"""
    
    def __init__(self, name, hp, armor, power):
        Hero.__init__(self, name, hp, armor, power, "Кинжалы")
    
    def hello(self):
        print(f"Стой! {self.name} здесь. Это моя территория!")
    
    def attack(self, enemy):
        print(f"[РАЗБОЙНИК] {self.name} выпрыгивает из тени и наносит удар кинжалами по {enemy.name}!")
        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.hp += enemy.armor
            enemy.armor = 0


class MainHero(Hero):
    """Главный герой"""
    
    def __init__(self, name, hp, armor, power, weapon):
        Hero.__init__(self, name, hp, armor, power, weapon)
    
    def hello(self):
        print(f"Я {self.name}, отважный путник. Я пришел с миром.")


# Создание персонажей
main_hero = MainHero("Артур", 300, 150, 200, "Топор")
warrior = Warrior("Торин", 350, 180, 180)
mage = Mage("Мерлин", 250, 100, 400)
rogue = Rogue("Тень", 200, 120, 250)

print("""
╔════════════════════════════════════════╗
║   ДОБРО ПОЖАЛОВАТЬ В ТЕМНЫЙ ЛЕС        ║
║   Ваша судьба в ваших руках...         ║
╚════════════════════════════════════════╝
""")

finish = True
while finish:
    action = input("\nВыберите путь:\n1 - Идти к башне мага\n2 - Пойти к воротам крепости\n3 - Свернуть в темную рощу\nВаш выбор: ")
    
    if action == '1':
        print("\n--- ВЫ ВХОДИТЕ В ДРЕВНЮЮ БАШНЮ ---")
        mage.hello()
        answer = input("\nВаши действия?\n1 - Представиться\n2 - Атаковать\nВыбор: ")
        
        if answer == '1':
            main_hero.hello()
            print(f"\n{mage.name} кивает и пропускает вас.")
            print("\n*** ПОБЕДА! ВЫ ПРОШЛИ ИГРУ ***")
            break
        else:
            print("\n=== НАЧИНАЕТСЯ БОЙ ===\n")
            while True:
                if mage.hp <= 0:
                    print(f"\n{mage.name} повержен!")
                    main_hero.hp += 150
                    main_hero.power += 80
                    print("LEVEL UP! +150 HP, +80 силы")
                    break
                if main_hero.hp <= 0:
                    print("\nВЫ ПОГИБЛИ...")
                    finish = False
                    break
                
                turn = randint(1, 2)
                if turn == 1:
                    main_hero.attack(mage)
                else:
                    mage.attack(main_hero)
                
                sleep(1)
                print(f"\nВаши характеристики: HP={main_hero.hp}, Броня={main_hero.armor}")
                print(f"Противник: HP={mage.hp}, Броня={mage.armor}\n")
            
            if finish:
                print("\n*** ПОБЕДА! ***")
                break
    
    elif action == '2':
        print("\n--- ВЫ ПОДХОДИТЕ К ВОРОТАМ КРЕПОСТИ ---")
        warrior.hello()
        answer = input("\nВаши действия?\n1 - Представиться\n2 - Атаковать\nВыбор: ")
        
        if answer == '1':
            main_hero.hello()
            print(f"\n{warrior.name} опускает оружие и открывает ворота.")
            print("\n*** ПОБЕДА! ВЫ ПРОШЛИ ИГРУ ***")
            break
        else:
            print("\n=== НАЧИНАЕТСЯ БОЙ ===\n")
            while True:
                if warrior.hp <= 0:
                    print(f"\n{warrior.name} повержен!")
                    main_hero.hp += 150
                    main_hero.power += 80
                    print("LEVEL UP! +150 HP, +80 силы")
                    break
                if main_hero.hp <= 0:
                    print("\nВЫ ПОГИБЛИ...")
                    finish = False
                    break
                
                turn = randint(1, 2)
                if turn == 1:
                    main_hero.attack(warrior)
                else:
                    warrior.attack(main_hero)
                
                sleep(1)
                print(f"\nВаши характеристики: HP={main_hero.hp}, Броня={main_hero.armor}")
                print(f"Противник: HP={warrior.hp}, Броня={warrior.armor}\n")
            
            if finish:
                print("\n*** ПОБЕДА! ***")
                break
    
    elif action == '3':
        print("\n--- ВЫ ЗАХОДИТЕ В ТЕМНУЮ РОЩУ ---")
        rogue.hello()
        answer = input("\nВаши действия?\n1 - Представиться\n2 - Атаковать\nВыбор: ")
        
        if answer == '1':
            main_hero.hello()
            print(f"\n{rogue.name} исчезает в тени, пропуская вас.")
            print("\n*** ПОБЕДА! ВЫ ПРОШЛИ ИГРУ ***")
            break
        else:
            print("\n=== НАЧИНАЕТСЯ БОЙ ===\n")
            while True:
                if rogue.hp <= 0:
                    print(f"\n{rogue.name} повержен!")
                    main_hero.hp += 150
                    main_hero.power += 80
                    print("LEVEL UP! +150 HP, +80 силы")
                    break
                if main_hero.hp <= 0:
                    print("\nВЫ ПОГИБЛИ...")
                    finish = False
                    break
                
                turn = randint(1, 2)
                if turn == 1:
                    main_hero.attack(rogue)
                else:
                    rogue.attack(main_hero)
                
                sleep(1)
                print(f"\nВаши характеристики: HP={main_hero.hp}, Броня={main_hero.armor}")
                print(f"Противник: HP={rogue.hp}, Броня={rogue.armor}\n")
            
            if finish:
                print("\n*** ПОБЕДА! ***")
                break
    else:
        print("\nНеверный выбор! Попробуйте снова.")

print("\nСпасибо за игру!")