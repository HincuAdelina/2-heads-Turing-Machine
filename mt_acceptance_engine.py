# Examen
# grupa 144
# Georgescu Alina-Mihaela, Hincu Adelina-Cristina, Matei Alina-Cristina

from mt_parser_engine import transitions, start_state, accept_state, reject_state

with open('mt_parser_engine.py') as f: exec(f.read())


def mt_accept(transitions, start_state, accept_state, reject_state, string):
    blank_string = " "*100              #cream tape-ul prin adaugarea la finalul stringului un numar mare de spatii
    string = string + blank_string
    state = start_state
    head1 = head2 = 0           #ambele capete incep de pe prima pozitie
    i = 1           #contor pentru numarul de modificari din sir
    while state != accept_state and state != reject_state:
        for transition in transitions:
            if transition[0] == state and transition[2] == string[head1] and transition[3] == string[head2]:            #cautam tranzitia potrivita
                state = transition[1]           #cand o gasim, trecem la starea urmatoare
                string = string[:head1] + transition[4] + string[head1+1:]          #modificam simbolurile pentru ambele capete
                string = string[:head2] + transition[5] + string[head2+1:]
                print("Faza", i, ": ", string)          #afisam modificarile string-ului la fiecare pas
                i += 1                                  #incrementam contorul
                if transition[6] == 'L':                #mutam primul capat la stanga
                    if head1-1 >= 0:
                        head1 -= 1
                    else:
                        state = reject_state            #cum banda este infinita doar in dreapta, nu putem sa ne deplasam la stanga de pe pozitia 0
                        break
                if transition[6] == 'R':                #mutam primul capat la dreapta
                    head1 += 1
                if transition[7] == 'L':                #mutam cel de-al doilea capat la stanga
                    if head2-1 >= 0:
                        head2 -= 1
                    else:
                        state = reject_state            #cum banda este infinita doar in dreapta, nu putem sa ne deplasam la stanga de pe pozitia 0
                        break
                if transition[7] == 'R':                #mutam cel de-al doilea capat la dreapta
                    head2 += 1
                #pentru citirea simbolului 'N', nu mutam capetele

    if state == accept_state:                           #verificam starea finala
        print("\nAccepted! :)")

    elif state == reject_state:
        print("\nRejected! :(")



mt_accept(transitions, start_state, accept_state, reject_state, "aaabbaaabb")