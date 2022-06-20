from tkinter import*
import random
import time
import datetime

root = Tk()
root.geometry("1600x8000")
root.title("Restaurant management System")
Tops=Frame(root, width=1600,relief=SUNKEN)  # A relief is a border decoration. The possible values are:SUNKEN,RAISED,GROOVE,RIDGE,and FLAT.
Tops.pack(side=TOP)

f1 = Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

#=================================================================================
#                  TIME
#================================================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('helvetica',20,'italic'),text="APANA RESTAURANT ",fg="Red",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

def Ref():
    x = random.randint(10000, 500000)
    random_reference = str(x)
    rand.set(random_reference)

    if (Fries.get() == ""):
        cost_Fries = 0
    else:
        cost_Fries = float(Fries.get())

    if (Noodles.get() == ""):
        cost_Noodles = 0
    else:
        cost_Noodles = float(Noodles.get())

    if (Drinks.get() == ""):
        cost_Drinks = 0
    else:
        cost_Drinks = float(Drinks.get())

    if (Soups.get() == ""):
        cost_Soups = 0
    else:
        cost_Soups = float(Soups.get())

    if (Biryani.get() == ""):
        cost_Biryani = 0
    else:
        cost_Biryani = float(Biryani.get())

    if (Pizzas.get() == ""):
        cost_Pizzas = 0
    else:
        cost_Pizzas = float(Pizzas.get())

    if (Burgers.get() == ""):
        cost_Burgers = 0
    else:
        cost_Burgers = float(Burgers.get())

    if (Sandwiches.get() == ""):
        cost_Sandwiches = 0
    else:
        cost_Sandwiches = float(Sandwiches.get())

    cost_of_Fries = cost_Fries * 50
    cost_of_Noodles = cost_Noodles * 70
    cost_of_Drinks = cost_Drinks * 40
    cost_of_Soups = cost_Soups * 80
    cost_of_Biryani = cost_Biryani * 200
    cost_of_Pizzas = cost_Pizzas * 180
    cost_of_Burgers = cost_Burgers * 120
    cost_of_Sandwiches = cost_Sandwiches * 60

    cost_of_Meal = "Rs.", str("%.2f" %(cost_of_Fries + cost_of_Noodles + cost_of_Drinks + cost_of_Soups + cost_of_Biryani + cost_of_Pizzas + cost_of_Burgers + cost_of_Sandwiches))

    cost_of_Tax = ((cost_of_Fries + cost_of_Noodles + cost_of_Drinks + cost_of_Soups + cost_of_Biryani + cost_of_Pizzas + cost_of_Burgers + cost_of_Sandwiches)* 0.2 )

    Total_charges = ((cost_of_Fries + cost_of_Noodles + cost_of_Drinks + cost_of_Soups + cost_of_Biryani + cost_of_Pizzas + cost_of_Burgers + cost_of_Sandwiches ))

    Service_charges1 = ((cost_of_Fries + cost_of_Noodles + cost_of_Drinks + cost_of_Soups + cost_of_Biryani + cost_of_Pizzas + cost_of_Burgers + cost_of_Sandwiches)/ 99)

    Service = "Rs.", str("%.2f" % Service_charges)

    Overall_cost = "Rs.", str("%.2f" %(cost_of_Tax + Total_charges + Service_charges))

    Paid_Tax = "Rs.", str("%.2f" %(cost_of_Tax))

    Service_charges.set(Service_charges1)

    Cost.set(cost_of_Meal)

    Tax.set(Paid_Tax)

    Subtotal.set(cost_of_Meal)

    Total.set(Overall_cost)





def ref_Exit():
    root.destroy()

def ref_Reset():
    rand.set("")
    Fries.set("")
    Noodles.set("")
    Drinks.set("")
    Soups.set("")
    Biryani.set("")
    Pizzas.set("")
    Burgers.set("")
    Sandwiches.set("")
    Subtotal.set("")
    Total.set("")
    Service_charges.set("")
    Tax.set("")








############################################## RESTAURANT INFO #############################################
rand = StringVar()
Fries = StringVar()
Noodles = StringVar()
Drinks = StringVar()
Soups = StringVar()
Biryani = StringVar()
Pizzas = StringVar()
Burgers = StringVar()
Sandwiches = StringVar()


Subtotal = StringVar()
Total = StringVar()
Service_charges = StringVar()
Tax = StringVar()





################################################ Reference #############################################################

lblreference = Label(f1, font = ("Times New Roman",16,"bold"),text = "Reference",bd = 16,anchor = "w")
lblreference.grid(row = 0, column = 0)
textreference = Entry(f1, font = ("Times New Roman",16,"bold"),textvariable = rand, bd = 10, insertwidth = 4, bg = "powder blue", justify = "right")
textreference.grid(row = 0, column = 1)

################################################ Fries  ################################################################

lblFries = Label(f1, font = ("Times New Roman",16,"bold"),text = "Fries",bd = 16,anchor = "w")
lblFries.grid(row = 1, column = 0)
textFries = Entry(f1, font = ("Times New Roman",16,"bold"),textvariable = Fries, bd = 10, insertwidth = 4, bg = "powder blue", justify = "right")
textFries.grid(row = 1, column = 1)

################################################ Noodles  ##############################################################

lblNoodles = Label(f1, font = ("Times New Roman",16,"bold"),text = "Noodles",bd = 16,anchor = "w")
lblNoodles.grid(row = 2, column = 0)
textNoodles = Entry(f1, font = ("Times New Roman",16,"bold"),textvariable = Noodles, bd = 10, insertwidth = 4, bg = "powder blue", justify = "right")
textNoodles.grid(row = 2, column = 1)

################################################ Drinks  ###############################################################

lblDrinks = Label(f1, font = ("Times New Roman",16,"bold"),text = "Drinks",bd = 16,anchor = "w")
lblDrinks.grid(row = 3, column = 0)
textDrinks = Entry(f1, font = ("Times New Roman",16,"bold"),textvariable = Drinks, bd = 10, insertwidth = 4, bg = "powder blue", justify = "right")
textDrinks.grid(row = 3, column = 1)

################################################ 2nd Info ##############################################################
################################################ Soups #################################################################

lblSoups = Label(f1, font = ("Times New Roman",16,"bold"),text = "Soups",bd = 16,anchor = "w")
lblSoups.grid(row = 0, column = 2)
textSoups = Entry(f1, font = ("Times New Roman",16,"bold"),textvariable = Soups, bd = 10, insertwidth = 4, bg = "powder blue", justify = "right")
textSoups.grid(row = 0, column = 3)

################################################ Biryanis  #############################################################

lblBiryanis = Label(f1, font = ("Times New Roman",16,"bold"),text = "Biryanis",bd = 16,anchor = "w")
lblBiryanis.grid(row = 1, column = 2)
textBiryanis = Entry(f1, font = ("Times New Roman",16,"bold"),textvariable = Biryani, bd = 10, insertwidth = 4, bg = "powder blue", justify = "right")
textBiryanis.grid(row = 1, column = 3)

################################################ Pizzas  ###############################################################

lblPizzas= Label(f1, font = ("Times New Roman",16,"bold"),text = "Pizzas",bd = 16,anchor = "w")
lblPizzas.grid(row = 2, column = 2)
textPizzas = Entry(f1, font = ("Times New Roman",16,"bold"),textvariable = Pizzas, bd = 10, insertwidth = 4, bg = "powder blue", justify = "right")
textPizzas.grid(row = 2, column = 3)

################################################ Burgers  ##############################################################

lblBurgerss = Label(f1, font = ("Times New Roman",16,"bold"),text = "Burgers",bd = 16,anchor = "w")
lblBurgerss.grid(row = 3, column = 2)
textBurgerss = Entry(f1, font = ("Times New Roman",16,"bold"),textvariable = Burgers, bd = 10, insertwidth = 4, bg = "powder blue", justify = "right")
textBurgerss.grid(row = 3, column = 3)

################################################ Sandwiches  ###########################################################

lblSandwichess = Label(f1, font = ("Times New Roman",16,"bold"),text = "Sandwiches",bd = 16,anchor = "w")
lblSandwichess.grid(row = 4, column = 0)
textSandwiches = Entry(f1, font = ("Times New Roman",16,"bold"),textvariable = Sandwiches, bd = 10, insertwidth = 4, bg = "powder blue", justify = "right")
textSandwiches.grid(row = 4, column = 1)
################################################ 3rd Info ##############################################################
################################################ Subtotal  #############################################################

lblSubtotal = Label(f1, font = ("Times New Roman",16,"bold"),text = "Subtotal",bd = 16,anchor = "w")
lblSubtotal.grid(row = 0, column = 4)
textSubtotal = Entry(f1, font = ("Times New Roman",16,"bold"),textvariable = Subtotal, bd = 10, insertwidth = 4, bg = "powder blue", justify = "right")
textSubtotal.grid(row = 0, column = 5)

################################################ Total  ################################################################

lblTotal = Label(f1, font = ("Times New Roman",16,"bold"),text = "Total",bd = 16,anchor = "w")
lblTotal.grid(row = 1, column = 4)
textTotal = Entry(f1, font = ("Times New Roman",16,"bold"),textvariable = Total, bd = 10, insertwidth = 4, bg = "powder blue", justify = "right")
textTotal.grid(row = 1, column = 5)

################################################ Service_charges  ######################################################

lblService_charges = Label(f1, font = ("Times New Roman",16,"bold"),text = "Service_charges",bd = 16,anchor = "w")
lblService_charges.grid(row = 2, column = 4)
textService_charges = Entry(f1, font = ("Times New Roman",16,"bold"),textvariable = Service_charges, bd = 10, insertwidth = 4, bg = "powder blue", justify = "right")
textService_charges.grid(row = 2, column = 5)

################################################ Tax  ##################################################################

lblTax = Label(f1, font = ("Times New Roman",16,"bold"),text = "Tax",bd = 16,anchor = "w")
lblTax.grid(row = 3, column = 4)
textTax = Entry(f1, font = ("Times New Roman",16,"bold"),textvariable = Tax, bd = 10, insertwidth = 4, bg = "powder blue", justify = "right")
textTax.grid(row = 3, column = 5)



########################################### Buttons ########################################

btn_total = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", font = ("Times New Roman",16,"bold"), width = 10, text = "Total", bg = "powder blue", command = Ref )
btn_total.grid(row = 7, column = 1)

btn_reset = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", font = ("Times New Roman",16,"bold"), width = 10, text = "Reset", bg = "powder blue", command = ref_Reset )
btn_reset.grid(row = 7 , column = 2)

btn_exit = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", font = ("Times New Roman",16,"bold"), width = 10, text = "Exit", bg = "powder blue", command = ref_Exit )
btn_exit.grid(row = 7, column = 3)






root.mainloop()
