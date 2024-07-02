import tkinter as tk
from tkinter import ttk, messagebox
from classes import MotorVehicles, PKW, LKW, Motorrad

# Function to add a new vehicle
def button_add_vehicle(class_name, id, kilometers, tank, license_tag, type_of_fuel):
    try:
        if class_name == 'PKW':
            PKW.add_vehicle(id, kilometers, tank, license_tag, type_of_fuel)
        elif class_name == 'LKW':
            LKW.add_vehicle(id, kilometers, tank, license_tag, type_of_fuel)
        elif class_name == 'Motorrad':
            Motorrad.add_vehicle(id, kilometers, tank, license_tag, type_of_fuel)
        else:
            messagebox.showerror("Error", f"Invalid class name: {class_name}")
            return

        messagebox.showinfo("Success", f"{class_name} added successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add vehicle: {e}")

# Window to add a new vehicle
def button_add_object():
    new_window = tk.Toplevel(root)
    new_window.title("Add New Vehicle")
    new_window.geometry("600x370")
    new_window.configure(bg="#f7f7f7")

    # Define and place widgets with padding and a modern look
    labels_texts = ["Class:", "ID:", "Kilometers:", "Tank:", "License Tag:", "Fuel Type:"]
    entries = []
    
    for i, text in enumerate(labels_texts):
        label = ttk.Label(new_window, text=text, font=("Helvetica", 12))
        label.grid(row=i, column=0, padx=10, pady=5, sticky="E")
        entry = ttk.Entry(new_window, width=30)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)
    
    class_entry, id_entry, kilometers_entry, tank_entry, license_tag_entry, fuel_type_entry = entries

    def add_vehicle():
        try:
            id = int(id_entry.get())
            kilometers = int(kilometers_entry.get())
            tank = int(tank_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for ID, kilometers, and tank.")
            return
        
        class_name = class_entry.get()
        license_tag = license_tag_entry.get()
        type_of_fuel = fuel_type_entry.get()

        if not all([class_name, license_tag, type_of_fuel]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        button_add_vehicle(class_name, id, kilometers, tank, license_tag, type_of_fuel)

    add_vehicle_button = ttk.Button(new_window, text='Add Vehicle', command=add_vehicle)
    add_vehicle_button.grid(row=6, column=0, columnspan=2, pady=10)
    
    close_button = ttk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.grid(row=7, column=0, columnspan=2, pady=10)

# Remove object window
def button_remove_object():
    new_window = tk.Toplevel(root)
    new_window.title("Remove Vehicle")
    new_window.geometry("500x250")
    new_window.configure(bg="#f7f7f7")

    id_label = ttk.Label(new_window, text="ID:", font=("Helvetica", 12))
    id_label.grid(row=1, column=0, padx=10, pady=10)
    id_entry = ttk.Entry(new_window, width=30)
    id_entry.grid(row=1, column=1, padx=10, pady=10)

    def remove_vehicle():
        try:
            id = int(id_entry.get())
            for vehicle in MotorVehicles.instances:
                if vehicle.id == id:
                    vehicle.remove_vehicle()
                    messagebox.showinfo("Success", f"Vehicle with ID {id} removed successfully!")
                    return
            messagebox.showerror("Error", f"No vehicle found with ID {id}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numerical ID.")

    remove_vehicle_button = ttk.Button(new_window, text='Remove Vehicle', command=remove_vehicle)
    remove_vehicle_button.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

    close_button = ttk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

# Function to tank a vehicle
def button_tank_up():
    new_window = tk.Toplevel(root)
    new_window.title("Tank Up Vehicle")
    new_window.geometry("500x309")
    new_window.configure(bg="#f7f7f7")

    labels_texts = ["ID:", "Amount:", "Fuel:"]
    entries = []
    
    for i, text in enumerate(labels_texts):
        label = ttk.Label(new_window, text=text, font=("Helvetica", 12))
        label.grid(row=i, column=0, padx=10, pady=5, sticky="E")
        entry = ttk.Entry(new_window, width=30)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)
    
    id_entry, amount_entry, fuel_entry = entries

    def tank_up():
        try:
            id = int(id_entry.get())
            amount = int(amount_entry.get())
            fuel = fuel_entry.get()
            
            for vehicle in MotorVehicles.instances:
                if vehicle.id == id:
                    if vehicle.__class__.__name__ == 'PKW':
                        PKW.tank_up(id, amount, fuel)
                    elif vehicle.__class__.__name__ == 'LKW':
                        LKW.tank_up(id, amount, fuel)
                    elif vehicle.__class__.__name__ == 'Motorrad':
                        Motorrad.tank_up(id, amount, fuel)
                    else:
                        messagebox.showerror("Error", f"Invalid class name: {vehicle.__class__.__name__}")
                        return
                    messagebox.showinfo("Success", f"Tanked up vehicle with ID {id} with {amount} liters of {fuel}.")
                    return
            messagebox.showerror("Error", f"No vehicle found with ID {id}.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for ID and amount.")

    button_tank_up = ttk.Button(new_window, text='Confirm', command=tank_up)
    button_tank_up.grid(row=4, column=0, columnspan=2, pady=10)

    close_button = ttk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.grid(row=5, column=0, columnspan=2, pady=10)

def get_fuel():  
    messagebox.showinfo("Fuel by Month", f"{MotorVehicles.get_tank_by_month()}")

# Function to read out all objects based on class name
def button_readout_class():
    class_name = button_readout_entry.get().strip()

    try:
        if class_name == 'MotorVehicles':
            all_vehicles_info = MotorVehicles.get_all_vehicles_information()
        elif class_name == 'PKW':
            all_vehicles_info = PKW.get_all_vehicles_information()
        elif class_name == 'LKW':
            all_vehicles_info = LKW.get_all_vehicles_information()
        elif class_name == 'Motorrad':
            all_vehicles_info = Motorrad.get_all_vehicles_information()
        else:
            messagebox.showerror("Error", f"Invalid class name: {class_name}")
            return

        messagebox.showinfo(f"All {class_name} Information", all_vehicles_info)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read out class information: {e}")

# Main tkinter window setup
root = tk.Tk()
root.title("Vehicle Management System")
root.geometry("707x436")
root.configure(bg="#f7f7f7")

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12), background="#f7f7f7")
style.configure("TButton", font=("Helvetica", 12), padding=10)

label = ttk.Label(root, text="Choose an action", font=("Helvetica", 14, "bold"))
label.grid(row=0, column=1, padx=20, pady=20, columnspan=2)

# Button for adding a new object
button_class_label = ttk.Label(root, text='Add a new vehicle')
button_class_label.grid(row=1, column=0, padx=25, pady=10, sticky="W")
button_class = ttk.Button(root, text="Add", command=button_add_object)
button_class.grid(row=1, column=1, padx=25, pady=10)

# Button for deleting an object 
button_remove_label = ttk.Label(root, text='Remove a vehicle')
button_remove_label.grid(row=2, column=0, padx=25, pady=10, sticky="W")
button_remove = ttk.Button(root, text="Remove", command=button_remove_object)
button_remove.grid(row=2, column=1, padx=25, pady=10)

# Tank up a vehicle
button_tank_label = ttk.Label(root, text="Tank up")
button_tank_label.grid(row=3, column=0, padx=20, pady=10, sticky="W")
button_tank = ttk.Button(root, text="Tank", command=button_tank_up)
button_tank.grid(row=3, column=1, padx=25, pady=10)

# Get fuel for last month
button_get_fuel_label = ttk.Label(root, text="Fuel by month")
button_get_fuel_label.grid(row=4, column=0, padx=20, pady=10, sticky="W")
button_get_fuel = ttk.Button(root, text="Info", command=get_fuel)
button_get_fuel.grid(row=4, column=1, padx=25, pady=10)

# Entry and button for reading out all objects of a specified class
button_readout_label = ttk.Label(root, text="PKW, LKW, Motorrad\nor MotorVehicles:")
button_readout_label.grid(row=5, column=0, padx=25, pady=10, sticky="W")

button_readout_entry = ttk.Entry(root, width=20)
button_readout_entry.grid(row=5, column=1, padx=25, pady=10)

button_readout = ttk.Button(root, text="Readout", command=button_readout_class)
button_readout.grid(row=5, column=2, padx=25, pady=10)

# Run the tkinter main loop
root.mainloop()
