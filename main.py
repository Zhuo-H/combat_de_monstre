# auteur: Zhuo.H, classe 407
# Ce programme est de faire un combat de monstre


import random
import time

print(
    "Bienvenu au combat de monstre! Vous êtes coincé dans ce donjon où le seul façon de sortir c'est de battre niveau 3!")
print("Après chaque niveau, vous receverais d'esperience où vous pouvez l'utiliser pour améliorer vos abilité.")

monster = [10, 3, 1]  # health, damage, level
player = [20, 5, 1]  # health, damage, level

m_health = monster[0]
m_damage = monster[1]
m_level = monster[2]

health = player[0]
damage = player[1]
level = player[2]

turn = 1


def dice(faces):
    return random.randint(1, faces)


while True:
    if m_level == 4:
        time.sleep(0.5)
        print("vous avez gagner!")
        time.sleep(0.5)
        restart = input("voulez-vouz continuer a l'infini ou terminer le jeu?(y/n)")
        if restart == "y":
            time.sleep(0.5)
        else:
            print("merci au revoir!")
            exit()
    print(f"niveau {m_level}. Le monstre a {m_health} hp")
    time.sleep(0.5)
    print(f"vous avez: {health}hp")
    time.sleep(0.5)

    # user code

    if turn == 1:
        decision = input(f"Voulez vous attaquer(1) ou regénerer(2)?")
        try:
            decision = int(decision)
        except ValueError:
            print("réponse non accepter! veuiller recomencer")
            continue
        if decision == 1:
            time.sleep(0.5)
            print("vous attaquer!")
            time.sleep(0.5)
            result = dice(6)
            m_result = dice(6)
            print(f"Vous avez eu un:{result} et le monstre a un:{m_result}")
            difference = result - m_result
            time.sleep(0.5)
            if difference >= 4:
                time.sleep(0.5)
                print("Dégas critique!")
                m_health = m_health - 2 * damage
            elif 1 <= difference <= 3:
                time.sleep(0.5)
                print(f"attaque reussite! vous faite: {damage} dégas.")
                m_health = m_health - damage
            else:
                time.sleep(0.5)
                print("Attaque non réussit!")


        elif decision == 2:
            regenerate = dice(4)
            health = health + regenerate
            time.sleep(0.5)
            print(f"vous ajouter: {regenerate} hp!")

        else:
            print("Écrivez 1 ou 2!")
            time.sleep(0.5)

    # monster AI section

    elif turn == -1:

        time.sleep(0.5)
        print("c'est au tour du monstre!")
        choice = dice(3)
        if choice == 1 or choice == 2:
            print("le monstre vous attaque!")
            time.sleep(0.5)
            print("vous devez avoir un resultat plus ou égal qu'au monstre pour que tu ne subis pas de dégas!")
            time.sleep(0.5)
            m_score = dice(6)
            score = dice(6)
            difference = m_score - score
            print(f"le monstre a un {m_score} et vous avez eu un {score}")
            time.sleep(0.5)
            if difference >= 4:
                print("le monstre a fait une attaque critique!")
                time.sleep(0.5)
                print(f"le monstre a fait {m_damage * 2} de dégas!")
                health = health - m_damage * 2
            elif 1 <= difference <= 3:
                time.sleep(0.5)
                print(f"le monstre a fait {m_damage} de dégas!")
                health = health - m_damage
            else:
                time.sleep(0.5)
                print("le monstre a rater son coûp!")
        else:
            print("c'est au tour du monstre!")
            m_regenerate = dice(4)
            print(f"le monstre a regénérer {m_regenerate}hp!")
            m_health += m_regenerate
    turn = turn * -1

    if m_health <= 0:
        print("vous avez vaincu le monstre!")
        m_level = m_level + 1
        m_health = 10 * m_level
        m_damage = 3 * m_level
        damage = damage * 1.5
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
            time.sleep(0.5)
            print("restarting...")
        elif restart == "n":
            time.sleep(0.5)
            print("Merci de jouer!")
            exit()

