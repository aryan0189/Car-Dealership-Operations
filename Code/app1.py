import tkinter as tk
from tkinter import ttk
import mysql.connector

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Student493",
    database="cds"
)
cursor = db.cursor()

# GUI setup
root = tk.Tk()
root.title("Car Dealership Management")

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# ----------------------------------- Customer Management -----------------------------------
customer_frame = ttk.Frame(notebook)
notebook.add(customer_frame, text='Customers')

# Customer form
customer_form_frame = ttk.LabelFrame(customer_frame, text='Customer Form')
customer_form_frame.pack(fill='x', padx=10, pady=10)

customer_first_name = tk.StringVar()
customer_last_name = tk.StringVar()
customer_email = tk.StringVar()
customer_phone = tk.StringVar()
customer_address = tk.StringVar()

ttk.Label(customer_form_frame, text='First Name:').grid(row=0, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(customer_form_frame, textvariable=customer_first_name).grid(row=0, column=1, padx=5, pady=5)
# Add more form fields for other customer details

# Customer list
customer_list_frame = ttk.LabelFrame(customer_frame, text='Customer List')
customer_list_frame.pack(fill='both', padx=10, pady=10, expand=True)

customer_list = ttk.Treeview(customer_list_frame, columns=('CustomerID', 'FirstName', 'LastName', 'Email', 'Phone', 'Address'), show='headings')
customer_list.pack(fill='both', expand=True)

# Configure column headings
customer_list.heading('CustomerID', text='Customer ID')
customer_list.heading('FirstName', text='First Name')
customer_list.heading('LastName', text='Last Name')
customer_list.heading('Email', text='Email')
customer_list.heading('Phone', text='Phone')
customer_list.heading('Address', text='Address')

# Configure column widths
customer_list.column('CustomerID', width=100)
customer_list.column('FirstName', width=150)
customer_list.column('LastName', width=150)
customer_list.column('Email', width=200)
customer_list.column('Phone', width=150)
customer_list.column('Address', width=250)

# Populate customer list
def populate_customer_list():
    cursor.execute("SELECT * FROM Customers")
    customers = cursor.fetchall()
    customer_list.delete(*customer_list.get_children())
    for customer in customers:
        customer_list.insert('', 'end', values=customer)

populate_customer_list()

# ----------------------------------- Employee Management -----------------------------------
employee_frame = ttk.Frame(notebook)
notebook.add(employee_frame, text='Employees')

# Employee form
employee_form_frame = ttk.LabelFrame(employee_frame, text='Employee Form')
employee_form_frame.pack(fill='x', padx=10, pady=10)

employee_first_name = tk.StringVar()
employee_last_name = tk.StringVar()
employee_email = tk.StringVar()
employee_phone = tk.StringVar()
employee_department = tk.StringVar()
employee_salary = tk.DoubleVar()

ttk.Label(employee_form_frame, text='First Name:').grid(row=0, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(employee_form_frame, textvariable=employee_first_name).grid(row=0, column=1, padx=5, pady=5)
# Add more form fields for other employee details

# Employee list
employee_list_frame = ttk.LabelFrame(employee_frame, text='Employee List')
employee_list_frame.pack(fill='both', padx=10, pady=10, expand=True)

employee_list = ttk.Treeview(employee_list_frame, columns=('EmployeeID', 'FirstName', 'LastName', 'Email', 'Phone', 'Department', 'Salary'), show='headings')
employee_list.pack(fill='both', expand=True)

# Configure column headings and widths
employee_list.heading('EmployeeID', text='Employee ID')
employee_list.column('EmployeeID', width=100)
# Configure other columns

# Populate employee list
def populate_employee_list():
    cursor.execute("SELECT * FROM Employees")
    employees = cursor.fetchall()
    employee_list.delete(*employee_list.get_children())
    for employee in employees:
        employee_list.insert('', 'end', values=employee)

populate_employee_list()

# ----------------------------------- Supplier Management -----------------------------------
supplier_frame = ttk.Frame(notebook)
notebook.add(supplier_frame, text='Suppliers')

# Supplier form
supplier_form_frame = ttk.LabelFrame(supplier_frame, text='Supplier Form')
supplier_form_frame.pack(fill='x', padx=10, pady=10)

supplier_name = tk.StringVar()
supplier_contact_person = tk.StringVar()
supplier_email = tk.StringVar()
supplier_phone = tk.StringVar()
supplier_address = tk.StringVar()

ttk.Label(supplier_form_frame, text='Supplier Name:').grid(row=0, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(supplier_form_frame, textvariable=supplier_name).grid(row=0, column=1, padx=5, pady=5)
# Add more form fields for other supplier details

# Supplier list
supplier_list_frame = ttk.LabelFrame(supplier_frame, text='Supplier List')
supplier_list_frame.pack(fill='both', padx=10, pady=10, expand=True)

supplier_list = ttk.Treeview(supplier_list_frame, columns=('SupplierID', 'SupplierName', 'ContactPerson', 'Email', 'Phone', 'Address'), show='headings')
supplier_list.pack(fill='both', expand=True)

# Configure column headings and widths
supplier_list.heading('SupplierID', text='Supplier ID')
supplier_list.column('SupplierID', width=100)
# Configure other columns

# Populate supplier list
def populate_supplier_list():
    cursor.execute("SELECT * FROM Suppliers")
    suppliers = cursor.fetchall()
    supplier_list.delete(*supplier_list.get_children())
    for supplier in suppliers:
        supplier_list.insert('', 'end', values=supplier)

populate_supplier_list()

# ----------------------------------- Parts Management -----------------------------------
parts_frame = ttk.Frame(notebook)
notebook.add(parts_frame, text='Parts')

# Parts form
parts_form_frame = ttk.LabelFrame(parts_frame, text='Parts Form')
parts_form_frame.pack(fill='x', padx=10, pady=10)

part_name = tk.StringVar()
part_description = tk.StringVar()
part_supplier_id = tk.IntVar()
part_cost = tk.DoubleVar()

ttk.Label(parts_form_frame, text='Part Name:').grid(row=0, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(parts_form_frame, textvariable=part_name).grid(row=0, column=1, padx=5, pady=5)
# Add more form fields for other part details

# Parts list
parts_list_frame = ttk.LabelFrame(parts_frame, text='Parts List')
parts_list_frame.pack(fill='both', padx=10, pady=10,)
# ----------------------------------- Inventory Management -----------------------------------
inventory_frame = ttk.Frame(notebook)
notebook.add(inventory_frame, text='Inventory')

# Inventory form
inventory_form_frame = ttk.LabelFrame(inventory_frame, text='Inventory Form')
inventory_form_frame.pack(fill='x', padx=10, pady=10)

inventory_part_id = tk.IntVar()
inventory_quantity = tk.IntVar()

ttk.Label(inventory_form_frame, text='Part ID:').grid(row=0, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(inventory_form_frame, textvariable=inventory_part_id).grid(row=0, column=1, padx=5, pady=5)
ttk.Label(inventory_form_frame, text='Quantity:').grid(row=1, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(inventory_form_frame, textvariable=inventory_quantity).grid(row=1, column=1, padx=5, pady=5)

# Inventory list
inventory_list_frame = ttk.LabelFrame(inventory_frame, text='Inventory List')
inventory_list_frame.pack(fill='both', padx=10, pady=10, expand=True)

inventory_list = ttk.Treeview(inventory_list_frame, columns=('InventoryID', 'PartID', 'Quantity'), show='headings')
inventory_list.pack(fill='both', expand=True)

# Configure column headings and widths
inventory_list.heading('InventoryID', text='Inventory ID')
inventory_list.column('InventoryID', width=100)
inventory_list.heading('PartID', text='Part ID')
inventory_list.column('PartID', width=100)
inventory_list.heading('Quantity', text='Quantity')
inventory_list.column('Quantity', width=100)

# Populate inventory list
def populate_inventory_list():
    cursor.execute("SELECT * FROM Inventory")
    inventory_data = cursor.fetchall()
    inventory_list.delete(*inventory_list.get_children())
    for item in inventory_data:
        inventory_list.insert('', 'end', values=item)

populate_inventory_list()

# ----------------------------------- Models Management -----------------------------------
models_frame = ttk.Frame(notebook)
notebook.add(models_frame, text='Models')

# Models form
models_form_frame = ttk.LabelFrame(models_frame, text='Models Form')
models_form_frame.pack(fill='x', padx=10, pady=10)

model_name = tk.StringVar()
model_brand = tk.StringVar()
model_year = tk.IntVar()
model_price = tk.DoubleVar()

ttk.Label(models_form_frame, text='Model Name:').grid(row=0, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(models_form_frame, textvariable=model_name).grid(row=0, column=1, padx=5, pady=5)
ttk.Label(models_form_frame, text='Brand:').grid(row=1, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(models_form_frame, textvariable=model_brand).grid(row=1, column=1, padx=5, pady=5)
ttk.Label(models_form_frame, text='Year:').grid(row=2, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(models_form_frame, textvariable=model_year).grid(row=2, column=1, padx=5, pady=5)
ttk.Label(models_form_frame, text='Price:').grid(row=3, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(models_form_frame, textvariable=model_price).grid(row=3, column=1, padx=5, pady=5)

# Models list
models_list_frame = ttk.LabelFrame(models_frame, text='Models List')
models_list_frame.pack(fill='both', padx=10, pady=10, expand=True)

models_list = ttk.Treeview(models_list_frame, columns=('ModelID', 'ModelName', 'Brand', 'Year', 'Price'), show='headings')
models_list.pack(fill='both', expand=True)

# Configure column headings and widths
models_list.heading('ModelID', text='Model ID')
models_list.column('ModelID', width=100)
models_list.heading('ModelName', text='Model Name')
models_list.column('ModelName', width=200)
models_list.heading('Brand', text='Brand')
models_list.column('Brand', width=100)
models_list.heading('Year', text='Year')
models_list.column('Year', width=100)
models_list.heading('Price', text='Price')
models_list.column('Price', width=100)

# Populate models list
def populate_models_list():
    cursor.execute("SELECT * FROM Models")
    models_data = cursor.fetchall()
    models_list.delete(*models_list.get_children())
    for model in models_data:
        models_list.insert('', 'end', values=model)

populate_models_list()

# ----------------------------------- Cars Management -----------------------------------
cars_frame = ttk.Frame(notebook)
notebook.add(cars_frame, text='Cars')

# Cars form
cars_form_frame = ttk.LabelFrame(cars_frame, text='Cars Form')
cars_form_frame.pack(fill='x', padx=10, pady=10)

car_model_id = tk.IntVar()
car_vin = tk.StringVar()
car_color = tk.StringVar()
car_mileage = tk.IntVar()

ttk.Label(cars_form_frame, text='Model ID:').grid(row=0, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(cars_form_frame, textvariable=car_model_id).grid(row=0, column=1, padx=5, pady=5)
ttk.Label(cars_form_frame, text='VIN:').grid(row=1, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(cars_form_frame, textvariable=car_vin).grid(row=1, column=1, padx=5, pady=5)
ttk.Label(cars_form_frame, text='Color:').grid(row=2, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(cars_form_frame, textvariable=car_color).grid(row=2, column=1, padx=5, pady=5)
ttk.Label(cars_form_frame, text='Mileage:').grid(row=3, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(cars_form_frame, textvariable=car_mileage).grid(row=3, column=1, padx=5, pady=5)

# Cars list
cars_list_frame = ttk.LabelFrame(cars_frame, text='Cars List')
cars_list_frame.pack(fill='both', padx=10, pady=10, expand=True)

cars_list = ttk.Treeview(cars_list_frame, columns=('CarID', 'ModelID', 'VIN', 'Color', 'Mileage'), show='headings')
cars_list.pack(fill='both', expand=True)

# Configure column headings and widths
cars_list.heading('CarID', text='Car ID')
cars_list.column('CarID', width=100)
cars_list.heading('ModelID', text='Model ID')
cars_list.column('ModelID', width=100)
cars_list.heading('VIN', text='VIN')
cars_list.column('VIN', width=200)
cars_list.heading('Color', text='Color')
cars_list.column('Color', width=100)
cars_list.heading('Mileage', text='Mileage')
cars_list.column('Mileage', width=100)

# Populate cars list
def populate_cars_list():
    cursor.execute("SELECT * FROM Cars")
    cars_data = cursor.fetchall()
    cars_list.delete(*cars_list.get_children())
    for car in cars_data:
        cars_list.insert('', 'end', values=car)

populate_cars_list()

# ----------------------------------- Sales Management -----------------------------------
sales_frame = ttk.Frame(notebook)
notebook.add(sales_frame, text='Sales')

# Sales form
sales_form_frame = ttk.LabelFrame(sales_frame, text='Sales Form')
sales_form_frame.pack(fill='x', padx=10, pady=10)

sale_car_id = tk.IntVar()
sale_customer_id = tk.IntVar()
sale_employee_id = tk.IntVar()
sale_date = tk.StringVar()
sale_price = tk.DoubleVar()

ttk.Label(sales_form_frame, text='Car ID:').grid(row=0, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(sales_form_frame, textvariable=sale_car_id).grid(row=0, column=1, padx=5, pady=5)
ttk.Label(sales_form_frame, text='Customer ID:').grid(row=1, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(sales_form_frame, textvariable=sale_customer_id).grid(row=1, column=1, padx=5, pady=5)
ttk.Label(sales_form_frame, text='Employee ID:').grid(row=2, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(sales_form_frame, textvariable=sale_employee_id).grid(row=2, column=1, padx=5, pady=5)
ttk.Label(sales_form_frame, text='Sale Date:').grid(row=3, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(sales_form_frame, textvariable=sale_date).grid(row=3, column=1, padx=5, pady=5)
ttk.Label(sales_form_frame, text='Sale Price:').grid(row=4, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(sales_form_frame, textvariable=sale_price).grid(row=4, column=1, padx=5, pady=5)

# Sales list
sales_list_frame = ttk.LabelFrame(sales_frame, text='Sales List')
sales_list_frame.pack(fill='both', padx=10, pady=10, expand=True)

sales_list = ttk.Treeview(sales_list_frame, columns=('SaleID', 'CarID', 'CustomerID', 'EmployeeID', 'SaleDate', 'SalePrice'), show='headings')
sales_list.pack(fill='both', expand=True)

# Configure column headings and widths
sales_list.heading('SaleID', text='Sale ID')
sales_list.column('SaleID', width=100)
sales_list.heading('CarID', text='Car ID')
sales_list.column('CarID', width=100)
sales_list.heading('CustomerID', text='Customer ID')
sales_list.column('CustomerID', width=100)
sales_list.heading('EmployeeID', text='Employee ID')
sales_list.column('EmployeeID', width=100)
sales_list.heading('SaleDate', text='Sale Date')
sales_list.column('SaleDate', width=100)
sales_list.heading('SalePrice', text='Sale Price')
sales_list.column('SalePrice', width=100)

# Populate sales list
def populate_sales_list():
    cursor.execute("SELECT * FROM Sales")
    sales_data = cursor.fetchall()
    sales_list.delete(*sales_list.get_children())
    for sale in sales_data:
        sales_list.insert('', 'end', values=sale)

populate_sales_list()

# ----------------------------------- Services Management -----------------------------------
services_frame = ttk.Frame(notebook)
notebook.add(services_frame, text='Services')

# Services form
services_form_frame = ttk.LabelFrame(services_frame, text='Services Form')
services_form_frame.pack(fill='x', padx=10, pady=10)

service_car_id = tk.IntVar()
service_employee_id = tk.IntVar()
service_date = tk.StringVar()
service_description = tk.StringVar()
service_cost = tk.DoubleVar()

ttk.Label(services_form_frame, text='Car ID:').grid(row=0, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(services_form_frame, textvariable=service_car_id).grid(row=0, column=1, padx=5, pady=5)
ttk.Label(services_form_frame, text='Employee ID:').grid(row=1, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(services_form_frame, textvariable=service_employee_id).grid(row=1, column=1, padx=5, pady=5)
ttk.Label(services_form_frame, text='Service Date:').grid(row=2, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(services_form_frame, textvariable=service_date).grid(row=2, column=1, padx=5, pady=5)
ttk.Label(services_form_frame, text='Description:').grid(row=3, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(services_form_frame, textvariable=service_description).grid(row=3, column=1, padx=5, pady=5)
ttk.Label(services_form_frame, text='Cost:').grid(row=4, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(services_form_frame, textvariable=service_cost).grid(row=4, column=1, padx=5, pady=5)

# Services list
services_list_frame = ttk.LabelFrame(services_frame, text='Services List')
services_list_frame.pack(fill='both', padx=10, pady=10, expand=True)

services_list = ttk.Treeview(services_list_frame, columns=('ServiceID', 'CarID', 'EmployeeID', 'ServiceDate', 'ServiceDescription', 'Cost'), show='headings')
services_list.pack(fill='both', expand=True)

# Configure column headings and widths
services_list.heading('ServiceID', text='Service ID')
services_list.column('ServiceID', width=100)
services_list.heading('CarID', text='Car ID')
services_list.column('CarID', width=100)
services_list.heading('EmployeeID', text='Employee ID')
services_list.column('EmployeeID', width=100)
services_list.heading('ServiceDate', text='Service Date')
services_list.column('ServiceDate', width=100)
services_list.heading('ServiceDescription', text='Description')
services_list.column('ServiceDescription', width=200)
services_list.heading('Cost', text='Cost')
services_list.column('Cost', width=100)

# Populate services list
def populate_services_list():
    cursor.execute("SELECT * FROM Services")
    services_data = cursor.fetchall()
    services_list.delete(*services_list.get_children())
    for service in services_data:
        services_list.insert('', 'end', values=service)

populate_services_list()

# ----------------------------------- Warranties Management -----------------------------------
warranties_frame = ttk.Frame(notebook)
notebook.add(warranties_frame, text='Warranties')

# Warranties form
warranties_form_frame = ttk.LabelFrame(warranties_frame, text='Warranties Form')
warranties_form_frame.pack(fill='x', padx=10, pady=10)

warranty_car_id = tk.IntVar()
warranty_start_date = tk.StringVar()
warranty_end_date = tk.StringVar()
warranty_terms = tk.StringVar()

ttk.Label(warranties_form_frame, text='Car ID:').grid(row=0, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(warranties_form_frame, textvariable=warranty_car_id).grid(row=0, column=1, padx=5, pady=5)
ttk.Label(warranties_form_frame, text='Start Date:').grid(row=1, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(warranties_form_frame, textvariable=warranty_start_date).grid(row=1, column=1, padx=5, pady=5)
ttk.Label(warranties_form_frame, text='End Date:').grid(row=2, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(warranties_form_frame, textvariable=warranty_end_date).grid(row=2, column=1, padx=5, pady=5)
ttk.Label(warranties_form_frame, text='Terms:').grid(row=3, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(warranties_form_frame, textvariable=warranty_terms).grid(row=3, column=1, padx=5, pady=5)

# Warranties list
warranties_list_frame = ttk.LabelFrame(warranties_frame, text='Warranties List')
warranties_list_frame.pack(fill='both', padx=10, pady=10, expand=True)

warranties_list = ttk.Treeview(warranties_list_frame, columns=('WarrantyID', 'CarID', 'WarrantyStartDate', 'WarrantyEndDate', 'WarrantyTerms'), show='headings')
warranties_list.pack(fill='both', expand=True)

# Configure column headings and widths
warranties_list.heading('WarrantyID', text='Warranty ID')
warranties_list.column('WarrantyID', width=100)
warranties_list.heading('CarID', text='Car ID')
warranties_list.column('CarID', width=100)
warranties_list.heading('WarrantyStartDate', text='Start Date')
warranties_list.column('WarrantyStartDate', width=100)
warranties_list.heading('WarrantyEndDate', text='End Date')
warranties_list.column('WarrantyEndDate', width=100)
warranties_list.heading('WarrantyTerms', text='Terms')
warranties_list.column('WarrantyTerms', width=200)

# Populate warranties list
def populate_warranties_list():
    cursor.execute("SELECT * FROM Warranties")
    warranties_data = cursor.fetchall()
    warranties_list.delete(*warranties_list.get_children())
    for warranty in warranties_data:
        warranties_list.insert('', 'end', values=warranty)

populate_warranties_list()

root.mainloop()

# ----------------------------------- Appointments Management -----------------------------------
appointments_frame = ttk.Frame(notebook)
notebook.add(appointments_frame, text='Appointments')

# Appointments form
appointments_form_frame = ttk.LabelFrame(appointments_frame, text='Appointments Form')
appointments_form_frame.pack(fill='x', padx=10, pady=10)

appointment_customer_id = tk.IntVar()
appointment_employee_id = tk.IntVar()
appointment_date = tk.StringVar()
appointment_time = tk.StringVar()
appointment_reason = tk.StringVar()

ttk.Label(appointments_form_frame, text='Customer ID:').grid(row=0, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(appointments_form_frame, textvariable=appointment_customer_id).grid(row=0, column=1, padx=5, pady=5)
ttk.Label(appointments_form_frame, text='Employee ID:').grid(row=1, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(appointments_form_frame, textvariable=appointment_employee_id).grid(row=1, column=1, padx=5, pady=5)
ttk.Label(appointments_form_frame, text='Date:').grid(row=2, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(appointments_form_frame, textvariable=appointment_date).grid(row=2, column=1, padx=5, pady=5)
ttk.Label(appointments_form_frame, text='Time:').grid(row=3, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(appointments_form_frame, textvariable=appointment_time).grid(row=3, column=1, padx=5, pady=5)
ttk.Label(appointments_form_frame, text='Reason:').grid(row=4, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(appointments_form_frame, textvariable=appointment_reason).grid(row=4, column=1, padx=5, pady=5)

# Appointments list
appointments_list_frame = ttk.LabelFrame(appointments_frame, text='Appointments List')
appointments_list_frame.pack(fill='both', padx=10, pady=10, expand=True)

appointments_list = ttk.Treeview(appointments_list_frame, columns=('AppointmentID', 'CustomerID', 'EmployeeID', 'AppointmentDate', 'AppointmentTime', 'Reason'), show='headings')
appointments_list.pack(fill='both', expand=True)

# Configure column headings and widths
appointments_list.heading('AppointmentID', text='Appointment ID')
appointments_list.column('AppointmentID', width=100)
appointments_list.heading('CustomerID', text='Customer ID')
appointments_list.column('CustomerID', width=100)
appointments_list.heading('EmployeeID', text='Employee ID')
appointments_list.column('EmployeeID', width=100)
appointments_list.heading('AppointmentDate', text='Date')
appointments_list.column('AppointmentDate', width=100)
appointments_list.heading('AppointmentTime', text='Time')
appointments_list.column('AppointmentTime', width=100)
appointments_list.heading('Reason', text='Reason')
appointments_list.column('Reason', width=200)

# Populate appointments list
def populate_appointments_list():
    cursor.execute("SELECT * FROM Appointments")
    appointments_data = cursor.fetchall()
    appointments_list.delete(*appointments_list.get_children())
    for appointment in appointments_data:
        appointments_list.insert('', 'end', values=appointment)

populate_appointments_list()

# ----------------------------------- Finance Management -----------------------------------
finance_frame = ttk.Frame(notebook)
notebook.add(finance_frame, text='Finance')

# Finance form
finance_form_frame = ttk.LabelFrame(finance_frame, text='Finance Form')
finance_form_frame.pack(fill='x', padx=10, pady=10)

finance_customer_id = tk.IntVar()
finance_loan_amount = tk.DoubleVar()
finance_interest_rate = tk.DoubleVar()
finance_loan_term = tk.IntVar()
finance_monthly_payment = tk.DoubleVar()

ttk.Label(finance_form_frame, text='Customer ID:').grid(row=0, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(finance_form_frame, textvariable=finance_customer_id).grid(row=0, column=1, padx=5, pady=5)
ttk.Label(finance_form_frame, text='Loan Amount:').grid(row=1, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(finance_form_frame, textvariable=finance_loan_amount).grid(row=1, column=1, padx=5, pady=5)
ttk.Label(finance_form_frame, text='Interest Rate:').grid(row=2, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(finance_form_frame, textvariable=finance_interest_rate).grid(row=2, column=1, padx=5, pady=5)
ttk.Label(finance_form_frame, text='Loan Term:').grid(row=3, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(finance_form_frame, textvariable=finance_loan_term).grid(row=3, column=1, padx=5, pady=5)
ttk.Label(finance_form_frame, text='Monthly Payment:').grid(row=4, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(finance_form_frame, textvariable=finance_monthly_payment).grid(row=4, column=1, padx=5, pady=5)

# Finance list
finance_list_frame = ttk.LabelFrame(finance_frame, text='Finance List')
finance_list_frame.pack(fill='both', padx=10, pady=10, expand=True)

finance_list = ttk.Treeview(finance_list_frame, columns=('FinanceID', 'CustomerID', 'LoanAmount', 'InterestRate', 'LoanTerm', 'MonthlyPayment'), show='headings')
finance_list.pack(fill='both', expand=True)

# Configure column headings and widths
finance_list.heading('FinanceID', text='Finance ID')
finance_list.column('FinanceID', width=100)
finance_list.heading('CustomerID', text='Customer ID')
finance_list.column('CustomerID', width=100)
finance_list.heading('LoanAmount', text='Loan Amount')
finance_list.column('LoanAmount', width=100)
finance_list.heading('InterestRate', text='Interest Rate')
finance_list.column('InterestRate', width=100)
finance_list.heading('LoanTerm', text='Loan Term')
finance_list.column('LoanTerm', width=100)
finance_list.heading('MonthlyPayment', text='Monthly Payment')
finance_list.column('MonthlyPayment', width=100)

# Populate finance list
def populate_finance_list():
    cursor.execute("SELECT * FROM Finance")
    finance_data = cursor.fetchall()
    finance_list.delete(*finance_list.get_children())
    for finance_record in finance_data:
        finance_list.insert('', 'end', values=finance_record)

populate_finance_list()

root.mainloop()

# ----------------------------------- Reviews Management -----------------------------------
reviews_frame = ttk.Frame(notebook)
notebook.add(reviews_frame, text='Reviews')

# Reviews form
reviews_form_frame = ttk.LabelFrame(reviews_frame, text='Reviews Form')
reviews_form_frame.pack(fill='x', padx=10, pady=10)

review_customer_id = tk.IntVar()
review_car_id = tk.IntVar()
review_rating = tk.IntVar()
review_text = tk.StringVar()
review_date = tk.StringVar()

ttk.Label(reviews_form_frame, text='Customer ID:').grid(row=0, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(reviews_form_frame, textvariable=review_customer_id).grid(row=0, column=1, padx=5, pady=5)
ttk.Label(reviews_form_frame, text='Car ID:').grid(row=1, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(reviews_form_frame, textvariable=review_car_id).grid(row=1, column=1, padx=5, pady=5)
ttk.Label(reviews_form_frame, text='Rating:').grid(row=2, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(reviews_form_frame, textvariable=review_rating).grid(row=2, column=1, padx=5, pady=5)
ttk.Label(reviews_form_frame, text='Review Text:').grid(row=3, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(reviews_form_frame, textvariable=review_text).grid(row=3, column=1, padx=5, pady=5)
ttk.Label(reviews_form_frame, text='Review Date:').grid(row=4, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(reviews_form_frame, textvariable=review_date).grid(row=4, column=1, padx=5, pady=5)

# Reviews list
reviews_list_frame = ttk.LabelFrame(reviews_frame, text='Reviews List')
reviews_list_frame.pack(fill='both', padx=10, pady=10, expand=True)

reviews_list = ttk.Treeview(reviews_list_frame, columns=('ReviewID', 'CustomerID', 'CarID', 'Rating', 'ReviewText', 'ReviewDate'), show='headings')
reviews_list.pack(fill='both', expand=True)

# Configure column headings and widths
reviews_list.heading('ReviewID', text='Review ID')
reviews_list.column('ReviewID', width=100)
reviews_list.heading('CustomerID', text='Customer ID')
reviews_list.column('CustomerID', width=100)
reviews_list.heading('CarID', text='Car ID')
reviews_list.column('CarID', width=100)
reviews_list.heading('Rating', text='Rating')
reviews_list.column('Rating', width=100)
reviews_list.heading('ReviewText', text='Review Text')
reviews_list.column('ReviewText', width=300)
reviews_list.heading('ReviewDate', text='Review Date')
reviews_list.column('ReviewDate', width=100)

# Populate reviews list
def populate_reviews_list():
    cursor.execute("SELECT * FROM Reviews")
    reviews_data = cursor.fetchall()
    reviews_list.delete(*reviews_list.get_children())
    for review in reviews_data:
        reviews_list.insert('', 'end', values=review)

populate_reviews_list()

# ----------------------------------- Promotions Management -----------------------------------
promotions_frame = ttk.Frame(notebook)
notebook.add(promotions_frame, text='Promotions')

# Promotions form
promotions_form_frame = ttk.LabelFrame(promotions_frame, text='Promotions Form')
promotions_form_frame.pack(fill='x', padx=10, pady=10)

promotion_name = tk.StringVar()
promotion_description = tk.StringVar()
promotion_start_date = tk.StringVar()
promotion_end_date = tk.StringVar()
promotion_discount_percentage = tk.DoubleVar()

ttk.Label(promotions_form_frame, text='Promotion Name:').grid(row=0, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(promotions_form_frame, textvariable=promotion_name).grid(row=0, column=1, padx=5, pady=5)
ttk.Label(promotions_form_frame, text='Description:').grid(row=1, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(promotions_form_frame, textvariable=promotion_description).grid(row=1, column=1, padx=5, pady=5)
ttk.Label(promotions_form_frame, text='Start Date:').grid(row=2, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(promotions_form_frame, textvariable=promotion_start_date).grid(row=2, column=1, padx=5, pady=5)
ttk.Label(promotions_form_frame, text='End Date:').grid(row=3, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(promotions_form_frame, textvariable=promotion_end_date).grid(row=3, column=1, padx=5, pady=5)
ttk.Label(promotions_form_frame, text='Discount Percentage:').grid(row=4, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(promotions_form_frame, textvariable=promotion_discount_percentage).grid(row=4, column=1, padx=5, pady=5)

# Promotions list
promotions_list_frame = ttk.LabelFrame(promotions_frame, text='Promotions List')
promotions_list_frame.pack(fill='both', padx=10, pady=10, expand=True)

promotions_list = ttk.Treeview(promotions_list_frame, columns=('PromotionID', 'PromotionName', 'PromotionDescription', 'StartDate', 'EndDate', 'DiscountPercentage'), show='headings')
promotions_list.pack(fill='both', expand=True)

# Configure column headings and widths
promotions_list.heading('PromotionID', text='Promotion ID')
promotions_list.column('PromotionID', width=100)
promotions_list.heading('PromotionName', text='Promotion Name')
promotions_list.column('PromotionName', width=150)
promotions_list.heading('PromotionDescription', text='Description')
promotions_list.column('PromotionDescription', width=300)
promotions_list.heading('StartDate', text='Start Date')
promotions_list.column('StartDate', width=100)
promotions_list.heading('EndDate', text='End Date')
promotions_list.column('EndDate', width=100)
promotions_list.heading('DiscountPercentage', text='Discount Percentage')
promotions_list.column('DiscountPercentage', width=150)

# Populate promotions list
def populate_promotions_list():
    cursor.execute("SELECT * FROM Promotions")
    promotions_data = cursor.fetchall()
    promotions_list.delete(*promotions_list.get_children())
    for promotion in promotions_data:
        promotions_list.insert('', 'end', values=promotion)

populate_promotions_list()

root.mainloop()

# ----------------------------------- Accessories Management -----------------------------------
accessories_frame = ttk.Frame(notebook)
notebook.add(accessories_frame, text='Accessories')

# Accessories form
accessories_form_frame = ttk.LabelFrame(accessories_frame, text='Accessories Form')
accessories_form_frame.pack(fill='x', padx=10, pady=10)

accessory_name = tk.StringVar()
accessory_description = tk.StringVar()
accessory_price = tk.DoubleVar()

ttk.Label(accessories_form_frame, text='Accessory Name:').grid(row=0, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(accessories_form_frame, textvariable=accessory_name).grid(row=0, column=1, padx=5, pady=5)
ttk.Label(accessories_form_frame, text='Description:').grid(row=1, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(accessories_form_frame, textvariable=accessory_description).grid(row=1, column=1, padx=5, pady=5)
ttk.Label(accessories_form_frame, text='Price:').grid(row=2, column=0, padx=5, pady=5, sticky='W')
ttk.Entry(accessories_form_frame, textvariable=accessory_price).grid(row=2, column=1, padx=5, pady=5)

# Accessories list
accessories_list_frame = ttk.LabelFrame(accessories_frame, text='Accessories List')
accessories_list_frame.pack(fill='both', padx=10, pady=10, expand=True)

accessories_list = ttk.Treeview(accessories_list_frame, columns=('AccessoryID', 'AccessoryName', 'AccessoryDescription', 'Price'), show='headings')
accessories_list.pack(fill='both', expand=True)

# Configure column headings and widths
accessories_list.heading('AccessoryID', text='Accessory ID')
accessories_list.column('AccessoryID', width=100)
accessories_list.heading('AccessoryName', text='Accessory Name')
accessories_list.column('AccessoryName', width=200)
accessories_list.heading('AccessoryDescription', text='Description')
accessories_list.column('AccessoryDescription', width=300)
accessories_list.heading('Price', text='Price')
accessories_list.column('Price', width=100)

# Populate accessories list
def populate_accessories_list():
    cursor.execute("SELECT * FROM Accessories")
    accessories_data = cursor.fetchall()
    accessories_list.delete(*accessories_list.get_children())
    for accessory in accessories_data:
        accessories_list.insert('', 'end', values=accessory)

populate_accessories_list()

root.mainloop()

#TO DO THIS
'''
try:
    # Your code here
    root.mainloop()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    db.close()
'''