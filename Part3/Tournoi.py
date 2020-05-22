from random import randint
class Equipe():
    def __init__(self,Nom,NB_Match,Total_Point,NB_Victoir,NB_Defait,NB_Match_Null,But_Marque,But_Concede):
        self.Nom=Nom
        self.NB_Match=NB_Match
        self.Total_Point=Total_Point
        self.NB_Victoir=NB_Victoir
        self.NB_Defait=NB_Defait
        self.NB_Match_Null=NB_Match_Null
        self.But_Marque=But_Marque
        self.But_Concede=But_Concede
    
    def Affichage(self):
        print(self.__dict__)

    def Calcul_Point(self):
          self.Total_Point +=(self.NB_Victoir*3)+self.NB_Match_Null+(self.NB_Defait*0)
          return self.Total_Point
    
    def Goal_Average(self):
        return self.But_Marque-self.But_Concede

class Poule():
    def __init__(self,Poule_Name):
        self.Poule_Name=Poule_Name
        self.Equipes=list()

    def Afficher(self):        
        print('Poule Name :%s' % self.Poule_Name) 
        [Equipe.Affichage() for Equipe in self.Equipes]
        
    def Ajouter_Equipe(self,obj):
        if (len(self.Equipes)>3):
            print("__ limite exited __")
            pass
        else:
            self.Equipes.append(obj)#dynamic maping
    
    def Supprimer_Equipe(self,nom):
        for _,Equipe in enumerate(self.Equipes):
            if Equipe.__dict__['Nom']==nom:
                del self.Equipes[_]

    def Total_Buts_Marque(self):
        return sum([_.__dict__['But_Marque'] for _ in self.Equipes])
    
    #shit needs to change
    def Qualification(self):
            #there is somthong needs to fix about random choise
            [print(e.Calcul_Point()) for e in self.Equipes]
            tirage=[e.Total_Point for e in self.Equipes]
            avg=[e.Goal_Average() for e in self.Equipes]
            E1=(max(tirage))
            E1_pos=tirage.index(max(tirage))
            tirage.remove(max(tirage))
            E2=max(tirage)
            E2_pos=tirage.index(max(tirage))+1
            if (E1!=E2):
                return self.Equipes[E1_pos].Nom,self.Equipes[E2_pos].Nom
            elif(E1==E2):
                E1=(max(avg))
                E1_pos=avg.index(max(avg))
                avg.remove(max(avg))
                E2=max(avg)
                E2_pos=avg.index(max(avg))+1
                return self.Equipes[E1_pos].Nom,self.Equipes[E2_pos].Nom
            else:
                return self.Equipes[randint(0,3)].Nom,self.Equipes[randint(0,3)].Nom

