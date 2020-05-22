from Tournoi import *
from operator import attrgetter
import json
pols=[Poule(chr(_).capitalize()) for _ in range(97,105)]

def cree_Poules():
    pol=input('Select poules pour remplire: A/H').capitalize()
    for p in pols :
        if( p.Poule_Name==pol):
            p.Ajouter_Equipe(Equipe(
            input('Nom:'),
            int(input('Nb_Match:')),
            int(input('Total point:') or 0) ,
            int(input('NB_Victoire:')),
            int(input('NB_Defait')),
            int(input('NB_Match_Null')),
            int(input('But_Marque')),
            int(input('But_Concede'))))

def tree_poules():
    for p in pols:
        [print(e.Calcul_Point()) for e in p.Equipes] 
    for p in pols:   
        p.Equipes.sort(key=lambda x:x.Total_Point, reverse=True)


while (True):

        print('''
 ----------MENU-----------
|    1:create poules      |
|    2:sort poules        |
|    3:view poules        |
|    0:exit               |
|                         |
 ------------------------- ''')
        choix=int(input('select choise :'))
        if(choix==1):
            cree_Poules()
            with open('Poules.txt','w')as file:
                for p in pols:
                    json.dump({"Poule_Name":p.Poule_Name,"Equipes":[e.__dict__ for e in p.Equipes]},file,indent=4)
                file.close()
        elif(choix==2):
            tree_poules()
            with open('Poules.txt','w')as file:
                for p in pols:
                    json.dump({"Poule_Name":p.Poule_Name,"Equipes":[e.__dict__ for e in p.Equipes]},file,indent=4)
                file.close()

        elif(choix==3):
            for p in pols:
                p.Afficher()
        elif(choix==0):
            break

