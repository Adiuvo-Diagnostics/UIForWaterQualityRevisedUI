import json
import os

class ConfigHandler:
    CONFIG_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../utils/config.json")

    def __init__(self):
        with open(self.CONFIG_FILE_PATH, 'r') as file:
            self.data = json.load(file)

    def save_data(self):
        with open(self.CONFIG_FILE_PATH, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get_current_experiment(self):
        return self.data.get("currentExperiment")

    def get_current_experiment_path(self):
        return self.data.get("currentExperimentPath")

    def get_acquisition_duration_in_secs(self):
        return int(self.data.get("acquisitionDurationInSecs"))

    def get_threshold_delta_peak_counts(self):
        return float(self.data.get("thresholdDeltaPeakCounts"))

    def get_threshold_delta_total_counts(self):
        return float(self.data.get("thresholdDeltaTotalCounts"))

    def set_current_experiment(self, value):
        self.data["currentExperiment"] = value
        self.save_data()

    def set_current_experiment_path(self, value):
        self.data["currentExperimentPath"] = value
        self.save_data()

    def set_acquisition_duration_in_secs(self, value):
        self.data["acquisitionDurationInSecs"] = int(value)
        self.save_data()

    def set_threshold_delta_peak_counts(self, value):
        self.data["thresholdDeltaPeakCounts"] = float(value)
        self.save_data()

    def set_threshold_delta_total_counts(self, value):
        self.data["thresholdDeltaTotalCounts"] = float(value)
        self.save_data()
