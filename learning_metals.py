import tkinter as tk
from tkinter import messagebox

# User login details
users = {"admin": "123"}  # Username: Password

# Data for groups and descriptions
groups = {
    "Group 1 (Alkali Metals)": ["Lithium (Li)", "Sodium (Na)", "Potassium (K)", "Rubidium (Rb)", "Cesium (Cs)", "Francium (Fr)"],
    "Group 2 (Alkaline Earth Metals)": ["Beryllium (Be)", "Magnesium (Mg)", "Calcium (Ca)", "Strontium (Sr)", "Barium (Ba)", "Radium (Ra)"],
    "Group 3 (Scandium Group)": ["Scandium (Sc)", "Yttrium (Y)", "Lanthanum (La)", "Actinium (Ac)"],
    "Group 4 (Titanium Group)": ["Titanium (Ti)", "Zirconium (Zr)", "Hafnium (Hf)", "Rutherfordium (Rf)"],
    "Group 5 (Vanadium Group)": ["Vanadium (V)", "Niobium (Nb)", "Tantalum (Ta)", "Dubnium (Db)"],
    "Group 6 (Chromium Group)": ["Chromium (Cr)", "Molybdenum (Mo)", "Tungsten (W)", "Seaborgium (Sg)"],
    "Group 7 (Manganese Group)": ["Manganese (Mn)", "Technetium (Tc)", "Rhenium (Re)", "Bohrium (Bh)"],
    "Group 8 (Iron Group)": ["Iron (Fe)", "Ruthenium (Ru)", "Osmium (Os)", "Hassium (Hs)"],
    "Group 9 (Cobalt Group)": ["Cobalt (Co)", "Rhodium (Rh)", "Iridium (Ir)", "Meitnerium (Mt)"],
    "Group 10 (Nickel Group)": ["Nickel (Ni)", "Palladium (Pd)", "Platinum (Pt)", "Darmstadtium (Ds)"],
    "Group 11 (Coinage Metals)": ["Copper (Cu)", "Silver (Ag)", "Gold (Au)", "Roentgenium (Rg)"],
    "Group 12 (Zinc Group)": ["Zinc (Zn)", "Cadmium (Cd)", "Mercury (Hg)", "Copernicium (Cn)"],
    "Group 13 (Boron Group)": ["Boron (B)", "Aluminum (Al)", "Gallium (Ga)", "Indium (In)", "Thallium (Tl)", "Nihonium (Nh)"],
    "Group 14 (Carbon Group)": ["Carbon (C)", "Silicon (Si)", "Germanium (Ge)", "Tin (Sn)", "Lead (Pb)", "Flerovium (Fl)"],
    "Group 15 (Nitrogen Group)": ["Nitrogen (N)", "Phosphorus (P)", "Arsenic (As)", "Antimony (Sb)", "Bismuth (Bi)", "Moscovium (Mc)"],
    "Group 16 (Chalcogens)": ["Oxygen (O)", "Sulfur (S)", "Selenium (Se)", "Tellurium (Te)", "Polonium (Po)", "Livermorium (Lv)"],
    "Group 17 (Halogens)": ["Fluorine (F)", "Chlorine (Cl)", "Bromine (Br)", "Iodine (I)", "Astatine (At)", "Tennessine (Ts)"],
    "Group 18 (Noble Gases)": ["Helium (He)", "Neon (Ne)", "Argon (Ar)", "Krypton (Kr)", "Xenon (Xe)", "Radon (Rn)", "Oganesson (Og)"]
}

descriptions = {
    "Group 1 (Alkali Metals)": "Highly reactive, soft metals that react vigorously with water.",
    "Group 2 (Alkaline Earth Metals)": "Shiny, silvery-white metals. Less reactive than alkali metals.",
    "Group 3 (Scandium Group)": "Transition metals used in aerospace due to their strength and light weight.",
    "Group 4 (Titanium Group)": "Strong, corrosion-resistant metals used in engineering and construction.",
    "Group 5 (Vanadium Group)": "Metals known for high melting points and resistance to corrosion.",
    "Group 6 (Chromium Group)": "Metals used in making tools and as catalysts, known for high melting points.",
    "Group 7 (Manganese Group)": "Essential for steel manufacturing and batteries.",
    "Group 8 (Iron Group)": "Crucial for human life and industrial processes.",
    "Group 9 (Cobalt Group)": "Used in magnets, batteries, and pigments.",
    "Group 10 (Nickel Group)": "Corrosion-resistant metals often used in coins and industrial processes.",
    "Group 11 (Coinage Metals)": "Traditionally used for coin production due to malleability and resistance to corrosion.",
    "Group 12 (Zinc Group)": "Metals with low melting points, used in galvanization and batteries.",
    "Group 13 (Boron Group)": "Elements range from non-metals to metals. Found in Group 13.",
    "Group 14 (Carbon Group)": "A mix of non-metals, metalloids, and metals. Carbon is essential to organic chemistry.",
    "Group 15 (Nitrogen Group)": "Nitrogen and phosphorus are essential for life.",
    "Group 16 (Chalcogens)": "Oxygen is vital for life. Found in Group 16 of the periodic table.",
    "Group 17 (Halogens)": "Highly reactive non-metals, form salts when combined with metals.",
    "Group 18 (Noble Gases)": "Colorless, odorless, and stable gases. Found in Group 18."
    }

# Learner performance tracking
learner_performance = {"total_questions": 0, "correct_answers": 0}

# Function to confirm application closure
def close_application():
    response = messagebox.askyesno("Exit Application", "Are you sure you want to exit?")
    if response:
        exit()

# Logout function
def logout():
    response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if response:
        # Hide current window and reopen the login screen
        main_window.destroy()
        login_window.deiconify()

# Main menu
def main_menu():
    global main_window
    main_window = tk.Tk()
    main_window.title("Learning Metals of Periodic Table")
    main_window.attributes("-fullscreen", True)

    # Display performance stats
    correct = learner_performance["correct_answers"]
    total = learner_performance["total_questions"]
    performance_text = f"Performance: {correct}/{total} ({(correct/total*100 if total > 0 else 0):.2f}%)"

    # Main menu layout
    tk.Label(main_window, text="Main Menu", font=("Arial", 30)).pack(pady=20)
    tk.Label(main_window, text=performance_text, font=("Arial", 20)).pack(pady=10)

    # Scrollable list of groups
    canvas = tk.Canvas(main_window)
    scrollbar = tk.Scrollbar(main_window, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas)

    for group in groups:
        tk.Button(scroll_frame, text=group, width=50, font=("Arial", 14), command=lambda g=group: group_details(g)).pack(pady=5)

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    scroll_frame.update_idletasks()
    canvas.configure(yscrollcommand=scrollbar.set, scrollregion=canvas.bbox("all"))

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tk.Button(main_window, text="Logout", command=logout, bg="red", fg="white", font=("Arial", 20)).pack(pady=20)
    tk.Button(main_window, text="Close Application", command=close_application, bg="black", fg="white", font=("Arial", 20)).pack(pady=10)

# Group details screen
def group_details(group):
    main_window.withdraw()
    details_window = tk.Toplevel()
    details_window.title(group)
    details_window.attributes("-fullscreen", True)

    tk.Label(details_window, text=group, font=("Arial", 30)).pack(pady=20)
    tk.Label(details_window, text=descriptions[group], font=("Arial", 20), wraplength=1000).pack(pady=20)

    tk.Label(details_window, text="Elements:", font=("Arial", 20)).pack(pady=10)
    for element in groups[group]:
        tk.Label(details_window, text=element, font=("Arial", 16)).pack()

    tk.Button(details_window, text="Take Quiz", font=("Arial", 14), command=lambda: take_quiz(group, details_window)).pack(pady=20)
    tk.Button(details_window, text="Back", font=("Arial", 14), command=lambda: back_to_main(details_window)).pack(pady=10)
    tk.Button(details_window, text="Close Application", font=("Arial", 14), command=close_application).pack(pady=10)

# Quiz screen
def take_quiz(group, previous_window):
    previous_window.withdraw()
    quiz_window = tk.Toplevel()
    quiz_window.title(f"Quiz: {group}")
    quiz_window.attributes("-fullscreen", True)

    question = f"What is a key property of elements in {group}?"
    correct_answer = "reactive"  # Example answer

    tk.Label(quiz_window, text=question, font=("Arial", 20)).pack(pady=50)

    def submit_answer(answer):
        learner_performance["total_questions"] += 1
        if answer.lower() == correct_answer.lower():
            learner_performance["correct_answers"] += 1
            messagebox.showinfo("Correct!", "You answered correctly!")
        else:
            messagebox.showerror("Incorrect", f"Correct answer: {correct_answer}")
        quiz_window.destroy()
        previous_window.deiconify()

    tk.Button(quiz_window, text="Reactive", font=("Arial", 14), command=lambda: submit_answer("reactive")).pack(pady=10)
    tk.Button(quiz_window, text="Non-reactive", font=("Arial", 14), command=lambda: submit_answer("non-reactive")).pack(pady=10)
    tk.Button(quiz_window, text="Back", font=("Arial", 14), command=lambda: back_to_group(previous_window, quiz_window)).pack(pady=20)
    tk.Button(quiz_window, text="Close Application", font=("Arial", 14), command=close_application).pack(pady=10)

# Navigation functions
def back_to_main(window):
    window.destroy()
    main_menu()

def back_to_group(previous_window, quiz_window):
    quiz_window.destroy()
    previous_window.deiconify()

# Login screen
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username in users and users[username] == password:
        login_window.withdraw()
        main_menu()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")

# Login window setup
login_window = tk.Tk()
login_window.title("Login - Learning Metals of Periodic Table")
login_window.attributes("-fullscreen", True)

tk.Label(login_window, text="Learning Metals of Periodic Table", font=("Arial", 30)).pack(pady=50)
tk.Label(login_window, text="Username:", font=("Arial", 20)).pack(pady=10)
username_entry = tk.Entry(login_window, width=30, font=("Arial", 16))
username_entry.pack(pady=10)

tk.Label(login_window, text="Password:", font=("Arial", 20)).pack(pady=10)
password_entry = tk.Entry(login_window, width=30, font=("Arial", 16), show="*")
password_entry.pack(pady=10)

tk.Button(login_window, text="Login", font=("Arial", 20), command=login).pack(pady=20)
tk.Button(login_window, text="Close Application", font=("Arial", 20), command=close_application, bg="black", fg="white").pack(pady=20)

login_window.mainloop()
