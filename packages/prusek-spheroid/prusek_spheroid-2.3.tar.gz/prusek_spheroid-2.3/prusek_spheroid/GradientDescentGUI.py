import numpy as np
import time
import zipfile
import os
from concurrent.futures import ThreadPoolExecutor


def unzip(zip_file_path, extract_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

    # Assuming the content is directly in the extracted folder
    extracted_folder = extract_path

    return extracted_folder


class GradientDescent:
    def __init__(self, COCO_address, outputAddress, projekt, algorithm, learning_rate,
                 num_iterations, delta, f, progress_window=None, inner_contours=False):
        self.projekt = projekt
        self.algorithm = algorithm
        self.progress_window = progress_window

        annotationsAddress = unzip(COCO_address, os.path.dirname(COCO_address))

        self.adresaDatasetu = annotationsAddress + "/annotations/"
        self.adresaObrazku = annotationsAddress + "/images/"
        self.outputAddress = outputAddress


        self.cont_parameters = {}
        self.cont_param_ranges = {}
        # Define parameter dictionaries
        if self.algorithm in {"Sauvola", "Niblack", "Gaussian"}:
            self.cont_parameters.update({"window_size": 800})
            self.cont_param_ranges.update({"window_size": [1, 2001]})

        if self.algorithm == "Niblack":
            self.cont_parameters.update({"k": 0.2})
            self.cont_param_ranges.update({"k": [0.0, 0.35]})
        elif self.algorithm == "Mean Shift":
            self.cont_parameters.update({"k": 0.1})
            self.cont_param_ranges.update({"k": [0.0, 0.25]})
        elif self.algorithm == "Gaussian":
            self.cont_parameters.update({"k": 0.0})
            self.cont_param_ranges.update({"k": [-255.0, 255.0]})

        self.cont_parameters.update({"min_area": 5000, "sigma": 1.0, "std_k": 0.5})
        self.cont_param_ranges.update({"min_area": [0, 50000], "sigma": [0.0, 5.0], "std_k": [0.0, 3.0]})

        self.disc_parameters = {"dilation_size": 2}
        self.disc_param_ranges = {"dilation_size": [0, 10]}

        if inner_contours:
            self.cont_parameters.update({"holes_t": 100})
            self.cont_param_ranges.update({"holes_t": [0, 255]})

        self.lr = learning_rate
        self.num_iterations = num_iterations
        self.epsilon = 0.05
        self.delta = delta
        self.f = f
        self.instance = self.f(self.adresaDatasetu, self.adresaObrazku, self.outputAddress, self.projekt,
                               self.algorithm, inner_contours=inner_contours)

        # Initialize cont_normalized_parameters
        self.cont_normalized_parameters = self.normalize_parameters(self.cont_parameters)

    def evaluate_function(self, parameters):
        cont_parameters = self.denormalize_parameters(parameters)
        disc_parameters = self.disc_parameters

        return self.instance.run({**cont_parameters, **disc_parameters}, False)

    def compute_gradient_parallel(self):
        gradient = {param_name: 0 for param_name in self.cont_parameters.keys()}

        with ThreadPoolExecutor() as executor:
            futures = []
            for param_name in self.cont_parameters.keys():
                cont_normalized_parameters_plus = self.cont_normalized_parameters.copy()
                cont_normalized_parameters_minus = self.cont_normalized_parameters.copy()

                epsilon = self.epsilon  # Malá hodnota pro aproximaci
                cont_normalized_parameters_plus[param_name] += min(epsilon, 1-cont_normalized_parameters_plus[param_name])
                cont_normalized_parameters_minus[param_name] -= min(epsilon, cont_normalized_parameters_minus[param_name])

                future_plus = executor.submit(self.evaluate_function, cont_normalized_parameters_plus)
                future_minus = executor.submit(self.evaluate_function, cont_normalized_parameters_minus)

                futures.append((param_name, future_plus, future_minus))

            for param_name, future_plus, future_minus in futures:
                f_plus_epsilon = future_plus.result()
                f_minus_epsilon = future_minus.result()

                gradient[param_name] = (f_plus_epsilon - f_minus_epsilon) / (2 * self.epsilon)

        return gradient

    def normalize_parameters(self, parameters):
        normalized_parameters = {
            name: (value - self.cont_param_ranges[name][0]) / (
                    self.cont_param_ranges[name][1] - self.cont_param_ranges[name][0])
            for name, value in parameters.items()
        }
        return normalized_parameters

    def denormalize_parameters(self, normalized_parameters):
        parameters = {
            name: value * (self.cont_param_ranges[name][1] - self.cont_param_ranges[name][0]) +
                  self.cont_param_ranges[name][0]
            for name, value in normalized_parameters.items()
        }
        return parameters

    def adam_optimizer_parallel(self):
        parameters_array = []
        IoU_array = []
        iterations = 0
        beta1 = 0.9
        beta2 = 0.999
        epsilon = 1e-8

        m_t = {param_name: 0 for param_name in self.cont_parameters.keys()}
        v_t = {param_name: 0 for param_name in self.cont_parameters.keys()}

        while iterations < self.num_iterations:
            startCas = time.time()

            parameters_prev = np.r_[list(self.cont_parameters.values()), list(self.disc_parameters.values())]

            gradient = self.compute_gradient_parallel()

            iterations += 1
            m_t = {param_name: beta1 * m_t[param_name] + (1 - beta1) * gradient[param_name] for param_name in
                   self.cont_parameters.keys()}
            v_t = {param_name: beta2 * v_t[param_name] + (1 - beta2) * (gradient[param_name] ** 2) for param_name in
                   self.cont_parameters.keys()}

            m_t_hat = {param_name: m_t[param_name] / (1 - beta1 ** iterations) for param_name in
                       self.cont_parameters.keys()}
            v_t_hat = {param_name: v_t[param_name] / (1 - beta2 ** iterations) for param_name in
                       self.cont_parameters.keys()}

            for param_name in self.cont_normalized_parameters.keys():
                self.cont_normalized_parameters[param_name] += self.lr * m_t_hat[param_name] / (
                        np.sqrt(v_t_hat[param_name]) + epsilon)

                # Clip normalized parameters to [0, 1]
                self.cont_normalized_parameters[param_name] = np.clip(self.cont_normalized_parameters[param_name], 0, 1)

            # Denormalize parameters back to the original range
            self.cont_parameters = self.denormalize_parameters(self.cont_normalized_parameters)

            f_original = self.instance.run({**self.cont_parameters, **self.disc_parameters}, False)

            for i in range(len(self.disc_parameters)):
                param_name = list(self.disc_parameters.keys())[i]

                parameters = self.disc_parameters.copy()
                if parameters[param_name] >= self.disc_param_ranges[param_name][0] + 1:
                    parameters[param_name] += -1
                    f_minus_one = self.instance.run({**self.cont_parameters, **parameters}, False)
                else:
                    f_minus_one = 0

                parameters = self.disc_parameters.copy()
                if parameters[param_name] <= self.disc_param_ranges[param_name][1] - 1:
                    parameters[param_name] += 1
                    f_plus_one = self.instance.run({**self.cont_parameters, **parameters}, False)
                else:
                    f_plus_one = 0

                index = np.argmax([f_minus_one, f_original, f_plus_one])
                self.disc_parameters[param_name] += index - 1

            parameters_new_values = np.r_[list(self.cont_parameters.values()), list(self.disc_parameters.values())]
            parameters_new = {**self.cont_parameters, **self.disc_parameters}

            parameter_change = np.linalg.norm(
                np.divide(
                    np.subtract(parameters_new_values, parameters_prev),
                    np.subtract(
                        np.r_[(list(self.cont_param_ranges.values()), list(self.disc_param_ranges.values()))][:, 1],
                        np.r_[(list(self.cont_param_ranges.values()), list(self.disc_param_ranges.values()))][:,
                        0]))) / (
                                       len(self.disc_param_ranges) + len(self.cont_param_ranges))

            iou = self.instance.run({**self.cont_parameters, **self.disc_parameters}, False)
            IoU_array.append(iou)
            parameters_array.append(parameters_new)

            cas_iterace = time.time() - startCas

            rounded_parameters_new = {key: round(value, 3) for key, value in parameters_new.items()}

            if self.progress_window:
                self.progress_window.update_info(self.projekt, self.algorithm, iterations, round(iou * 100, 2),
                                                 round(cas_iterace * (self.num_iterations - iterations)))

            print(f"Projekt: {self.projekt}, Algoritmus: {self.algorithm}, Iterace {iterations}, "
                  f"IoU: {round(iou * 100, 2)}%, Parametry = {rounded_parameters_new}, "
                  f"změna parametrů = {round(parameter_change, 4)}, čas iterace: {round(cas_iterace)} sekund, "
                  f"předpokládaný zbývající čas: {round(cas_iterace * (self.num_iterations - iterations))} sekund")

            if parameter_change < self.delta:
                break

        index = np.argmax(IoU_array)
        _ = self.instance.run(parameters_array[index], True)

        print(f"Optimalizace ukončena. IoU: {round(IoU_array[index] * 100, 2)}%")
        return parameters_array[index], IoU_array[index]

    def run(self):
        parameters = {**self.cont_parameters, **self.disc_parameters}
        print(f"Projekt: {self.projekt}, Algoritmus: {self.algorithm}, Iterace {0}, Parametry = {parameters}")

        parameters, iou = self.adam_optimizer_parallel()  # Zavolání Adam optimizeru

        return parameters, iou
