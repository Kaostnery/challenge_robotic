# utilitaire permettant de charger les donnees de la carte du
# challenge et de la visualiser
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import math

tColorTab = {1:'red', 2:'green', 3:'blue'}
dbRayon = 0.85
##########################
# point d'entree du script 
##########################
sys.argv="/Users/kaost/Downloads/donnees-map.txt"
argc = len(sys.argv)

if argc < 2:
    print("preciser le nom du fichier de donnees en argument...")
    exit()
#lecture du fichier
DataMap = np.loadtxt(sys.argv, skiprows=1, dtype=float)
#affichage des donnees de la carte
x=DataMap[:,0]
y=DataMap[:,1]
t=DataMap[:,2]
n = len(x)
fig = plt.figure(1)
ax = fig.gca()
for i in range(n):
    plt.plot(x[i],y[i],marker='+',color=tColorTab[int(t[i])])
    c1 = plt.Circle((x[i],y[i]), dbRayon,color=tColorTab[int(t[i])] )
    ax.add_patch(c1)
plt.show()


class robot():
    def __init__(self, v0,a,liste_x,liste_y,t,x_dbt,y_dbt):
        self.liste_x=liste_x
        self.liste_y=liste_y
        self.q=1
        self.position_x=x_dbt
        self.position_y=y_dbt
        self.gain=0
        self.type=t
        self.node_parcouru=[]
        self.poids=0
        self.v0=1
        self.a=6.98*(10**(-2))
        self.vmax=self.v0*self.a*math.exp(-self.a*self.poids)
        
    def cout_temporel(self):
        
        for i in range(len(self.liste_x)):
            if i not in self.node_parcouru:  
                tempo=math.sqrt((self.position_x-self.liste_x[i])**2+(self.position_y-self.liste_y[i])**2)/self.vmax
            print(tempo)
            
    def node_selectione(self,i):
        self.node_parcouru.append(i)
        self.position_x=self.liste_x[i]
        self.position_y=self.liste_y[i]
        self.vmax=self.v0*self.a*math.exp(-self.a*self.poids)
        
        self.poids+=0.5*(int(self.type[i])+1)
        self.gain+=int(self.type(i))
        
    def cout_carbonne(self):
        
        for i in range(len(self.liste_x)):
            if i not in self.node_parcouru:  
                tempo=self.q*math.sqrt((self.position_x-self.liste_x[i])**2+(self.position_y-self.liste_y[i])**2)/self.vmax
            print(tempo)
            
    def cout(self,a,b ):
        for i in range(len(self.liste_x)):
            if i not in self.node_parcouru:  
                tempo=((self.q*a)+(b/self.vmax))*math.sqrt((self.position_x-self.liste_x[i])**2+(self.position_y-self.liste_y[i])**2)/self.vmax
            print(tempo)
        
        
    
       
