import time
import numpy as np
import pandas as pd
from ctypes import *
from config_handler import ConfigHandler
import RPi.GPIO as GPIO
class Processor:
    _instance = None
    BuzzerPin = 21
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Processor, cls).__new__(cls)
            GPIO.setwarnings(False)
            # BCM is 21 PIN 40
            GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme
            GPIO.setup(21, GPIO.OUT)  # LED pin set as output
            # Initialization code here
            cls._instance.config_handler = ConfigHandler()
            cls._instance.thesPeak = cls._instance.config_handler.get_threshold_delta_peak_counts()
            cls._instance.thesTotal = cls._instance.config_handler.get_threshold_delta_total_counts()
            cls._instance.samplingTimeInSeconds = cls._instance.config_handler.get_acquisition_duration_in_secs()
            cls._instance.DataforSaline = []
            cls._instance.DataforBioBurden = []

        return cls._instance


    def BuzzerSound(self):
        GPIO.output(self.BuzzerPin, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(self.BuzzerPin, GPIO.LOW)
        time.sleep(0.1)
        pass  # GPIO logic for buzzer can be added here

    def StartTestForReference(self):
        self.BuzzerSound()
        SampleCSVFilepath = self.config_handler.get_current_experiment_path()+"/ref.csv"
        libCalc = CDLL("./timedAcq.so")
        for i in range(0, len(SampleCSVFilepath)):
            libCalc.path(ord(SampleCSVFilepath[i]), 0)
        libCalc.path(ord('\0'), 1)
        libCalc.main(self.samplingTimeInSeconds)
        self.BuzzerSound()
        self.ReferenceAnalysis()

    def ReferenceAnalysis(self):
        data = pd.read_csv(self.config_handler.get_current_experiment_path()+"/ref.csv")
        datacounts, bins = np.histogram(data['tof'], bins=np.arange(0, 100, 0.2))
        datacounts = self.removeOffset(datacounts)
        self.DataforReference.append(max(datacounts))
        self.DataforReference.append(self.GetTotalCounts(datacounts, bins))

    def StartTestForSample(self):
        self.BuzzerSound()
        SampleCSVFilepath = self.config_handler.get_current_experiment_path()+"/sam.csv"
        libCalc = CDLL("./timedAcq.so")
        for i in range(0, len(SampleCSVFilepath)):
            libCalc.path(ord(SampleCSVFilepath[i]), 0)
        libCalc.path(ord('\0'), 1)
        libCalc.main(self.samplingTimeInSeconds)
        self.BuzzerSound()
        self.SampleAnalysis()

    def SampleAnalysis(self):
        data = pd.read_csv(self.config_handler.get_current_experiment_path()+"/sam.csv")
        datacounts, bins = np.histogram(data['tof'], bins=np.arange(0, 100, 0.2))
        datacounts = self.removeOffset(datacounts)
        self.DataforSample.append(max(datacounts))
        self.DataforSample.append(self.GetTotalCounts(datacounts, bins))

    def GetTotalCounts(self, data, bins):
        CountStart = 10            # START TIME AND END TIME FOR AREA UNDER CURVE
        CountStop = 15
        sum = 0
        for i in range(len(data)):
            if ((bins[i] > CountStart) and (bins[i] < CountStop)):
                sum = sum + data[i]
        return sum
    def removeOffset(self,data):
        DecayIdleTailDurationNs = 20
        HistbinInterval = 0.2
        tailLen = int(np.floor(DecayIdleTailDurationNs/HistbinInterval))
        return data - np.mean(data[-tailLen:])
    def Result(self):
        if (((self.DataforSample[0] - self.DataforReference[0])/self.DataforReference[0] )> self.thesPeak) or (
                ((self.DataforSample[1] - self.DataforReference[1])/self.DataforReference[1]) > self.thesTotal):
            results = "Positive"
        else:
            results = "Negative"
        return results

