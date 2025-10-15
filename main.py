"""
auteur: Zhuo.H, classe 407
Ce programme est de faire un combat de monstre

"""

import random

print("Vous êtes coincé dans ce donjon où le seul façon de sortir c'est de battre niveau 3!")
print("Après chaque niveau, vous receverais d'esperience où vous pouvez l'utiliser pour améliorer vos abilité.")

monster = [10, 3, 1]  # health, damage, level
player = [20, 8, 1]  # health, damage, level

m_health = monster[0]
m_damage = monster[1]
m_level = monster[2]

health = player[0]
damage = player[1]
level = player[2]

turn = 1
wins = 0


def dice(faces):
    return random.randint(1, faces)


while True:

    # boss battle
    if wins % 3 == 0:
        print("vous trouver face à face à un boss!")
        m_health = random.randint(100, 300)
        m_damage = random.randint(15, 30)
        alive = True
        while alive:
            print(f" Le boss a {m_health} hp")
            print(f"vous avez: {health}hp")
            if turn == 1:
                decision = input(f"Voulez vous attaquer(1), regénerer(2), tutoriel(3) ou quitter(4)?")
                try:
                    decision = int(decision)
                except ValueError:
                    print("réponse non accepter! veuiller recomencer")
                    continue
                if decision == 1:
                    print("vous attaquer!")
                    result = dice(6)
                    m_result = dice(6)
                    print(f"Vous avez eu un:{result} et le monstre a un:{m_result}")
                    difference = result - m_result
                    if difference >= 4:
                        print("Dégas critique!")
                        m_health = m_health - 2 * damage
                    elif 1 <= difference <= 3:
                        print(f"attaque reussite! vous faite: {damage} dégas.")
                        m_health = m_health - damage
                    else:
                        print("Attaque non réussit!")
                elif decision == 2:
                    regenerate = dice(4)
                    health = health + regenerate
                    print(f"vous ajouter: {regenerate} hp!")
                elif decision == 3:
                    print("Le but du jeu c'est de battre le boss au niveau 4.")
                    print("Vous améliorez votre experience par tuer des montre.")
                    print("Dans les combats, vous pouvez attaquer ou regenèrer")
                    print(f"vous devez rouler un dée avec le monstre et si votre nombre est plus grande, ")
                    print("vous ferrez du degas")
                    print("Vous ne pouvez pas contourner le boss!")
                    continue
                elif decision == 4:
                    print("merci de jouer!")
                    exit()

                else:
                    print("Écrivez 1, 2,3 ou 4!")
                    continue

            # monster AI section

            elif turn == -1:

                print("c'est au tour du boss!")
                choice = dice(3)
                if choice == 1 or choice == 2:
                    print("le boss vous attaque!")
                    print("vous devez avoir un resultat plus ou égal qu'au monstre pour que tu ne subis pas de dégas!")
                    m_score = dice(6)
                    score = dice(6)
                    difference = m_score - score
                    print(f"le monstre a un {m_score} et vous avez eu un {score}")
                    if difference >= 4:
                        print("le boss a fait une attaque critique!")
                        print(f"le boss a fait {m_damage * 2} de dégas!")
                        health = health - m_damage * 2
                    elif 1 <= difference <= 3:
                        print(f"le boss a fait {m_damage} de dégas!")
                        health = health - m_damage
                    else:
                        print("le monstre a rater son coûp!")
                else:
                    m_regenerate = dice(6)
                    print(f"le boss a regénérer {m_regenerate}hp!")
                    m_health += m_regenerate
            turn = turn * -1

            if m_health <= 0:
                print("vous avez vaincu le boss! Vous avez gagner!")
                restart = input("Veux-tu recommencer?(y/n)")
                if restart == "y":
                    m_health = 10
                    m_damage = 3
                    m_level = 1
                    health = 20
                    damage = 5
                    level = 1
                    turn = 1
                    print("restarting...")
                    break
                elif restart == "n":
                    print("Merci de jouer!")
                    exit()
            elif health <= 0:
                print("le monstre vous avez vaincu!")
                restart = input("Veux-tu recommencer?(y/n)")
                if restart == "y":
                    m_health = 10
                    m_damage = 3
                    m_level = 1
                    health = 20
                    damage = 5
                    level = 1
                    turn = 1
                    print("restarting...")
                elif restart == "n":
                    print("Merci de jouer!")
                    exit()

    print(f"niveau {m_level}. Le monstre a {m_health} hp")
    print(f"vous avez: {health}hp")
    # user code

    if turn == 1:
        decision = input(f"Voulez vous attaquer(1), regénerer(2), contourner le monstre(3), regles(4) ou quitter(5)?")
        try:
            decision = int(decision)
        except ValueError:
            print("réponse non accepter! veuiller recomencer")
            continue
        if decision == 1:
            print("vous attaquer!")
            result = dice(6)
            m_result = dice(6)
            print(f"Vous avez eu un:{result} et le monstre a un:{m_result}")
            difference = result - m_result
            if difference >= 4:
                print("Dégas critique!")
                m_health = m_health - 2 * damage
            elif 1 <= difference <= 3:
                print(f"attaque reussite! vous faite: {damage} dégas.")
                m_health = m_health - damage
            else:
                print("Attaque non réussit!")
        elif decision == 2:
            regenerate = dice(4)
            health += regenerate
            print(f"vous ajouter: {regenerate} hp!")
        elif decision == 3:
            m_level = m_level + 1
            health -= 1
            print("vous contournez le monstre!")
            continue
        elif decision == 4:
            print("Le but du jeu c'est de battre le boss au niveau 4.")
            print("Vous améliorez votre experience par tuer des montre.")
            print("Dans les combats, vous pouvez attaquer ou regenèrer")
            print(f"vous devez rouler un dée avec le monstre et si votre nombre est plus grande, vous ferez du dégas.")
            print("Vous ne pouvez pas contourner le boss!")
            continue
        elif decision == 5:
            print("merci de jouer!")
            exit()
        else:
            print("Écrivez 1, 2, 3, 4 ou 5!")
            continue

    # monster AI section

    elif turn == -1:
        print("c'est au tour du monstre!")
        choice = dice(3)
        if choice == 1 or choice == 2:
            print("le monstre vous attaque!")
            print("vous devez avoir un resultat plus ou égal qu'au monstre pour que tu ne subis pas de dégas!")
            m_score = dice(6)
            score = dice(6)
            difference = m_score - score
            print(f"le monstre a un {m_score} et vous avez eu un {score}")
            if difference >= 4:
                print("le monstre a fait une attaque critique!")
                print(f"le monstre a fait {m_damage * 2} de dégas!")
                health = health - m_damage * 2
            elif 1 <= difference <= 3:
                print(f"le monstre a fait {m_damage} de dégas!")
                health = health - m_damage
            else:
                print("le monstre a rater son coûp!")
        else:
            m_regenerate = dice(4)
            print(f"le monstre a regénérer {m_regenerate}hp!")
            m_health += m_regenerate

    if m_health <= 0:
        print("vous avez vaincu l'ennemi!")
        m_level += 1
        wins += 1
        m_health = 10 * m_level
        m_damage = 3 * m_level
        damage = damage * 1.5
        continue
    elif health <= 0:
        print("le monstre vous avez vaincu!")
        restart = input("Veux-tu recommencer?(y/n)")
        if restart == "y":
            m_health = 10
            m_damage = 3
            m_level = 1
            health = 20
            damage = 5
            level = 1
            turn = 1
            print("restarting...")
        elif restart == "n":
            print("Merci de jouer!")
            exit()
    turn *= -1
