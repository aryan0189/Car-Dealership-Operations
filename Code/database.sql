-- Create the database
CREATE DATABASE CarDealerShip;
USE CarDealerShip;

-- Create the tables
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    Address VARCHAR(200)
);

CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    Department VARCHAR(50),
    Salary DECIMAL(10, 2)
);

CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,
    SupplierName VARCHAR(100),
    ContactPerson VARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    Address VARCHAR(200)
);

CREATE TABLE Parts (
    PartID INT AUTO_INCREMENT PRIMARY KEY,
    PartName VARCHAR(100),
    PartDescription VARCHAR(200),
    SupplierID INT,
    Cost DECIMAL(10, 2),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

CREATE TABLE Inventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY,
    PartID INT,
    Quantity INT,
    FOREIGN KEY (PartID) REFERENCES Parts(PartID)
);

CREATE TABLE Models (
    ModelID INT AUTO_INCREMENT PRIMARY KEY,
    ModelName VARCHAR(100),
    Brand VARCHAR(50),
    Year INT,
    Price DECIMAL(10, 2)
);

CREATE TABLE Cars (
    CarID INT AUTO_INCREMENT PRIMARY KEY,
    ModelID INT,
    VIN VARCHAR(50),
    Color VARCHAR(50),
    Mileage INT,
    FOREIGN KEY (ModelID) REFERENCES Models(ModelID)
);

CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY,
    CarID INT,
    CustomerID INT,
    EmployeeID INT,
    SaleDate DATE,
    SalePrice DECIMAL(10, 2),
    FOREIGN KEY (CarID) REFERENCES Cars(CarID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,
    CarID INT,
    EmployeeID INT,
    ServiceDate DATE,
    ServiceDescription VARCHAR(200),
    Cost DECIMAL(10, 2),
    FOREIGN KEY (CarID) REFERENCES Cars(CarID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

CREATE TABLE Warranties (
    WarrantyID INT AUTO_INCREMENT PRIMARY KEY,
    CarID INT,
    WarrantyStartDate DATE,
    WarrantyEndDate DATE,
    WarrantyTerms VARCHAR(200),
    FOREIGN KEY (CarID) REFERENCES Cars(CarID)
);

CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    EmployeeID INT,
    AppointmentDate DATE,
    AppointmentTime TIME,
    Reason VARCHAR(200),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

CREATE TABLE Finance (
    FinanceID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    LoanAmount DECIMAL(10, 2),
    InterestRate DECIMAL(5, 2),
    LoanTerm INT,
    MonthlyPayment DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    CarID INT,
    Rating INT,
    ReviewText VARCHAR(500),
    ReviewDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (CarID) REFERENCES Cars(CarID)
);

CREATE TABLE Promotions (
    PromotionID INT AUTO_INCREMENT PRIMARY KEY,
    PromotionName VARCHAR(100),
    PromotionDescription VARCHAR(200),
    StartDate DATE,
    EndDate DATE,
    DiscountPercentage DECIMAL(5, 2)
);

CREATE TABLE Accessories (
    AccessoryID INT AUTO_INCREMENT PRIMARY KEY,
    AccessoryName VARCHAR(100),
    AccessoryDescription VARCHAR(200),
    Price DECIMAL(10, 2)
);

-- Insert sample data into the tables
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address) VALUES
    ('Rahul', 'Sharma', 'rahul.sharma@example.com', '9876543210', '123 Main Street, New Delhi'),
    ('Priya', 'Gupta', 'priya.gupta@example.com', '8765432109', '456 Park Avenue, Mumbai'),
    ('Anil', 'Kumar', 'anil.kumar@example.com', '7654321098', '789 Oak Road, Bangalore'),
    ('Neha', 'Patel', 'neha.patel@example.com', '6543210987', '321 Maple Lane, Chennai'),
    ('Rohit', 'Singh', 'rohit.singh@example.com', '5432109876', '987 Pine Drive, Kolkata'),
    ('Pooja', 'Desai', 'pooja.desai@example.com', '4321098765', '654 Cedar Street, Hyderabad'),
    ('Amit', 'Kapoor', 'amit.kapoor@example.com', '3210987654', '246 Elm Avenue, Ahmedabad'),
    ('Kavita', 'Rao', 'kavita.rao@example.com', '2109876543', '369 Birch Road, Pune'),
    ('Sanjay', 'Gupta', 'sanjay.gupta@example.com', '1098765432', '753 Willow Lane, Jaipur'),
    ('Divya', 'Malhotra', 'divya.malhotra@example.com', '9012345678', '159 Oak Street, Chandigarh');

INSERT INTO Employees (FirstName, LastName, Email, Phone, Department, Salary) VALUES
    ('Aman', 'Verma', 'aman.verma@example.com', '9876543211', 'Sales', 50000.00),
    ('Sonali', 'Nair', 'sonali.nair@example.com', '8765432110', 'Service', 45000.00),
    ('Arjun', 'Reddy', 'arjun.reddy@example.com', '7654321099', 'Finance', 60000.00),
    ('Simran', 'Chopra', 'simran.chopra@example.com', '6543210988', 'Marketing', 55000.00),
    ('Yash', 'Malhotra', 'yash.malhotra@example.com', '5432109877', 'Sales', 52000.00),
    ('Ishita', 'Sharma', 'ishita.sharma@example.com', '4321098766', 'Service', 48000.00),
    ('Rohan', 'Gupta', 'rohan.gupta@example.com', '3210987655', 'Parts', 42000.00),
    ('Nisha', 'Rao', 'nisha.rao@example.com', '2109876544', 'Finance', 58000.00),
    ('Ankit', 'Patel', 'ankit.patel@example.com', '1098765433', 'Sales', 51000.00),
    ('Preeti', 'Singh', 'preeti.singh@example.com', '9012345679', 'Marketing', 54000.00);

INSERT INTO Suppliers (SupplierName, ContactPerson, Email, Phone, Address) VALUES
    ('Auto Parts Ltd.', 'Rajesh Mehta', 'sales@autopartsltd.com', '9876543212', '456 Industrial Estate, Mumbai'),
    ('Precision Components', 'Aarti Kapoor', 'info@precisioncomponents.com', '8765432111', '789 Tech Park, Bangalore'),
    ('Quality Spares Inc.', 'Sanjay Malhotra', 'sales@qualityspares.com', '7654321100', '321 Commercial Complex, Delhi'),
    ('Automotive Supplies Co.', 'Deepika Singh', 'contact@autosupplies.com', '6543210989', '654 Trade Center, Chennai'),
    ('Reliable Parts Corp.', 'Arjun Rao', 'sales@reliableparts.com', '5432109878', '987 Industrial Area, Hyderabad'),
    ('Supreme Spares Ltd.', 'Priya Gupta', 'info@supremespares.com', '4321098767', '246 Business Park, Kolkata'),
    ('Genuine Parts Distributors', 'Amit Sharma', 'sales@genuineparts.com', '3210987656', '369 Industrial Zone, Ahmedabad'),
    ('Auto Solutions Pvt. Ltd.', 'Neha Patel', 'contact@autosolutions.com', '2109876545', '753 Tech Hub, Pune'),
    ('Premier Parts Co.', 'Rohit Singh', 'sales@premierparts.com', '1098765434', '159 Commercial Estate, Jaipur'),
    ('Automotive Essentials Inc.', 'Pooja Desai', 'info@autoessentials.com', '9012345670', '753 Industrial Park, Chandigarh');

INSERT INTO Parts (PartName, PartDescription, SupplierID, Cost) VALUES
    ('Engine Oil Filter', 'High-quality oil filter for engine', 1, 500.00),
    ('Brake Pads', 'Durable brake pads for safe braking', 2, 1200.00),
    ('Spark Plugs', 'Iridium spark plugs for better performance', 3, 800.00),
    ('Air Filter', 'Reusable air filter for enhanced engine protection', 4, 400.00),
    ('Timing Belt', 'High-strength timing belt for reliable operation', 5, 1500.00),
    ('Headlights', 'LED headlights for improved visibility', 6, 2000.00),
    ('Battery', 'Long-lasting car battery', 7, 3500.00),
    ('Wiper Blades', 'Premium wiper blades for clear vision', 8, 300.00),
    ('Tires', 'All-season tires for excellent grip', 9, 4000.00),
    ('Exhaust Pipe', 'Stainless steel exhaust pipe for better performance', 10, 2500.00);

INSERT INTO Inventory (PartID, Quantity) VALUES
    (1, 50),
    (2, 30),
    (3, 40),
    (4, 60),
    (5, 25),
    (6, 35),
    (7, 20),
    (8, 70),
    (9, 45),
    (10, 30);

INSERT INTO Models (ModelName, Brand, Year, Price) VALUES
    ('Nexon', 'Tata', 2022, 800000.00),
    ('Baleno', 'Maruti Suzuki', 2021, 650000.00),
    ('Creta', 'Hyundai', 2023, 1200000.00),
    ('Verna', 'Hyundai', 2020, 900000.00),
    ('Kicks', 'Nissan', 2022, 1100000.00),
    ('City', 'Honda', 2021, 1000000.00),
    ('Seltos', 'Kia', 2023, 1300000.00),
    ('Harrier', 'Tata', 2022, 1400000.00),
    ('Amaze', 'Honda', 2020, 700000.00),
    ('Sonet', 'Kia', 2023, 900000.00);

INSERT INTO Cars (ModelID, VIN, Color, Mileage) VALUES
    (1, 'MA1234567890ABCDE', 'Red', 5000),
    (2, 'MB0987654321FGHIJ', 'White', 10000),
    (3, 'MC2345678901KLMNO', 'Black', 8000),
    (4, 'MD6789012345PQRST', 'Silver', 12000),
    (5, 'ME0123456789UVWXY', 'Blue', 7000),
    (6, 'MF4567890123ZABCD', 'Gray', 9000),
    (7, 'MG8901234567EFGHI', 'Red', 6000),
    (8, 'MH2345678901JKLMN', 'White', 11000),
    (9, 'MI6789012345OPQRS', 'Black', 4000),
    (10, 'MJ0123456789TUVWX', 'Silver', 8000);

INSERT INTO Sales (CarID, CustomerID, EmployeeID, SaleDate, SalePrice) VALUES
    (1, 1, 1, '2023-01-15', 780000.00),
    (2, 2, 5, '2022-11-20', 630000.00),
    (3, 3, 3, '2023-03-05', 1180000.00),
    (4, 4, 7, '2022-09-10', 880000.00),
    (5, 5, 2, '2023-02-01', 1080000.00),
    (6, 6, 6, '2022-12-15', 980000.00),
    (7, 7, 9, '2023-01-25', 1280000.00),
    (8, 8, 4, '2022-10-20', 1380000.00),
    (9, 9, 8, '2022-11-05', 680000.00),
    (10, 10, 10, '2023-03-10', 880000.00);

INSERT INTO Services (CarID, EmployeeID, ServiceDate, ServiceDescription, Cost) VALUES
    (1, 2, '2023-03-01', 'Oil Change', 3000.00),
    (2, 6, '2023-02-15', 'Brake Pad Replacement', 5000.00),
    (3, 4, '2023-03-10', 'Engine Tune-up', 8000.00),
    (4, 8, '2023-01-20', 'Tire Rotation', 2000.00),
    (5, 3, '2023-02-25', 'Battery Replacement', 10000.00),
    (6, 7, '2023-03-05', 'Headlight Replacement', 6000.00),
    (7, 5, '2023-01-30', 'Wiper Blade Replacement', 1500.00),
    (8, 9, '2023-02-10', 'Air Filter Replacement', 2500.00),
    (9, 1, '2023-03-15', 'Timing Belt Replacement', 12000.00),
    (10, 10, '2023-01-05', 'Exhaust System Repair', 7000.00);

INSERT INTO Warranties (CarID, WarrantyStartDate, WarrantyEndDate, WarrantyTerms) VALUES
    (1, '2023-01-15', '2028-01-14', '5 years or 100,000 km'),
    (2, '2022-11-20', '2027-11-19', '5 years or 80,000 km'),
    (3, '2023-03-05', '2028-03-04', '5 years or 120,000 km'),
    (4, '2022-09-10', '2027-09-09', '5 years or 90,000 km'),
    (5, '2023-02-01', '2028-01-31', '5 years or 110,000 km'),
    (6, '2022-12-15', '2027-12-14', '5 years or 100,000 km'),
    (7, '2023-01-25', '2028-01-24', '5 years or 130,000 km'),
    (8, '2022-10-20', '2027-10-19', '5 years or 120,000 km'),
    (9, '2022-11-05', '2027-11-04', '5 years or 80,000 km'),
    (10, '2023-03-10', '2028-03-09', '5 years or 110,000 km');

-- Appointments table
INSERT INTO Appointments (CustomerID, EmployeeID, AppointmentDate, AppointmentTime, Reason) VALUES
    (1, 2, '2023-04-01', '10:00:00', 'Oil Change'),
    (2, 6, '2023-04-05', '14:30:00', 'Brake Inspection'),
    (3, 4, '2023-04-10', '09:00:00', 'Engine Diagnostics'),
    (4, 8, '2023-04-15', '11:30:00', 'Tire Rotation'),
    (5, 3, '2023-04-20', '16:00:00', 'Battery Replacement'),
    (6, 7, '2023-04-25', '13:00:00', 'Headlight Alignment'),
    (7, 5, '2023-04-30', '10:30:00', 'Wiper Blade Replacement'),
    (8, 9, '2023-05-05', '15:00:00', 'Air Filter Change'),
    (9, 1, '2023-05-10', '11:00:00', 'Timing Belt Inspection'),
    (10, 10, '2023-05-15', '09:30:00', 'Exhaust System Check');

-- Finance table
INSERT INTO Finance (CustomerID, LoanAmount, InterestRate, LoanTerm, MonthlyPayment) VALUES
    (1, 600000.00, 8.5, 60, 12500.00),
    (2, 500000.00, 9.0, 48, 12000.00),
    (3, 900000.00, 7.8, 72, 15000.00),
    (4, 700000.00, 8.2, 60, 13500.00),
    (5, 800000.00, 8.7, 66, 14000.00),
    (6, 650000.00, 9.2, 54, 13250.00),
    (7, 950000.00, 7.5, 78, 15500.00),
    (8, 1000000.00, 8.0, 84, 16000.00),
    (9, 550000.00, 9.5, 42, 13750.00),
    (10, 750000.00, 8.3, 69, 13000.00);

-- Reviews table
INSERT INTO Reviews (CustomerID, CarID, Rating, ReviewText, ReviewDate) VALUES
    (1, 1, 5, 'Excellent car! Highly recommended.', '2023-03-01'),
    (2, 2, 4, 'Good value for money. Satisfied with the purchase.', '2023-02-20'),
    (3, 3, 5, 'Impressive performance and features. Loving my new car!', '2023-03-15'),
    (4, 4, 3, 'Average car. Could have been better in certain aspects.', '2023-01-25'),
    (5, 5, 4, 'Comfortable ride and good mileage. Worth the investment.', '2023-03-10'),
    (6, 6, 5, 'Stylish and feature-packed. Exceeds my expectations.', '2023-02-28'),
    (7, 7, 4, 'Decent car for the price. Satisfied overall.', '2023-03-05'),
    (8, 8, 5, 'Powerful engine and smooth handling. Highly recommended.', '2023-02-12'),
    (9, 9, 3, 'Average performance. Could have been better.', '2023-01-30'),
    (10, 10, 4, 'Good value for money. Meets my needs.', '2023-03-20');

-- Promotions table
INSERT INTO Promotions (PromotionName, PromotionDescription, StartDate, EndDate, DiscountPercentage) VALUES
    ('Summer Sale', 'Enjoy discounts on selected models', '2023-06-01', '2023-08-31', 10.0),
    ('Festival Offer', 'Special offers and discounts for the festive season', '2023-10-01', '2023-11-30', 12.5),
    ('Trade-in Bonus', 'Get additional value for your old car when trading in', '2023-04-01', '2023-06-30', 5.0),
    ('Loyalty Rewards', 'Exclusive discounts for our loyal customers', '2023-09-01', '2023-09-30', 8.0),
    ('New Model Launch', 'Introductory offers on our latest model', '2023-07-15', '2023-08-31', 7.5),
    ('Year-end Clearance', 'Clear

ance sale on outgoing models', '2023-12-01', '2024-01-31', 15.0),
    ('Employee Discount', 'Special discounts for employees of our partners', '2023-05-01', '2023-07-31', 10.0),
    ('Student Offer', 'Discounts for students on select models', '2023-08-01', '2023-09-30', 8.0),
    ('Military Discount', 'Exclusive offers for military personnel', '2023-11-01', '2023-11-30', 12.0),
    ('Anniversary Sale', 'Celebrate our anniversary with exciting discounts', '2023-10-15', '2023-11-15', 10.0);

-- Accessories table
INSERT INTO Accessories (AccessoryName, AccessoryDescription, Price) VALUES
    ('Floor Mats', 'Premium quality floor mats for your car', 1500.00),
    ('Roof Rack', 'Sturdy roof rack for carrying luggage or sports equipment', 3000.00),
    ('Seat Covers', 'Stylish and durable seat covers for added protection', 2000.00),
    ('Dash Cam', 'High-resolution dash cam for recording your drives', 4000.00),
    ('Tire Inflator', 'Portable tire inflator for emergencies', 1000.00),
    ('Car Vacuum', 'Handy car vacuum for keeping your vehicle clean', 2500.00),
    ('Jump Starter', 'Powerful jump starter for dead batteries', 3500.00),
    ('Steering Wheel Cover', 'Comfortable steering wheel cover for better grip', 800.00),
    ('Car Charger', 'Multi-port car charger for charging devices on the go', 1200.00),
    ('Sunshades', 'Foldable sunshades for blocking UV rays', 1000.00);