from tkinter import *
from tkinter import ttk, simpledialog
import random
from BubbleSort import bubble_sort
from LinearSearch import Linear_Search
from BinarySearch import  Binary_Search

# Creating the main window
root = Tk()
root.title("Sorting Algorithm Visualizer")
root.maxsize(1920, 1080)
root.config(bg='#2C3E50')

# Variables
selected_alg = StringVar()
selected_search = StringVar()
data = []


# The main function that Draws the bars in the Canvas
def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 580
    c_width = 850
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [i / max(data) for i in data]  # normalizing the data to scale with the canvas
    for i, height in enumerate(normalizedData):  # Create boxes
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 500
        # bottom right
        x1 = ((i + 1) * x_width) + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))  # Text over boxes
    root.update_idletasks()


def edit_data():
    global data

    # Create a new window for editing the data
    edit_window = Toplevel(root)
    edit_window.title('Edit Data')
    edit_window.geometry('300x350')

    # Create a listbox containing the current data list
    data_listbox = Listbox(edit_window)
    data_listbox.pack(fill=BOTH, expand=YES)
    data_listbox.config(font=('Helvetica', 14))
    for item in data:
        data_listbox.insert(END, str(item))

    # Add a button for deleting the currently selected item from the listbox and data list
    def delete_item():
        selected = data_listbox.curselection()
        if selected:
            index = selected[0]
            data_listbox.delete(index)
            data.pop(index)

    delete_button = Button(edit_window, text='Delete Selected Item', command=delete_item)
    delete_button.pack()

    # Add a button for modifying the currently selected item in the listbox and data list
    def modify_item():
        selected = data_listbox.curselection()
        if selected:
            index = selected[0]
            new_value = simpledialog.askinteger('Modify Item', 'Enter new value:')
            if new_value is not None:
                data[index] = new_value
                data_listbox.delete(index)
                data_listbox.insert(index, str(new_value))

    modify_button = Button(edit_window, text='Modify Selected Item', command=modify_item)
    modify_button.pack()

    # Add a button for adding a new item to the listbox and data list
    def add_item():
        new_value = simpledialog.askinteger('Add Item', 'Enter new value:')
        if new_value is not None:
            data.append(new_value)
            data_listbox.insert(END, str(new_value))

    add_button = Button(edit_window, text='Add Item', command=add_item)
    add_button.pack()

    # Add a button for saving the changes and closing the window
    def save_changes():
        # Update the data list with the new values in the listbox
        new_data = []
        for i in range(data_listbox.size()):
            new_data.append(int(data_listbox.get(i)))
        data = new_data
        edit_window.destroy()
        drawData(data, ['#ADD8E6' for x in range(len(data))])

    save_button = Button(edit_window, text='Save Changes', command=save_changes)
    save_button.pack()


# Function to generate values within given range
def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    # Get input values from the input_box Text widget and split them into separate integers
    input_values = input_box.get(1.0, END).strip().split()
    input_values = [int(val) for val in input_values]

    # Add input values to the data list
    data = input_values + [random.randrange(minVal, maxVal + 1) for _ in range(size - len(input_values))]
    drawData(data, ['#ADD8E6' for x in range(len(data))])

    # Create an Edit button
    edit_button = Button(UI_frame, text='Edit', command=edit_data, bg='#FFB830', fg='black', font=('Helvetica', 12))
    edit_button.grid(row=10, column=0, padx=5, pady=5)


# Function to start the bubble sort algorithm
def StartAlgorithm():
    global data
    bubble_sort(data, drawData, speedScale.get())


# Function to start searching
def StartSearching():
    global data
    search_item = int(input_searchbox.get(1.0, END))
    if selected_search.get() == "Linear Search":
        Linear_Search(data, drawData, speedScale.get(), search_item)
    else:
        Binary_Search(data, drawData, speedScale.get(), search_item)

# UI Base Frame

# Interface to hold the widgets
UI_frame = Frame(root, width=400, height=700, bg='#34495E')
UI_frame.grid(row=0, column=1, padx=20, pady=10)

# Interface for graphics
canvas = Canvas(root, width=900, height=580, bg='white')
canvas.grid(row=0, column=0, padx=20, pady=10)

# User Interface Area

algo_label = Label(UI_frame, text='Algorithm:', bg='#34495E', fg='white', font=('Helvetica', 16, 'bold'))
algo_label.grid(row=0, column=0, padx=5, pady=5)

# Dropdown menu for algorithms
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge sort'], font=('Consolas', 12))
algMenu.grid(row=1, column=0, padx=5, pady=5)
algMenu.current(0)  # Default value of dropdown box

# Speed Scale to choose how fast or slow
speedScale = Scale(UI_frame, from_=0, to=2.0, length=200, digits=2, resolution=0.1, orient=HORIZONTAL,
                   label="Select Speed [s]", font=('Consolas', 10))
speedScale.set(0.1)
speedScale.configure(sliderrelief="flat", activebackground='#D50032')
speedScale.grid(row=5, column=0, padx=5, pady=5)

# Start button to start the sorting process
start_button = Button(UI_frame, text='Start', command=StartAlgorithm, bg='#D50032', fg='white', font=('Helvetica', 14))
start_button.grid(row=9, column=0, padx=5, pady=5)

# Slider to select the size of the array
sizeEntry = Scale(UI_frame, from_=3, to=40, length=200, resolution=1, orient=HORIZONTAL, label="Data Size",
                  font=('Consolas', 10))
sizeEntry.set(20)
sizeEntry.configure(sliderrelief="flat", activebackground='#D50032')
sizeEntry.grid(row=2, column=0, padx=5, pady=5)

# Slider to select the minimum value of the array
minEntry = Scale(UI_frame, from_=0, to=10, length=200, resolution=1, orient=HORIZONTAL, label="Min Value",
                 font=('Consolas', 10))
minEntry.configure(sliderrelief="flat", activebackground='#D50032')
minEntry.grid(row=3, column=0, padx=5, pady=5)

# Slider to select the maximum value of the array
maxEntry = Scale(UI_frame, from_=15, to=150, length=200, resolution=1, orient=HORIZONTAL, label="Max Value",
                 font=('Consolas', 10))
maxEntry.set(50)
maxEntry.configure(sliderrelief="flat", activebackground='#D50032')
maxEntry.grid(row=4, column=0, padx=5, pady=5)

# Generate button to create random data
generate_button = Button(UI_frame, text='Generate', command=Generate, bg='#3498DB', fg='black', font=('Helvetica', 14))
generate_button.grid(row=8, column=0, padx=5, pady=5)

# Text box for manual user input
input_label = Label(UI_frame, text='Input Values:', bg='#34495E', fg='white', font=('Helvetica', 12, 'bold'))
input_label.grid(row=6, column=0, padx=5, pady=5)

input_box = Text(UI_frame, height=1, width=30, font=('Consolas', 10))
input_box.grid(row=7, column=0, padx=5, pady=5, columnspan=2)

# searching part

# Interface to hold the search widgets
UI_searchframe = Frame(root, width=400, height=700, bg='#34495E')
UI_searchframe.grid(row=1, column=0, padx=20, pady=10)

# User Interface Area for search

search_label = Label(UI_searchframe, text='Search:', bg='#34495E', fg='white', font=('Helvetica', 16, 'bold'))
search_label.grid(row=0, column=0, padx=5, pady=5)

# Dropdown menu for search
searchMenu = ttk.Combobox(UI_searchframe, textvariable=selected_search, values=['Linear Search', 'Binary Search'], font=('Consolas', 12))
searchMenu.grid(row=0, column=1, padx=5, pady=5)
searchMenu.current(0)  # Default value of dropdown search box

# Text box for manual search input
input_searchlabel = Label(UI_searchframe, text='Input search element:', bg='#34495E', fg='white', font=('Helvetica', 12, 'bold'))
input_searchlabel.grid(row=0, column=2, padx=5, pady=5)

input_searchbox = Text(UI_searchframe, height=1, width=30, font=('Consolas', 10))
input_searchbox.grid(row=0, column=3, padx=5, pady=5)

# Search button to start the searching process
search_button = Button(UI_searchframe, text='Search', command=StartSearching, bg='#D50032', fg='white', font=('Helvetica', 14))
search_button.grid(row=0, column=4, padx=5, pady=5)

# Main graphics loop
root.mainloop()
