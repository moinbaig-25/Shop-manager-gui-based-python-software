products = []
billing = []
import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox
import json
from pathlib import Path
shop_file = Path(__file__).with_name("shop.json")
if not shop_file.exists():
    shop_file.write_text("[]")

with open(shop_file,"r") as file:
    products = json.load(file)


shop_billing = Path(__file__).with_name("billing.json")

with open(shop_billing,"r") as file:
    billing = json.load(file)




def add_products():

    product_name = entry_name.get()
    product_price = int(entry_price.get())
    product_quantity = int(quantity.get())

    product_id = int(entry_id.get())

    for product in products:
        if product_name.lower() == product["Product"].lower():
            product["Quantity"] += product_quantity
            

    
        

    else:

        product_dict = {"Product":product_name,"ID":product_id,"Price":product_price,"Quantity":product_quantity}

        products.append(product_dict)

    with open(shop_file,"w") as file:
        json.dump(products,file,indent=4)

        entry_name.delete(0,tk.END)
        entry_id.delete(0,tk.END)
        entry_price.delete(0,tk.END)
        quantity.set("")

    messagebox.showinfo("success",f"{product_name} was added successfully!")


def show_list():

    list_items.delete(0,tk.END)
    for product in products:

        name = product["Product"]
        ids= product["ID"]
        price=product["Price"]
        quant= product["Quantity"]

        list_items.insert(tk.END,f"Name of product:  {name}")
        list_items.insert(tk.END,f"ID:{ids}")
        list_items.insert(tk.END ,f"Price:{price}₹")
        stock_index = list_items.size()
        list_items.insert(tk.END,f"In stock:{quant} left")
        if quant <= 3:
            list_items.itemconfig(stock_index,fg="red")
        list_items.insert(tk.END,"--------------------------------")

       


def ok_command():
    list_items.delete(0,tk.END)




def add_amount():
    grand_total = 0
    list_box_total.delete(0,tk.END)
    
    
    
    product_name = entry_bill_name.get()
    product_q = int(entry_quant.get())


    for product in products:
        if product_name.lower() == product["Product"].lower():
            name_1 = product["Product"]
            price = product["Price"]
            quantity = (product["Quantity"])

            
            billing_dict = {"name":name_1,"price":price,"quantity":product_q}
            billing.append(billing_dict)
    with open(shop_billing,"w") as file:
        json.dump(billing,file,indent=4)

    for items in billing:
        grand_total += items["price"] * items["quantity"]

    list_box_total.insert(tk.END,f"{grand_total}")

    entry_bill_name.delete(0,tk.END)
    entry_quant.set("")



def list_of_bill_items():

    list_added.delete(0,tk.END)

    number = 1

    for bill in billing:
        name = bill["name"]
        price = bill["price"]
        quantity = bill ["quantity"]

        amount = price * quantity

        list_added.insert(tk.END,f"{number}.{name}--{price}₹--{quantity}X--{amount}₹")

        number +=1 


def done_button():
    list_added.delete(0,tk.END)
    list_box_total.delete(0,tk.END)

    billing.clear() 

    with open(shop_billing,"w") as file:
       json.dump(billing,file,indent=4)


def update_stock():

    for product in products:
        for bill in billing:

            if bill["name"] == product["Product"]:

                product["Quantity"] -= bill["quantity"]


    with open(shop_file,"w") as file:
        json.dump(products,file,indent=4)









                











#--------------------------------------------------------------------------------------

window = tk.Tk()
window.geometry("1500x1000")
window.title("Shop Manager")

frame = tk.Frame(window,width= 500 , height= 400, bg="#B2BEB5")
frame.pack()

title_1 = tk.Label(window,text="Add products",font=("arial",15),bg="#B2BEB5")
title_1.place(x=678,y=30)

entry_name_label = tk.Label(window,text="Name of product:-",font=("arial",9),bg="#B2BEB5")
entry_name_label.place(x=565,y=80)

entry_name = tk.Entry(window)
entry_name.place(x=678, y= 80)

entry_id = tk.Entry(window)
entry_id.place(x= 678,y= 120)

entry_id_label = tk.Label(window,text= "Enter product ID:-",font=("arial",9),bg="#B2BEB5")
entry_id_label.place(x=565,y=120)

entry_price = tk.Entry(window)
entry_price.place(x="678",y= 160)

entry_price_label =tk.Label(window,text="Enter product's price:-",font=("arial",9),bg="#B2BEB5")
entry_price_label.place(x=555,y=160)

combobox_label= tk.Label(window,text="Select quantity:",font=("arial",9),bg="#B2BEB5")
combobox_label.place(x=565,y=200)

quantity= ttk.Combobox(window,values= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
quantity.place(x=678,y= 200)

add_button = tk.Button(window,text="ADD",command=add_products)
add_button.place(x= 678,y= 240)

list_frame = tk.Frame(window,width= 300, height= 500,bg="#B2BEB5")
list_frame.place(x= 30, y=30)

list_items = tk.Listbox(window, width= 42, height = 20)
list_items.place(x=50 , y= 80)

list_items_label = tk.Label(window,text= "list of items: ",font=("arial",15),bg="#B2BEB5")
list_items_label.place(x=120,y=40)

list_button = tk.Button(window,text="SHOW",command=show_list)
list_button.place(x=140, y= 430)

ok_button = tk.Button(window, text="OK",command= ok_command)
ok_button.place(x= 200 ,y=430)

billing_frame = tk.Frame(window,width= 370 ,height= 300,bg="#B2BEB5")
billing_frame.place(x=1050,y=30)

billing_label = tk.Label(window,text="Billing:-",font=("arial",16),bg="#B2BEB5")
billing_label.place(x=1100,y=40)

entry_bill_name = tk.Entry(window)
entry_bill_name.place(x=1200,y= 100)

label_name = tk.Label(window,text="name of product:-",font=("arial",12),bg="#B2BEB5")
label_name.place(x=1070,y=100)

entry_quant = ttk.Combobox(window,values=[1,2,3,4,5,6,7,8,9,10],width=10)
entry_quant.place(x=1200,y= 130)

entry_q_label = tk.Label(window,text="Quantity:-",bg="#B2BEB5",font=("arial",12))
entry_q_label.place(x=1100,y=130)

list_box_total = tk.Listbox(window,width= 10,height=1)
list_box_total.place(x= 1100,y=300)

add_amount_1 = tk.Button(window,text="Add",command = lambda:(add_amount(),list_of_bill_items(),update_stock()) )
add_amount_1.place(x=1090,y=200)

cal_button = tk.Button(window,text="DONE",command= done_button)
cal_button.place(x=1150,y=200)

list_added = tk.Listbox(window,width=25,height=8)
list_added.place(x=1230,y=170)

label_total = tk.Label(window,text="Total:-",font=("arial",9),bg="#B2BEB5")
label_total.place(x=1060,y=300)




window.mainloop()




