import os
import numpy as np
import cv2 as cv
from skimage.filters import threshold_sauvola, threshold_niblack
from skimage import img_as_ubyte
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from threading import Lock
from prusek_spheroid import Funkce as f
from prusek_spheroid import characteristic_functions as cf
import json
import sys
import glob
import zipfile
from skimage import feature


def find_intersection(img_binary, filtered_contours, edges):
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


def create_binary_mask(img_gray, threshold, dilation_size):
    img_binary = img_as_ubyte(img_gray > threshold)
    img_binary = np.invert(img_binary)
    img_binary = f.Dilation(img_binary, dilation_size, 1)
    return img_binary


def calculate_canny_edges(img_gray, std_k, sigma):
    mean = np.mean(img_gray)
    std = np.std(img_gray)
    low_threshold = mean - std_k * std / 2
    high_threshold = mean + std_k * std / 2
    edges = feature.canny(img_gray, sigma=sigma, low_threshold=low_threshold, high_threshold=high_threshold)
    return edges


def filter_contours(contours, img_shape, min_area, detect_corrupted=True):
    if detect_corrupted:
        height, width = img_shape
        filtered_contours = []
        for contour in contours:
            if not (np.any(contour[:, :, 0] == 0) or np.any(contour[:, :, 1] == 0) or
                    np.any(contour[:, :, 0] == width - 1) or np.any(contour[:, :, 1] == height - 1)) and \
                    cv.contourArea(contour) >= min_area:
                filtered_contours.append(contour)
        return filtered_contours
    else:
        filtered_contours = []
        for contour in contours:
            if cv.contourArea(contour) >= min_area:
                filtered_contours.append(contour)
        return filtered_contours


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
    def apply_segmentation_algorithm(self, algorithm, parameters, img, img_rgb, img_name, detect_corrupted):
        if algorithm == "Sauvola":
            return self.sauvola(parameters, img, img_name, detect_corrupted)
        elif algorithm == "Niblack":
            return self.niblack(parameters, img, img_name, detect_corrupted)
        elif algorithm == "Mean Shift":
            return self.mean_shift(parameters, img_rgb, detect_corrupted)
        elif algorithm == "Gaussian":
            return self.gaussian_adaptive(parameters, img, detect_corrupted)
        else:
            print(f"Algoritmus s názvem {algorithm} nenalezen.")
            sys.exit(1)

    @staticmethod
    def sauvola(parameters, img_gray, img_name, detect_corrupted):
        window_size = check_window_size(int(parameters["window_size"]))
        std_k = parameters["std_k"]
        min_area = parameters["min_area"]
        dilation_size = int(parameters["dilation_size"])
        sigma = parameters["sigma"]

        thresh_sauvola = threshold_sauvola(img_gray, window_size=window_size)
        img_binary = create_binary_mask(img_gray, thresh_sauvola, dilation_size)
        edges = calculate_canny_edges(img_gray, std_k, sigma)

        contours, _ = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        filtered_contours = filter_contours(contours, img_gray.shape, min_area, detect_corrupted)

        return find_intersection(img_binary, filtered_contours, edges)

    @staticmethod
    def niblack(parameters, img_gray, img_name, detect_corrupted):
        window_size = check_window_size(int(parameters["window_size"]))
        k = parameters["k"]
        min_area = parameters["min_area"]
        std_k = parameters["std_k"]
        dilation_size = int(parameters["dilation_size"])
        sigma = parameters["sigma"]

        thresh_niblack = threshold_niblack(img_gray, window_size=window_size, k=k)
        img_binary = create_binary_mask(img_gray, thresh_niblack, dilation_size)
        edges = calculate_canny_edges(img_gray, std_k, sigma)

        contours, _ = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        filtered_contours = filter_contours(contours, img_gray.shape, min_area, detect_corrupted)

        return find_intersection(img_binary, filtered_contours, edges)

    @staticmethod
    def gaussian_adaptive(parameters, img_gray, detect_corrupted):
        window_size = check_window_size(int(parameters["window_size"]))
        k = parameters["k"]
        min_area = parameters["min_area"]
        std_k = parameters["std_k"]
        dilation_size = int(parameters["dilation_size"])
        sigma = parameters["sigma"]

        adaptive_threshold = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                                  window_size, k)

        img_binary = create_binary_mask(img_gray, adaptive_threshold, dilation_size)
        edges = calculate_canny_edges(img_gray, std_k, sigma)

        contours, _ = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        filtered_contours = filter_contours(contours, img_gray.shape, min_area, detect_corrupted)

        return find_intersection(img_binary, filtered_contours, edges)

    @staticmethod
    def gaussian(x, mean, amplitude, standard_deviation):
        return amplitude * np.exp(- ((x - mean) ** 2 / (2 * standard_deviation ** 2)))

    @staticmethod
    def find_holes(img_gray, mask_img, parameters):
        holes_t = parameters["holes_t"]

        background_mask = cv.bitwise_not(mask_img)
        background = cv.bitwise_and(img_gray, img_gray, mask=background_mask)

        # Výpočet histogramu pro referenční oblast pozadí
        hist_background = cv.calcHist([background], [0], background_mask, [256], [0, 256])

        # Normalizace histogramu
        cv.normalize(hist_background, hist_background, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)

        hist_background[0] = 0

        # Zpětná projekce histogramu
        back_project = cv.calcBackProject([img_gray], [0], hist_background, [0, 256], 1)

        # Aplikace zpětné projekce pouze na oblast sféroidu
        spheroid_back_project = cv.bitwise_and(back_project, back_project, mask=mask_img)

        # Prahování s použitím Otsuovy metody
        _, img_binary = cv.threshold(spheroid_back_project, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

        img_binary = f.Dilation(f.Erosion(img_binary, 3, 1), 3, 1)

        return img_binary, spheroid_back_project

    @staticmethod
    def mean_shift(parameters, img, detect_corrupted):
        k = parameters["k"]
        min_area = parameters["min_area"]
        std_k = parameters["std_k"]
        dilation_size = int(parameters["dilation_size"])
        sigma = parameters["sigma"]

        spatial_radius, color_radius = f.compute_optimal_radii(img, k)

        shifted = cv.pyrMeanShiftFiltering(img, spatial_radius, color_radius)

        shifted_gray = cv.cvtColor(shifted, cv.COLOR_BGR2GRAY)

        _, img_binary = cv.threshold(shifted_gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

        img_binary = np.invert(img_binary)
        # img_binary = f.Dilation(f.Erosion(img_binary, closing_size), closing_size)
        img_binary = f.Dilation(img_binary, dilation_size)

        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        edges = calculate_canny_edges(img_gray, std_k, sigma)

        # Určení kontur z dilatovaného binárního obrázku
        contours, _ = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        filtered_contours = filter_contours(contours, img_gray.shape, min_area, detect_corrupted)

        return find_intersection(img_binary, filtered_contours, edges)


class Contours(BaseImageProcessing):
    def __init__(self, adresaDatasetu, adresa_output, projekt, algorithm, parameters, show_img, function,
                 inner_contours, detect_corrupted, create_json, calculate_properties,
                 progress_window=None):
        super().__init__()
        self.adresaDatasetu = adresaDatasetu
        self.output_json_path = f"{adresa_output}/{projekt}/CVAT/{algorithm}/annotations/instances_default.json"
        self.output_images_path = f"{adresa_output}/{projekt}/CVAT/{algorithm}/images"
        self.output_segmented_path = f"{adresa_output}/{projekt}/segmented_images/{algorithm}"
        self.zipfile_address = f"{adresa_output}/{projekt}/CVAT/{algorithm}"
        self.excel_address = f"{adresa_output}/{projekt}"
        self.coco_data = f.initialize_coco_data()
        self.show_img = show_img
        self.projekt = projekt
        self.algorithm = algorithm
        self.parameters = parameters
        self.inner_contours = inner_contours
        self.detect_corrupted = detect_corrupted
        self.create_json = create_json
        self.calculate_properties = calculate_properties
        self.f = function
        self.counter = 1
        self.progress_window = progress_window

        create_directory(os.path.dirname(self.output_json_path))
        create_directory(self.output_images_path)
        create_directory(f"{self.output_segmented_path}/masks")
        create_directory(f"{self.output_segmented_path}/results")

    def run(self):
        all_contour_data = []
        filenames = os.listdir(self.adresaDatasetu)
        total_files = len(filenames)
        for filename in glob.glob(os.path.join(self.adresaDatasetu, '*.bmp')):
            with open(os.path.join(os.getcwd(), filename), 'r'):
                img = cv.imread(filename)
                basename = os.path.basename(filename)

                img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

                img_binary = self.apply_segmentation_algorithm(self.algorithm, self.parameters, img_gray, img,
                                                               basename.replace(".bmp", ".png"), self.detect_corrupted)

                if self.inner_contours:
                    holes_mask, holes_map = self.find_holes(img_gray, img_binary, self.parameters)

                    binary_with_holes = img_binary * 255 - holes_mask

                    # "Clipping" hodnot pixelů na rozmezí 0 až 255+
                    binary_with_holes = np.clip(binary_with_holes, 0, 255).astype(np.uint8)

                    contours, hierarchy = cv.findContours(binary_with_holes, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
                else:

                    contours, hierarchy = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
                    contours = sorted(contours, key=cv.contourArea, reverse=True)

                height, width = np.shape(img_binary)

                mask = np.zeros_like(img_gray, dtype=np.uint8)
                if not contours:
                    cv.line(img, (0, 0), (width - 1, height - 1), (0, 0, 255), 5)
                    cv.line(img, (0, height - 1), (width - 1, 0), (0, 0, 255), 5)
                else:
                    if self.create_json:
                        cv.imwrite(f"{self.output_images_path}/{basename}", img)

                    inner_contours = []
                    if self.inner_contours:
                        outer_contours = []
                        # Inicializace seznamů pro vnější a vnitřní kontury
                        blue_color = (255, 0, 0)  # Modrá
                        red_color = (0, 0, 255)  # Červená

                        for i, contour in enumerate(contours):
                            # Získání indexu rodiče pro aktuální konturu
                            parent_index = hierarchy[0][i][3]

                            if parent_index != -1:
                                # Kontrola, zda má rodič této kontury také rodiče (kontury druhého řádu)
                                grandparent_index = hierarchy[0][parent_index][3]
                                if grandparent_index == -1:
                                    # Kontura je prvního řádu (má rodiče, ale nemá dědečka)
                                    cv.drawContours(img, [contour], -1, blue_color, 2)
                                    inner_contours.append(contour)
                            else:
                                # Kontura nemá rodiče (vnější kontura)
                                cv.drawContours(img, [contour], -1, red_color, 2)
                                outer_contours.append(contour)
                    else:
                        outer_contours = contours
                        for index, contour in enumerate(outer_contours):
                            cv.drawContours(img, [contour], -1, [0, 0, 255], 2)
                            cv.drawContours(mask, [contour], -1, color=255, thickness=-1)

                            if self.calculate_properties:
                                contour_data = {
                                    'MaskName': os.path.basename(filename),
                                    'ContourOrder': index + 1
                                }

                                additional_data = cf.calculate_all(contour)
                                contour_data.update(additional_data)

                                all_contour_data.append(contour_data)

                    if self.create_json:
                        self.coco_data = f.convert_contours_to_coco(outer_contours, inner_contours, height, width, basename,
                                                                    self.counter,
                                                                    self.coco_data)

                cv.imwrite(f"{self.output_segmented_path}/results/result_{basename}", img)
                cv.imwrite(f"{self.output_segmented_path}/masks/mask_{basename}", mask)

                if self.progress_window:
                    progress_text = f"{self.counter}/{total_files}"
                    self.progress_window.update_progress(progress_text)
                    self.counter += 1

        if self.create_json or self.calculate_properties:
            if self.progress_window:
                self.progress_window.update_progress("dumping...")

            if self.calculate_properties:
                all_contour_data.sort(key=lambda x: x['MaskName'])
                df = pd.DataFrame(all_contour_data, columns=[
                    'MaskName', 'ContourOrder', 'Area', 'Circularity', 'Compactness', 'Convexity',
                    'EquivalentDiameter', 'FeretAspectRatio', 'FeretDiameterMax',
                    'FeretDiameterMaxOrthogonalDistance', 'FeretDiameterMin',
                    'LengthMajorDiameterThroughCentroid', 'LengthMinorDiameterThroughCentroid',
                    'Perimeter', 'Solidity', 'Sphericity'
                ])
                df.to_excel(f"{self.excel_address}/contour_properties.xlsx")

            if self.create_json:
                with open(self.output_json_path, "w") as json_file:
                    json.dump(self.coco_data, json_file)
                if self.progress_window:
                    self.progress_window.update_progress("zipping folder...")
                zip_folder(self.zipfile_address, f"{self.zipfile_address}.zip")

        if self.progress_window:
            self.progress_window.update_progress("FINISHED")


class IoU(BaseImageProcessing):
    def __init__(self, adresaAnotaci, adresaObrazku, adresa_output, projekt, algorithm, inner_contours):
        super().__init__()
        self.adresaAnotaci = adresaAnotaci
        self.adresaObrazku = adresaObrazku
        self.adresa_output = f"{adresa_output}/{projekt}/IoU"
        self.adresa_plots = f"{adresa_output}/{projekt}/IoU/plots"
        self.projekt = projekt
        self.algorithm = algorithm
        self.margin = 2
        self.inner_contours = inner_contours

        create_directory(self.adresa_output)
        create_directory(self.adresa_plots)

        self.plot_lock = Lock()

        self.contours_CVAT, self.masks, self.img_names = f.load_annotations(
            os.path.join(self.adresaAnotaci, 'instances_default.json'))
        print(f"Načteno {len(self.img_names)} anotovaných obrázků")

        # for mask, name in zip(self.masks, self.img_names):
        #    cv.imwrite(f"img_print/{name}",mask)

    def process_and_compute_iou(self, img_name, parameters, save, lock):
        img = cv.imread(os.path.join(self.adresaObrazku, img_name))
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        _, holes_mask = cv.threshold(img_gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

        # Zde předpokládám, že následující metody jsou definovány pro různé algoritmy segmentace
        img_binary = self.apply_segmentation_algorithm(self.algorithm, parameters, img_gray, img,
                                                       img_name.replace("bpm", "png"), detect_corrupted=False)

        if self.inner_contours:
            holes_mask, holes_map = self.find_holes(img_gray, img_binary, parameters)

            binary_with_holes = img_binary * 255 - holes_mask

            binary_with_holes = np.clip(binary_with_holes, 0, 255).astype(np.uint8)

            contours, hierarchy = cv.findContours(binary_with_holes, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        else:
            contours, hierarchy = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

        mask = np.zeros_like(img_binary, dtype=np.uint8)
        if not contours:
            contour = np.array([[0, 0]], dtype=np.int32)
            cv.drawContours(mask, [contour], 0, color=255, thickness=-1)
        else:
            for contour in contours:
                cv.drawContours(mask, [contour], 0, color=255, thickness=-1)

        mask_index = self.img_names.index(img_name)
        iou, tpr, ppv = f.IoU(self.projekt, self.algorithm, self.masks[mask_index], mask, img_name, save=save,
                              lock=lock,
                              address=self.adresa_plots)

        return iou, tpr, ppv

    def run(self, parameters, save_txt):
        IoUbuffer = []
        ratesBuffer = []

        lock = Lock()  # Create a Lock for thread-safe IoU calculations
        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(self.process_and_compute_iou, img_name, parameters, save_txt, lock): img_name for
                       img_name in self.img_names}

            for future in concurrent.futures.as_completed(futures):
                img_name = futures[future]
                iou, tpr, ppv = future.result()
                IoUbuffer.append([img_name, iou])
                ratesBuffer.append([tpr, ppv])

        IoUs = [entry[1] for entry in IoUbuffer]
        averageIoU = np.average(IoUs)

        if save_txt:
            rounded_parameters = {key: round(value, 2) for key, value in parameters.items()}
            TPRs = [entry[0] for entry in ratesBuffer]
            PPVs = [entry[1] for entry in ratesBuffer]
            averageTPR = np.average(TPRs)
            averagePPV = np.average(PPVs)

            print(f"TPR: {round(averageTPR * 100, 2)}%")
            print(f"PPV: {round(averagePPV * 100, 2)}%")

            # Uložení do JSON
            json_data = {
                "method": self.algorithm,
                "parameters": rounded_parameters,
                "averageIoU": round(averageIoU * 100, 2),
                "averageTPR": round(averageTPR * 100, 2),
                "averagePPV": round(averagePPV * 100, 2),
                "inner_contours": self.inner_contours  # Přidáme inner_contours do JSON dat
            }

            class NumpyEncoder(json.JSONEncoder):
                def default(self, obj):
                    if isinstance(obj, np.integer):
                        return int(obj)
                    return super(NumpyEncoder, self).default(obj)

            if not self.inner_contours:
                inner_contours_string = "WITHOUT_inner_contours"
            else:
                inner_contours_string = "WITH_inner_contours"

            with open(
                    f"{self.adresa_output}/results_{self.projekt}_{self.algorithm}_IoU_{round(averageIoU * 100, 2)}_{inner_contours_string}.json",
                    "w") as json_file:
                json.dump(json_data, json_file, indent=4, cls=NumpyEncoder)

        return averageIoU
