import sqlite3
con = sqlite3.connect("registry.db")

# Create a cursor object
cur = con.cursor()

# Create a table of patients
cur.execute("CREATE TABLE patients (id INTEGER PRIMARY KEY, name TEXT, CNP TEXT, ocupation TEXT, address TEXT, phone TEXT, email TEXT, birthdate TEXT)")

#create registry of consultations
cur.execute("CREATE TABLE consultations (id INTEGER PRIMARY KEY, patient_id INTEGER, date TEXT, doctor TEXT, simptons TEXT, diagnosis TEXT, diagnosis_code, treatment TEXT, type TEXT, FOREIGN KEY(patient_id) REFERENCES patients(id))")

def add_patient(name, CNP, ocupation, address, phone, email, birthdate):
    cur.execute("INSERT INTO patients (name, CNP, ocupation, address, phone, email, birthdate) VALUES (?, ?, ?, ?, ?, ?, ?)", (name, CNP, ocupation, address, phone, email, birthdate))
    con.commit()

def add_consultation(patient_id, date, doctor, simptons, diagnosis, diagnosis_code, treatment, type):
    cur.execute("INSERT INTO consultations (patient_id, date, doctor, simptons, diagnosis, diagnosis_code, treatment, type) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (patient_id, date, doctor, simptons, diagnosis, diagnosis_code, treatment, type))
    con.commit()

def get_patient_by_CNP(CNP):
    cur.execute("SELECT * FROM patients WHERE CNP = ?", (CNP,))
    return cur.fetchone()

def get_patient_by_name(name):
    cur.execute("SELECT * FROM patients WHERE name = ?", (name,))
    return cur.fetchone()

def get_consulations(patient_id):
    cur.execute("SELECT * FROM consultations WHERE patient_id = ?", (patient_id,))
    return cur.fetchall()

def get_all_consultations():
    cur.execute("SELECT * FROM consultations")
    return cur.fetchall()

def get_consultations_by_date(date):
    cur.execute("SELECT * FROM consultations WHERE date = ?", (date,))
    return cur.fetchall()

def get_consulations_by_month_and_year(month, year):
    cur.execute("SELECT * FROM consultations WHERE date LIKE ?", (year + "/" + month,))
    return cur.fetchall()

def get_consultations_by_month_year_until_month_year(month1, year1, month2, year2):
    cur.execute("SELECT * FROM consultations WHERE date BETWEEN ? AND ?", (year1 + "/" + month1 +"/01", year2 + "/" + month2 + "/31"))
    return cur.fetchall()

