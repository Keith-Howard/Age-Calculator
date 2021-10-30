import tkinter as tk
from tkinter import messagebox
from calendar import monthrange


def create_label(module, window, background_color, text, row, column):
    return module.Label(window, background=background_color, text=text).grid(row=row, column=column)


def display_labels(module, window, row):
    heading_color = 'light blue'
    label_color = 'light green'
    create_label(module, window, heading_color, 'Date of Birth', row, 1)
    create_label(module, window, heading_color, 'Given Date', row, 4)
    row += 1
    create_label(module, window, label_color, 'Day', row, 0)
    create_label(module, window, label_color, 'Day', row, 3)
    row += 1
    create_label(module, window, label_color, 'Month', row, 0)
    create_label(module, window, label_color, 'Month', row, 3)
    row += 1
    create_label(module, window, label_color, 'Year', row, 0)
    create_label(module, window, label_color, 'Year', row, 3)
    row += 1
    create_label(module, window, label_color, ' ', row, 0)
    row += 1
    create_label(module, window, label_color, 'Years', row, 2)
    row += 2
    create_label(module, window, label_color, 'Months', row, 2)
    row += 2
    create_label(module, window, label_color, 'Days', row, 2)


def calculate_years(b_month, given_month, b_day, given_day, b_year, given_year):
    if b_month > given_month or (b_month == given_month and b_day > given_day):
        given_year -= 1
    return given_year - b_year


def calculate_months(b_month, given_month, b_day, given_day):
    if b_month > given_month:
        given_month += 12
    elif b_month == given_month and b_day > given_day:
        given_month += 11
    elif b_month < given_month and b_day > given_day:
        given_month -= 1
    return given_month - b_month


def calculate_days(given_month, b_day, given_day):
    given_year = int(entered_given_year.get())
    days_in_given_month = find_days_in_month(given_month, given_year)
    if b_day > given_day:
        given_day = given_day + days_in_given_month
    return given_day - b_day


def calculate_resultant_age():
    if is_valid_textboxes(entered_birth_day.get(), entered_birth_month.get(), entered_birth_year.get(),
                          entered_given_day.get(),
                          entered_given_month.get(), entered_given_year.get()):
        if is_day_valid(entered_birth_day.get(), int(entered_birth_month.get()), int(entered_birth_year.get())) and \
                is_day_valid(entered_given_day.get(), int(entered_given_month.get()), int(entered_given_year.get())):
            clear_outbox_textboxes()
            birth_day = int(entered_birth_day.get())
            birth_month = int(entered_birth_month.get())
            birth_year = int(entered_birth_year.get())
            future_day = int(entered_given_day.get())
            future_month = int(entered_given_month.get())
            future_year = int(entered_given_year.get())
            # year
            year_ans = calculate_years(birth_month, future_month, birth_day, future_day, birth_year, future_year)
            # month
            month_ans = calculate_months(birth_month, future_month, birth_day, future_day)
            # day
            day_ans = calculate_days(birth_month, birth_day, future_day)
            output_days_textbox.insert(0, day_ans)
            output_months_textbox.insert(0, month_ans)
            output_years_textbox.insert(0, year_ans)
        else:
            messagebox.showerror("error", "Incorrect Data in Textbox")


def is_valid_textboxes(birthday, birthmonth, birthyear, givenday, givenmonth, givenyear):
    if birthday == "" or birthmonth == "" or birthyear == "" or givenday == "" or givenmonth == "" or givenyear == "":
        messagebox.showerror("Error", "Empty Textbox")
        return False
    else:
        return True


def find_days_in_month(month, year):
    amount_of_days = monthrange(year, month)
    return amount_of_days[1]


def set_year_textbox_focus(textbox, err):
    messagebox.showerror("error", err)
    if textbox == 'birth_year_textbox':
        birth_year_textbox.focus_set()
    else:
        given_year_textbox.focus_set()

# input a string
# input
# processing check if num string is a digit
# processing if a digit convert to integer
# processing check if integer is valid in between 2 different number
# output True or False


def is_number_valid(string_num, high_num, low_num):
    if string_num.isdigit():
        converted_num = int(string_num)
        if high_num >= converted_num > low_num:
            return True
        else:
            return False
    else:
        if string_num == '':
            return True
        else:
            return False


def is_year_valid(year):
    return is_number_valid(year, 9999, 0)


def is_month_valid(month):
    return is_number_valid(month, 12, 0)


def is_day_valid(day, month, year):
    days_in_month = find_days_in_month(month, year)
    return is_number_valid(day, days_in_month, 0)


# if year is emtpy return
    # if year is valid    digits and > 0 <= 9999
    #     if month is valid  digit  and 1 and 12
    #         if day is valid   digit > 0 and within the month
    #              if year and month and day has valid data then doing something
    #              return true
    #         else messagebox(bad day) and return false
    #      else messagebox(bad month) and return false
    # else messagebox(bad year) and return false


def validate_year(year, year_textbox):
    return_code = False
    if year_textbox == 'birth_year_textbox':
        month = entered_birth_month.get()
        day = entered_birth_day.get()
    else:
        month = entered_given_month.get()
        day = entered_given_day.get()
    if year != "":
        if is_number_valid(year, 9999, 0):
            converted_year = int(year)
            if month != "":
                if is_number_valid(month, 12, 0):
                    converted_month = int(month)
                    if is_day_valid(day, converted_month, converted_year):
                        return_code = True
                    else:
                        set_year_textbox_focus(year_textbox, "Too Many Days in Month " + month)
                else:
                    set_year_textbox_focus(year_textbox, year + " doesn't exist Year")
            else:
                return_code = True
        else:
            set_year_textbox_focus(year_textbox, "Enter Integer for Year")
    else:
        return_code = True
    return return_code


def validate_day(day, day_textbox):
    return_code = False
    if day_textbox == 'birth_day_textbox':
        month = entered_birth_month.get()
        year = entered_birth_year.get()
    else:
        month = entered_given_month.get()
        year = entered_given_year.get()
    if day != "":
        if is_number_valid(day, 31, 0):
            converted_day = int(day)
            if month != "":
                if is_number_valid(month, 12, 0):
                    converted_month = int(month)
                    if is_number_valid(year, 9999, 0):
                        converted_year = int(year)
                        days_in_month = find_days_in_month(converted_month, converted_year)
                        if days_in_month >= converted_day > 0:
                            return_code = True
                        else:
                            messagebox.showerror("Error", "Too Many Days in Month " + month)
            else:
                return_code = True
        else:
            messagebox.showerror("Error", "Please enter a valid Day")
    else:
        return_code = True
    return return_code


def validate_month(month, month_textbox):
    return_code = False
    if month_textbox == 'birth_month_textbox':
        day = entered_birth_day.get()
        year = entered_birth_year.get()
    else:
        day = entered_given_day.get()
        year = entered_given_year.get()
    if month != "":
        if is_number_valid(month, 12, 0):
            converted_month = int(month)
            if year != "":
                if is_number_valid(year, 9999, 0):
                    converted_year = int(year)
                    if is_day_valid(day, converted_month, converted_year):
                        return_code = True
                    else:
                        messagebox.showerror("Error", "Too Many Days in Month")
                else:
                    messagebox.showerror("Error", "Enter a valid Year")
            else:
                return_code = True
        else:
            messagebox.showerror("Error", "Enter a valid Month")
    else:
        return_code = True
    return return_code


def clear_textboxes():
    birth_day_textbox.delete(0, tk.END)
    birth_month_textbox.delete(0, tk.END)
    birth_year_textbox.delete(0, tk.END)
    given_day_textbox.delete(0, tk.END)
    given_month_textbox.delete(0, tk.END)
    given_year_textbox.delete(0, tk.END)
    clear_outbox_textboxes()


def clear_outbox_textboxes():
    output_days_textbox.delete(0, tk.END)
    output_months_textbox.delete(0, tk.END)
    output_years_textbox.delete(0, tk.END)


def create_textbox(module, window, row, column, text_var=None):
    if text_var is None:
        textbox = module.Entry(window)
    else:
        textbox = module.Entry(window, textvariable=text_var)
    textbox.grid(row=row, column=column)
    return textbox


def create_button(module, window, background_color, text, command, row, column, padding):
    return module.Button(window, background=background_color, text=text, command=command).grid(row=row, column=column,
                                                                                               pady=padding)


main_window = tk.Tk(screenName=None, baseName=None, className=" Age Calculator")
main_window.configure(background='light green')
main_window.geometry('460x300')

row = 0
button_color = 'red'
display_labels(tk, main_window, row)
row += 1

entered_birth_day = tk.StringVar()
birth_day_textbox = create_textbox(tk, main_window, row, 1, entered_birth_day)
day_register = main_window.register(validate_day)
birth_day_textbox.config(validate="key", validatecommand=(day_register, '%P', 'birth_day_textbox'))

entered_given_day = tk.StringVar()
given_day_textbox = create_textbox(tk, main_window, row, 4, entered_given_day)
# reuse callback from day_register, provide extra parameter to identify the textbox for validation
given_day_textbox.config(validate="key", validatecommand=(day_register, '%P', 'given_day_textbox'))
row += 1

entered_birth_month = tk.StringVar()
birth_month_textbox = create_textbox(tk, main_window, row, 1, entered_birth_month)
month_register = main_window.register(validate_month)
birth_month_textbox.config(validate="key", validatecommand=(month_register, '%P', 'birth_month_textbox'))

entered_given_month = tk.StringVar()
given_month_textbox = create_textbox(tk, main_window, row, 4, entered_given_month)
given_month_textbox.config(validate="key", validatecommand=(month_register, '%P', 'given_month_textbox'))
row += 1

entered_birth_year = tk.StringVar()
birth_year_textbox = create_textbox(tk, main_window, row, 1, entered_birth_year)
year_register = main_window.register(validate_year)
birth_year_textbox.config(validate="focusout", validatecommand=(year_register, '%P', 'birth_year_textbox'))

entered_given_year = tk.StringVar()
given_year_textbox = create_textbox(tk, main_window, row, 4, entered_given_year)
given_year_textbox.config(validate="focusout", validatecommand=(year_register, '%P', 'given_year_textbox'))

row += 1
resultant_age = create_button(tk, main_window, button_color, 'Resultant Age', calculate_resultant_age, row, 2, 0)
row += 2
output_years_textbox = create_textbox(tk, main_window, row, 2)
row += 2
output_months_textbox = create_textbox(tk, main_window, row, 2)
row += 2
output_days_textbox = create_textbox(tk, main_window, row, 2)
row += 1
create_button(tk, main_window, button_color, 'Clear All', clear_textboxes, row, 2, 5)

main_window.mainloop()
