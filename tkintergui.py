
# create window open program using library tkinter
import os
import pymysql
import tkinter as tk

root = tk.Tk()  # capital letter used for class
root.geometry("1250x650+0+0")  # geometry function for give width and height to window
root.title("Result")  # title function for give title to that window
root.config(bg="black")  # config is used for give colour to the window


def reset_window():
    sid.set("")
    name.set("")
    degree.set("")
    class_.set("")
    phone.set('')
    email.set("")
    python.set(0)
    ml.set(0)
    sql.set(0)
    total.set(0)
    per.set(0)
    grade.set("")


def close_window():
    root.destroy()
    pass
   

def search_file():
    a = os.listdir("result")
    if f"{sid.get()}.txt" in a:
        with open(f"result\{sid.get()}.txt", "r") as f:
            info = f.read().split(",")
            name.set(info[1])
            degree.set(info[2])
            class_.set(info[3])
            phone.set(info[4])
            email.set(info[5])
            python.set(info[6])
            ml.set(info[7])
            sql.set(info[8])
            total.set(info[9])
            per.set(info[10])
            grade.set(info[11])

    else:
        tk.messagebox.showerror("ERROR", "record does not exist")


def tot():
    a = python.get() + ml.get() + sql.get()
    total.set(a)

    percent = a / 3
    per.set(percent)

    if percent > 75:
        grade.set("A")
    elif percent > 65:
        grade.set("B")
    elif percent > 55:
        grade.set("C")
    elif percent > 35:
        grade.set("D")
    else:
        grade.set("F")


def connect_db():
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="cdac",
                         
                         database="pydb")
    cursor = db.cursor()
    return db, cursor


# connect_db()


def save_db():
    tot()
    db, cursor = connect_db()
    query = f"""insert into result3 values('{sid.get()}','{name.get()}',
    '{degree.get()}','{class_.get()}','{phone.get()}','{email.get()}',
    {python.get()},{ml.get()},{sql.get()},{total.get()},{per.get()},'{grade.get()}')"""
    cursor.execute(query)
    db.commit()
    cursor.close()
    db.close()


def saves():
    db, cursor = connect_db()
    query = f'select sid from result3 where sid= {sid.get()}'
    cursor.execute(query)
    res = cursor.fetchone()
    if res:
        query = f'delete from result3 where sid={sid.get()}'
        cursor.execute(query)
        db.commit()
        save_db()
        tk.messagebox.showinfo('success', 'record updated successfully')
    else:
        save_db()
        tk.messagebox.showinfo("success", "record saved successfully")

    cursor.close()


def search_db():
    db, cursor = connect_db()
    query = f'select*from result3 where sid={sid.get()}'
    cursor.execute(query)
    record = cursor.fetchone()
    if record:
        name.set(record[1])
        degree.set(record[2])
        class_.set(record[3])
        phone.set(record[4])
        email.set(record[5])
        python.set(record[6])
        ml.set(record[7])
        sql.set(record[8])
        total.set(record[9])
        per.set(record[10])
        grade.set(record[11])
    else:
        tk.messagebox.showinfo('not found', 'record does not exist')


top_frame = tk.Frame(root, bg="white")  # frame is used for create  frame
top_frame.place(x=5, y=5, width=1240, height=100)  # place function is used for where we want that frame

left_frame = tk.Frame(root, bg="white")  # same for left frame
left_frame.place(x=5, y=110, width=617, height=430)

right_frame = tk.Frame(root, bg="white")  # same for right frame
right_frame.place(x=628, y=110, width=617, height=430)

btn_frame = tk.Frame(root, bg="white")  # same for btn frame
btn_frame.place(x=5, y=545, width=1240, height=100)

title = tk.Label(top_frame, text="Result 2.0", font=("times new roman", 40, "bold"), bg="white",
                 fg="red")  # lable is used for text
title.pack(pady=25)

font = ("times new roman", 20, "bold")
bg = "white"
fg = "black"

#  left frame informtion

sid = tk.StringVar()  # Stringvar is used for  information written is consider as string

S_info = tk.Label(left_frame, text="S_info", font=font, bg=bg, fg='purple')
S_info.grid(row=0, column=0, padx=5, pady=5)  # grid function is used for to give place to veriable

sid_text = tk.Label(left_frame, text="S_id", font=font, bg=bg, fg=fg)
sid_text.grid(row=1, column=0, padx=5, pady=5)

sid_entry = tk.Entry(left_frame, textvariable=sid, font=font, bg=bg, fg=fg)
sid_entry.grid(row=1, column=1, padx=5, pady=5)

name = tk.StringVar()
name_text = tk.Label(left_frame, text="Name", font=font, bg=bg, fg=fg)
name_text.grid(row=2, column=0, padx=5, pady=5)

name_entry = tk.Entry(left_frame, textvariable=name, font=font, bg=bg, fg=fg)
name_entry.grid(row=2, column=1, padx=5, pady=5)

degree = tk.StringVar()

degree_text = tk.Label(left_frame, text="Degree", font=font, bg=bg, fg=fg)
degree_text.grid(row=3, column=0, padx=5, pady=5)

degree_entry = tk.Entry(left_frame, textvariable=degree, font=font, bg=bg, fg=fg)
degree_entry.grid(row=3, column=1, padx=5, pady=5)

class_ = tk.StringVar()

class_text = tk.Label(left_frame, text="Class", font=font, bg=bg, fg=fg)
class_text.grid(row=4, column=0, padx=5, pady=5)

class_entry = tk.Entry(left_frame, textvariable=class_, font=font, bg=bg, fg=fg)
class_entry.grid(row=4, column=1, padx=5, pady=6)

phone = tk.StringVar()

phone_text = tk.Label(left_frame, text="Phone", font=font, bg=bg, fg=fg)
phone_text.grid(row=5, column=0, padx=5, pady=5)

phone_entry = tk.Entry(left_frame, textvariable=phone, font=font, bg=bg, fg=fg)
phone_entry.grid(row=5, column=1, padx=5, pady=5)

email = tk.StringVar()

email_text = tk.Label(left_frame, text="Email", font=font, bg=bg, fg=fg)
email_text.grid(row=6, column=0, padx=5, pady=5)

email_entry = tk.Entry(left_frame, textvariable=email, font=font, bg=bg, fg=fg)
email_entry.grid(row=6, column=1, padx=5, pady=5)

# right frame information


M_info = tk.Label(right_frame, text="M_info", font=font, bg=bg, fg='purple')
M_info.grid(row=0, column=0, padx=5, pady=5)

python = tk.IntVar()

python_text = tk.Label(right_frame, text="Python", font=font, bg=bg, fg=fg)
python_text.grid(row=1, column=0, padx=5, pady=5)

python_entry = tk.Entry(right_frame, textvariable=python, font=font, bg=bg)
python_entry.grid(row=1, column=1, padx=5, pady=5)

ml = tk.IntVar()

ml_text = tk.Label(right_frame, text="ML", font=font, bg=bg, fg=fg)
ml_text.grid(row=2, column=0, padx=5, pady=5)

ml_entry = tk.Entry(right_frame, textvariable=ml, font=font, bg=bg)
ml_entry.grid(row=2, column=1, padx=5, pady=5)

sql = tk.IntVar()

sql_text = tk.Label(right_frame, text="SQL", font=font, bg=bg, fg=fg)
sql_text.grid(row=3, column=0, padx=5, pady=5)

sql_entry = tk.Entry(right_frame, textvariable=sql, font=font, bg=bg)
sql_entry.grid(row=3, column=1, padx=5, pady=5)

total = tk.IntVar()


total_text = tk.Label(right_frame, text="Total", font=font, bg=bg, fg=fg)
total_text.grid(row=4, column=0, padx=5, pady=5)

total_entry = tk.Entry(right_frame, textvariable=total, font=font, bg=bg, fg=fg)
total_entry.grid(row=4, column=1, padx=5, pady=5)

per = tk.IntVar()

per_text = tk.Label(right_frame, text="Percentage %", font=font, bg=bg, fg=fg)
per_text.grid(row=5, column=0, padx=5, pady=5)

per_entry = tk.Entry(right_frame, textvariable=per, font=font, bg=bg, fg=fg)
per_entry.grid(row=5, column=1, padx=5, pady=5)

grade = tk.StringVar()

grade_text = tk.Label(right_frame, text="Grade", font=font, bg=bg, fg=fg)
grade_text.grid(row=6, column=0, padx=5, pady=5)

grade_entry = tk.Entry(right_frame, textvariable=grade, font=font, bg=bg, fg=fg)
grade_entry.grid(row=6, column=1, padx=5, pady=6)

# creating buttuns in btn frame

exit_btn = tk.Button(btn_frame, text="Exit", font=font, bg="red", fg='black', command=close_window)
exit_btn.pack(padx=5, pady=30, side=tk.RIGHT)

save_btn = tk.Button(btn_frame, text="Save", font=font, bg="green", fg='black', command=saves)
save_btn.pack(padx=5, pady=30, side=tk.RIGHT)

reset_btn = tk.Button(btn_frame, text="Reset", font=font, bg="skyblue", fg='black', command=reset_window)
reset_btn.pack(padx=5, pady=30, side=tk.RIGHT)

search_btn = tk.Button(btn_frame, text="search", font=font, bg="skyblue", fg='black', command=search_db)
search_btn.pack(padx=5, pady=30, side=tk.RIGHT)

root.mainloop()  # used to continue window





