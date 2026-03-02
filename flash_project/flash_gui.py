import tkinter as tk
from tkinter import filedialog
import sqlite3

from flash_process import perform_flash


DB_NAME = "flash_database.db"


# Load Binary File
def browse_binary():

    file_path = filedialog.askopenfilename(

        title="Select Binary File",

        filetypes=[("Binary Files","*.bin"),
                   ("All Files","*.*")]
    )

    binary_entry.delete(0,tk.END)

    binary_entry.insert(0,file_path)



# Start Flashing
def start_flash():

    ecu_id = ecu_entry.get()

    binary = binary_entry.get()

    old_sw = old_entry.get()

    new_sw = new_entry.get()


    session_id,steps,status,error,recovery = perform_flash(

        ecu_id,
        binary,
        old_sw,
        new_sw
    )


    result_box.delete(1.0,tk.END)


    result_box.insert(tk.END,"SESSION ID : "+session_id+"\n\n")

    result_box.insert(tk.END,"FLASHING STEPS\n\n")


    for s in steps:

        result_box.insert(tk.END,s+"\n")


    result_box.insert(tk.END,"\n")


    result_box.insert(tk.END,"FINAL STATUS : "+status+"\n")

    result_box.insert(tk.END,"ERROR : "+error+"\n")

    result_box.insert(tk.END,"RECOVERY : "+recovery+"\n")



# View Flash History
def view_history():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM flash_history_customer")

    records = cursor.fetchall()

    conn.close()


    result_box.delete(1.0,tk.END)

    result_box.insert(tk.END,"FLASH HISTORY\n\n")


    for row in records:

        result_box.insert(tk.END,
        "Session ID : "+row[0]+"\n")

        result_box.insert(tk.END,
        "ECU ID : "+row[1]+"\n")

        result_box.insert(tk.END,
        "Status : "+row[2]+"\n")

        result_box.insert(tk.END,
        "Timestamp : "+row[3]+"\n")

        result_box.insert(tk.END,
        "Binary : "+row[4]+"\n")

        result_box.insert(tk.END,
        "Old SW : "+row[5]+"\n")

        result_box.insert(tk.END,
        "New SW : "+row[6]+"\n")

        result_box.insert(tk.END,
        "Error : "+row[7]+"\n")

        result_box.insert(tk.END,
        "Recovery : "+row[8]+"\n")

        result_box.insert(tk.END,
        "--------------------------\n")



# GUI Window

root = tk.Tk()

root.title("Customer ECU Flashing Tool")

root.geometry("600x550")



tk.Label(root,text="ECU ID").pack()

ecu_entry = tk.Entry(root,width=40)

ecu_entry.pack()



tk.Label(root,text="Binary File").pack()

binary_entry = tk.Entry(root,width=50)

binary_entry.pack()


tk.Button(root,

          text="Load Binary File",

          command=browse_binary).pack()



tk.Label(root,text="Existing Software Version").pack()

old_entry = tk.Entry(root)

old_entry.pack()



tk.Label(root,text="New Software Version").pack()

new_entry = tk.Entry(root)

new_entry.pack()



tk.Button(root,

          text="Start Flashing",

          command=start_flash,

          bg="green",

          fg="white").pack(pady=10)



tk.Button(root,

          text="View Flash History",

          command=view_history,

          bg="blue",

          fg="white").pack()



result_box = tk.Text(root,

                     height=20,

                     width=70)

result_box.pack()


root.mainloop()