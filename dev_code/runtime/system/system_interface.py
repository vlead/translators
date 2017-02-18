# Need to change the root PYTHONPATH during runtime
from dev_code.runtime.system.system import System
# from runtime.system.system import System

# Need to change the root PYTHONPATH during runtime
from dev_code.runtime.config.config import Config
# from runtime.config.config import Config


class SystemInterface():

    def __init__(self):
        pass

    @staticmethod
    def create_experiment(experiment_dict):
        System.create_dir(experiment_dict['id'], Config.SYSTEMPATH)
        # System.create_file(experiment_dict['id']+"/makefile", Config.SYSTEMPATH) # check makefile contents
        System.create_file(experiment_dict['id'] + "/README.org", Config.SYSTEMPATH)
        System.create_dir(experiment_dict['id'] + "/src", Config.SYSTEMPATH)
        for section in experiment_dict['sections']:
            System.create_file(experiment_dict['id'] + "/src/" + section + ".org", Config.SYSTEMPATH)
