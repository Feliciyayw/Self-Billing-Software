# @contributed by 'Web Code' youtube
# @Develop by Feliciya-C13210027, Joyceline-C13210026, Tamara-C13210067

from tkinter import*
import math,random,os
from tkinter import messagebox
import pandas as pd
import numpy as np

file_database_object = 'C:/Users/Lenovo/Documents/College/2nd Semester/Computer science/Data Analysis/DatabaseCode.csv'
data=pd.read_csv(file_database_object, low_memory=False)

##Merchandise Price###
A1_price=data.loc[data['CodeA']=='A1','PriceA'].iloc[0]
A2_price=data.loc[data['CodeA']=='A2','PriceA'].iloc[0]
A3_price=data.loc[data['CodeA']=='A3','PriceA'].iloc[0]
A4_price=data.loc[data['CodeA']=='A4','PriceA'].iloc[0]
A5_price=data.loc[data['CodeA']=='A5','PriceA'].iloc[0]
A6_price=data.loc[data['CodeA']=='A6','PriceA'].iloc[0]

###Drinks Price##
B1_price=data.loc[data['CodeB']=='B1','PriceB'].iloc[0]
B2_price=data.loc[data['CodeB']=='B2','PriceB'].iloc[0]
B3_price=data.loc[data['CodeB']=='B3','PriceB'].iloc[0]
B4_price=data.loc[data['CodeB']=='B4','PriceB'].iloc[0]
B5_price=data.loc[data['CodeB']=='B5','PriceB'].iloc[0]
B6_price=data.loc[data['CodeB']=='B6','PriceB'].iloc[0]

##Food Price###
C1_price=data.loc[data['CodeC']=='C1','PriceC'].iloc[0]
C2_price=data.loc[data['CodeC']=='C2','PriceC'].iloc[0]
C3_price=data.loc[data['CodeC']=='C3','PriceC'].iloc[0]
C4_price=data.loc[data['CodeC']=='C4','PriceC'].iloc[0]
C5_price=data.loc[data['CodeC']=='C5','PriceC'].iloc[0]
C6_price=data.loc[data['CodeC']=='C6','PriceC'].iloc[0]

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("SNEAKY HONEY SELF-BILLING")
        col_violet="#06114F"
        text_color="#D90077"
        bg_color="#F89F58"
        title=Label(self.root,text="SNEAKY HONEY SELF-BILLING",bd=10,relief=GROOVE,bg=col_violet,fg=text_color,font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #========Variable===================
        #========Merchandise=================
        self.tumbler=IntVar()
        self.mug=IntVar()
        self.t_shirt=IntVar()
        self.tote_bag=IntVar()
        self.photocard=IntVar()
        self.notebook=IntVar()
        #========Drinks===================
        self.java_tea=IntVar()
        self.milo_dinosaur=IntVar()
        self.coca_cola=IntVar()
        self.sprite=IntVar()
        self.fanta=IntVar()
        self.mineral_water=IntVar()
        #=======Food===============
        self.popcorn=IntVar()
        self.hotdog=IntVar()
        self.fish_and_chip=IntVar()
        self.nachos=IntVar()
        self.burger=IntVar()
        self.french_fries=IntVar()

        #==========Total Product Price & Tax Variable=====
        self.merchandise_price=StringVar()
        self.drinks_price=StringVar()
        self.food_price=StringVar()

        self.merchandise_tax=StringVar()
        self.drinks_tax=StringVar()
        self.food_tax=StringVar()

        #==========Customer=================
        self.c_name=StringVar()
        self.c_phone=StringVar()

        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()



        #=================Customer Detail Frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="#3F1651",bg=bg_color)
        F1.place(x=0,y=73,relwidth=1,height=100)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg=text_color,font=("times new roman",18,"bold")).grid(row=0, column=0,padx=20,pady=1)
        cname_txt=Entry(F1, width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=1,padx=10)

        cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg=text_color,font=("times new roman",18,"bold")).grid(row=0, column=2,padx=20,pady=5)
        cphn_txt=Entry(F1, width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg=text_color,font=("times new roman",18,"bold")).grid(row=0, column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1, width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=7,bd=7,font="arial 12 bold").grid(row=0, column=6,padx=10,pady=10)


        #=========merchandise Frame==================
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Merchandise Frame",font=("times new roman",15,"bold"),fg="#3F1651",bg=bg_color)
        F2.place(x=0,y=177,width=325,height=330)

        tumbler_lbl=Label(F2,text="Tumbler",font=("times new roman",16,"bold"),bg=bg_color,fg="#2E36AA").grid(row=0,column=0,padx=10,pady=5,sticky="w")
        tumbler_txt=Entry(F2,width=10,textvariable=self.tumbler,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        mug_lbl=Label(F2,text="Mug",font=("times new roman",16,"bold"),bg=bg_color,fg="#2E36AA").grid(row=1,column=0,padx=10,pady=5,sticky="w")
        mug_txt=Entry(F2,width=10,textvariable=self.mug,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)

        t_shirt_lbl=Label(F2,text="T-Shirt",font=("times new roman",16,"bold"),bg=bg_color,fg="#2E36AA").grid(row=2,column=0,padx=10,pady=5,sticky="w")
        t_shirt_txt=Entry(F2,width=10,textvariable=self.t_shirt,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=5)

        tote_bag_lbl=Label(F2,text="Tote Bag",font=("times new roman",16,"bold"),bg=bg_color,fg="#2E36AA").grid(row=3,column=0,padx=10,pady=5,sticky="w")
        tote_bag_txt=Entry(F2,width=10,textvariable=self.tote_bag,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=5)

        photocard_lbl=Label(F2,text="Photocard",font=("times new roman",16,"bold"),bg=bg_color,fg="#2E36AA").grid(row=4,column=0,padx=10,pady=5,sticky="w")
        photocard_txt=Entry(F2,width=10,textvariable=self.photocard,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=5)

        notebook_lbl=Label(F2,text="Notebook",font=("times new roman",16,"bold"),bg=bg_color,fg="#2E36AA").grid(row=5,column=0,padx=10,pady=5,sticky="w")
        notebook_txt=Entry(F2,width=10,textvariable=self.notebook,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=5)

        #=========Drinks Frame==================
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Drinks Frame",font=("times new roman",15,"bold"),fg="#3F1651",bg=bg_color)
        F3.place(x=335,y=177,width=285,height=330)

        d1_lbl=Label(F3,text="Java Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="#2E36AA").grid(row=0,column=0,padx=10,pady=5,sticky="w")
        d1_txt=Entry(F3,width=10,textvariable=self.java_tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        d2_lbl=Label(F3,text="Milo Dino",font=("times new roman",16,"bold"),bg=bg_color,fg="#2E36AA").grid(row=1,column=0,padx=10,pady=5,sticky="w")
        d2_txt=Entry(F3,width=10,textvariable=self.milo_dinosaur,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)

        d3_lbl=Label(F3,text="Coca Cola",font=("times new roman",16,"bold"),bg=bg_color,fg="#2E36AA").grid(row=2,column=0,padx=10,pady=5,sticky="w")
        d3_txt=Entry(F3,width=10,textvariable=self.coca_cola,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=5)

        d4_lbl=Label(F3,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="#2E36AA").grid(row=3,column=0,padx=10,pady=5,sticky="w")
        d4_txt=Entry(F3,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=5)

        d5_lbl=Label(F3,text="Fanta",font=("times new roman",16,"bold"),bg=bg_color,fg="#2E36AA").grid(row=4,column=0,padx=10,pady=5,sticky="w")
        d5_txt=Entry(F3,width=10,textvariable=self.fanta,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=5)

        d6_lbl=Label(F3,text="Water",font=("times new roman",16,"bold"),bg=bg_color,fg="#2E36AA").grid(row=5,column=0,padx=10,pady=5,sticky="w")
        d6_txt=Entry(F3,width=10,textvariable=self.mineral_water,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=5)

        #=========Food Frame==================
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Food",font=("times new roman",15,"bold"),fg="#3F1651",bg=bg_color)
        F4.place(x=630,y=177,width=310,height=330)

        f1_lbl=Label(F4,text="Popcorn",font=("times new roman",16,"bold"),bg=bg_color,fg="#2E36AA").grid(row=0,column=0,padx=10,pady=5,sticky="w")
        f1_txt=Entry(F4,width=10,textvariable=self.popcorn,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        f2_lbl=Label(F4,text="Hotdog",font=("times new roman",16,"bold"),bg=bg_color,fg="#2E36AA").grid(row=1,column=0,padx=10,pady=5,sticky="w")
        f2_txt=Entry(F4,width=10,textvariable=self.hotdog,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)

        f3_lbl=Label(F4,text="Fish n Chip",font=("times new roman",16,"bold"),bg=bg_color,fg="#2E36AA").grid(row=2,column=0,padx=10,pady=5,sticky="w")
        f3_txt=Entry(F4,width=10,textvariable=self.fish_and_chip,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=5)

        f4_lbl=Label(F4,text="Nachos",font=("times new roman",16,"bold"),bg=bg_color,fg="#2E36AA").grid(row=3,column=0,padx=10,pady=5,sticky="w")
        f4_txt=Entry(F4,width=10,textvariable=self.nachos,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=5)

        f5_lbl=Label(F4,text="Burger",font=("times new roman",16,"bold"),bg=bg_color,fg="#2E36AA").grid(row=4,column=0,padx=10,pady=5,sticky="w")
        f5_txt=Entry(F4,width=10,textvariable=self.burger,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=5)

        f6_lbl=Label(F4,text="French Fries",font=("times new roman",16,"bold"),bg=bg_color,fg="#2E36AA").grid(row=5,column=0,padx=10,pady=5,sticky="w")
        f6_txt=Entry(F4,width=10,textvariable=self.french_fries,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=5)

        #=======Bill Area===========
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=950,y=177,width=330,height=330)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #========Button Frame===========
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="#3F1651",bg=bg_color)
        F6.place(x=0,y=510,relwidth=1,height=140)\

        m1=Label(F6,text="Total Merchandise Price",bg=bg_color,fg="#2E36AA",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=0.5,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.merchandise_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=0.5)

        m2=Label(F6,text="Total Drinks Price",bg=bg_color,fg="#2E36AA",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.drinks_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3=Label(F6,text="Total Food Price",bg=bg_color,fg="#2E36AA",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.food_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1=Label(F6,text="Merchan Tax",bg=bg_color,fg="#2E36AA",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=0.5,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.merchandise_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=0.5)

        c2=Label(F6,text="Drinks  Tax",bg=bg_color,fg="#2E36AA",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.drinks_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3=Label(F6,text="Food Tax",bg=bg_color,fg="#2E36AA",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.food_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=740,width=510,height=95)

        total_btn=Button(btn_F,command=self.total,text="Total",bg=text_color,fg="white",bd=2,pady=17,width=10,font="arial 12 bold").grid(row=0,column=0,padx=5,pady=6)
        Gbill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg=text_color,fg="white",bd=2,pady=17,width=11,font="arial 12 bold").grid(row=0,column=1,padx=5,pady=6)
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg=text_color,fg="white",bd=2,pady=17,width=10,font="arial 12 bold").grid(row=0,column=2,padx=5,pady=6)
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg=text_color,fg="white",bd=2,pady=17,width=10,font="arial 12 bold").grid(row=0,column=3,padx=5,pady=6)
        self.welcome_bill()
    
    def total(self):
        
        self.m_t_p=self.tumbler.get()*int(A1_price)
        self.m_m_p=self.mug.get()*int(A2_price)
        self.m_ts_p=self.t_shirt.get()*int(A3_price)
        self.m_tb_p=self.tote_bag.get()*int(A4_price)
        self.m_pc_p=self.photocard.get()*int(A5_price)
        self.m_nb_p=self.notebook.get()*int(A6_price)

        self.total_merchandise_price=float(
                                        self.m_t_p+
                                        self.m_m_p+
                                        self.m_ts_p+
                                        self.m_tb_p+
                                        self.m_pc_p+
                                        self.m_nb_p
                                        )
        self.merchandise_price.set("USD "+str(self.total_merchandise_price))
        self.m_tax=round((self.total_merchandise_price*0.11),2)
        self.merchandise_tax.set("USD "+str(self.m_tax))
        

        self.d_jt_p=self.java_tea.get()*int(B1_price)
        self.d_md_p=self.milo_dinosaur.get()*int(B2_price)
        self.d_cc_p=self.coca_cola.get()*int(B3_price)
        self.d_s_p=self.sprite.get()*int(B4_price)
        self.d_f_p=self.fanta.get()*int(B5_price)
        self.d_mw_p=self.mineral_water.get()*int(B6_price)

        self.total_drinks_price=float(
                                        self.d_jt_p+
                                        self.d_md_p+
                                        self.d_cc_p+
                                        self.d_s_p+
                                        self.d_f_p+
                                        self.d_mw_p
                                        )
        self.drinks_price.set("USD "+str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price*0.11),2)
        self.drinks_tax.set("USD "+str(self.d_tax))

        self.f_pc_p=self.popcorn.get()*int(C1_price)
        self.f_hd_p=self.hotdog.get()*int(C2_price)
        self.f_fnc_p=self.fish_and_chip.get()*int(C3_price)
        self.f_n_p=self.nachos.get()*int(C4_price)
        self.f_b_p=self.burger.get()*int(C5_price)
        self.f_ff_p=self.french_fries.get()*int(C6_price)

        self.total_food_price=float(
                                        self.f_pc_p+
                                        self.f_hd_p+
                                        self.f_fnc_p+
                                        self.f_n_p+
                                        self.f_b_p+
                                        self.f_ff_p
                                        )
        self.food_price.set("USD "+str(self.total_food_price))
        self.f_tax=round((self.total_food_price*0.11),2)
        self.food_tax.set("USD "+str(self.f_tax))

        self.Total_bill=float(  self.total_merchandise_price+
                                self.total_drinks_price+
                                self.total_food_price+
                                self.m_tax+
                                self.d_tax+
                                self.f_tax
                            )
        self.Total_bill=round((self.Total_bill*1),3)

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWELCOME TO SNEAKY HONEY")
        self.txtarea.insert(END,"\t                        ")
        self.txtarea.insert(END,f"\nBill Number   : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone Number  : {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n====================================")
        self.txtarea.insert(END,f"\n  Products\t\t    QTY\t    Price")
        self.txtarea.insert(END,f"\n====================================")
        

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("System Error","Customer details are must be filled")
        elif self.merchandise_price.get()=="USD 0.0" and self.drinks_price.get()=="USD 0.0" and self.food_price.get()=="USD 0.0":
            messagebox.showerror("System Error","No product purchased")
        elif self.merchandise_price.get()=="" and self.drinks_price.get()=="" and self.food_price.get()=="":
            messagebox.showerror("System Error","No product purchased")
        else:
            self.welcome_bill()
            #=======merchandise==========
            if self.tumbler.get()!=0:
                self.txtarea.insert(END,f"\n  Tumbler\t\t     {self.tumbler.get()}\t    {self.m_t_p}")

            if self.mug.get()!=0:
                self.txtarea.insert(END,f"\n  Mug\t\t     {self.mug.get()}\t    {self.m_m_p}")

            if self.t_shirt.get()!=0:
                self.txtarea.insert(END,f"\n  T-Shirt\t\t     {self.t_shirt.get()}\t    {self.m_ts_p}")
            
            if self.tote_bag.get()!=0:
                self.txtarea.insert(END,f"\n  Tote Bag\t\t     {self.tote_bag.get()}\t    {self.m_tb_p}")

            if self.photocard.get()!=0:
                self.txtarea.insert(END,f"\n  Photocard\t\t     {self.photocard.get()}\t    {self.m_pc_p}")

            if self.notebook.get()!=0:
                self.txtarea.insert(END,f"\n  Notebook\t\t     {self.notebook.get()}\t    {self.m_nb_p}")
            
            #=======Drinks==========
            if self.java_tea.get()!=0:
                self.txtarea.insert(END,f"\n  Java Tea\t\t     {self.java_tea.get()}\t    {self.d_jt_p}")

            if self.milo_dinosaur.get()!=0:
                self.txtarea.insert(END,f"\n  Milo Dinosaur\t\t    {self.milo_dinosaur.get()}\t    {self.d_md_p}")

            if self.coca_cola.get()!=0:
                self.txtarea.insert(END,f"\n  Coca Cola\t\t     {self.coca_cola.get()}\t    {self.d_cc_p}")
            
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n  Sprite\t\t     {self.sprite.get()}\t    {self.d_s_p}")

            if self.fanta.get()!=0:
                self.txtarea.insert(END,f"\n  Fanta\t\t     {self.fanta.get()}\t    {self.d_f_p}")

            if self.mineral_water.get()!=0:
                self.txtarea.insert(END,f"\n  Mineral Water\t\t    {self.mineral_water.get()}\t    {self.d_mw_p}")
            
            #=======Food==========
            if self.popcorn.get()!=0:
                self.txtarea.insert(END,f"\n  Popcorn\t\t     {self.popcorn.get()}\t    {self.f_pc_p}")

            if self.hotdog.get()!=0:
                self.txtarea.insert(END,f"\n  Hotdog\t\t     {self.hotdog.get()}\t    {self.f_hd_p}")

            if self.fish_and_chip.get()!=0:
                self.txtarea.insert(END,f"\n  Fish n Chips\t\t     {self.fish_and_chip.get()}\t    {self.f_fnc_p}")
            
            if self.nachos.get()!=0:
                self.txtarea.insert(END,f"\n  Nachos\t\t     {self.nachos.get()}\t    {self.f_n_p}")

            if self.burger.get()!=0:
                self.txtarea.insert(END,f"\n  Burger\t\t     {self.burger.get()}\t    {self.f_b_p}")

            if self.french_fries.get()!=0:
                self.txtarea.insert(END,f"\n  French Fries\t\t     {self.french_fries.get()}\t    {self.f_ff_p}")

            self.txtarea.insert(END,f"\n------------------------------------")
            if self.merchandise_tax.get()!="USD 0.0":
                self.txtarea.insert(END,f"\n  Merchandise Tax\t\t  \t{self.merchandise_tax.get()}")

            if self.drinks_tax.get()!="USD 0.0":
                self.txtarea.insert(END,f"\n  Drinks Tax\t\t  \t{self.drinks_tax.get()}")

            if self.food_tax.get()!="USD 0.0":
                self.txtarea.insert(END,f"\n  Food Tax\t\t  \t{self.food_tax.get()}")
            

            self.txtarea.insert(END,f"\n  Total Bill\t\t  \tUSD {str(self.Total_bill)}")
            self.txtarea.insert(END,f"\n------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("C:/Users/Lenovo/Documents/College/2nd Semester/Computer science/PROJECT/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no-{self.bill_no.get()} saved successfully")
        else:
            return
        
    def find_bill(self):
        present="no"                                                                                  
        for i in os.listdir("C:/Users/Lenovo/Documents/College/2nd Semester/Computer science/PROJECT/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"C:/Users/Lenovo/Documents/College/2nd Semester/Computer science/PROJECT/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid bill No.")
    
    def clear_data(self):
        op=messagebox.askyesno("Clear Data","Do you really want to Clear Data ?")
        if op>0:

            #========merchandise=================
            self.tumbler.set(0)
            self.mug.set(0)
            self.t_shirt.set(0)
            self.tote_bag.set(0)
            self.photocard.set(0)
            self.notebook.set(0)
            #========drinks===================
            self.java_tea.set(0)
            self.milo_dinosaur.set(0)
            self.coca_cola.set(0)
            self.sprite.set(0)
            self.fanta.set(0)
            self.mineral_water.set(0)
            #=======Cold Drink===============
            self.popcorn.set(0)
            self.hotdog.set(0)
            self.fish_and_chip.set(0)
            self.nachos.set(0)
            self.burger.set(0)
            self.french_fries.set(0)

            #==========Total Product Price & Tax Variable=====
            self.merchandise_price.set("")
            self.drinks_price.set("")
            self.food_price.set("")

            self.merchandise_tax.set("")
            self.drinks_tax.set("")
            self.food_tax.set("")

            #==========Customer=================
            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to Exit ?")
        if op>0:
            self.root.destroy()
        


root=Tk()
obj = Bill_App(root)
root.mainloop()