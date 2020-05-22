from Tournoi import *
import sqlite3
import json

conn=sqlite3.connect('Poules.db')
cursor=conn.cursor()
pols=[Poule(chr(_).capitalize()) for _ in range(97,105)]

def cree_Poules():

    pol=input('Select poules pour remplire: A/H').capitalize()
    for p in pols :
        if( p.Poule_Name==pol):
            try:
                cursor.execute('''
                CREATE  TABLE Poules_{}(  
                    Nom TEXT(20)  PRIMARY KEY ,
                    Nb_Match INTEGER,
                    Total_Point INTEGER,
                    NB_Victoire INTEGER,
                    NB_Defait INTEGER,
                    NB_Match_Null INTEGER,
                    But_Marque INTEGER,
                    But_Concede INTEGER
                )
                '''.format(p.Poule_Name))
                print('Table Poules_{} Created !'.format(p.Poule_Name))
            except Exception :
                print('Poules exist insert data in it !')
            p.Ajouter_Equipe(Equipe(
            input('Nom:'),
            int(input('NB_Match:')),
            int(input('Total point:') or 0) ,
            int(input('NB_Victoire:')),
            int(input('NB_Defait:')),
            int(input('NB_Match_Null:')),
            int(input('But_Marque:')),
            int(input('But_Concede:'))))
            for e in p.Equipes:
                try :
            
                    cursor.execute('Insert into Poules_{} values(\'{}\',{},{},{},{},{},{},{})'.format(
                        p.Poule_Name,
                        e.Nom,
                        e.NB_Match,
                        e.Total_Point,
                        e.NB_Victoir,
                        e.NB_Defait,
                        e.NB_Match_Null,
                        e.But_Marque,
                        e.But_Concede
                        )
                        )
                except Exception as e:
                    print(e)
            conn.commit()

            

def tree_poules():

    for p in pols:   
        try:
             conn.execute("REPLACE  INTO Poules_{} SELECT * FROM Poules_{}  ORDER BY Total_Point DESC".format(p.Poule_Name,p.Poule_Name,p.Poule_Name))#NICE SHIT sort fe data base
        except Exception as e:
            print(e)
    conn.commit()
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
        
        elif(choix==2):
            
            tree_poules()

        elif(choix==3):
                for p in pols:
                    print('Table Poules_{}'.format(p.Poule_Name)) 
                    try: 
                        for row in conn.execute('Select * from Poules_{}'.format(p.Poule_Name)):
                            print(row)
                    except Exception:
                            print('ALL Data has been fetched')
        elif(choix==0):
            break

