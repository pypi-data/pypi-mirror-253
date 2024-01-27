import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from prusek_spheroid import GradientDescentGUI as g
from prusek_spheroid import ContoursClassGUI as f
import threading
import time


class ProcessingProgressWindow(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.title("Processing Progress")

        self.geometry("500x250")
        self.resizable(width=False, height=False)

        # Frame pro centrování obsahu
        center_frame = tk.Frame(self)
        center_frame.pack(expand=True)

        # Label ve frame pro centrování
        self.label_progress = tk.Label(center_frame, text="Progress: ")
        self.label_progress.pack()

    def update_progress(self, progress):
        self.label_progress.config(text=f"Progress: {progress}")


class OptimizationProgressWindow(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.title("Optimization Progress")

        self.geometry("500x250")  # Šířka x Výška
        self.resizable(width=False, height=False)

        # Frame pro centrování obsahu
        center_frame = tk.Frame(self)
        center_frame.pack(expand=True)

        # Labely ve frame pro centrování
        self.label_project = tk.Label(center_frame, text="Project: ")
        self.label_project.pack()

        self.label_algorithm = tk.Label(center_frame, text="Algorithm: ")
        self.label_algorithm.pack()

        self.label_iteration = tk.Label(center_frame, text="Iteration: ")
        self.label_iteration.pack()

        self.label_iou = tk.Label(center_frame, text="IoU: ")
        self.label_iou.pack()

        self.label_parameters = tk.Label(center_frame, text="Estimated time remaining: ")
        self.label_parameters.pack()

    def update_info(self, project, algorithm, iteration, IoU, time):
        self.label_project.config(text=f"Project: {project}")
        self.label_algorithm.config(text=f"Algorithm: {algorithm}")
        self.label_iteration.config(text=f"Iteration: {iteration}")
        self.label_iou.config(text=f"IoU: {IoU}%")
        self.label_parameters.config(text=f"Estimated time remaining: {time} seconds")


class ParameterEntryDialog(tk.Toplevel):
    def __init__(self, master, algorithm):
        tk.Toplevel.__init__(self, master)
        self.title("Enter Parameters")

        self.algorithm = algorithm
        self.parameters = {}
        self.param_ranges = {}
        self.result = None

        self.initialize_parameters()

        # Create labels and entry widgets for each parameter
        self.entries = {}
        for param, value in self.parameters.items():
            label = tk.Label(self, text=f"{param} ({self.param_ranges[param][0]} - {self.param_ranges[param][1]}):")
            label.pack()
            entry = tk.Entry(self)
            entry.insert(0, str(value))
            entry.pack()
            self.entries[param] = entry

        # OK button to confirm parameter values
        ok_button = tk.Button(self, text="OK", command=self.confirm_parameters)
        ok_button.pack()

    def close_dialog(self):
        self.result = None
        self.destroy()

    def get_parameters(self):
        return self.parameters

    def update_parameters(self, new_parameters):
        # Update parameters in the main application when entering them manually
        self.parameters = new_parameters

    def initialize_parameters(self):
        if self.algorithm == "Sauvola":
            self.parameters = {"window_size": 800, "min_area": 1000, "sigma": 2.5, "dilation_size": 2,
                               "closing_size": 0}
            self.param_ranges = {
                "window_size": [1, 2001],
                "min_area": [0, 50000],
                "sigma": [0.0, 5.0],
                "dilation_size": [0, 20],
                "closing_size": [0, 20]
            }
        elif self.algorithm == "Niblack":
            self.parameters = {"window_size": 800, "k": 0.2, "min_area": 1000, "sigma": 2.5, "dilation_size": 2,
                               "closing_size": 0}
            self.param_ranges = {
                "window_size": [1, 2001],
                "k": [-0.5, 1.0],
                "min_area": [0, 50000],
                "sigma": [0.0, 5.0],
                "dilation_size": [0, 20],
                "closing_size": [0, 20]
            }
        elif self.algorithm == "Mean Shift":
            self.parameters = {"k": 0.1, "min_area": 1000, "sigma": 2.5, "dilation_size": 2, "closing_size": 0}
            self.param_ranges = {"k": [0.0, 0.25], "min_area": [0, 50000], "sigma": [0.0, 5.0],
                                 "dilation_size": [0, 20], "closing_size": [0, 20]}
        elif self.algorithm == "Gaussian":
            self.parameters = {"window_size": 800, "k": 0.0, "min_area": 1000, "sigma": 2.5, "dilation_size": 2,
                               "closing_size": 0}
            self.param_ranges = {"window_size": [1, 2001], "k": [-255.0, 255.0], "min_area": [0, 50000],
                                 "sigma": [0.0, 5.0], "dilation_size": [0, 20],
                                 "closing_size": [0, 20]}

    def confirm_parameters(self):
        # Validate and retrieve parameter values
        new_parameters = {}
        for param, entry in self.entries.items():
            try:
                value = float(entry.get())
                if self.param_ranges.get(param) and not (
                        self.param_ranges[param][0] <= value <= self.param_ranges[param][1]):
                    raise ValueError(
                        f"{param} should be in the range [{self.param_ranges[param][0]}, {self.param_ranges[param][1]}]")
                new_parameters[param] = value
            except ValueError as e:
                print(f"Exception caught: {e}")
                messagebox.showerror("Error",
                                     f"{param} should be in the range [{self.param_ranges[param][0]}, {self.param_ranges[param][1]}]")
                return False

        # Update the parameters in the main application
        self.update_parameters(new_parameters)
        self.result = self.parameters
        self.destroy()

    def validate_input(self):
        # Validate input and check if it is within the specified ranges
        for param_name, entry_widget in zip(self.parameters.keys(), self.winfo_children()):
            try:
                entry_value = float(entry_widget.get())
                if not (self.param_ranges[param_name][0] <= entry_value <= self.param_ranges[param_name][1]):
                    messagebox.showerror("Error", f"Invalid value for {param_name}. "
                                                  f"Enter a value within the range [{self.param_ranges[param_name][0]}, {self.param_ranges[param_name][1]}].")
                    return False
            except ValueError:
                messagebox.showerror("Error", f"Invalid value for {param_name}. Enter a valid number.")
                return False


class SferoidSegmentationGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Spheroid segmentation")

        # Adresní sekce
        self.address_section_label = tk.Label(master, text="Address Settings", font=("Helvetica", 12, "bold"))
        self.address_section_label.pack()

        # File Dialog pro anotace COCO
        self.coco_annotation_path = self.create_file_dialog("COCO annotations zip file address (with images)")

        # Indikátor pro vyplnění adresy
        self.annotation_indicator_label = tk.Label(master, text="")
        self.annotation_indicator_label.pack()

        # File Dialog pro dataset obrázků (změna na askdirectory)
        self.image_dataset_path = self.create_directory_dialog("Dataset of images from the whole project address")

        # Indikátor pro vyplnění adresy
        self.dataset_indicator_label = tk.Label(master, text="")
        self.dataset_indicator_label.pack()

        # File Dialog pro výsledné segmentované obrázky (změna na askdirectory)
        self.output_path = self.create_directory_dialog("Address where to save the resulting segmented images")

        # Indikátor pro vyplnění adresy
        self.output_indicator_label = tk.Label(master, text="")
        self.output_indicator_label.pack()

        # Oddělovací čára mezi adresní a metody sekce
        self.address_separator = tk.Frame(master, height=2, bd=1, relief=tk.SUNKEN)
        self.address_separator.pack(fill=tk.X, padx=5, pady=5)

        # Metodická sekce
        self.method_section_label = tk.Label(master, text="Method Settings", font=("Helvetica", 12, "bold"))
        self.method_section_label.pack()

        # Checkbox pro znalost parametrů
        self.known_parameters_var = tk.IntVar()
        self.known_parameters_checkbox = tk.Checkbutton(master, text="I already know the parameters",
                                                        variable=self.known_parameters_var,
                                                        command=self.toggle_parameters_entry)
        self.known_parameters_checkbox.pack()

        # Textbox pro název projektu
        self.project_name_label = tk.Label(master, text="Project Name:")
        self.project_name_label.pack()
        self.project_name_entry = tk.Entry(master)
        self.project_name_entry.pack()

        # Checkboxy pro výběr metod
        self.methods_frame = tk.Frame(master)
        self.methods_frame.pack()
        self.method_labels = ["Sauvola", "Niblack", "Gaussian", "Mean Shift"]
        self.method_vars = [tk.IntVar() for _ in self.method_labels]
        for i, method_label in enumerate(self.method_labels):
            method_checkbox = tk.Checkbutton(self.methods_frame, text=method_label, variable=self.method_vars[i])
            method_checkbox.grid(row=0, column=i, padx=5, pady=5)

        # Textová pole pro zadání parametrů
        self.parameters_frame = tk.Frame(master)
        self.parameters_frame.pack()
        self.learning_rate_label = tk.Label(self.parameters_frame, text="Learning Rate:")
        self.learning_rate_label.grid(row=0, column=0, padx=5, pady=5)
        self.learning_rate_entry = tk.Entry(self.parameters_frame)
        self.learning_rate_entry.grid(row=0, column=1, padx=5, pady=5)

        self.iterations_label = tk.Label(self.parameters_frame, text="Number of Iterations:")
        self.iterations_label.grid(row=1, column=0, padx=5, pady=5)
        self.iterations_entry = tk.Entry(self.parameters_frame)
        self.iterations_entry.grid(row=1, column=1, padx=5, pady=5)

        self.stop_condition_label = tk.Label(self.parameters_frame, text="Stop Condition:")
        self.stop_condition_label.grid(row=2, column=0, padx=5, pady=5)
        self.stop_condition_entry = tk.Entry(self.parameters_frame)
        self.stop_condition_entry.grid(row=2, column=1, padx=5, pady=5)

        # Přednastavení hodnot parametrů
        self.learning_rate_entry.insert(0, "0.01")
        self.iterations_entry.insert(0, "50")
        self.stop_condition_entry.insert(0, "0.0002")

        # Tlačítko pro spuštění
        self.run_button = tk.Button(master, text="Run", command=self.run_method)
        self.run_button.pack()

    def create_file_dialog(self, title):
        file_dialog_path = tk.StringVar()
        file_dialog_button = tk.Button(self.master, text=title,
                                       command=lambda: self.browse_file(file_dialog_path, title))
        file_dialog_button.pack()
        return file_dialog_path

    def create_directory_dialog(self, title):
        directory_dialog_path = tk.StringVar()
        directory_dialog_button = tk.Button(self.master, text=title,
                                            command=lambda: self.browse_directory(directory_dialog_path, title))
        directory_dialog_button.pack()
        return directory_dialog_path

    def browse_file(self, var, title):
        file_path = filedialog.askopenfilename()
        var.set(file_path)
        # Aktualizace indikátoru pro vybranou adresu
        if title == "COCO annotations zip file address (with images)":
            self.annotation_indicator_label.config(text=f"Anotace COCO: {file_path}")

    def browse_directory(self, var, title):
        directory_path = filedialog.askdirectory()
        var.set(directory_path)
        # Aktualizace indikátoru pro vybranou adresu
        if title == "Dataset of images from the whole project address":
            self.dataset_indicator_label.config(text=f"Dataset obrázků: {directory_path}")
        elif title == "Address where to save the resulting segmented images":
            self.output_indicator_label.config(text=f"Výsledné obrázky: {directory_path}")

    def toggle_parameters_entry(self):
        # Zablokování/odblokování zadávání parametrů podle stavu checkboxu
        state = tk.NORMAL if not self.known_parameters_var.get() else tk.DISABLED
        self.learning_rate_entry.config(state=state)
        self.iterations_entry.config(state=state)
        self.stop_condition_entry.config(state=state)

    def run_method(self):
        # Zkontroluj, zda je vyplněn textbox s názvem projektu
        project_name = self.project_name_entry.get()
        if not project_name:
            messagebox.showerror("Error", "Název projektu musí být vyplněn.")
            return

        # Zkontroluj, zda jsou všechny tři adresy vyplněné
        if not all([self.coco_annotation_path.get(), self.image_dataset_path.get(), self.output_path.get()]):
            messagebox.showerror("Error", "Všechny tři adresy v sekci 'Address Settings' musí být vyplněné.")
            return

        # Zkontroluj, zda je vyplněna alespoň jedna z pěti metod segmentace
        if not any(var.get() == 1 for var in self.method_vars):
            messagebox.showerror("Error", "Musí být vybrána alespoň jedna z pěti metod segmentace.")
            return

        # Pokud není zaškrtnut checkbox "I already know the parameters", zkontroluj vyplnění všech tří parametrů
        if not self.known_parameters_var.get():
            if not all([self.learning_rate_entry.get(), self.iterations_entry.get(),
                        self.stop_condition_entry.get(), project_name]):
                messagebox.showerror("Error", "Všechny tři parametry a název projektu musí být vyplněné.")
                return

        # Převedení hodnot na správný datový typ
        coco_address = self.coco_annotation_path.get()
        dataset_address = self.image_dataset_path.get()
        output_address = self.output_path.get()
        algorithms = [method for method, var in zip(["Sauvola", "Niblack", "Gaussian", "Mean Shift"],
                                                    self.method_vars) if var.get() == 1]
        learning_rate = float(self.learning_rate_entry.get())
        num_iterations = int(self.iterations_entry.get())
        stop_condition = float(self.stop_condition_entry.get())

        progress_window2 = ProcessingProgressWindow(root)
        progress_window2.update_progress("Initializing...")
        progress_window2.withdraw()

        if self.known_parameters_var.get():
            num_selected_methods = sum(var.get() == 1 for var in self.method_vars)
            if num_selected_methods != 1:
                messagebox.showerror("Error", "Při znalosti parametrů je třeba vybrat právě jednu metodu.")
                return

            selected_algorithm = next(
                (label for label, var in zip(self.method_labels, self.method_vars) if var.get() == 1), None)
            parameter_entry_dialog = ParameterEntryDialog(self.master, selected_algorithm)
            self.master.wait_window(parameter_entry_dialog)

            parameters = parameter_entry_dialog.result
            if parameters is not None:
                # Now you have the parameters, use them as needed
                print("Parameters:", parameters)
            else:
                # If result is None, return to the original window without executing further code
                return

            run_thread = threading.Thread(target=self.run_main, args=(
                coco_address, dataset_address, output_address, project_name, algorithms, learning_rate, num_iterations,
                stop_condition, parameters, None, progress_window2))

            run_thread.start()
        else:
            progress_window1 = OptimizationProgressWindow(self.master)
            progress_window1.update_info(project_name, algorithms, 0, "Unknown", "Unknown")
            progress_window1.withdraw()

            run_thread = threading.Thread(target=self.run_main, args=(
                coco_address, dataset_address, output_address, project_name, algorithms, learning_rate, num_iterations,
                stop_condition, None, progress_window1, progress_window2))

            run_thread.start()

    @staticmethod
    def run_main(coco_address, dataset_address, output_address, project_name, algorithms,
                 learning_rate, num_iterations, stop_condition, known_parameters, progress_window1, progress_window2):
        totalTime = time.time()

        for algorithm in algorithms:
            startTime = time.time()

            if known_parameters is None:
                progress_window1.deiconify()
                parameters, iou = g.GradientDescent(coco_address, output_address, project_name, algorithm,
                                                    learning_rate,
                                                    num_iterations, stop_condition, f.IoU, progress_window1).run()
                print(f"Resulting parameters: {parameters}", f"IoU: {round(iou * 100, 2)}%")
                progress_window1.withdraw()
            else:
                parameters = known_parameters

            progress_window2.deiconify()
            f.Contours(dataset_address, output_address, project_name, algorithm, parameters,
                       False, f.IoU, progress_window2).run()
            print(f"Segmentation of the project took: {round(time.time() - startTime)} seconds")
            progress_window2.withdraw()

        print(f"Total time: {round(time.time() - totalTime)} seconds")


if __name__ == "__main__":
    root = tk.Tk()
    app = SferoidSegmentationGUI(root)
    root.mainloop()
