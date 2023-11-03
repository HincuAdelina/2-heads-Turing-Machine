# Examen
# grupa 144
# Georgescu Alina-Mihaela, Hincu Adelina-Cristina, Matei Alina-Cristina

import sys

states = set()
input_alphabet = set()
tape_alphabet = set()
transitions = set()
moves = {'L', 'R', 'N'}
nr_of_starting_states = 0
nr_of_accepting_states = 0          #nu pot exista mai multe stari de acceptare
nr_of_rejecting_states = 0          #nu pot exista mai multe stari de respingere
nr_of_sections = 0          #contorizam numarul de sectiuni pentru a ne asigura ca nu lipseste niciuna

f = open("mt_config_file_ex2.txt", "r")
linie = f.readline()
while linie != "":
    if linie == "States:\n":
        linie = f.readline()
        while linie != "End\n":
            if linie[0] != "#" and linie != '\n':
                linie = linie.strip()
                states.add(linie)           #se adauga starile in setul de stari
            linie = f.readline()
        nr_of_sections += 1
    elif linie == "Input alphabet:\n":
        linie = f.readline()
        while linie != "End\n":
            if linie[0] != "#" and linie != '\n':
                linie = linie.strip()
                input_alphabet.add(linie)           #se adauga simbolurile in setul input_alphabet
            linie = f.readline()
        nr_of_sections += 1
    elif linie == "Tape alphabet:\n":
        linie = f.readline()
        while linie != "End\n":
            if linie[0] != "#" and linie != '\n':
                linie = linie.strip()
                if linie == '':
                    tape_alphabet.add(' ')
                else:
                    tape_alphabet.add(linie)  # se adauga simbolurile in setul tape_alphabet
            linie = f.readline()
        nr_of_sections += 1
    elif linie == "Transitions:\n":
        linie = f.readline()
        while linie != "End\n":
            if linie[0] != "#" and linie != '\n':
                linie = linie.strip()               #separam linia dupa "," adaugam componentele intr-un tuplu ce va fi adaugat in setul de tranzitii , astfel:
                linie = linie.split(",")            #pe pozitia 0 se afla starea in care ne aflam, pe pozitia 1 se afla starea in care ajungem, pe pozitiile 2 si 3 se afla cele doua simboluri citite de capatul stang, respectiv drept
                transitions.add(tuple(linie))       #pe pozitiile 4 si 5 se afla simbolurile ce vor suprascrie simbolurile de pe pozitiile 2 si 3, iar pe pozitiile 6 si 7 se afla directia de deplasarea celor doua capete
            linie = f.readline()                    #   L = left    R = right   N = not moving
        nr_of_sections += 1
    elif linie == "Start state:\n":
        linie = f.readline()
        while linie != "End\n":
            if linie[0] != "#" and linie != '\n':
                linie = linie.strip()
                start_state = linie                 #se citeste starea initiala
            linie = f.readline()
        nr_of_starting_states += 1
        nr_of_sections += 1
    elif linie == "Accept state:\n":
        linie = f.readline()
        while linie != "End\n":
            if linie[0] != "#" and linie != '\n':
                linie = linie.strip()
                accept_state = linie                #se citeste starea de acceptare
            linie = f.readline()
        nr_of_accepting_states += 1
        nr_of_sections += 1
    elif linie == "Reject state:\n":
        linie = f.readline()
        while linie != "End\n":
            if linie[0] != "#" and linie != '\n':
                linie = linie.strip()
                reject_state = linie                #se citeste starea de respingere
            linie = f.readline()
        nr_of_rejecting_states += 1
        nr_of_sections += 1
    else:
        linie = f.readline()

#verificari corectitudine fisier de intrare
for tuple in transitions:
    if tuple[0] not in states:
        print("Invalid current state")
        exit()
    if tuple[1] not in states:          #cazul in care una din starile date nu exista
        print("Invalid next state")
        exit()
    if input_alphabet.issubset((tape_alphabet)) == False:           #input_alphabet trebuie sa fie inclus in tape_alphabet
        print("Invalid tape alphabet")
        exit()
    if (tuple[2] not in tape_alphabet or tuple[3] not in tape_alphabet) or (tuple[4] not in tape_alphabet or tuple[5] not in tape_alphabet):        #verificam daca caracterele date se afla in tape_alphabet, deoarece am verificat anterior ca input_alphabet este inclus in tape_alphabet
        print("Given symbols not in alphabet")
        exit()
    if tuple[6] not in moves or tuple[7] not in moves:     #verificam daca directiile de deplasare sunt valide
        print("Not a valid move")
        exit()
    if nr_of_sections != 7 or nr_of_starting_states != 1 or nr_of_accepting_states != 1 or nr_of_rejecting_states != 1:         #verificarea sectiunilor
        print("Invalid configuration file")
        exit()

