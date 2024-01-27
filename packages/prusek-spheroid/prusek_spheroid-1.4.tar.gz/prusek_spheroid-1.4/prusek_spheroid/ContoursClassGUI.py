import os
import numpy as np
import cv2 as cv
from skimage.filters import threshold_sauvola, threshold_niblack
from skimage import img_as_ubyte
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from threading import Lock
from prusek_spheroid import Funkce as f
import json
import sys
import glob
import zipfile
from skimage import feature


def check_window_size(window_size):
    return window_size + 1 if window_size % 2 == 0 else window_size


def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def zip_folder(folder_path, zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname=arcname)


class BaseImageProcessing:
    def apply_segmentation_algorithm(self, algorithm, parameters, img, img_rgb, img_name):
        if algorithm == "Sauvola":
            return self.sauvola(parameters, img, img_name)
        elif algorithm == "Niblack":
            return self.niblack(parameters, img, img_name)
        elif algorithm == "Mean Shift":
            return self.mean_shift(parameters, img_rgb)
        elif algorithm == "Gaussian":
            return self.gaussian_adaptive(parameters, img)
        else:
            print(f"Algoritmus s názvem {algorithm} nenalezen.")
            sys.exit(1)

    @staticmethod
    def sauvola(parameters, img_gray, img_name):
        window_size = check_window_size(int(parameters["window_size"]))
        closing_size = int(parameters["closing_size"])
        dilation_size = int(parameters["dilation_size"])
        sigma = parameters["sigma"]

        thresh_sauvola = threshold_sauvola(img_gray, window_size=window_size)
        img_binary = img_as_ubyte(img_gray > thresh_sauvola)

        # Invertování binárního obrázku
        img_binary = np.invert(img_binary)
        img_binary = f.Dilation(f.Erosion(img_binary, closing_size), closing_size)
        img_binary = f.Dilation(img_binary, dilation_size)

        # Aktualizace Cannyho detektoru hran s sigma 2.5
        edges = feature.canny(img_gray, sigma=sigma)

        # Určení kontur z dilatovaného binárního obrázku
        contours, _ = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        height, width = img_gray.shape
        filtered_contours = []

        for contour in contours:
            if not (np.any(contour[:, :, 0] == 0) or np.any(contour[:, :, 1] == 0) or np.any(
                    contour[:, :, 0] == width - 1) or np.any(contour[:, :, 1] == height - 1)):
                filtered_contours.append(contour)

        # Vytvoření výsledné masky pro průnik s Cannyho detektorem
        result_mask = np.zeros_like(img_binary, dtype=np.uint8)

        for contour in filtered_contours:
            # Vyplnění kontury
            filled_contour = cv.fillPoly(np.zeros_like(img_binary), [contour], 1)

            # Průnik s Cannyho detektorem
            intersection = filled_contour & edges

            # Kontrola neprázdného průniku a přidání do výsledné masky
            if np.any(intersection):
                result_mask = result_mask | filled_contour

        return result_mask

    @staticmethod
    def niblack(parameters, img_gray, img_name):
        window_size = check_window_size(int(parameters["window_size"]))
        closing_size = int(parameters["closing_size"])
        dilation_size = int(parameters["dilation_size"])
        k = parameters["k"]
        sigma = parameters["sigma"]

        thresh_niblack = threshold_niblack(img_gray, window_size=window_size, k=k)
        img_binary = img_as_ubyte(img_gray > thresh_niblack)

        img_binary = np.invert(img_binary)
        img_binary = f.Dilation(f.Erosion(img_binary, closing_size), closing_size)
        img_binary = f.Dilation(img_binary, dilation_size)

        # Aktualizace Cannyho detektoru hran s sigma 2.5
        edges = feature.canny(img_gray, sigma=sigma)

        # Určení kontur z dilatovaného binárního obrázku
        contours, _ = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        height, width = img_gray.shape
        filtered_contours = []

        for contour in contours:
            if not (np.any(contour[:, :, 0] == 0) or np.any(contour[:, :, 1] == 0) or np.any(
                    contour[:, :, 0] == width - 1) or np.any(contour[:, :, 1] == height - 1)):
                filtered_contours.append(contour)

        # Vytvoření výsledné masky pro průnik s Cannyho detektorem
        result_mask = np.zeros_like(img_binary, dtype=np.uint8)

        for contour in filtered_contours:
            # Vyplnění kontury
            filled_contour = cv.fillPoly(np.zeros_like(img_binary), [contour], 1)

            # Průnik s Cannyho detektorem
            intersection = filled_contour & edges

            # Kontrola neprázdného průniku a přidání do výsledné masky
            if np.any(intersection):
                result_mask = result_mask | filled_contour

        return result_mask

    @staticmethod
    def gaussian_adaptive(parameters, img_gray):
        window_size = check_window_size(int(parameters["window_size"]))
        closing_size = int(parameters["closing_size"])
        dilation_size = int(parameters["dilation_size"])
        k = parameters["k"]
        sigma = parameters["sigma"]

        adaptive_threshold = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                                  window_size, k)

        img_binary = img_as_ubyte(adaptive_threshold > 0)

        # Invert the binary image
        img_binary = np.invert(img_binary)

        # Apply closing operation
        img_binary = f.Dilation(f.Erosion(img_binary, closing_size), closing_size)

        # Apply dilation operation
        img_binary = f.Dilation(img_binary, dilation_size)

        # Aktualizace Cannyho detektoru hran s sigma 2.5
        edges = feature.canny(img_gray, sigma=sigma)

        # Určení kontur z dilatovaného binárního obrázku
        contours, _ = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        height, width = img_gray.shape
        filtered_contours = []

        for contour in contours:
            if not (np.any(contour[:, :, 0] == 0) or np.any(contour[:, :, 1] == 0) or np.any(
                    contour[:, :, 0] == width - 1) or np.any(contour[:, :, 1] == height - 1)):
                filtered_contours.append(contour)

        # Vytvoření výsledné masky pro průnik s Cannyho detektorem
        result_mask = np.zeros_like(img_binary, dtype=np.uint8)

        for contour in filtered_contours:
            # Vyplnění kontury
            filled_contour = cv.fillPoly(np.zeros_like(img_binary), [contour], 1)

            # Průnik s Cannyho detektorem
            intersection = filled_contour & edges

            # Kontrola neprázdného průniku a přidání do výsledné masky
            if np.any(intersection):
                result_mask = result_mask | filled_contour

        return result_mask



    @staticmethod
    def mean_shift(parameters, img):
        k = parameters["k"]
        closing_size = int(parameters["closing_size"])
        dilation_size = int(parameters["dilation_size"])
        sigma = parameters["sigma"]

        spatial_radius, color_radius = f.compute_optimal_radii(img, k)

        shifted = cv.pyrMeanShiftFiltering(img, spatial_radius, color_radius)

        shifted_gray = cv.cvtColor(shifted, cv.COLOR_BGR2GRAY)

        _, img_binary = cv.threshold(shifted_gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

        img_binary = np.invert(img_binary)
        img_binary = f.Dilation(f.Erosion(img_binary, closing_size), closing_size)
        img_binary = f.Dilation(img_binary, dilation_size)

        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # Aktualizace Cannyho detektoru hran s sigma 2.5
        edges = feature.canny(img_gray, sigma=sigma)

        # Určení kontur z dilatovaného binárního obrázku
        contours, _ = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        height, width = np.shape(img)[:2]
        filtered_contours = []

        for contour in contours:
            if not (np.any(contour[:, :, 0] == 0) or np.any(contour[:, :, 1] == 0) or np.any(
                    contour[:, :, 0] == width - 1) or np.any(contour[:, :, 1] == height - 1)):
                filtered_contours.append(contour)

        # Vytvoření výsledné masky pro průnik s Cannyho detektorem
        result_mask = np.zeros_like(img_binary, dtype=np.uint8)

        for contour in filtered_contours:
            # Vyplnění kontury
            filled_contour = cv.fillPoly(np.zeros_like(img_binary), [contour], 1)

            # Průnik s Cannyho detektorem
            intersection = filled_contour & edges

            # Kontrola neprázdného průniku a přidání do výsledné masky
            if np.any(intersection):
                result_mask = result_mask | filled_contour

        return result_mask


class Contours(BaseImageProcessing):
    def __init__(self, adresaDatasetu, adresa_output, projekt, algorithm, parameters, show_img, function,
                 progress_window=None):
        super().__init__()
        self.adresaDatasetu = adresaDatasetu
        self.output_json_path = f"{adresa_output}/{projekt}/CVAT/{algorithm}/annotations/instances_default.json"
        self.output_images_path = f"{adresa_output}/{projekt}/CVAT/{algorithm}/images"
        self.output_segmented_path = f"{adresa_output}/{projekt}/segmented_images/{algorithm}"
        self.zipfile_address = f"{adresa_output}/{projekt}/CVAT/{algorithm}"
        self.coco_data = f.initialize_coco_data()
        self.show_img = show_img
        self.projekt = projekt
        self.algorithm = algorithm
        self.parameters = parameters
        self.f = function
        self.counter = 1
        self.progress_window = progress_window

        create_directory(self.output_segmented_path)
        create_directory(os.path.dirname(self.output_json_path))
        create_directory(self.output_images_path)

    def run(self):
        filenames = os.listdir(self.adresaDatasetu)
        total_files = len(filenames)
        for filename in glob.glob(os.path.join(self.adresaDatasetu, '*.bmp')):
            with open(os.path.join(os.getcwd(), filename), 'r'):
                img = cv.imread(filename)
                basename = os.path.basename(filename)

                img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

                img_binary = self.apply_segmentation_algorithm(self.algorithm, self.parameters, img_gray, img,
                                                               basename.replace("bpm", "png"))

                contours, hierarchy = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

                filtered_contours = f.filter_contours_by_min_area(contours, self.parameters["min_area"])

                height, width = np.shape(img_binary)

                if not filtered_contours:
                    cv.line(img, (0, 0), (width - 1, height - 1), (0, 0, 255), 5)
                    cv.line(img, (0, height - 1), (width - 1, 0), (0, 0, 255), 5)
                else:
                    cv.imwrite(f"{self.output_images_path}/{basename}", img)
                    for contour in filtered_contours:
                        cv.drawContours(img, [contour], -1, [0, 0, 255], 2)

                    self.coco_data = f.convert_contours_to_coco(filtered_contours, height, width, basename,
                                                                self.counter,
                                                                self.coco_data)

                cv.imwrite(f"{self.output_segmented_path}/result_{basename}", img)

                if self.progress_window:
                    progress_text = f"{self.counter}/{total_files}"
                    self.progress_window.update_progress(progress_text)
                    self.counter += 1

        if self.progress_window:
            self.progress_window.update_progress("dumping json...")
        with open(self.output_json_path, "w") as json_file:
            json.dump(self.coco_data, json_file)
        if self.progress_window:
            self.progress_window.update_progress("zipping folder...")
        zip_folder(self.zipfile_address, f"{self.zipfile_address}.zip")

        if self.progress_window:
            self.progress_window.update_progress("FINISHED")


class IoU(BaseImageProcessing):
    def __init__(self, adresaAnotaci, adresaObrazku, adresa_output, projekt, algorithm):
        super().__init__()
        self.adresaAnotaci = adresaAnotaci
        self.adresaObrazku = adresaObrazku
        self.adresa_output = f"{adresa_output}/{projekt}/IoU"
        self.adresa_plots = f"{adresa_output}/{projekt}/IoU/plots"
        self.projekt = projekt
        self.algorithm = algorithm
        self.margin = 2

        create_directory(self.adresa_output)
        create_directory(self.adresa_plots)

        self.plot_lock = Lock()

        # Načtení anotací, masek a názvů obrázků
        self.contours_CVAT, self.masks, self.img_names = f.load_annotations(
            os.path.join(self.adresaAnotaci, 'instances_default.json'))
        print(f"Načteno {len(self.img_names)} anotovaných obrázků")

    def process_and_compute_iou(self, img_name, parameters, save, lock):
        img = cv.imread(os.path.join(self.adresaObrazku, img_name))
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Zde předpokládám, že následující metody jsou definovány pro různé algoritmy segmentace
        img_binary = self.apply_segmentation_algorithm(self.algorithm, parameters, img_gray, img,
                                                       img_name.replace("bpm", "png"))

        contours, _ = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        filtered_contours = f.filter_contours_by_min_area(contours, parameters["min_area"])

        mask = np.zeros_like(img_binary, dtype=np.uint8)
        if not filtered_contours:
            contour = np.array([[0, 0]], dtype=np.int32)
            cv.drawContours(mask, [contour], 0, color=255, thickness=-1)
        else:

            for contour in filtered_contours:
                cv.drawContours(mask, [contour], 0, color=255, thickness=-1)

        mask_index = self.img_names.index(img_name)
        iou = f.IoU(self.projekt, self.algorithm, self.masks[mask_index], mask, img_name, save=save, lock=lock,
                    address=self.adresa_plots)

        return iou

    def run(self, parameters, save_txt):
        IoUbuffer = []

        lock = Lock()  # Create a Lock for thread-safe IoU calculations
        with ThreadPoolExecutor() as executor:
            if save_txt:
                futures = {executor.submit(self.process_and_compute_iou, img_name, parameters, True, lock): img_name for
                           img_name
                           in
                           self.img_names}
            else:
                futures = {executor.submit(self.process_and_compute_iou, img_name, parameters, False, lock): img_name
                           for img_name
                           in
                           self.img_names}

            for future in concurrent.futures.as_completed(futures):
                img_name = futures[future]
                iou = future.result()
                IoUbuffer.append([img_name, iou])

        IoUs = [entry[1] for entry in IoUbuffer]
        averageIoU = np.average(IoUs)

        if save_txt:
            rounded_parameters = {key: round(value, 2) for key, value in parameters.items()}

            np.savetxt(
                f"{self.adresa_output}/IoU:{round(averageIoU * 100, 2)}, {self.projekt}, {self.algorithm}, {rounded_parameters}.csv",
                [f"{entry[0]} - {round(100 * entry[1], 2)}%" for entry in IoUbuffer], delimiter=", ", fmt='% s')

        return averageIoU
