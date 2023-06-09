# Arianne Gravel
# 1928883

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter.constants import *
from Garage import *
from Reparation import *


class ProjetFinalUI:
    def __init__(self, top=None):
        # Création de l'établissement
        self.mongarage: Garage = None
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""

        top.geometry("600x523+660+210")
        top.minsize(120, 1)
        top.maxsize(3844, 1068)
        top.resizable(1, 1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")

        self.top = top

        # Configuration du Notebook

        self.TNotebook1 = ttk.Notebook(self.top)
        self.TNotebook1.place(relx=0.0, rely=0.0, relheight=0.99, relwidth=0.99)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text='''Garage''', compound="left"
                            , underline='''-1''', )
        self.TNotebook1_t1.configure(background="#8080ff")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(1, text='''Voitures''', compound="left"
                            , underline='''-1''', )
        self.TNotebook1_t2.configure(background="#fcf503")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")
        self.TNotebook1_t3 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3, padding=3)
        self.TNotebook1.tab(2, text='''Réparations''', compound="left"
                            , underline='''-1''', )
        self.TNotebook1_t3.configure(background="#ff80c0")
        self.TNotebook1_t3.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t3.configure(highlightcolor="black")
        self.TNotebook1_t4 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t4, padding=3)
        self.TNotebook1.tab(3, text='''Consultations''', compound="left"
                            , underline='''-1''', )
        self.TNotebook1_t4.configure(background="#80ffff")
        self.TNotebook1_t4.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t4.configure(highlightcolor="black")

        # Page Garage

        self.Labelframe1 = tk.LabelFrame(self.TNotebook1_t1)
        self.Labelframe1.place(relx=0.017, rely=0.049, relheight=0.63
                               , relwidth=0.966)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="#000000")
        self.Labelframe1.configure(text='''Infos garage''')
        self.Labelframe1.configure(background="#d70428")
        self.Label1 = tk.Label(self.Labelframe1)
        self.Label1.place(relx=0.035, rely=0.123, height=48, width=154
                          , bordermode='ignore')
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Nom :''')
        self.Label1_1 = tk.Label(self.Labelframe1)
        self.Label1_1.place(relx=0.035, rely=0.316, height=47, width=154
                            , bordermode='ignore')
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(anchor='w')
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(compound='left')
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Adresse :''')
        self.Label1_1_1 = tk.Label(self.Labelframe1)
        self.Label1_1_1.place(relx=0.035, rely=0.506, height=48, width=154
                              , bordermode='ignore')
        self.Label1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1.configure(anchor='w')
        self.Label1_1_1.configure(background="#d9d9d9")
        self.Label1_1_1.configure(compound='left')
        self.Label1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1.configure(foreground="#000000")
        self.Label1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1.configure(highlightcolor="black")
        self.Label1_1_1.configure(text='''Téléphone :''')
        self.Entry_nom_garage = tk.Entry(self.Labelframe1)
        self.Entry_nom_garage.place(relx=0.368, rely=0.123, height=40
                                    , relwidth=0.516, bordermode='ignore')
        self.Entry_nom_garage.configure(background="white")
        self.Entry_nom_garage.configure(disabledforeground="#a3a3a3")
        self.Entry_nom_garage.configure(font="TkFixedFont")
        self.Entry_nom_garage.configure(foreground="#000000")
        self.Entry_nom_garage.configure(insertbackground="black")
        self.Entry_adresse_garage = tk.Entry(self.Labelframe1)
        self.Entry_adresse_garage.place(relx=0.368, rely=0.316, height=40
                                        , relwidth=0.604, bordermode='ignore')
        self.Entry_adresse_garage.configure(background="white")
        self.Entry_adresse_garage.configure(cursor="fleur")
        self.Entry_adresse_garage.configure(disabledforeground="#a3a3a3")
        self.Entry_adresse_garage.configure(font="TkFixedFont")
        self.Entry_adresse_garage.configure(foreground="#000000")
        self.Entry_adresse_garage.configure(insertbackground="black")
        self.Entry_telephone_garage = tk.Entry(self.Labelframe1)
        self.Entry_telephone_garage.place(relx=0.368, rely=0.51, height=40
                                          , relwidth=0.375, bordermode='ignore')
        self.Entry_telephone_garage.configure(background="white")
        self.Entry_telephone_garage.configure(disabledforeground="#a3a3a3")
        self.Entry_telephone_garage.configure(font="TkFixedFont")
        self.Entry_telephone_garage.configure(foreground="#000000")
        self.Entry_telephone_garage.configure(insertbackground="black")
        self.Button_cree_garage = tk.Button(self.Labelframe1)
        self.Button_cree_garage.place(relx=0.368, rely=0.716, height=54
                                      , width=167, bordermode='ignore')
        self.Button_cree_garage.configure(activebackground="beige")
        self.Button_cree_garage.configure(activeforeground="black")
        self.Button_cree_garage.configure(background="#d9d9d9")
        self.Button_cree_garage.configure(compound='left')
        self.Button_cree_garage.configure(disabledforeground="#a3a3a3")
        self.Button_cree_garage.configure(foreground="#000000")
        self.Button_cree_garage.configure(highlightbackground="#d9d9d9")
        self.Button_cree_garage.configure(highlightcolor="black")
        self.Button_cree_garage.configure(pady="0")
        self.Button_cree_garage.configure(text='''Créer garage''')
        self.Label2 = tk.Label(self.TNotebook1_t1)
        self.Label2.place(relx=0.051, rely=0.711, height=40, width=154)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Fichier :''')
        self.Entry_fichier_garage = tk.Entry(self.TNotebook1_t1)
        self.Entry_fichier_garage.place(relx=0.373, rely=0.711, height=40
                                        , relwidth=0.498)
        self.Entry_fichier_garage.configure(background="white")
        self.Entry_fichier_garage.configure(cursor="fleur")
        self.Entry_fichier_garage.configure(disabledforeground="#a3a3a3")
        self.Entry_fichier_garage.configure(font="-family {Courier New} -size 10")
        self.Entry_fichier_garage.configure(foreground="#000000")
        self.Entry_fichier_garage.configure(insertbackground="black")
        self.Button_deseriliser_garage = tk.Button(self.TNotebook1_t1)
        self.Button_deseriliser_garage.place(relx=0.153, rely=0.833, height=64
                                             , width=167)
        self.Button_deseriliser_garage.configure(activebackground="beige")
        self.Button_deseriliser_garage.configure(activeforeground="black")
        self.Button_deseriliser_garage.configure(background="#d9d9d9")
        self.Button_deseriliser_garage.configure(compound='left')
        self.Button_deseriliser_garage.configure(disabledforeground="#a3a3a3")
        self.Button_deseriliser_garage.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Button_deseriliser_garage.configure(foreground="#000000")
        self.Button_deseriliser_garage.configure(highlightbackground="#d9d9d9")
        self.Button_deseriliser_garage.configure(highlightcolor="black")
        self.Button_deseriliser_garage.configure(pady="0")
        self.Button_deseriliser_garage.configure(text='''Désériliser''')
        self.Button_seseriliser_garage = tk.Button(self.TNotebook1_t1)
        self.Button_seseriliser_garage.place(relx=0.542, rely=0.833, height=64
                                             , width=167)
        self.Button_seseriliser_garage.configure(activebackground="beige")
        self.Button_seseriliser_garage.configure(activeforeground="black")
        self.Button_seseriliser_garage.configure(background="#d9d9d9")
        self.Button_seseriliser_garage.configure(compound='left')
        self.Button_seseriliser_garage.configure(disabledforeground="#a3a3a3")
        self.Button_seseriliser_garage.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Button_seseriliser_garage.configure(foreground="#000000")
        self.Button_seseriliser_garage.configure(highlightbackground="#d9d9d9")
        self.Button_seseriliser_garage.configure(highlightcolor="black")
        self.Button_seseriliser_garage.configure(pady="0")
        self.Button_seseriliser_garage.configure(text='''Sésériliser''')

        # Page Voitures

        self.Labelframe2 = tk.LabelFrame(self.TNotebook1_t2)
        self.Labelframe2.place(relx=0.0, rely=0.02, relheight=0.376
                               , relwidth=1.0)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="#000000")
        self.Labelframe2.configure(text='''Infos voiture''')
        self.Labelframe2.configure(background="#ff8040")
        self.Label3 = tk.Label(self.Labelframe2)
        self.Label3.place(relx=0.017, rely=0.162, height=41, width=124
                          , bordermode='ignore')
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Num. Plaque :''')
        self.Label3_1 = tk.Label(self.Labelframe2)
        self.Label3_1.place(relx=0.017, rely=0.432, height=41, width=124
                            , bordermode='ignore')
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(anchor='w')
        self.Label3_1.configure(background="#d9d9d9")
        self.Label3_1.configure(compound='left')
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(foreground="#000000")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''Marque :''')
        self.Label3_1_1 = tk.Label(self.Labelframe2)
        self.Label3_1_1.place(relx=0.017, rely=0.703, height=41, width=124
                              , bordermode='ignore')
        self.Label3_1_1.configure(activebackground="#f9f9f9")
        self.Label3_1_1.configure(anchor='w')
        self.Label3_1_1.configure(background="#d9d9d9")
        self.Label3_1_1.configure(compound='left')
        self.Label3_1_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1_1.configure(foreground="#000000")
        self.Label3_1_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1_1.configure(highlightcolor="black")
        self.Label3_1_1.configure(text='''Couleur :''')
        self.Label3_1_1_1 = tk.Label(self.Labelframe2)
        self.Label3_1_1_1.place(relx=0.525, rely=0.432, height=41, width=124
                                , bordermode='ignore')
        self.Label3_1_1_1.configure(activebackground="#f9f9f9")
        self.Label3_1_1_1.configure(anchor='w')
        self.Label3_1_1_1.configure(background="#d9d9d9")
        self.Label3_1_1_1.configure(compound='left')
        self.Label3_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1_1_1.configure(foreground="#000000")
        self.Label3_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1_1_1.configure(highlightcolor="black")
        self.Label3_1_1_1.configure(text='''Modele :''')
        self.Label3_1_1_1_1 = tk.Label(self.Labelframe2)
        self.Label3_1_1_1_1.place(relx=0.525, rely=0.703, height=41, width=124
                                  , bordermode='ignore')
        self.Label3_1_1_1_1.configure(activebackground="#f9f9f9")
        self.Label3_1_1_1_1.configure(anchor='w')
        self.Label3_1_1_1_1.configure(background="#d9d9d9")
        self.Label3_1_1_1_1.configure(compound='left')
        self.Label3_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1_1_1_1.configure(foreground="#000000")
        self.Label3_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1_1_1_1.configure(highlightcolor="black")
        self.Label3_1_1_1_1.configure(text='''Année :''')
        self.Entry_num_plaque_voiture = tk.Entry(self.Labelframe2)
        self.Entry_num_plaque_voiture.place(relx=0.254, rely=0.162, height=40
                                            , relwidth=0.244, bordermode='ignore')
        self.Entry_num_plaque_voiture.configure(background="white")
        self.Entry_num_plaque_voiture.configure(disabledforeground="#a3a3a3")
        self.Entry_num_plaque_voiture.configure(font="TkFixedFont")
        self.Entry_num_plaque_voiture.configure(foreground="#000000")
        self.Entry_num_plaque_voiture.configure(insertbackground="black")
        self.Entry_marque_voiture = tk.Entry(self.Labelframe2)
        self.Entry_marque_voiture.place(relx=0.254, rely=0.432, height=40
                                        , relwidth=0.244, bordermode='ignore')
        self.Entry_marque_voiture.configure(background="white")
        self.Entry_marque_voiture.configure(disabledforeground="#a3a3a3")
        self.Entry_marque_voiture.configure(font="TkFixedFont")
        self.Entry_marque_voiture.configure(foreground="#000000")
        self.Entry_marque_voiture.configure(insertbackground="black")
        self.Entry_couleur_voiture = tk.Entry(self.Labelframe2)
        self.Entry_couleur_voiture.place(relx=0.254, rely=0.703, height=40
                                         , relwidth=0.244, bordermode='ignore')
        self.Entry_couleur_voiture.configure(background="white")
        self.Entry_couleur_voiture.configure(disabledforeground="#a3a3a3")
        self.Entry_couleur_voiture.configure(font="TkFixedFont")
        self.Entry_couleur_voiture.configure(foreground="#000000")
        self.Entry_couleur_voiture.configure(insertbackground="black")
        self.Entry_modele_voiture = tk.Entry(self.Labelframe2)
        self.Entry_modele_voiture.place(relx=0.763, rely=0.432, height=40
                                        , relwidth=0.21, bordermode='ignore')
        self.Entry_modele_voiture.configure(background="white")
        self.Entry_modele_voiture.configure(disabledforeground="#a3a3a3")
        self.Entry_modele_voiture.configure(font="TkFixedFont")
        self.Entry_modele_voiture.configure(foreground="#000000")
        self.Entry_modele_voiture.configure(insertbackground="black")
        self.Entry_annee_voiture = tk.Entry(self.Labelframe2)
        self.Entry_annee_voiture.place(relx=0.763, rely=0.703, height=40
                                       , relwidth=0.21, bordermode='ignore')
        self.Entry_annee_voiture.configure(background="white")
        self.Entry_annee_voiture.configure(disabledforeground="#a3a3a3")
        self.Entry_annee_voiture.configure(font="TkFixedFont")
        self.Entry_annee_voiture.configure(foreground="#000000")
        self.Entry_annee_voiture.configure(insertbackground="black")
        self.Labelframe3 = tk.LabelFrame(self.TNotebook1_t2)
        self.Labelframe3.place(relx=0.0, rely=0.386, relheight=0.498
                               , relwidth=1.0)
        self.Labelframe3.configure(relief='groove')
        self.Labelframe3.configure(foreground="#000000")
        self.Labelframe3.configure(text='''Infos propriétaire''')
        self.Labelframe3.configure(background="#ff8040")
        self.Labelframe3.configure(cursor="fleur")
        self.Label4 = tk.Label(self.Labelframe3)
        self.Label4.place(relx=0.017, rely=0.122, height=39, width=124
                          , bordermode='ignore')
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Nom :''')
        self.Label4_1 = tk.Label(self.Labelframe3)
        self.Label4_1.place(relx=0.017, rely=0.327, height=39, width=124
                            , bordermode='ignore')
        self.Label4_1.configure(activebackground="#f9f9f9")
        self.Label4_1.configure(anchor='w')
        self.Label4_1.configure(background="#d9d9d9")
        self.Label4_1.configure(compound='left')
        self.Label4_1.configure(cursor="fleur")
        self.Label4_1.configure(disabledforeground="#a3a3a3")
        self.Label4_1.configure(foreground="#000000")
        self.Label4_1.configure(highlightbackground="#d9d9d9")
        self.Label4_1.configure(highlightcolor="black")
        self.Label4_1.configure(text='''Prénom :''')
        self.Label4_1_1 = tk.Label(self.Labelframe3)
        self.Label4_1_1.place(relx=0.017, rely=0.531, height=39, width=124
                              , bordermode='ignore')
        self.Label4_1_1.configure(activebackground="#f9f9f9")
        self.Label4_1_1.configure(anchor='w')
        self.Label4_1_1.configure(background="#d9d9d9")
        self.Label4_1_1.configure(compound='left')
        self.Label4_1_1.configure(disabledforeground="#a3a3a3")
        self.Label4_1_1.configure(foreground="#000000")
        self.Label4_1_1.configure(highlightbackground="#d9d9d9")
        self.Label4_1_1.configure(highlightcolor="black")
        self.Label4_1_1.configure(text='''Courriel :''')
        self.Label4_1_1_1 = tk.Label(self.Labelframe3)
        self.Label4_1_1_1.place(relx=0.017, rely=0.735, height=39, width=124
                                , bordermode='ignore')
        self.Label4_1_1_1.configure(activebackground="#f9f9f9")
        self.Label4_1_1_1.configure(anchor='w')
        self.Label4_1_1_1.configure(background="#d9d9d9")
        self.Label4_1_1_1.configure(compound='left')
        self.Label4_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label4_1_1_1.configure(foreground="#000000")
        self.Label4_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label4_1_1_1.configure(highlightcolor="black")
        self.Label4_1_1_1.configure(text='''Téléphone :''')
        self.Entry_nom_proprio_voiture = tk.Entry(self.Labelframe3)
        self.Entry_nom_proprio_voiture.place(relx=0.254, rely=0.122, height=40
                                             , relwidth=0.363, bordermode='ignore')
        self.Entry_nom_proprio_voiture.configure(background="white")
        self.Entry_nom_proprio_voiture.configure(disabledforeground="#a3a3a3")
        self.Entry_nom_proprio_voiture.configure(font="TkFixedFont")
        self.Entry_nom_proprio_voiture.configure(foreground="#000000")
        self.Entry_nom_proprio_voiture.configure(insertbackground="black")
        self.Entry_prenom_proprio_voiture = tk.Entry(self.Labelframe3)
        self.Entry_prenom_proprio_voiture.place(relx=0.254, rely=0.327, height=40
                                                , relwidth=0.566, bordermode='ignore')
        self.Entry_prenom_proprio_voiture.configure(background="white")
        self.Entry_prenom_proprio_voiture.configure(disabledforeground="#a3a3a3")
        self.Entry_prenom_proprio_voiture.configure(font="TkFixedFont")
        self.Entry_prenom_proprio_voiture.configure(foreground="#000000")
        self.Entry_prenom_proprio_voiture.configure(insertbackground="black")
        self.Entry_courriel_proprio_voiture = tk.Entry(self.Labelframe3)
        self.Entry_courriel_proprio_voiture.place(relx=0.254, rely=0.531
                                                  , height=40, relwidth=0.6, bordermode='ignore')
        self.Entry_courriel_proprio_voiture.configure(background="white")
        self.Entry_courriel_proprio_voiture.configure(disabledforeground="#a3a3a3")
        self.Entry_courriel_proprio_voiture.configure(font="TkFixedFont")
        self.Entry_courriel_proprio_voiture.configure(foreground="#000000")
        self.Entry_courriel_proprio_voiture.configure(insertbackground="black")
        self.Entry_telephone_proprio_voiture = tk.Entry(self.Labelframe3)
        self.Entry_telephone_proprio_voiture.place(relx=0.254, rely=0.735
                                                   , height=40, relwidth=0.481, bordermode='ignore')
        self.Entry_telephone_proprio_voiture.configure(background="white")
        self.Entry_telephone_proprio_voiture.configure(disabledforeground="#a3a3a3")
        self.Entry_telephone_proprio_voiture.configure(font="TkFixedFont")
        self.Entry_telephone_proprio_voiture.configure(foreground="#000000")
        self.Entry_telephone_proprio_voiture.configure(insertbackground="black")
        self.Button_ajouter_voiture = tk.Button(self.TNotebook1_t2)
        self.Button_ajouter_voiture.place(relx=0.169, rely=0.894, height=44
                                          , width=167)
        self.Button_ajouter_voiture.configure(activebackground="beige")
        self.Button_ajouter_voiture.configure(activeforeground="black")
        self.Button_ajouter_voiture.configure(background="#d9d9d9")
        self.Button_ajouter_voiture.configure(compound='left')
        self.Button_ajouter_voiture.configure(disabledforeground="#a3a3a3")
        self.Button_ajouter_voiture.configure(foreground="#000000")
        self.Button_ajouter_voiture.configure(highlightbackground="#d9d9d9")
        self.Button_ajouter_voiture.configure(highlightcolor="black")
        self.Button_ajouter_voiture.configure(pady="0")
        self.Button_ajouter_voiture.configure(text='''Ajouter''')
        self.Button_rechercher_voiture = tk.Button(self.TNotebook1_t2)
        self.Button_rechercher_voiture.place(relx=0.508, rely=0.894, height=44
                                             , width=187)
        self.Button_rechercher_voiture.configure(activebackground="beige")
        self.Button_rechercher_voiture.configure(activeforeground="black")
        self.Button_rechercher_voiture.configure(background="#d9d9d9")
        self.Button_rechercher_voiture.configure(compound='left')
        self.Button_rechercher_voiture.configure(disabledforeground="#a3a3a3")
        self.Button_rechercher_voiture.configure(foreground="#000000")
        self.Button_rechercher_voiture.configure(highlightbackground="#d9d9d9")
        self.Button_rechercher_voiture.configure(highlightcolor="black")
        self.Button_rechercher_voiture.configure(pady="0")
        self.Button_rechercher_voiture.configure(text='''Rechercher''')

        # Page réparations

        self.Label5 = tk.Label(self.TNotebook1_t3)
        self.Label5.place(relx=0.034, rely=0.041, height=51, width=204)
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Numéro plaque :''')
        self.Label5_1 = tk.Label(self.TNotebook1_t3)
        self.Label5_1.place(relx=0.034, rely=0.183, height=51, width=204)
        self.Label5_1.configure(activebackground="#f9f9f9")
        self.Label5_1.configure(anchor='w')
        self.Label5_1.configure(background="#d9d9d9")
        self.Label5_1.configure(compound='left')
        self.Label5_1.configure(disabledforeground="#a3a3a3")
        self.Label5_1.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label5_1.configure(foreground="#000000")
        self.Label5_1.configure(highlightbackground="#d9d9d9")
        self.Label5_1.configure(highlightcolor="black")
        self.Label5_1.configure(text='''Numéro technicien  :''')
        self.Entry_numero_plaque_reparations = tk.Entry(self.TNotebook1_t3)
        self.Entry_numero_plaque_reparations.place(relx=0.407, rely=0.041
                                                   , height=50, relwidth=0.498)
        self.Entry_numero_plaque_reparations.configure(background="white")
        self.Entry_numero_plaque_reparations.configure(disabledforeground="#a3a3a3")
        self.Entry_numero_plaque_reparations.configure(font="TkFixedFont")
        self.Entry_numero_plaque_reparations.configure(foreground="#000000")
        self.Entry_numero_plaque_reparations.configure(insertbackground="black")
        self.Entry_num_technicien_reparation = tk.Entry(self.TNotebook1_t3)
        self.Entry_num_technicien_reparation.place(relx=0.407, rely=0.183
                                                   , height=50, relwidth=0.498)
        self.Entry_num_technicien_reparation.configure(background="white")
        self.Entry_num_technicien_reparation.configure(disabledforeground="#a3a3a3")
        self.Entry_num_technicien_reparation.configure(font="TkFixedFont")
        self.Entry_num_technicien_reparation.configure(foreground="#000000")
        self.Entry_num_technicien_reparation.configure(insertbackground="black")
        self.Labelframe4 = tk.LabelFrame(self.TNotebook1_t3)
        self.Labelframe4.place(relx=0.034, rely=0.325, relheight=0.457
                               , relwidth=0.932)
        self.Labelframe4.configure(relief='groove')
        self.Labelframe4.configure(foreground="#000000")
        self.Labelframe4.configure(text='''Infos réparation''')
        self.Labelframe4.configure(background="#ff8040")
        self.Label6 = tk.Label(self.Labelframe4)
        self.Label6.place(relx=0.018, rely=0.089, height=51, width=134
                          , bordermode='ignore')
        self.Label6.configure(anchor='w')
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(compound='left')
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Code :''')
        self.Label6_1 = tk.Label(self.Labelframe4)
        self.Label6_1.place(relx=0.018, rely=0.356, height=51, width=134
                            , bordermode='ignore')
        self.Label6_1.configure(activebackground="#f9f9f9")
        self.Label6_1.configure(anchor='w')
        self.Label6_1.configure(background="#d9d9d9")
        self.Label6_1.configure(compound='left')
        self.Label6_1.configure(disabledforeground="#a3a3a3")
        self.Label6_1.configure(foreground="#000000")
        self.Label6_1.configure(highlightbackground="#d9d9d9")
        self.Label6_1.configure(highlightcolor="black")
        self.Label6_1.configure(text='''Description :''')
        self.Label6_1_1 = tk.Label(self.Labelframe4)
        self.Label6_1_1.place(relx=0.018, rely=0.756, height=51, width=134
                              , bordermode='ignore')
        self.Label6_1_1.configure(activebackground="#f9f9f9")
        self.Label6_1_1.configure(anchor='w')
        self.Label6_1_1.configure(background="#d9d9d9")
        self.Label6_1_1.configure(compound='left')
        self.Label6_1_1.configure(disabledforeground="#a3a3a3")
        self.Label6_1_1.configure(foreground="#000000")
        self.Label6_1_1.configure(highlightbackground="#d9d9d9")
        self.Label6_1_1.configure(highlightcolor="black")
        self.Label6_1_1.configure(text='''Date :''')
        self.Entry_code_reparations = tk.Entry(self.Labelframe4)
        self.Entry_code_reparations.place(relx=0.273, rely=0.089, height=50
                                          , relwidth=0.262, bordermode='ignore')
        self.Entry_code_reparations.configure(background="white")
        self.Entry_code_reparations.configure(disabledforeground="#a3a3a3")
        self.Entry_code_reparations.configure(font="TkFixedFont")
        self.Entry_code_reparations.configure(foreground="#000000")
        self.Entry_code_reparations.configure(insertbackground="black")
        self.Entry_description_reparations = tk.Entry(self.Labelframe4)
        self.Entry_description_reparations.place(relx=0.273, rely=0.356
                                                 , height=80, relwidth=0.698, bordermode='ignore')
        self.Entry_description_reparations.configure(background="white")
        self.Entry_description_reparations.configure(disabledforeground="#a3a3a3")
        self.Entry_description_reparations.configure(font="TkFixedFont")
        self.Entry_description_reparations.configure(foreground="#000000")
        self.Entry_description_reparations.configure(insertbackground="black")
        self.Entry_date_reparations = tk.Entry(self.Labelframe4)
        self.Entry_date_reparations.place(relx=0.273, rely=0.756, height=50
                                          , relwidth=0.262, bordermode='ignore')
        self.Entry_date_reparations.configure(background="white")
        self.Entry_date_reparations.configure(disabledforeground="#a3a3a3")
        self.Entry_date_reparations.configure(font="TkFixedFont")
        self.Entry_date_reparations.configure(foreground="#000000")
        self.Entry_date_reparations.configure(insertbackground="black")
        self.Label6_1_1_1 = tk.Label(self.Labelframe4)
        self.Label6_1_1_1.place(relx=0.564, rely=0.756, height=51, width=94
                                , bordermode='ignore')
        self.Label6_1_1_1.configure(activebackground="#f9f9f9")
        self.Label6_1_1_1.configure(anchor='w')
        self.Label6_1_1_1.configure(background="#d9d9d9")
        self.Label6_1_1_1.configure(compound='left')
        self.Label6_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label6_1_1_1.configure(foreground="#000000")
        self.Label6_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label6_1_1_1.configure(highlightcolor="black")
        self.Label6_1_1_1.configure(text='''Montant :''')
        self.Entry_montant_reparations = tk.Entry(self.Labelframe4)
        self.Entry_montant_reparations.place(relx=0.745, rely=0.756, height=50
                                             , relwidth=0.225, bordermode='ignore')
        self.Entry_montant_reparations.configure(background="white")
        self.Entry_montant_reparations.configure(disabledforeground="#a3a3a3")
        self.Entry_montant_reparations.configure(font="TkFixedFont")
        self.Entry_montant_reparations.configure(foreground="#000000")
        self.Entry_montant_reparations.configure(insertbackground="black")
        self.Button_ajouter_reparations = tk.Button(self.TNotebook1_t3)
        self.Button_ajouter_reparations.place(relx=0.203, rely=0.813, height=64
                                              , width=157)
        self.Button_ajouter_reparations.configure(activebackground="beige")
        self.Button_ajouter_reparations.configure(activeforeground="black")
        self.Button_ajouter_reparations.configure(background="#d9d9d9")
        self.Button_ajouter_reparations.configure(compound='left')
        self.Button_ajouter_reparations.configure(cursor="fleur")
        self.Button_ajouter_reparations.configure(disabledforeground="#a3a3a3")
        self.Button_ajouter_reparations.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Button_ajouter_reparations.configure(foreground="#000000")
        self.Button_ajouter_reparations.configure(highlightbackground="#d9d9d9")
        self.Button_ajouter_reparations.configure(highlightcolor="black")
        self.Button_ajouter_reparations.configure(pady="0")
        self.Button_ajouter_reparations.configure(text='''Ajouter''')
        self.Button_supprimer_reparations_1 = tk.Button(self.TNotebook1_t3)
        self.Button_supprimer_reparations_1.place(relx=0.525, rely=0.813
                                                  , height=64, width=157)
        self.Button_supprimer_reparations_1.configure(activebackground="beige")
        self.Button_supprimer_reparations_1.configure(activeforeground="black")
        self.Button_supprimer_reparations_1.configure(background="#d9d9d9")
        self.Button_supprimer_reparations_1.configure(compound='left')
        self.Button_supprimer_reparations_1.configure(disabledforeground="#a3a3a3")
        self.Button_supprimer_reparations_1.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Button_supprimer_reparations_1.configure(foreground="#000000")
        self.Button_supprimer_reparations_1.configure(highlightbackground="#d9d9d9")
        self.Button_supprimer_reparations_1.configure(highlightcolor="black")
        self.Button_supprimer_reparations_1.configure(pady="0")
        self.Button_supprimer_reparations_1.configure(text='''Supprimer''')

        # Page consultations

        self.Label7 = tk.Label(self.TNotebook1_t4)
        self.Label7.place(relx=0.051, rely=0.041, height=61, width=154)
        self.Label7.configure(anchor='w')
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(compound='left')
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Numéro plaque :''')
        self.Label7_1 = tk.Label(self.TNotebook1_t4)
        self.Label7_1.place(relx=0.051, rely=0.203, height=61, width=154)
        self.Label7_1.configure(activebackground="#f9f9f9")
        self.Label7_1.configure(anchor='w')
        self.Label7_1.configure(background="#d9d9d9")
        self.Label7_1.configure(compound='left')
        self.Label7_1.configure(disabledforeground="#a3a3a3")
        self.Label7_1.configure(foreground="#000000")
        self.Label7_1.configure(highlightbackground="#d9d9d9")
        self.Label7_1.configure(highlightcolor="black")
        self.Label7_1.configure(text='''Marque Voiture :''')
        self.Entry_marque_voiture_consultations = tk.Entry(self.TNotebook1_t4)
        self.Entry_marque_voiture_consultations.place(relx=0.339, rely=0.203
                                                      , height=60, relwidth=0.278)
        self.Entry_marque_voiture_consultations.configure(background="white")
        self.Entry_marque_voiture_consultations.configure(disabledforeground="#a3a3a3")
        self.Entry_marque_voiture_consultations.configure(font="TkFixedFont")
        self.Entry_marque_voiture_consultations.configure(foreground="#000000")
        self.Entry_marque_voiture_consultations.configure(insertbackground="black")
        self.Button_afficher_reparation_consultations = tk.Button(self.TNotebook1_t4)
        self.Button_afficher_reparation_consultations.place(relx=0.712
                                                            , rely=0.041, height=54, width=137)
        self.Button_afficher_reparation_consultations.configure(activebackground="beige")
        self.Button_afficher_reparation_consultations.configure(activeforeground="black")
        self.Button_afficher_reparation_consultations.configure(background="#d9d9d9")
        self.Button_afficher_reparation_consultations.configure(compound='left')
        self.Button_afficher_reparation_consultations.configure(disabledforeground="#a3a3a3")
        self.Button_afficher_reparation_consultations.configure(foreground="#000000")
        self.Button_afficher_reparation_consultations.configure(highlightbackground="#d9d9d9")
        self.Button_afficher_reparation_consultations.configure(highlightcolor="black")
        self.Button_afficher_reparation_consultations.configure(pady="0")
        self.Button_afficher_reparation_consultations.configure(text='''Afficher réparations''')

        # Cération du combo box
        self.cbnumplaque = ttk.Combobox(self.TNotebook1_t4)
        self.cbnumplaque.place(relx=0.339, rely=0.041, relheight=0.126, relwidth=0.346)

        # Cération du tableau (treeview)
        colonnes: tuple[int] = (1, 2, 3, 4, 5)
        self.treeview = ttk.Treeview(self.TNotebook1_t4, columns=colonnes, show="headings")

        # associer des titres aux  colonnes du tableau
        self.treeview.heading(column=1, text='Code Réparations ')
        self.treeview.heading(column=2, text='Description')
        self.treeview.heading(column=3, text='Intervenant')
        self.treeview.heading(column=4, text='Date')
        self.treeview.heading(column=5, text='Montant')

        # configurer les colonnes du tableau (taille, allignement)
        self.treeview.column(1, width=80, anchor='e')
        self.treeview.column(2, width=80)
        self.treeview.column(3, width=80, anchor='e')
        self.treeview.column(4, width=80, anchor='e')
        self.treeview.column(5, width=80, anchor='e')

        # placer le treeview sur la fenetre principale
        self.treeview.place(relx=0.051, rely=0.366, height=241, width=524)

        # La gestion des événements
        self.Button_cree_garage.configure(command=self.btnCreerGarageClick)
        self.Button_seseriliser_garage.configure(command=self.btnSerialiserClick)
        self.Button_deseriliser_garage.configure(command=self.btnDeSerialiserClick)
        self.Button_ajouter_voiture.configure(command=self.btnAjouterVoitureClick)
        self.Button_afficher_reparation_consultations.configure(command=self.btnAfficherReparationClick)

    # Configuration des boutons

    # Boutons de la page garage
    def btnCreerGarageClick(self):
        try:
            # lire les valeurs des entry du formulaire
            nom: str = self.Entry_nom_garage.get()
            adresse: str = self.Entry_adresse_garage.get()
            telephone: str = self.Entry_telephone_garage.get()
            # ajouter le garage
            self.mongarage = Garage(nom, adresse, telephone)
        except Exception as ex:
            messagebox.showerror("Erreur", ex)

    def btnSerialiserClick(self):
        try:
            if self.Entry_fichier_garage.get().__len__() > 0:
                jsonserialiseur: Garage.serialisergarage = Garage.serialisergarage(self.mongarage, self.Entry_fichier_garage.get())
        except Exception as ex:
            messagebox.showinfo('Erreurs', 'Le nom du fichier est vide...')

    def btnDeSerialiserClick(self, *args):
        try:
            if self.Entry_fichier_garage.get().__len__() > 0:
                jsonserialiseur: Garage.deserialisergarage = Garage.deserialisergarage(self.Entry_fichier_garage.get())
                # Affecte le résultat à la propriété "__mongarage"
                self.mongarage = jsonserialiseur
        except Exception as ex:
            messagebox.showinfo('Erreurs', 'Le nom du fichier est vide...')

    # Boutons de la page voiture
    def btnAjouterVoitureClick(self):
        try:
            # lire les valeurs des entry du formulaire
            num_plaque: str = self.Entry_num_plaque_voiture.get()
            marque: str = self.Entry_marque_voiture.get()
            couleur: str = self.Entry_couleur_voiture.get()
            modele: str = self.Entry_modele_voiture.get()
            annee: int = int(self.Entry_annee_voiture.get())
            nom_proprio: str = self.Entry_nom_proprio_voiture.get()
            prenom_proprio: str = self.Entry_prenom_proprio_voiture.get()
            courriel_proprio: str = self.Entry_courriel_proprio_voiture.get()
            telephone_proprio: str = self.Entry_telephone_proprio_voiture.get()
            # créer une voiture
            voiture: Voiture = Voiture(num_plaque, marque, modele, couleur, annee, Client(nom_proprio, prenom_proprio, telephone_proprio, courriel_proprio))
            # appelle la méthode et lui envoie une valeur en paramètre
            self.mongarage.ajoutervoiture(voiture)
            messagebox.showinfo('Infos', 'Voiture et propriétaire ajouté avec succès !')
        except ValueError as ex:
            messagebox.showerror('Erreur', ex.args[0])

    # Boutons et autre fonction de la page configuration
    def get_numero_plaque_Combobox(self):
        ls_numero_plaque = []
        num_plaque: str = self.Entry_num_plaque_voiture.get()
        voiture: Voiture = self.mongarage.getvoiture(num_plaque)
        if voiture is not None:
            ls_numero_plaque.append(voiture.get_numeroplaque())
        self.cbnumplaque.configure(values=ls_numero_plaque)

    def btnAfficherReparationClick(self):
        # Vider le treeview
        for element in self.treeview.get_children():
            self.treeview.delete(element)
        # Remplir le treeview
        i = 0
        num_plaque = self.cbnumplaque
        try:
            for voiture in num_plaque:
                if self.mongarage.getvoiture(voiture) == num_plaque:
                    i += 1
                    self.treeview.insert("", "end", iid=str(i), values=(self.Entry_code_reparations,
                                                                        self.Entry_description_reparations,
                                                                        self.Entry_num_technicien_reparation,
                                                                        self.Entry_date_reparations,
                                                                        self.Entry_montant_reparations))
        except Exception as ex:
            messagebox.showerror("Erreur", ex)

def start_up():
    root = tk.Tk()
    projetfinalui: ProjetFinalUI = ProjetFinalUI(root)
    root.mainloop()

if __name__ == '__main__':
    start_up()
