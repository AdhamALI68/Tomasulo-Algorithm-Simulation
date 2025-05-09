# import tkinter as tk
# from tkinter import filedialog
# import subprocess
# import os
#
# class TomasuloSimulatorGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Tomasulo Simulator")
#
#         # Create layout
#         self.title_label = tk.Label(root, text="Tomasulo Simulator", font=("Arial", 14, "bold"))
#         self.title_label.pack(pady=10)
#
#         self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
#         self.browse_button.pack(pady=5)
#
#         self.run_button = tk.Button(root, text="Run", command=self.run_simulator)
#         self.run_button.pack(pady=5)
#
#         # Enlarge the output screen by adjusting height and width
#         self.output_area = tk.Text(root, height=30, width=100)  # Increased height and width
#         self.output_area.pack(pady=10)
#
#         self.file_path = None
#
#     def browse_file(self):
#         # Open file dialog to select the text file
#         self.file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
#
#     def run_simulator(self):
#         if not self.file_path:
#             self.output_area.insert(tk.END, "No file selected!\n")
#             return
#
#         # Ensure the C++ executable is in the same directory or specify full path
#         executable = '/Users/maha/Desktop/Source/cmake-build-debug/Source'  # For Linux or macOS
#         # or
#         # executable = 'tomasulo_simulator.exe'  # For Windows
#
#         # Check if the executable exists
#         if not os.path.exists(executable):
#             self.output_area.insert(tk.END, f"Error: Executable '{executable}' not found.\n")
#             return
#
#         # Call the C++ program via subprocess
#         try:
#             # Pass the file path as an argument to the executable
#             result = subprocess.run([executable, self.file_path],
#                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#
#             # Display the output in the output area (Text widget)
#             if result.returncode == 0:
#                 self.output_area.insert(tk.END, result.stdout)  # Standard output
#             else:
#                 self.output_area.insert(tk.END, f"Error: {result.stderr}\n")  # Error output
#         except Exception as e:
#             self.output_area.insert(tk.END, f"Failed to run simulator: {str(e)}\n")
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     gui = TomasuloSimulatorGUI(root)
#     root.mainloop()
#
#

# import tkinter as tk
# from tkinter import filedialog
# import subprocess
# import os
#
# class IntroWindow:
#     def __init__(self, parent_window):
#         self.parent_window = parent_window
#         self.parent_window.title("Tomasulo Simulation Interface")
#         self.parent_window.geometry("800x600")
#         self.parent_window.configure(bg="#2f2f2f")
#         self.display_intro()
#
#     def display_intro(self):
#         self.main_title = tk.Label(self.parent_window, text="Tomasulo Simulation Interface", font=("Verdana", 20, "bold"), fg="white", bg="#2f2f2f")
#         self.main_title.pack(pady=50)
#
#         self.course_details = tk.Label(self.parent_window, text="CSCE 3301 – Computer Architecture\nFall 2024", font=("Verdana", 16), fg="skyblue", bg="#2f2f2f")
#         self.course_details.pack(pady=20)
#
#         self.professor_name = tk.Label(self.parent_window, text="Instructor: Dr. Chrief Salama", font=("Verdana", 16), fg="yellow", bg="#2f2f2f")
#         self.professor_name.pack(pady=20)
#
#         self.authors_info = tk.Label(self.parent_window, text="Developed by\nSaif Abd Elfattah & Adham Ali", font=("Verdana", 14), fg="orange", bg="#2f2f2f")
#         self.authors_info.pack(pady=20)
#
#         self.start_button = tk.Button(self.parent_window, text="Try it", command=self.launch_simulation, bg="#4CAF50", fg="white", font=("Verdana", 14, "bold"), activebackground="#45a049", activeforeground="white", relief="raised")
#         self.start_button.pack(pady=30)
#
#     def launch_simulation(self):
#         self.parent_window.destroy()
#         sim_window = tk.Tk()
#         SimulationWindow(sim_window)
#         sim_window.mainloop()
#
#
# class SimulationWindow:
#     def __init__(self, window):
#         self.window = window
#         self.window.title("Simulation Main Interface")
#         self.window.geometry("1400x700")
#         self.setup_interface()
#
#     def setup_interface(self):
#         # Main frame
#         self.main_frame = tk.Frame(self.window, bg="#f2f2f2")
#         self.main_frame.pack(fill=tk.BOTH, expand=True)
#
#         # Input frame for file selection
#         self.input_frame = tk.Frame(self.main_frame, bg="#ffffff", bd=4, relief="groove")
#         self.input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=15, pady=15)
#
#         self.load_file_button = tk.Button(self.input_frame, text="Load Data", command=self.select_file, bg="#6c757d", fg="white", font=("Verdana", 13, "bold"), activebackground="#5a6268", activeforeground="white")
#         self.load_file_button.pack(pady=15)
#
#         self.file_display = tk.Text(self.input_frame, height=25, width=60, wrap=tk.WORD, bg="#fafafa", fg="black", font=("Verdana", 11), padx=10, pady=10)
#         self.file_display.pack(pady=15)
#
#         # Output frame for displaying results
#         self.output_frame = tk.Frame(self.main_frame, bg="#ffffff", bd=4, relief="groove")
#         self.output_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=15, pady=15)
#
#         self.start_process_button = tk.Button(self.output_frame, text="Start Process", command=self.execute_process, bg="#007bff", fg="white", font=("Verdana", 13, "bold"), activebackground="#0056b3", activeforeground="white")
#         self.start_process_button.pack(pady=15)
#
#         self.result_display = tk.Text(self.output_frame, height=25, width=60, wrap=tk.WORD, bg="#fafafa", fg="black", font=("Verdana", 11), padx=10, pady=10)
#         self.result_display.pack(pady=15)
#
#         self.clear_output_button = tk.Button(self.output_frame, text="Clear Output", command=self.reset_output, bg="#dc3545", fg="white", font=("Verdana", 13, "bold"), activebackground="#c82333", activeforeground="white")
#         self.clear_output_button.pack(pady=15)
#
#         self.file_path = None
#
#     def select_file(self):
#         selected_file = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text Files", "*.txt")])
#         if selected_file:
#             try:
#                 with open(selected_file, 'r') as file:
#                     file_content = file.read()
#                     self.file_display.delete("1.0", tk.END)
#                     self.file_display.insert(tk.END, file_content)
#                     self.file_path = selected_file
#             except Exception as e:
#                 self.file_display.delete("1.0", tk.END)
#                 self.file_display.insert(tk.END, f"Error reading file: {str(e)}")
#
#     def execute_process(self):
#         if not self.file_path:
#             self.result_display.insert(tk.END, "No file selected!\n")
#             return
#
#         executable = '/Users/maha/Desktop/Source/cmake-build-debug/Source'  # For Linux or macOS
#         # or
#         # executable = 'tomasulo_simulator.exe'  # For Windows
#
#         if not os.path.exists(executable):
#             self.result_display.insert(tk.END, f"Error: Executable '{executable}' not found.\n")
#             return
#
#         try:
#             result = subprocess.run([executable, self.file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#             if result.returncode == 0:
#                 self.result_display.delete("1.0", tk.END)
#                 self.result_display.insert(tk.END, result.stdout)
#             else:
#                 self.result_display.delete("1.0", tk.END)
#                 self.result_display.insert(tk.END, f"Error: {result.stderr}\n")
#         except Exception as e:
#             self.result_display.delete("1.0", tk.END)
#             self.result_display.insert(tk.END, f"Failed to run simulator: {str(e)}\n")
#
#     def reset_output(self):
#         self.result_display.delete("1.0", tk.END)
#
#
# if __name__ == "__main__":
#     main_window = tk.Tk()
#     IntroWindow(main_window)
#     main_window.mainloop()


import tkinter as tk
from tkinter import filedialog
import subprocess
import os

class IntroWindow:
    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.parent_window.title("Tomasulo Simulation Interface")
        self.parent_window.geometry("1000x700")  # Enlarge the intro window more
        self.parent_window.configure(bg="#2f2f2f")
        self.display_intro()

    def display_intro(self):
        self.main_title = tk.Label(self.parent_window, text="Tomasulo Simulation Interface", font=("Verdana", 20, "bold"), fg="white", bg="#2f2f2f")
        self.main_title.pack(pady=50)

        self.course_details = tk.Label(self.parent_window, text="CSCE 3301 – Computer Architecture\nFall 2024", font=("Verdana", 16), fg="skyblue", bg="#2f2f2f")
        self.course_details.pack(pady=20)

        self.professor_name = tk.Label(self.parent_window, text="Instructor: Dr. Chrief Salama", font=("Verdana", 16), fg="yellow", bg="#2f2f2f")
        self.professor_name.pack(pady=20)

        self.authors_info = tk.Label(self.parent_window, text="Developed by\nSaif Abd Elfattah & Adham Ali", font=("Verdana", 14), fg="orange", bg="#2f2f2f")
        self.authors_info.pack(pady=20)

        self.start_button = tk.Button(self.parent_window, text="Try it", command=self.launch_simulation, bg="#FF6347", fg="white", font=("Verdana", 14, "bold"), relief="raised")  # Tomato color for button
        self.start_button.pack(pady=30)

    def launch_simulation(self):
        self.parent_window.destroy()
        sim_window = tk.Tk()
        SimulationWindow(sim_window)
        sim_window.mainloop()


class SimulationWindow:
    def __init__(self, window):
        self.window = window
        self.window.title("Simulation Main Interface")
        self.window.geometry("1600x800")  # Enlarge the window further
        self.setup_interface()

    def setup_interface(self):
        # Main frame with background color change
        self.main_frame = tk.Frame(self.window, bg="#363636")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Input frame with background color change
        self.input_frame = tk.Frame(self.main_frame, bg="#555555", bd=4, relief="groove")
        self.input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=15, pady=15)

        self.load_file_button = tk.Button(self.input_frame, text="Load Data", command=self.select_file, bg="#5DADE2", fg="white", font=("Verdana", 13, "bold"), relief="raised")  # Sky blue color
        self.load_file_button.pack(pady=15)

        self.file_display = tk.Text(self.input_frame, height=25, width=80, wrap=tk.WORD, bg="#fafafa", fg="black", font=("Verdana", 11), padx=10, pady=10)
        self.file_display.pack(pady=15)

        # Output frame with background color change
        self.output_frame = tk.Frame(self.main_frame, bg="#555555", bd=4, relief="groove")
        self.output_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=15, pady=15)

        self.start_process_button = tk.Button(self.output_frame, text="Start Process", command=self.execute_process, bg="#28a745", fg="white", font=("Verdana", 13, "bold"), relief="raised")  # Green color
        self.start_process_button.pack(pady=15)

        # Enlarged result display
        self.result_display = tk.Text(self.output_frame, height=30, width=100, wrap=tk.WORD, bg="#fafafa", fg="black", font=("Verdana", 11), padx=10, pady=10)
        self.result_display.pack(pady=15)

        self.clear_output_button = tk.Button(self.output_frame, text="Clear Output", command=self.reset_output, bg="#DC3545", fg="white", font=("Verdana", 13, "bold"), relief="raised")  # Red color
        self.clear_output_button.pack(pady=15)

        self.file_path = None

    def select_file(self):
        selected_file = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text Files", "*.txt")])
        if selected_file:
            try:
                with open(selected_file, 'r') as file:
                    file_content = file.read()
                    self.file_display.delete("1.0", tk.END)
                    self.file_display.insert(tk.END, file_content)
                    self.file_path = selected_file
            except Exception as e:
                self.file_display.delete("1.0", tk.END)
                self.file_display.insert(tk.END, f"Error reading file: {str(e)}")

    def execute_process(self):
        if not self.file_path:
            self.result_display.insert(tk.END, "No file selected!\n")
            return

        executable = '/Users/maha/Desktop/Source/cmake-build-debug/Source'  # For Linux or macOS
        # or
        # executable = 'tomasulo_simulator.exe'  # For Windows

        if not os.path.exists(executable):
            self.result_display.insert(tk.END, f"Error: Executable '{executable}' not found.\n")
            return

        try:
            result = subprocess.run([executable, self.file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                self.result_display.delete("1.0", tk.END)
                self.result_display.insert(tk.END, result.stdout)
            else:
                self.result_display.delete("1.0", tk.END)
                self.result_display.insert(tk.END, f"Error: {result.stderr}\n")
        except Exception as e:
            self.result_display.delete("1.0", tk.END)
            self.result_display.insert(tk.END, f"Failed to run simulator: {str(e)}\n")

    def reset_output(self):
        self.result_display.delete("1.0", tk.END)


if __name__ == "__main__":
    main_window = tk.Tk()
    IntroWindow(main_window)
    main_window.mainloop()

