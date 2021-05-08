# -*- coding: utf-8 -*-
"""
Created on Sat May  8 11:10:08 2021

@author: ADMINS
"""

import tkinter as tk
    

def cal_newsal():
    w = int(workyear.get())
    c = int(cursal.get())
    if emtype==1:
        if w<5:
            ns = c+((c*4)/100)
        else:
           ns = c+((c*5)/100)
    else:
        if w<5:
            ns = c+((c*2.5)/100)
        else:
            ns = c+((c*3)/100)
    newSal.set(ns)
    

window = tk.Tk()
window.title("Salary Calculator Application")
window.geometry("600x300")


######################################################################
####################### HEAD LABEL ###################################
hlabel = tk.Label(window,
                  text="Salary Calculator Application",
                  font=("Helvetica", 25),
                  fg="DarkCyan"
                  )
hlabel.grid(row=0, column=0, columnspan=4, sticky='N', pady=30)
######################################################################


######################################################################
####################### EMPLOYEE TYPE ################################
em_type = tk.Label(window,
                   text="Employee Type:",
                   font=("Helvetica", 10)
                   )
em_type.grid(row=1, column=0, padx=30, pady=3) # Label -> widget

#RADIO BUTTON
emtype = tk.StringVar()
emtype.set(1)
rbt_ft = tk.Radiobutton(window,
                        text="Full-time",
                        variable=emtype,
                        value=1,
                        )
rbt_ft.grid(row=1, column=1, sticky='W')

rbt_pt = tk.Radiobutton(window,
                        text="Past-time",
                        variable=emtype,
                        value=2,
                        )
rbt_pt.grid(row=1, column=1, padx=80)
######################################################################


######################################################################
####################### EMPLOYEE WORK YEARS###########################
em_wy = tk.Label(window,
                 text="Working Years:",
                 font=("Helvetica", 10)
                 )
em_wy.grid(row=2, column=0, padx=30, pady=3)

#TEXT FIELD
workyear = tk.Entry(window, width=30)
workyear.grid(row=2, column=1, sticky='W')
######################################################################

######################################################################
####################### EMPLOYEE Salary ##############################
em_cursal = tk.Label(window,
                 text="Current Salary:",
                 font=("Helvetica", 10)
                 )
em_cursal.grid(row=3, column=0, padx=30, pady=3)

#TEXT FIELD
cursal = tk.Entry(window, width=30)
cursal.grid(row=3, column=1, sticky='W')
######################################################################

######################################################################
####################### CALCULATE BUTTON #############################
bt_cal = tk.Button(window,
                 text="Calculate",
                 width=10, height=1,
                 command = cal_newsal
                 )
bt_cal.grid(row=4, column=0, columnspan=4, sticky='S')
######################################################################

######################################################################
##################### EMPLOYEE SHOW SALARY ###########################
em_newsal = tk.Label(window,
                 text="New Salary:",
                 font=("Helvetica", 20)
                 )
em_newsal.grid(row=1, column=3, sticky='E')

#DISPLAY NEW SALARY
newSal = tk.StringVar()
em_shnewsal = tk.Label(window,
                 text="xxx",
                 font=("Helvetica", 15),
                 textvariable=newSal
                 )
em_shnewsal.grid(row=2, column=3)
######################################################################


######################################################################
########################### LICENSE ##################################
pro_license = tk.Label(window,
                 text="\n\n© 2021 - Powered by CE students, IT School\nMAE FAH LUANG UNIVERSIT",
                 font=("Helvetica", 8),
                 fg="DarkTurquoise"
                 )
pro_license.grid(row=5, column=0, columnspan=4, sticky='S')
######################################################################

window.mainloop()