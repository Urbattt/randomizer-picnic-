from tkinter import* 
import random 

root= Tk()
root.geometry("400x400")
root.title("Picnic Bag")

list1= ["Bottle", "Tiffin", "Id Card", "Chocolates", "Chips", "Ticket", "Hanky"]
print(list1)
picnic_bag = Label(root)
picnic_num = Label(root)
visable_list= Label(text="Bottle, Tiffin, Id Card, Chocolates, Chips, Ticket, Hanky")
visable_list.place(relx=0.5, rely=0.4, anchor=CENTER)

def random_number():
    random_no=random.randint(0,6)
    print(random_no)
    random_item = list1[random_no]
    print("The items is " + random_item)
    picnic_bag["text"]= str(random_item)
    picnic_num["text"]= str(random_no)
    
btn1 = Button(root, text="Your item is ", command=random_number)
btn1.place(relx=0.5, rely =0.5, anchor=CENTER)
picnic_bag.place(relx=0.5, rely= 0.6, anchor=CENTER)
picnic_num.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()