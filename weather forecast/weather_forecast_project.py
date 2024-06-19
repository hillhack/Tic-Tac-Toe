from tkinter import *
from tkinter import ttk
import requests
error_codes = ['404','401','400','429','5xx']
def get_data():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=bb47ed7648d9f4e75822376885517507").json()
    if data['cod'] in error_codes:
        print(data['message'])
        w_name_label1.config(text="")
        wd_name_label2.config(text="")
        temp_name_label3.config(text="")
        w_name_label4.config(text="")
        
        blank.config(text=data["message"])
    else:
        blank.config(text='')

        w_name_label1.config(text=data["weather"][0]["main"])
        wd_name_label2.config(text=data["weather"][0]["description"])
        temp_name_label3.config(text=str(int(data["main"]["temp"]-273.15)))
        w_name_label4.config(text=data["main"]["pressure"])

win = Tk()
win.title("Weather forecst")
win.config(bg = 'blue')
win.geometry("500x570")

name_label = Label(win,text="Weather App",
                   font = ("Time New Roman",20,'bold'))
name_label.place(x=25,y=50,height=50,width=450)

city_name=StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Search",values=list_name,
                   font = ("Time New Roman",20,'bold'),textvariable=city_name)
com.place(x=35,y=120,height=50,width=400)


w_name_label = Label(win,text="Weather climate",
                   font = ("Time New Roman",15,'bold'))
w_name_label.place(x=35,y=250,height=35,width=240)
w_name_label1 = Label(win,text="",
                   font = ("Time New Roman",15,'bold'))
w_name_label1.place(x=280,y=250,height=35,width=200)

wd_name_label = Label(win,text="Weather description",
                   font = ("Time New Roman",15,'bold'))
wd_name_label.place(x=35,y=300,height=35,width=240)
wd_name_label2 = Label(win,text="",
                   font = ("Time New Roman",15,'bold'))
wd_name_label2.place(x=280,y=300,height=35,width=200)

temp_name_label = Label(win,text="Temperature",
                   font = ("Time New Roman",15,'bold'))
temp_name_label.place(x=35,y=350,height=35,width=240)
temp_name_label3 = Label(win,text="",
                   font = ("Time New Roman",15,'bold'))
temp_name_label3.place(x=280,y=350,height=35,width=200)

w_name_label = Label(win,text="Pressure",
                   font = ("Time New Roman",15,'bold'))
w_name_label.place(x=35,y=400,height=35,width=240)
w_name_label4 = Label(win,text="",
                   font = ("Time New Roman",15,'bold'))
w_name_label4.place(x=280,y=400,height=35,width=200)

blank = Label(win,text ="",
            font = ("Time New Roman",15,'bold'))
blank.place(x=35,y=450,height=35,width=200)

done_button = Button(win,text="Done",
                     font=('Time New Roman',20,'bold'),command=get_data)
done_button.place(y = 190,height=40,width=100,x=200)

win.mainloop()