from tkinter import *

def selected_button(button):
    global equation_text
    equation_label.set("")
    equation_text += str(button)
    equation_label.set(equation_text)

def calc():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Math Error")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""
    except:
        equation_label.set("Unknown Error")
        equation_text = ""

def clear():
    global equation_text
    equation_text = ""
    equation_label.set("0")

window = Tk()
window.geometry("500x780")
window.title("calaculator App")
window.configure(bg="#1f1f2e")
window.resizable(False, False)

img = PhotoImage(file="calculator.png")
window.iconphoto(True, img)


equation_text = ""
equation_label = StringVar()
equation_label.set("0")

label = Label(window,
              font=("Segoe UI", 22, "bold"),
              textvariable=equation_label,
              bg="#2c3e50",
              fg="#fff",
              width=26,
              height=3,
              bd=5,
              relief="sunken",
              anchor="e",
              padx=10)
label.pack(pady=10)

frame = Frame(window, pady=5, bg="#1f1f2e")
frame.pack()

# Design
btn_color = "gray"
op_color = "#f39c12"
equal_color = "#000"
clear_color = "#e74c3c"
text_color = "white"
font_style = ("Segoe UI", 14, "bold")

# Numbers Buttons
button_1 = Button(frame, text=1, height=4, width=9, font=font_style,
                  bg=btn_color, fg=text_color, command=lambda: selected_button(1), cursor="hand2")
button_1.grid(row=0, column=0)

button_2 = Button(frame, text=2, height=4, width=9, font=font_style,
                  bg=btn_color, fg=text_color, command=lambda: selected_button(2), cursor="hand2")
button_2.grid(row=0, column=1)

button_3 = Button(frame, text=3, height=4, width=9, font=font_style,
                  bg=btn_color, fg=text_color, command=lambda: selected_button(3), cursor="hand2")
button_3.grid(row=0, column=2)

button_4 = Button(frame, text=4, height=4, width=9, font=font_style,
                  bg=btn_color, fg=text_color, command=lambda: selected_button(4), cursor="hand2")
button_4.grid(row=1, column=0)

button_5 = Button(frame, text=5, height=4, width=9, font=font_style,
                  bg=btn_color, fg=text_color, command=lambda: selected_button(5), cursor="hand2")
button_5.grid(row=1, column=1)

button_6 = Button(frame, text=6, height=4, width=9, font=font_style,
                  bg=btn_color, fg=text_color, command=lambda: selected_button(6), cursor="hand2")
button_6.grid(row=1, column=2)

button_7 = Button(frame, text=7, height=4, width=9, font=font_style,
                  bg=btn_color, fg=text_color, command=lambda: selected_button(7), cursor="hand2")
button_7.grid(row=2, column=0)

button_8 = Button(frame, text=8, height=4, width=9, font=font_style,
                  bg=btn_color, fg=text_color, command=lambda: selected_button(8), cursor="hand2")
button_8.grid(row=2, column=1)

button_9 = Button(frame, text=9, height=4, width=9, font=font_style,
                  bg=btn_color, fg=text_color, command=lambda: selected_button(9), cursor="hand2")
button_9.grid(row=2, column=2)

button_0 = Button(frame, text=0, height=4, width=9, font=font_style,
                  bg=btn_color, fg=text_color, command=lambda: selected_button(0), cursor="hand2")
button_0.grid(row=3, column=0)

# Operations Buttons
plus = Button(frame, text="+", height=4, width=9, font=font_style,
              bg=op_color, fg=text_color, command=lambda: selected_button("+"), cursor="hand2")
plus.grid(row=0, column=3)

minus = Button(frame, text="-", height=4, width=9, font=font_style,
               bg=op_color, fg=text_color, command=lambda: selected_button("-"), cursor="hand2")
minus.grid(row=1, column=3)

product = Button(frame, text="x", height=4, width=9, font=font_style,
                 bg=op_color, fg=text_color, command=lambda: selected_button("*"), cursor="hand2")
product.grid(row=2, column=3)

divide = Button(frame, text="÷", height=4, width=9, font=font_style,
                bg=op_color, fg=text_color, command=lambda: selected_button("/"), cursor="hand2")
divide.grid(row=3, column=3)

equal = Button(frame, text="=", height=4, width=9, font=font_style,
               bg=equal_color, fg=text_color, command=calc, cursor="hand2")
equal.grid(row=3, column=2)

decimal = Button(frame, text=".", height=4, width=9, font=font_style,
                 bg=btn_color, fg=text_color, command=lambda: selected_button("."), cursor="hand2")
decimal.grid(row=3, column=1)

clear_button = Button(frame, text="CLEAR", height=3, width=40, font=font_style,
                      bg=clear_color, fg="white", command=clear, cursor="hand2")
clear_button.grid(row=4, column=0, columnspan=4, pady=(10, 0))

window.mainloop()
