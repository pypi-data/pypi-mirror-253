import os
import inspect
import importlib.util
from .SpeakSynkFlowProcessor import SpeakSynkFlowProcessor

def discover_and_import_child_classes():
    child_classes = []

    current_dir = os.getcwd()
    for filename in os.listdir(current_dir):
        if filename.endswith('.py') and not validFiles(filename):
            module_name = filename[:-3]
            module_path = os.path.join(current_dir, filename)

            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, SpeakSynkFlowProcessor) and obj != SpeakSynkFlowProcessor:
                    child_classes.append(obj())

    return child_classes

def validFiles(filename):
    return filename.startswith('__') or filename.startswith('test_') or filename.startswith('main')

def main():
    child_classes = discover_and_import_child_classes()
    for child in child_classes:
        child.run()
        child.close()

if __name__ == "__main__":
    main()