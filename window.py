import tkinter.ttk
from tkinter import *
import matplotlib.pyplot as plt


import population


class window:
    def __init__(self):
        self.root = Tk()
        self.init_window()
        self.root.mainloop()

    def init_window(self):
        self.root.title("MM8")
        self.root.geometry("1280x800")
        self.init_menu()

    def start(self):
        pop = population.population(int(self.entry_list[0].get()),
                                    float(self.entry_list[1].get()),
                                    float(self.entry_list[2].get()),
                                    int(self.entry_list[3].get()),
                                    int(self.entry_list[4].get()))

        frame_tab = Frame(bg="red")
        heads = ['День', "Здоровые", "Латентные", "Заболевшие", "Выздоровившие"]
        table = tkinter.ttk.Treeview(frame_tab, show="headings")
        table["columns"] = heads

        size_pop = []
        latent = []
        infected = []
        recovered = []

        for header in heads:
            table.heading(header, text=header, anchor="center")
            table.column(header, anchor="center")
        for i in range(int(self.entry_list[-1].get())):
            tmp_data = pop.next_day()
            table.insert("", tkinter.END, values=(i, tmp_data["size"], tmp_data["latently_infected"], tmp_data["infected"], tmp_data["recovered"]))
            size_pop.append(tmp_data["size"])
            latent.append(tmp_data["latently_infected"])
            infected.append(tmp_data["infected"])
            recovered.append(tmp_data["recovered"])

        sb = tkinter.ttk.Scrollbar(frame_tab, command=table.yview)
        sb.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        table.pack(expand=tkinter.YES, fill=tkinter.BOTH)
        table.configure(yscrollcommand=sb.set)
        frame_tab.grid(row=0, column=2, rowspan=18, columnspan=2)


        fig, ax = plt.subplots()
        count_days = [i for i in range(int(self.entry_list[-1].get()))]
        ax.plot(count_days, size_pop,
                     count_days, latent,
                     count_days, infected,
                     count_days, recovered)

        ax.legend(labels=["Здоровые", "Латентные", "Заболевшие", "Выздоровившие"],
                  loc='upper center', bbox_to_anchor=(0.5, -0.05),
                  fancybox=True, shadow=True, ncol=5)
        ax.set_ylabel('Total population')

        plt.savefig("saved_figure.png")
        self.sreda = PhotoImage(file="saved_figure.png")
        panel = Label(image=self.sreda).grid(row=19, column=2, columnspan=2)





    def init_menu(self):
        sv_total_pop = StringVar(value="10000")
        sv_infectivity = StringVar(value="0.6")
        sv_contact_rate = StringVar(value="1.25")
        sv_incubation = StringVar(value="10")
        sv_average_illness = StringVar(value="15")
        sv_day_count = StringVar(value="100")
        self.entry_list = [sv_total_pop,
                           sv_infectivity,
                           sv_contact_rate,
                           sv_incubation,
                           sv_average_illness,
                           sv_day_count]

        Label(text="Население")\
            .grid(row=0, column=0)
        Entry(textvariable=sv_total_pop)\
            .grid(row=1, column=0)

        Label(text="Передача инфекции") \
            .grid(row=3, column=0)
        Entry(textvariable=sv_infectivity) \
            .grid(row=4, column=0)

        Label(text="Контакт с больными") \
            .grid(row=6, column=0)
        Entry(textvariable=sv_contact_rate) \
            .grid(row=7, column=0)

        Label(text="Инеубационный период") \
            .grid(row=9, column=0)
        Entry(textvariable=sv_incubation) \
            .grid(row=10, column=0)

        Label(text="Продолжительность болезни") \
            .grid(row=12, column=0)
        Entry(textvariable=sv_average_illness) \
            .grid(row=13, column=0)

        Label(text="Количество дней") \
            .grid(row=15, column=0)
        Entry(textvariable=sv_day_count) \
            .grid(row=16, column=0)

        Button(text="Старт", command=self.start)\
            .grid(row=18, column=0)
