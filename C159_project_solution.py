from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root. title("Country Maps")
root.geometry("500x500")
root.configure(background="aqua")

get_input = Entry(root)
show_label = Label(root)

india_map = ImageTk.PhotoImage(Image.open ("India.jpg"))
america_map = ImageTk.PhotoImage(Image.open ("America.jpg"))
australia_map = ImageTk.PhotoImage(Image.open ("Australia.png"))
philippines_map = ImageTk.PhotoImage(Image.open ("Japan.jpg"))
japan_map = ImageTk.PhotoImage(Image.open ("Philippines.png"))

maps_dictionary = { "India" : india_map , 
                    "America" : america_map ,
                    "Australia" : australia_map ,
                    "Philippines" : philippines_map,
                    "Japan" : japan_map,}
def showMaps():
    try:
        map_name = get_input.get()
        print(map_name)
        show_label['image'] = maps_dictionary[map_name]
    except:
        messagebox.showinfo("Error", "Sorry! This country flag is not present in our system")
        
btn = Button(root , text="Show FLAG", bg="green", command=showMaps)
get_input.place(relx=0.5, rely=0.1, anchor=CENTER)
btn.place(relx=0.5, rely=0.2, anchor=CENTER)

root.mainloop