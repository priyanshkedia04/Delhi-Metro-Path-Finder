from tkinter import *
from tkinter import ttk
from collections import defaultdict
from tkinter import messagebox
import webbrowser
import pickle
import sys
class Graph(object):
    def __init__(self):
        f=open("station_map","rb")
        self.a=pickle.load(f)
        self.b=pickle.load(f)
        self.graph =self.a
        self.station=[]
        self.distance=0
    def BFS(self,s,f):
        visited = [False] * (len(self.graph))
        queue=[]
        dist=[None]*(len(self.graph))
        pred=[None]*(len(self.graph))
        queue.append(s)
        visited[s]=True
        dist[s]=0
        s1=s
        while queue:
            s = queue.pop(0)
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    dist[i]=dist[s]+1
                    pred[i]=s
                    if i==f:
                        p=pred[i]
                        self.distance=dist[i]
                        self.station.append(self.b[f])
                        while p!=s1:
                            self.station.append(self.b[p])
                            p=pred[p]
                        else:
                            self.station.append(self.b[s1])

                        break


main_window = Tk()
main_window.title("DELHI METRO")
main_window.state("zoomed")
main_window.configure(background="yellow")

topside = LabelFrame(main_window , bd = 2,bg="#0032FF")
topside.pack(side=TOP,fill=X,pady=10,padx=5)

img = PhotoImage(file=r"logo.png")

photo_lable=Label(topside,image=img,bg="white")
photo_lable.pack(side=LEFT)

img2 = PhotoImage(file=r"logo.png")

photo_lable2=Label(topside,image=img2,bg="white")
photo_lable2.pack(side=RIGHT)

text_label=Label(topside,text="DELHI METRO ROUTE",font=("Arial",30),fg="white",bg="#0032FF")
text_label.pack(side=LEFT,padx=30)

leftside = LabelFrame(main_window , bd = 0,bg="yellow")
leftside.place(x = 100 , y = 200, height=200, width = 300)

start=Label(leftside,text="SOURCE",font=("Arial",18),fg="black",bg="yellow")
start.pack(side = TOP,padx=10,pady=30)
dest=Label(leftside,text="DESTINATION",font=("Arial",18),fg="black",bg="yellow")
dest.pack(side = TOP,padx=10,pady=27)

centerside = LabelFrame(main_window , bd = 0,bg="yellow")
centerside.place(x = 380 , y = 200, height=200, width = 300)
value1 = StringVar()
combo1 = ttk.Combobox(centerside,width=25,font=("Arial",16),height=10,textvariable=value1,state='readonly',justify = 'center')
combo1['values']=['Select Station','AIIMS Yellow Line', 'ANVT Pink Line', 'Adarsh Nagar Yellow Line', 'Arjan Garh Yellow Line', 'Arthala Red Line', 'Ashram Pink Line', 'Azadpur', 'Badarpur Violet Line', 'Badkal Mor Violet Line', 'Bata Chownk Violet Line', 'Bhikaji Cama Place Pink Line', 'Central Secretariat', 'Chandhni Chowk Yellow Line', 'Chawri Bazar Yellow Line', 'Chhattarpur Yellow Line', 'Civil Lines Yellow Line', 'Delhi Cantt Pink Line', 'Delhi Gate Violet Line', 'Dilshad Garden Red Line', 'Durgabai Deshmukh South Campus Pink Line', 'ESI Hospital Pink Line', 'East Azad Nagar Pink Line', 'Escorts Mujesar Violet Line', 'Faridabad Old Violet Line', 'GTB Nagar Yellow Line', 'Ghotorni Yellow Line', 'Gokulpuri Pink Line', 'Govindpuri Violet Line', 'Green Park Yellow Line', 'Gurudronacharya Yellow Line', 'Haiderpur Badli Mor Yellow Line', 'Hauz Khas Yellow Line', 'Hazrat Nizamuddin Pink Line', 'Hindon Red Line', 'Huda City Centre Yellow Line', 'IFFCO Chowk Yellow Line', 'INA', 'IP Extension Pink Line', 'ITO Violet Line', 'Inder Lok Red Line', 'JLN Violet Line', 'Jaffrabad Pink Line', 'Jahangirpuri Yellow Line', 'Jama Masjid Violet Line', 'Jangpura Violet Line', 'Janpath Violet Line', 'Jasola-Apollo Violet Line', 'Jhil Mil Red Line', 'Johri Enclave Pink Line', 'Jorbagh Yellow Line', 'Kailash Colony Violet Line', 'Kalkaji Mandir Violet Line', 'Kanhaiya Nagar Red Line', 'Karkarduma Court Pink Line', 'Karkarduma Pink Line', 'Kashmere Gate', 'Keshav Puram Red Line', 'Khan Market Violet Line', 'Kohat Enclave Red Line', 'Krishna Nagar Pink Line', 'Lajpat Nagar', 'Lal Quila Violet Line', 'Lok Kalyan Marg Yellow Line', 'MG Road Yellow Line', 'Majlis Park Pink Line', 'Major Mohit Sharma Red Line', 'Malvia Nagar Yellow Line', 'Mandawali - West Vinod Nagar Pink Line', 'Mandi House Violet Line', 'Mansarovar Park Red Line', 'Maujpur Pink Line', 'Maya Puri Pink Line', 'Mayur Vihar 1 Pink Line', 'Mayur Vihar Pocket 1 Pink Line', 'Mewla Maharajpur Violet Line', 'Model Town Yellow Line', 'Mohan Estate Violet Line', 'Mohan Nagar Red Line', 'Moolchand Violet Line', 'NHPC Chownk Violet Line', 'Naraina Vihar Pink Line', 'Neelam Chownk Ajronda Violet Line', 'Nehru Place Violet Line', 'Netaji Subhash Place', 'New Delhi Yellow Line', 'Okhla Violet Line', 'Patel Chowk Yellow Line', 'Pitam Pura Red Line', 'Pratap Nagar Red Line', 'Pul Bangash Red Line', 'Punjabi Bagh West Pink Line', 'Qutab Minar Yellow Line', 'Raj Bagh Red Line', 'Raja Nahar singh marg Violet Line', 'Rajiv Chowk Yellow Line', 'Rajouri Garden Pink Line', 'Rithala Red Line', 'Rohini East Red Line', 'Rohini Sector 18, 19 Yellow Line', 'Rohini West Red Line', 'Saket Yellow Line', 'Samaypur Badli Yellow Line', 'Sant Surdas Violet Line', 'Sarai Violet Line', 'Sarita Vihar Violet Line', 'Sarojini Nagar Pink Line', 'Sector 28 Violet Line', 'Seelampur Red Line', 'Shahdara Red Line', 'Shaheed Nagar Red Line', 'Shaheed Sthal(New Bus Adda) Red Line', 'Shakurpur Pink Line', 'Shalimar Bagh Pink Line', 'Shastri Nagar Red Line', 'Shastri Park Red Line', 'Shiv Vihar Pink Line', 'Shyam park Red Line', 'Sikandarpur. Yellow Line', 'Sir Vishweshwaraiah Moti Bagh Pink Line', 'South Extension Pink Line', 'Sultanpur Yellow Line', 'Tis Hazari Red Line', 'Trilokpuri Sanjay Lake Pink Line', 'Tuglakabad Violet Line', 'Udyog Bhawan Yellow Line', 'Vidhan Sabha Yellow Line', 'Vinobapuri Pink Line', 'Vinod Nagar East Pink Line', 'Viswavidyalaya Yellow Line', 'Welcome']
combo1.current(0)
combo1.pack(side=TOP,pady=30)

value2 = StringVar()
combo2 = ttk.Combobox(centerside,width=25,font=("Arial",16),height=10,textvariable=value2,state='readonly',justify = 'center')

combo2['values']=['Select Station','AIIMS Yellow Line', 'ANVT Pink Line', 'Adarsh Nagar Yellow Line', 'Arjan Garh Yellow Line', 'Arthala Red Line', 'Ashram Pink Line', 'Azadpur', 'Badarpur Violet Line', 'Badkal Mor Violet Line', 'Bata Chownk Violet Line', 'Bhikaji Cama Place Pink Line', 'Central Secretariat', 'Chandhni Chowk Yellow Line', 'Chawri Bazar Yellow Line', 'Chhattarpur Yellow Line', 'Civil Lines Yellow Line', 'Delhi Cantt Pink Line', 'Delhi Gate Violet Line', 'Dilshad Garden Red Line', 'Durgabai Deshmukh South Campus Pink Line', 'ESI Hospital Pink Line', 'East Azad Nagar Pink Line', 'Escorts Mujesar Violet Line', 'Faridabad Old Violet Line', 'GTB Nagar Yellow Line', 'Ghotorni Yellow Line', 'Gokulpuri Pink Line', 'Govindpuri Violet Line', 'Green Park Yellow Line', 'Gurudronacharya Yellow Line', 'Haiderpur Badli Mor Yellow Line', 'Hauz Khas Yellow Line', 'Hazrat Nizamuddin Pink Line', 'Hindon Red Line', 'Huda City Centre Yellow Line', 'IFFCO Chowk Yellow Line', 'INA', 'IP Extension Pink Line', 'ITO Violet Line', 'Inder Lok Red Line', 'JLN Violet Line', 'Jaffrabad Pink Line', 'Jahangirpuri Yellow Line', 'Jama Masjid Violet Line', 'Jangpura Violet Line', 'Janpath Violet Line', 'Jasola-Apollo Violet Line', 'Jhil Mil Red Line', 'Johri Enclave Pink Line', 'Jorbagh Yellow Line', 'Kailash Colony Violet Line', 'Kalkaji Mandir Violet Line', 'Kanhaiya Nagar Red Line', 'Karkarduma Court Pink Line', 'Karkarduma Pink Line', 'Kashmere Gate', 'Keshav Puram Red Line', 'Khan Market Violet Line', 'Kohat Enclave Red Line', 'Krishna Nagar Pink Line', 'Lajpat Nagar', 'Lal Quila Violet Line', 'Lok Kalyan Marg Yellow Line', 'MG Road Yellow Line', 'Majlis Park Pink Line', 'Major Mohit Sharma Red Line', 'Malvia Nagar Yellow Line', 'Mandawali - West Vinod Nagar Pink Line', 'Mandi House Violet Line', 'Mansarovar Park Red Line', 'Maujpur Pink Line', 'Maya Puri Pink Line', 'Mayur Vihar 1 Pink Line', 'Mayur Vihar Pocket 1 Pink Line', 'Mewla Maharajpur Violet Line', 'Model Town Yellow Line', 'Mohan Estate Violet Line', 'Mohan Nagar Red Line', 'Moolchand Violet Line', 'NHPC Chownk Violet Line', 'Naraina Vihar Pink Line', 'Neelam Chownk Ajronda Violet Line', 'Nehru Place Violet Line', 'Netaji Subhash Place', 'New Delhi Yellow Line', 'Okhla Violet Line', 'Patel Chowk Yellow Line', 'Pitam Pura Red Line', 'Pratap Nagar Red Line', 'Pul Bangash Red Line', 'Punjabi Bagh West Pink Line', 'Qutab Minar Yellow Line', 'Raj Bagh Red Line', 'Raja Nahar singh marg Violet Line', 'Rajiv Chowk Yellow Line', 'Rajouri Garden Pink Line', 'Rithala Red Line', 'Rohini East Red Line', 'Rohini Sector 18, 19 Yellow Line', 'Rohini West Red Line', 'Saket Yellow Line', 'Samaypur Badli Yellow Line', 'Sant Surdas Violet Line', 'Sarai Violet Line', 'Sarita Vihar Violet Line', 'Sarojini Nagar Pink Line', 'Sector 28 Violet Line', 'Seelampur Red Line', 'Shahdara Red Line', 'Shaheed Nagar Red Line', 'Shaheed Sthal(New Bus Adda) Red Line', 'Shakurpur Pink Line', 'Shalimar Bagh Pink Line', 'Shastri Nagar Red Line', 'Shastri Park Red Line', 'Shiv Vihar Pink Line', 'Shyam park Red Line', 'Sikandarpur. Yellow Line', 'Sir Vishweshwaraiah Moti Bagh Pink Line', 'South Extension Pink Line', 'Sultanpur Yellow Line', 'Tis Hazari Red Line', 'Trilokpuri Sanjay Lake Pink Line', 'Tuglakabad Violet Line', 'Udyog Bhawan Yellow Line', 'Vidhan Sabha Yellow Line', 'Vinobapuri Pink Line', 'Vinod Nagar East Pink Line', 'Viswavidyalaya Yellow Line', 'Welcome']
combo2.current(0)
combo2.pack(side=TOP,pady=30)


def print_route(arr_sta,dis):
    rightside = LabelFrame(main_window ,bg="yellow",bd=0)
    rightside.place(x = 900 , y = 150, height=600, width = 400)
    scrollbar = Scrollbar(rightside)
    scrollbar.pack( side = RIGHT, fill = Y )
    scrollbar2 = Scrollbar(rightside,orient="horizontal")
    scrollbar2.pack(fill=X,side=BOTTOM)
    listbox = Listbox(rightside,bd=2,bg="#0032FF",fg="white",font=("Arial",14,"bold"),yscrollcommand = scrollbar.set,xscrollcommand = scrollbar2.set)
    scrollbar.config(command=listbox.yview)
    scrollbar2.config(command=listbox.xview)
    listbox.insert(END, "              STATIONS TO CROSS : "+str(dis))
    listbox.selection_clear(0, 'end')
    for i in range(len(arr_sta)-1,-1,-1):
        listbox.insert(END, "   ")
        listbox.insert(END, "   "+str(len(arr_sta)-i)+"."+" "+arr_sta[i])


    listbox.pack(fill=BOTH,expand=TRUE)



def find_route(s,d):
    g=Graph()
    dict_station=g.b
    try:
        for i in range(len(dict_station)):
            if dict_station[i]==s:
                s_index=i
            elif dict_station[i]==d:
                d_index=i
            else:
                continue
        g.BFS(s_index,d_index)
        print_route(g.station,g.distance)
    except:
        messagebox.showinfo("Select Station", "Enter Valid Station" , icon = "warning")

def click_me():
    try:
       rightside.destroy()
    except:
        a=5
    source=value1.get()
    destination=value2.get()
    find_route(source,destination)

def exit_window():
        sys.exit()
def openlink():
    webbrowser.open_new("https://delhimetrorail.info/delhi-metro-map")

click_button=Button(main_window,text="Find Route",width=20,font=("Arial",14),command=click_me)
click_button.place(x=300,y=425)

link_button=Button(main_window,text="Click Here To View Map",width=20,font=("Arial",14),command=openlink)
link_button.place(x=300,y=475)

exit_button=Button(main_window,text="Exit",width=20,font=("Arial",14),command=exit_window)
exit_button.place(x=300,y=525)

main_window.mainloop()
