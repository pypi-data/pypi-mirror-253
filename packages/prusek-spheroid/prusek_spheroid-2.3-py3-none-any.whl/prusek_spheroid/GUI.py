import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from prusek_spheroid import GradientDescentGUI as g
from prusek_spheroid import ContoursClassGUI as f
import threading
import time
import json


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

    def update_info(self, project, algorithm, iteration, IoU, time_rem):
        self.label_project.config(text=f"Project: {project}")
        self.label_algorithm.config(text=f"Algorithm: {algorithm}")
        self.label_iteration.config(text=f"Iteration: {iteration}")
        self.label_iou.config(text=f"IoU: {IoU}%")
        self.label_parameters.config(text=f"Estimated time remaining: {time_rem} seconds")


class ParameterEntryDialog(tk.Toplevel):
    def __init__(self, master, algorithm, parameters):
        tk.Toplevel.__init__(self, master)
        self.title("Enter Parameters")

        self.algorithm = algorithm
        self.parameters = parameters  # Store loaded parameters from JSON
        self.result = None

        # Create labels and entry widgets for each parameter with descriptions and ranges
        self.entries = {}
        for param, value in self.parameters.items():
            label = tk.Label(self, text=f"{param}:")
            label.pack()
            entry = tk.Entry(self)
            entry.insert(0, str(value))
            entry.pack()
            self.entries[param] = entry

        # OK button to confirm parameter values
        ok_button = tk.Button(self, text="OK", command=self.confirm_parameters)
        ok_button.pack()

    def confirm_parameters(self):
        # Retrieve parameter values from entry widgets and update self.parameters
        for param, entry in self.entries.items():
            value = entry.get()
            try:
                value = float(value)
                self.parameters[param] = value
            except ValueError:
                # Handle invalid input, e.g., non-numeric values
                pass
        self.result = self.parameters  # Set the result to the updated parameters
        self.destroy()  # Close the dialog

    def close_dialog(self):
        self.result = None
        self.destroy()

    def get_parameters(self):
        return self.parameters

    def set_parameters(self, parameters):
        for param, value in parameters.items():
            if param in self.entries:
                self.entries[param].delete(0, tk.END)
                self.entries[param].insert(0, str(value))

    def update_parameters(self, new_parameters):
        # Update parameters in the main application when entering them manually
        self.parameters = new_parameters


class SferoidSegmentationGUI:
    def __init__(self, master):

        self.loaded_parameters = None
        self.loaded_method = None

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

        # Textbox pro název projektu
        self.project_name_label = tk.Label(master, text="Project Name:")
        self.project_name_label.pack()
        self.project_name_entry = tk.Entry(master)
        self.project_name_entry.pack()

        # Tlačítko pro načtení parametrů z JSON souboru
        self.load_parameters_button = tk.Button(master,
                                                text="I already know the parameters (load JSON file with parameters)",
                                                command=self.load_and_run_parameters)
        self.load_parameters_button.pack()

        # Create a frame to contain the label and button
        self.parameters_frame = tk.Frame(self.master)
        self.parameters_frame.pack()

        # Initially disable the "Parameters loaded" label and the "Cancel" button
        self.parameters_loaded_label = tk.Label(self.parameters_frame, text="Parameters loaded", state=tk.DISABLED)
        self.parameters_loaded_label.pack(side=tk.LEFT)  # Place label to the left

        self.cancel_button = tk.Button(self.parameters_frame, text="Cancel", command=self.cancel_parameters_loaded,
                                       state=tk.DISABLED)
        self.cancel_button.pack(side=tk.LEFT)  # Place button to the left

        # Checkboxy pro výběr metod
        self.methods_frame = tk.Frame(master)
        self.methods_frame.pack()
        self.method_labels = ["Sauvola", "Niblack", "Gaussian", "Mean Shift"]

        self.methods_checkboxes = []  # Create a list to store the checkboxes

        for i, method_label in enumerate(self.method_labels):
            method_var = tk.IntVar()
            method_checkbox = tk.Checkbutton(self.methods_frame, text=method_label, variable=method_var)
            method_checkbox.grid(row=0, column=i, padx=5, pady=5)

            self.methods_checkboxes.append((method_checkbox, method_var))

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

        # Oddělovací čára mezi adresní a metody sekce
        self.method_separator = tk.Frame(master, height=2, bd=1, relief=tk.SUNKEN)
        self.method_separator.pack(fill=tk.X, padx=5, pady=5)

        self.other_section_label = tk.Label(master, text="Other Settings", font=("Helvetica", 12, "bold"))
        self.other_section_label.pack()

        checkbox_frame = tk.Frame(master)
        checkbox_frame.pack()

        # Checkbox pro 'also find the inner contours'
        self.inner_contours_var = tk.BooleanVar()
        self.checkbox_inner_contours = tk.Checkbutton(checkbox_frame, text="Also find the inner contours",
                                                      variable=self.inner_contours_var,
                                                      onvalue=True, offvalue=False)
        self.checkbox_inner_contours.pack(side=tk.LEFT)

        self.detect_corrupted_var = tk.BooleanVar()
        self.checkbox_detect_corrupted = tk.Checkbutton(checkbox_frame, text="Detect and discard corrupted images",
                                                        variable=self.detect_corrupted_var, onvalue=True,
                                                        offvalue=False)
        self.checkbox_detect_corrupted.pack(side=tk.LEFT)

        # Checkbox pro 'Create JSON file for export to CVAT'
        self.create_json_var = tk.BooleanVar()
        self.checkbox_create_json = tk.Checkbutton(checkbox_frame, text="Create JSON file for export to CVAT",
                                                   variable=self.create_json_var,
                                                   onvalue=True, offvalue=False)
        self.checkbox_create_json.pack(side=tk.LEFT)

        # Checkbox pro 'Calculate contour properties'
        self.calculate_contours_var = tk.BooleanVar()
        self.checkbox_calculate_contours = tk.Checkbutton(checkbox_frame, text="Calculate contour properties",
                                                          variable=self.calculate_contours_var,
                                                          onvalue=True, offvalue=False)
        self.checkbox_calculate_contours.pack(side=tk.LEFT)

        # Tlačítko pro spuštění
        self.run_button = tk.Button(master, text="Run", command=self.run_method)
        self.run_button.pack()

    def show_completion_dialog(self, time_taken, output_folder):
        dialog = tk.Toplevel(self.master)
        dialog.title("Segmentation Completed")

        message = f"DONE.\nSegmentation took {time_taken:.2f} seconds.\nOutput stored in a folder: {output_folder}"
        tk.Label(dialog, text=message).pack(padx=20, pady=10)

        ok_button = tk.Button(dialog, text="OK", command=dialog.destroy)
        ok_button.pack(pady=10)
    def cancel_parameters_loaded(self):
        # Clear the loaded parameters
        self.loaded_parameters = {}

        # Reset the method selection
        for method_checkbox, _ in self.methods_checkboxes:
            method_checkbox.config(state=tk.NORMAL)

        # Unlock learning rate, number of iterations, and stop condition text fields
        self.learning_rate_entry.config(state=tk.NORMAL)
        self.iterations_entry.config(state=tk.NORMAL)
        self.stop_condition_entry.config(state=tk.NORMAL)

        # Unlock the inner contours checkbox
        self.checkbox_inner_contours.config(state=tk.NORMAL)

        self.parameters_loaded_label.config(state=tk.DISABLED)
        self.cancel_button.config(state=tk.DISABLED)

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

    def enable_parameter_entry(self):
        state = tk.NORMAL
        self.learning_rate_entry.config(state=state)
        self.iterations_entry.config(state=state)
        self.stop_condition_entry.config(state=state)

    def load_and_run_parameters(self):
        json_file_path = filedialog.askopenfilename(
            title="Select the JSON file in which the already found optimal parameters are uploaded:",
            filetypes=[("JSON files", "*.json")])
        if json_file_path:
            self.load_json_parameters(json_file_path)
            self.run_method_with_loaded_parameters()

    def load_json_parameters(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Extrahujte potřebná data
        self.loaded_method = data.get("method", "")
        self.loaded_parameters = data.get("parameters", {})
        self.inner_contours_var.set(data.get("inner_contours", False))

    def run_method_with_loaded_parameters(self):
        if not self.loaded_parameters:
            messagebox.showerror("Error", "No parameters loaded.")
            return

        # Předpokládá se, že tato metoda otevře dialog pro potvrzení parametrů
        parameter_entry_dialog = ParameterEntryDialog(self.master, self.loaded_method, self.loaded_parameters)
        self.master.wait_window(parameter_entry_dialog)

        if parameter_entry_dialog.result is None:
            messagebox.showinfo("Info", "Parameters were not saved.")
        else:
            self.parameters_loaded_label.config(state=tk.NORMAL)
            self.cancel_button.config(state=tk.NORMAL)

            loaded_method = self.loaded_method

            # Set the loaded method and lock all method checkboxes
            for checkbox, var in self.methods_checkboxes:
                if checkbox.cget("text") == loaded_method:
                    var.set(1)  # Check the loaded method's checkbox
                    checkbox.config(state=tk.DISABLED)
                else:
                    var.set(0)  # Uncheck other method checkboxes
                    checkbox.config(state=tk.DISABLED)

            # Lock learning rate, number of iterations, and stop condition text fields
            self.learning_rate_entry.config(state=tk.DISABLED)
            self.iterations_entry.config(state=tk.DISABLED)
            self.stop_condition_entry.config(state=tk.DISABLED)

            self.checkbox_inner_contours.config(state=tk.DISABLED)

    def run_method(self):
        project_name = self.project_name_entry.get()
        if not project_name:
            messagebox.showerror("Error", "Project name must be filled in.")
            return

        if not self.loaded_parameters:  # Check only when parameters are not loaded from JSON
            if not self.coco_annotation_path.get():
                messagebox.showerror("Error", "The first address in 'Address Settings' must be filled.")
                return

        # Check that the second and third addresses are always filled
        if not all([self.image_dataset_path.get(), self.output_path.get()]):
            messagebox.showerror("Error", "Both 'Image Dataset Path' and 'Output Path' must be filled.")
            return

        if not any(var.get() == 1 for _, var in self.methods_checkboxes):
            messagebox.showerror("Error", "At least one of the four segmentation methods must be selected.")
            return

        # Retrieve values from entry fields
        coco_address = self.coco_annotation_path.get()
        dataset_address = self.image_dataset_path.get()
        output_address = self.output_path.get()

        algorithms = [method for method, (checkbox, var) in
                      zip(["Sauvola", "Niblack", "Gaussian", "Mean Shift"], self.methods_checkboxes) if
                      var.get() == 1]

        # Načtené parametry z JSON souboru, pokud jsou k dispozici
        if self.loaded_parameters:
            parameters = self.loaded_parameters
            progress_window1 = None
        else:
            parameters = None
            progress_window1 = OptimizationProgressWindow(self.master)
            progress_window1.update_info(project_name, algorithms, 0, "Unknown", "Unknown")
            progress_window1.withdraw()

        inner_contours_value = self.inner_contours_var.get()
        detect_corrupted = self.detect_corrupted_var.get()
        create_json = self.create_json_var.get()
        calculate_properties = self.calculate_contours_var.get()

        progress_window2 = ProcessingProgressWindow(self.master)
        progress_window2.update_progress("Initializing...")
        progress_window2.withdraw()

        run_thread = threading.Thread(target=self.run_main, args=(
            coco_address, dataset_address, output_address, project_name, algorithms, parameters,
            inner_contours_value, detect_corrupted, create_json, calculate_properties, progress_window1, progress_window2))
        run_thread.start()

    def run_main(self, coco_address, dataset_address, output_address, project_name, algorithms, known_parameters,
                 inner_contours, detect_corrupted, create_json, calculate_properties, progress_window1, progress_window2):
        totalTime = time.time()

        for algorithm in algorithms:
            startTime = time.time()

            if known_parameters is None:
                learning_rate = float(self.learning_rate_entry.get())
                num_iterations = int(self.iterations_entry.get())
                stop_condition = float(self.stop_condition_entry.get())
                progress_window1.deiconify()
                parameters, iou = g.GradientDescent(coco_address, output_address, project_name, algorithm,
                                                    learning_rate,
                                                    num_iterations, stop_condition, f.IoU, progress_window1,
                                                    inner_contours=inner_contours).run()
                print(f"Resulting parameters: {parameters}", f"IoU: {round(iou * 100, 2)}%")
                progress_window1.withdraw()
            else:
                parameters = known_parameters

            progress_window2.deiconify()
            f.Contours(dataset_address, output_address, project_name, algorithm, parameters,
                       False, f.IoU, inner_contours, detect_corrupted, create_json, calculate_properties, progress_window2).run()
            print(f"Segmentation of the project took: {round(time.time() - startTime)} seconds")
            progress_window2.withdraw()

        print(f"Total time: {round(time.time() - totalTime)} seconds")

        # Zobrazit dialogové okno po dokončení segmentace
        self.show_completion_dialog(round(time.time() - totalTime), output_address)


if __name__ == "__main__":
    root = tk.Tk()
    app = SferoidSegmentationGUI(root)
    root.mainloop()
