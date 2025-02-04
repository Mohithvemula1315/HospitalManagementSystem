from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from tkcalendar import DateEntry 
def ex():
    result=messagebox.askyesno('Exit Confirmation',"Do you want to exit")
    if result:
        root.destroy()
    else:
        pass


def reset():
    
    box.set("Select A Tablet")
    refno_entry.delete(0, END)
    dose_entry.delete(0, END)
    tablets_entry.delete(0, END)
    lot_entry.delete(0, END)
    issue_date_entry.delete(0, END)
    exp_date_entry.delete(0, END)
    side_effect_entry.delete(0, END)
    daily_dose_entry.delete(0, END)
    futinfoentry.delete(0, END)
    blood_pressure_entry.delete(0, END)
    storage_advice_entry.delete(0, END)
    medication_entry.delete(0, END)
    patient_id_entry.delete(0, END)
    nhs_number_entry.delete(0, END)
    patient_name_entry.delete(0, END)
    dob_entry.delete(0, END)
    patient_address_entry.delete(0, END)

def search():
    def search_data():
        selected_column = combobox.get()
        search_value = entry.get()      

        
        for item in tree.get_children():
            tree.delete(item)

        
        try:
            query = f"SELECT * FROM prescriptions WHERE {selected_column} = %s"
            mycursor.execute(query, (search_value,))
            results = mycursor.fetchall()
            if not results:
                messagebox.showinfo("No Match Found", f"No records found for {selected_column} = '{search_value}'.")
                return

            for row in results:
                tree.insert("", END, values=row)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def update_label(event=None):
        selected_column = combobox.get()
        entry_label.config(text=f"Enter {selected_column}:")

    try:
        
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Mohith@1315',  
            database='hospital'
        )
        mycursor = con.cursor()

        mycursor.execute("DESCRIBE prescriptions")
        rows = mycursor.fetchall()
        columns = []
        for row in rows:
            columns.append(row[0])

        if not columns:
            messagebox.showerror("Error", "No columns found in the 'prescriptions' table.")
            return

        search_window = Toplevel()
        search_window.title('Search Prescriptions')
        search_window.grab_set()
        search_window.resizable(False, False)

        Label(search_window, text="Select Column:", font=('times new roman', 20, 'bold')).grid(row=0, column=0, padx=10, pady=5)
        combobox = ttk.Combobox(search_window, values=columns, state="readonly", font=('roman', 15, 'bold'), width=24)
        combobox.grid(row=0, column=1, padx=10, pady=5)
        combobox.current(0)  
        combobox.bind("<<ComboboxSelected>>", update_label)

        entry_label = Label(search_window, text=f"Enter {columns[0]}:", font=('times new roman', 20, 'bold'))
        entry_label.grid(row=1, column=0, padx=30, pady=15, sticky=W)

        entry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
        entry.grid(row=1, column=1, padx=10, pady=5)

        search_button = Button(search_window, text="Search", command=lambda: [search_data(), search_window.destroy()])
        search_button.grid(row=1, column=2, padx=10, pady=5)

        search_window.mainloop()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")



def display_data():
    try:
        global cur,con
        con = mysql.connector.connect(host="localhost", user="root", passwd="Mohith@1315", database="hospital")
        cur = con.cursor()

        select_query = "SELECT * FROM prescriptions"

        cur.execute(select_query)
        rows = cur.fetchall()
        tree.delete(*tree.get_children())

        if rows:
            for row in rows:
                tree.insert("", "end", values=row)

        messagebox.showinfo("Success", "Data loaded successfully.")

    except Exception as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")
    finally:
        if con.is_connected():
            cur.close()
            con.close()





def select(event):
    """Populate entry fields when a row in the Treeview is selected."""
    indexing = tree.focus()
    if not indexing:
        return

    content = tree.item(indexing)
    listdata = content['values']

    if not listdata or len(listdata) < 18:
        messagebox.showerror("Error", "Row data is incomplete or missing.")
        return

    try:
        box.delete(0, END)
        box.set(listdata[0])

        refno_entry.delete(0, END)
        refno_entry.insert(0, listdata[1])

        dose_entry.delete(0, END)
        dose_entry.insert(0, listdata[2])

        tablets_entry.delete(0, END)
        tablets_entry.insert(0, listdata[3])

        lot_entry.delete(0, END)
        lot_entry.insert(0, listdata[4])

        if isinstance(issue_date_entry, DateEntry):
            issue_date_entry.set_date(listdata[5])
        else:
            issue_date_entry.delete(0, END)
            issue_date_entry.insert(0, listdata[5])

        if isinstance(exp_date_entry, DateEntry):
            exp_date_entry.set_date(listdata[6])
        else:
            exp_date_entry.delete(0, END)
            exp_date_entry.insert(0, listdata[6])

        side_effect_entry.delete(0, END)
        side_effect_entry.insert(0, listdata[7])

        daily_dose_entry.delete(0, END)
        daily_dose_entry.insert(0, listdata[8])

        futinfoentry.delete(0, END)
        futinfoentry.insert(0, listdata[9])

        blood_pressure_entry.delete(0, END)
        blood_pressure_entry.insert(0, listdata[10])

        storage_advice_entry.delete(0, END)
        storage_advice_entry.insert(0, listdata[11])

        medication_entry.delete(0, END)
        medication_entry.insert(0, listdata[12])

        patient_id_entry.delete(0, END)
        patient_id_entry.insert(0, listdata[13])

        nhs_number_entry.delete(0, END)
        nhs_number_entry.insert(0, listdata[14])

        patient_name_entry.delete(0, END)
        patient_name_entry.insert(0, listdata[15])

        if isinstance(dob_entry, DateEntry):
            dob_entry.set_date(listdata[16])
        else:
            dob_entry.delete(0, END)
            dob_entry.insert(0, listdata[16])

        patient_address_entry.delete(0, END)
        patient_address_entry.insert(0, listdata[17])

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while populating fields: {e}")

def update():
    """Update the selected row in the database and Treeview."""
    indexing = tree.focus()
    if not indexing:
        messagebox.showwarning('No Selection', 'Please select a record to update.')
        return

    content = tree.item(indexing)
    listdata = content['values']

    if not listdata or len(listdata) < 18:
        messagebox.showerror("Error", "Row data is incomplete or missing.")
        return

    try:
        tablet_name = box.get()
        dose = dose_entry.get()
        no_of_tablets = tablets_entry.get()  
        lot = lot_entry.get()
        issue_date = issue_date_entry.get() if isinstance(issue_date_entry, DateEntry) else issue_date_entry.get()
        exp_date = exp_date_entry.get() if isinstance(exp_date_entry, DateEntry) else exp_date_entry.get()
        side_effect = side_effect_entry.get()
        daily_dose = daily_dose_entry.get()
        further_info = futinfoentry.get()
        blood_pressure = blood_pressure_entry.get()
        storage_advice = storage_advice_entry.get()
        medication = medication_entry.get()
        patient_id = patient_id_entry.get()
        nhs_number = nhs_number_entry.get()
        patient_name = patient_name_entry.get()
        dob = dob_entry.get() if isinstance(dob_entry, DateEntry) else dob_entry.get()
        patient_address = patient_address_entry.get()

        if not no_of_tablets.isdigit():
            messagebox.showerror("Invalid Input", "Number of tablets must be a valid integer.")
            return

        no_of_tablets = int(no_of_tablets)

        if no_of_tablets <= 0:
            messagebox.showerror("Invalid Input", "Number of tablets must be a positive integer.")
            return

        new_data = (
            tablet_name,
            dose,
            no_of_tablets,
            lot,
            issue_date,
            exp_date,
            side_effect,
            daily_dose,
            further_info,
            blood_pressure,
            storage_advice,
            medication,
            patient_id,
            nhs_number,
            patient_name,
            dob,
            patient_address,
        )

        if listdata[0:17] == new_data:
            messagebox.showerror("No Changes Made", "No changes detected. Please make updates before saving.")
            return

        con = mysql.connector.connect(host='localhost', user='root', password='Mohith@1315', database='hospital')
        mycursor = con.cursor()

        update_query = '''
            UPDATE prescriptions
            SET tablet_name=%s, dose=%s, no_of_tablets=%s, lot=%s, issue_date=%s, exp_date=%s, side_effect=%s,
            daily_dose=%s, further_info=%s, blood_pressure=%s, storage_advice=%s, medication=%s,
            patient_id=%s, nhs_number=%s, patient_name=%s, dob=%s, patient_address=%s
            WHERE reference_no=%s
        '''

        mycursor.execute(update_query, new_data + (listdata[1],))  
        con.commit()

        tree.item(indexing, values=(
         
            tablet_name,
            listdata[1],
            dose,
            no_of_tablets,
            lot,
            issue_date,
            exp_date,
            side_effect,
            daily_dose,
            further_info,
            blood_pressure,
            storage_advice,
            medication,
            patient_id,
            nhs_number,
            patient_name,
            dob,
            patient_address
        ))

        messagebox.showinfo("Success", "Data updated successfully.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

    finally:
        if 'con' in locals() and con.is_connected():
            con.close()



def delete():
    selected_item = tree.selection()
    
    if not selected_item:
        messagebox.showwarning("Select Row", "Please select a row to delete.")
        return

    selected_values = tree.item(selected_item, 'values')
    reference_no = selected_values[1]  

    con = mysql.connector.connect(host="localhost", user="root", passwd="Mohith@1315", database="hospital")
    cur = con.cursor()

    delete_query = "DELETE FROM prescriptions WHERE reference_no = %s"

    try:
        cur.execute(delete_query, (reference_no,))
        con.commit()

        tree.delete(selected_item)

        messagebox.showinfo("Success", f"Prescription with Reference No. {reference_no} deleted successfully.")

    except Exception as e:
        messagebox.showerror("Error", f"Error deleting data: {e}")
        con.rollback()

    finally:
        cur.close()
        con.close()



def insert_to_treeview():
    fields = [
        box.get(), refno_entry.get(), dose_entry.get(), tablets_entry.get(), lot_entry.get(),
        issue_date_entry.get(), exp_date_entry.get(), side_effect_entry.get(), daily_dose_entry.get(),
        futinfoentry.get(), blood_pressure_entry.get(), storage_advice_entry.get(), medication_entry.get(),
        patient_id_entry.get(), nhs_number_entry.get(), patient_name_entry.get(), dob_entry.get(), patient_address_entry.get()
    ]

    if any(field == "" for field in fields):
        messagebox.showerror("Error", "Please fill in all the fields.")
        return

    try:
        con = mysql.connector.connect(host="localhost", user="root", passwd="Mohith@1315")
        cur = con.cursor()

        cur.execute("CREATE DATABASE IF NOT EXISTS hospital")
        
        cur.execute("USE hospital")
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS prescriptions (
            tablet_name VARCHAR(100),
            reference_no VARCHAR(50),
            dose VARCHAR(50),
            no_of_tablets INT,
            lot VARCHAR(50),
            issue_date DATE,
            exp_date DATE,
            side_effect TEXT,
            daily_dose VARCHAR(50),
            further_info TEXT,
            blood_pressure VARCHAR(50),
            storage_advice TEXT,
            medication VARCHAR(50),
            patient_id VARCHAR(50),
            nhs_number VARCHAR(50),
            patient_name VARCHAR(100),
            dob DATE,
            patient_address TEXT
        )
        """
        cur.execute(create_table_query)

        insert_query = """
        INSERT INTO prescriptions (
            tablet_name, reference_no, dose, no_of_tablets, lot, issue_date, exp_date, side_effect, daily_dose,
            further_info, blood_pressure, storage_advice, medication, patient_id, nhs_number, patient_name,
            dob, patient_address
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
        """
        
        data = (
            box.get(), refno_entry.get(), dose_entry.get(), tablets_entry.get(), lot_entry.get(),
            issue_date_entry.get(), exp_date_entry.get(), side_effect_entry.get(), daily_dose_entry.get(),
            futinfoentry.get(), blood_pressure_entry.get(), storage_advice_entry.get(), medication_entry.get(),
            patient_id_entry.get(), nhs_number_entry.get(), patient_name_entry.get(), dob_entry.get(), patient_address_entry.get()
        )

        cur.execute(insert_query, data)
        con.commit()

        tree.insert("", "end", values=data)

        messagebox.showinfo("Success", "Prescription Data Inserted Successfully")

    except Exception as e:
        messagebox.showerror("Error", f"Error inserting data: {e}")
        return
    
    finally:
        if con.is_connected():
            cur.close()
            con.close()

       

def generate_prescription():
    fields = [
        box.get(),
        refno_entry.get(),
        dose_entry.get(),
        tablets_entry.get(),
        lot_entry.get(),
        issue_date_entry.get(),
        exp_date_entry.get(),
        side_effect_entry.get(),
        daily_dose_entry.get(),
        futinfoentry.get(),
        blood_pressure_entry.get(),
        storage_advice_entry.get(),
        medication_entry.get(),
        patient_id_entry.get(),
        nhs_number_entry.get(),
        patient_name_entry.get(),
        dob_entry.get(),
        patient_address_entry.get(),
    ]
    
    if any(field.strip() == "" for field in fields):
        messagebox.showwarning("Missing Fields", "Please fill in all the fields before generating the prescription.")
        return

    textReceipt.delete(1.0, END)
    
    prescription_data = f"""
    ---------------- Prescription ----------------
    Name of Tablet: {box.get()}
    Reference No: {refno_entry.get()}
    Dose: {dose_entry.get()}
    No of Tablets: {tablets_entry.get()}
    Lot: {lot_entry.get()}
    Issue Date: {issue_date_entry.get()}
    Exp Date: {exp_date_entry.get()}
    Side Effect: {side_effect_entry.get()}
    Daily Dose: {daily_dose_entry.get()}
    Further Information: {futinfoentry.get()}
    Blood Pressure: {blood_pressure_entry.get()}
    Storage Advice: {storage_advice_entry.get()}
    Medication: {medication_entry.get()}
    Patient ID: {patient_id_entry.get()}
    NHS Number: {nhs_number_entry.get()}
    Patient Name: {patient_name_entry.get()}
    Date of Birth: {dob_entry.get()}
    Patient Address: {patient_address_entry.get()}
    -------------------------------------------------
    """
    
    textReceipt.insert(END, prescription_data)
    messagebox.showinfo("Success", "Prescription has been successfully generated!")

    




root=Tk()
root.title("HMS")
root.geometry("1545x786+0+0")
root.resizable(0,0)
root.config(bg='silver')


headinglabel=Label(root,text="+ Hospital Management system",bd=10,font=('arial',45,'bold'),fg='black',bg='silver',relief=RIDGE)
headinglabel.pack(fill=X)

patientframe=Frame(root,bd=10,relief=RIDGE,bg='silver')
patientframe.place(x=0,y=95)

patinfolabelframe=LabelFrame(patientframe,text='Patient information',bd=5,relief=RIDGE,bg='silver',font=('arial',10,'bold'),fg='black')
patinfolabelframe.pack(side=LEFT)

nooftabletslabel=Label(patinfolabelframe,text='No Of Tablets',anchor="w",bg='silver',font=('arial',10,'bold'))
nooftabletslabel.grid(row=0,column=0, sticky=W, padx=5, pady=5)
tablets = [
    'Dolo 650', 'Omez', 'Panadol', 'Amoxil', 'Ciplox', 'Ciprofloxacin', 'Augmentin', 'Zyrtec', 
    'Piriton', 'Loratadine', 'Aciloc', 'Esomeprazole', 'Omeprazole', 'Ranitidine', 'Metformin'
]
box=ttk.Combobox(patinfolabelframe,values=tablets,state="readonly",width=50,font=('arial',10,'bold'))
box.set("Select A Tablet")
box.grid(row=0,column=1, padx=5, pady=5)

refno_label = Label(patinfolabelframe, text="Reference No:", anchor="w",bg='silver',font=('arial',10,'bold'))
refno_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
refno_entry = Entry(patinfolabelframe, width=60)
refno_entry.grid(row=1, column=1, padx=5, pady=5)

dose_label = Label(patinfolabelframe, text="Dose:", anchor="w",bg='silver',font=('arial',10,'bold'))
dose_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)
dose_entry = Entry(patinfolabelframe, width=60)
dose_entry.grid(row=2, column=1, padx=5, pady=5)

tablets_label = Label(patinfolabelframe, text="No of Tablets:", anchor="w",bg='silver',font=('arial',10,'bold'))
tablets_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)
tablets_entry = Entry(patinfolabelframe, width=60)
tablets_entry.grid(row=3, column=1, padx=5, pady=5)

lot_label = Label(patinfolabelframe, text="Lot:", anchor="w",bg='silver',font=('arial',10,'bold'))
lot_label.grid(row=4, column=0, sticky=W, padx=5, pady=5)
lot_entry = Entry(patinfolabelframe, width=60)
lot_entry.grid(row=4, column=1, padx=5, pady=5)

issue_date_label = Label(patinfolabelframe, text="Issue Date:", anchor="w",bg='silver',font=('arial',10,'bold'))
issue_date_label.grid(row=5, column=0, sticky=W, padx=5, pady=5)
issue_date_entry = Entry(patinfolabelframe, width=60)
issue_date_entry.grid(row=5, column=1, padx=5, pady=5)

exp_date_label = Label(patinfolabelframe, text="Exp Date:", anchor="w",bg='silver',font=('arial',10,'bold'))
exp_date_label.grid(row=6, column=0, sticky=W, padx=5, pady=5)
exp_date_entry = Entry(patinfolabelframe, width=60)
exp_date_entry.grid(row=6, column=1, padx=5, pady=5)

side_effect_label =Label(patinfolabelframe, text="Side Effect:", anchor="w", background='silver', font=('arial', 10, 'bold'))
side_effect_label.grid(row=7, column=0, sticky=W, padx=5, pady=5)
side_effect_entry = Entry(patinfolabelframe, width=60)
side_effect_entry.grid(row=7, column=1, padx=5, pady=5)

daily_dose_label = Label(patinfolabelframe, text="Daily Dose:", anchor="w", background='silver', font=('arial', 10, 'bold'))
daily_dose_label.grid(row=8, column=0, sticky=W, padx=5, pady=5)
daily_dose_entry = Entry(patinfolabelframe, width=60)
daily_dose_entry.grid(row=8, column=1, padx=5, pady=5)


futinfo=Label(patinfolabelframe,text='Further Information', anchor="w",bg='silver',font=('arial',10,'bold'))
futinfo.grid(row=0,column=2, sticky=W, padx=5, pady=5)
futinfoentry=Entry(patinfolabelframe,width=60)
futinfoentry.grid(row=0,column=3,padx=5, pady=5)

blood_pressure_label = Label(patinfolabelframe, text="Blood Pressure:", anchor="w",bg='silver',font=('arial',10,'bold'))
blood_pressure_label.grid(row=1, column=2, sticky=W, padx=5, pady=5)
blood_pressure_entry = Entry(patinfolabelframe, width=60)
blood_pressure_entry.grid(row=1, column=3, padx=5, pady=5)

storage_advice_label = Label(patinfolabelframe, text="Storage advice:", anchor="w",bg='silver',font=('arial',10,'bold'))
storage_advice_label.grid(row=2, column=2, sticky=W, padx=5, pady=5)
storage_advice_entry = Entry(patinfolabelframe, width=60)
storage_advice_entry.grid(row=2, column=3, padx=5, pady=5)

medication_label = Label(patinfolabelframe, text="Medication:", anchor="w",bg='silver',font=('arial',10,'bold'))
medication_label.grid(row=3, column=2, sticky=W, padx=5, pady=5)
medication_entry = Entry(patinfolabelframe, width=60)
medication_entry.grid(row=3, column=3, padx=5, pady=5)

patient_id_label = Label(patinfolabelframe, text="Patient Id:", anchor="w",bg='silver',font=('arial',10,'bold'))
patient_id_label.grid(row=4, column=2, sticky=W, padx=5, pady=5)
patient_id_entry = Entry(patinfolabelframe, width=60)
patient_id_entry.grid(row=4, column=3, padx=5, pady=5)

nhs_number_label = Label(patinfolabelframe, text="NHS Number:", anchor="w",bg='silver',font=('arial',10,'bold'))
nhs_number_label.grid(row=5, column=2, sticky=W, padx=5, pady=5)
nhs_number_entry = Entry(patinfolabelframe, width=60)
nhs_number_entry.grid(row=5, column=3, padx=5, pady=5)

patient_name_label = Label(patinfolabelframe, text="Patient Name:", anchor="w",bg='silver',font=('arial',10,'bold'))
patient_name_label.grid(row=6, column=2, sticky=W, padx=5, pady=5)
patient_name_entry = Entry(patinfolabelframe, width=60)
patient_name_entry.grid(row=6, column=3, padx=5, pady=5)

dob_label = Label(patinfolabelframe, text="Date Of Birth:", anchor="w",bg='silver',font=('arial',10,'bold'))
dob_label.grid(row=7, column=2, sticky=W, padx=5, pady=5)
dob_entry = Entry(patinfolabelframe, width=60)
dob_entry.grid(row=7, column=3, padx=5, pady=5)

patient_address_label = Label(patinfolabelframe, text="Patient Address:", anchor="w",bg='silver',font=('arial',10,'bold'))
patient_address_label.grid(row=8, column=2, sticky=W, padx=5, pady=5)
patient_address_entry = Entry(patinfolabelframe, width=60)
patient_address_entry.grid(row=8, column=3, padx=5, pady=5)

prescriptionframe=LabelFrame(patientframe,text="Precription",bd=5,relief=RIDGE,bg='silver',font=('arial',10,'bold'),fg='black')
prescriptionframe.pack()

textReceipt=Text(prescriptionframe,font=('arial',12,'bold'),bd=5,width=52,height=15)
textReceipt.grid(row=0,column=0)

buttonframe=Frame(root,bd=10,relief=RIDGE,bg='silver')
buttonframe.place(x=0,y=438)

prescriptionbutton=Button(buttonframe,text='Prescription',anchor=CENTER,bg='green',font=('arial',10,'bold'),width=23,command=generate_prescription)
prescriptionbutton.grid(row=0,column=0)

prescriptiondatabutton=Button(buttonframe,text='Prescription Data',anchor=CENTER,bg='green',font=('arial',10,'bold'),width=23,command=insert_to_treeview)
prescriptiondatabutton.grid(row=0,column=1)

updatebutton=Button(buttonframe,text='Update',anchor=CENTER,bg='green',font=('arial',10,'bold'),width=23,command=update)
updatebutton.grid(row=0,column=2)

deletebutton=Button(buttonframe,text='Delete',anchor=CENTER,bg='green',font=('arial',10,'bold'),width=23,command=delete)
deletebutton.grid(row=0,column=3)

searchbutton=Button(buttonframe,text='search',anchor=CENTER,bg='green',font=('arial',10,'bold'),width=23,command=search)
searchbutton.grid(row=0,column=5)

display_data_button = Button(buttonframe, text='Display Data', anchor=CENTER, bg='green', font=('arial', 10, 'bold'), width=23, command=display_data)
display_data_button.grid(row=0, column=4)


resetbutton=Button(buttonframe,text='Reset',anchor=CENTER,bg='green',font=('arial',10,'bold'),width=23,command=reset)
resetbutton.grid(row=0,column=6)



exitbutton=Button(buttonframe,text='Exit',anchor=CENTER,bg='green',font=('arial',10,'bold'),width=23,command=ex)
exitbutton.grid(row=0,column=7)

treeframe=Frame(root,bd=10,relief=RIDGE,bg='silver')
treeframe.place(x=0,y=490,width=1528,height=298)

columns = [
    "Name Of Tablets", "Reference no", "Dose", "No of tablets", "Lot", "Issue Date",
    "Exp Date", "Side Effect", "Daily Dose", "Further Information", "Blood Pressure",
    "Storage advice", "Medication", "Patient Id", "NHS Number", "Patient Name",
    "Date Of Birth", "Patient Address"
]
tree=ttk.Treeview(treeframe,columns=columns,show="headings")

tree.heading("Name Of Tablets", text="Name Of Tablets")
tree.heading("Reference no", text="Reference no")
tree.heading("Dose", text="Dose")
tree.heading("No of tablets", text="No of tablets")
tree.heading("Lot", text="Lot")
tree.heading("Issue Date", text="Issue Date")
tree.heading("Exp Date", text="Exp Date")
tree.heading("Side Effect", text="Side Effect")
tree.heading("Daily Dose", text="Daily Dose")
tree.heading("Further Information", text="Further Information")
tree.heading("Blood Pressure", text="Blood Pressure")
tree.heading("Storage advice", text="Storage advice")
tree.heading("Medication", text="Medication")
tree.heading("Patient Id", text="Patient Id")
tree.heading("NHS Number", text="NHS Number")
tree.heading("Patient Name", text="Patient Name")
tree.heading("Date Of Birth", text="Date Of Birth")
tree.heading("Patient Address", text="Patient Address")

tree.column("Name Of Tablets", width=250, anchor=W)
tree.column("Reference no", width=150, anchor=W)
tree.column("Dose", width=100, anchor=W)
tree.column("No of tablets", width=100, anchor=W)
tree.column("Lot", width=100, anchor=W)
tree.column("Issue Date", width=120, anchor=W)
tree.column("Exp Date", width=120, anchor=W)
tree.column("Side Effect", width=200, anchor=W)
tree.column("Daily Dose", width=120, anchor=W)
tree.column("Further Information", width=200, anchor=W)
tree.column("Blood Pressure", width=120, anchor=W)
tree.column("Storage advice", width=150, anchor=W)
tree.column("Medication", width=100, anchor=W)
tree.column("Patient Id", width=120, anchor=W)
tree.column("NHS Number", width=120, anchor=W)
tree.column("Patient Name", width=150, anchor=W)
tree.column("Date Of Birth", width=120, anchor=W)
tree.column("Patient Address", width=200, anchor=W)
scrollbar_y = ttk.Scrollbar(treeframe, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar_y.set)
scrollbar_y.pack(side=RIGHT, fill=Y)

scrollbar_x = ttk.Scrollbar(treeframe, orient="horizontal", command=tree.xview)
tree.configure(xscroll=scrollbar_x.set)
scrollbar_x.pack(side=BOTTOM, fill=X)

tree.pack(fill=BOTH, expand=True)
tree.bind("<<TreeviewSelect>>", select)




root.mainloop()
