import json
import os

from python_sdk_remote.mini_logger import MiniLogger
from python_sdk_remote.utilities import our_get_env

from .Component import Component
from .LoggerOutputEnum import LoggerOutputEnum
from .MessageSeverity import MessageSeverity

DEFAULT_MIN_SEVERITY = "Warning"
DEFULT_LOGGER_JSON_SUFFIX = '.logger.json'
DEFAULT_LOGGER_CONFIGURATION_JSON_PATH = our_get_env('LOGGER_CONFIGURATION_JSON_PATH')
DEFAULT_LOGGER_MINIMUM_SEVERITY = our_get_env('LOGGER_MINIMUM_SEVERITY')
PRINTED_ENVIRONMENT_VARIABLES = False


class DebugMode:
    def __init__(self, logger_minimum_severity: int | str = None,
                 logger_configuration_json_path: str = DEFAULT_LOGGER_CONFIGURATION_JSON_PATH):
        global PRINTED_ENVIRONMENT_VARIABLES
        # set default values that may be overridden
        self.debug_everything = False
        self.logger_json = {}

        # Minimal severity in case there is not LOGGER_MINIMUM_SEVERITY environment variable
        logger_minimum_severity = logger_minimum_severity or DEFAULT_LOGGER_MINIMUM_SEVERITY
        if logger_minimum_severity is None:
            self.logger_minimum_severity = self.__get_severity_level(DEFAULT_MIN_SEVERITY)
            if not PRINTED_ENVIRONMENT_VARIABLES:
                MiniLogger.info(f"Using LOGGER_MINIMUM_SEVERITY={DEFAULT_MIN_SEVERITY} from Logger default "
                                f"(can be overridden by LOGGER_MINIMUM_SEVERITY environment variable or "
                                f"{DEFULT_LOGGER_JSON_SUFFIX} file per component and logger output")

        else:
            self.logger_minimum_severity = self.__get_severity_level(logger_minimum_severity)
            if not PRINTED_ENVIRONMENT_VARIABLES:
                MiniLogger.info(
                    f"Using LOGGER_MINIMUM_SEVERITY={DEFAULT_LOGGER_MINIMUM_SEVERITY} from environment variable. "
                    f"Can be overridden by {DEFULT_LOGGER_JSON_SUFFIX} file per component and logger output.")

        try:
            if not logger_configuration_json_path:
                logger_configuration_json_path = os.path.join(os.getcwd(), DEFULT_LOGGER_JSON_SUFFIX)

            if os.path.exists(logger_configuration_json_path):
                with open(logger_configuration_json_path, 'r') as file:
                    self.logger_json = json.load(file)
                for component_id, component_info in self.logger_json.items():
                    for logger_output, severity_level in component_info.items():
                        component_info[logger_output] = self.__get_severity_level(severity_level)
                if not PRINTED_ENVIRONMENT_VARIABLES:
                    MiniLogger.info(
                        f"Using {logger_configuration_json_path} file to configure the logger, with the following "
                        f"configuration: {self.logger_json}")
            else:
                if not PRINTED_ENVIRONMENT_VARIABLES:
                    MiniLogger.info(f"Using default logger configuration. "
                                    f"You can add LOGGER_CONFIGURATION_JSON_PATH environment variable to override it. ")

                self.debug_everything = True

            PRINTED_ENVIRONMENT_VARIABLES = True
        except Exception as e:
            MiniLogger.exception("Failed to load logger configuration file. "
                                 "Using default logger configuration instead.", e)
            raise

    def is_logger_output(self, component_id: str, logger_output: LoggerOutputEnum, severity_level: int) -> bool:
        # Debug everything that has a severity level higher than the minimum required
        if self.debug_everything:
            return severity_level >= self.logger_minimum_severity

        component_id = str(component_id)  # in case the component_id is an int, as logger_json keys are strings

        component_id_or_name = component_id
        if component_id not in self.logger_json:  # search by component name
            component_details = Component.getDetailsByComponentId(component_id)
            if component_details:
                component_id_or_name = component_details[0]

        if component_id_or_name not in self.logger_json:
            component_id_or_name = "default"

        if component_id_or_name in self.logger_json:
            output_info = self.logger_json[component_id_or_name]
            if logger_output.value in output_info:
                result = severity_level >= output_info[logger_output.value]
                return result

        # In case the component does not exist in the logger configuration file or the logger_output was not specified
        return True

    @staticmethod
    def __get_severity_level(severity_level: int | str) -> int:
        if str(severity_level).lower() == "info":
            severity_level = "Information"

        if hasattr(MessageSeverity, str(severity_level).capitalize()):
            severity_level = MessageSeverity[severity_level.capitalize()].value
        elif str(severity_level).isdigit():
            severity_level = int(severity_level)
        else:
            raise Exception(f"invalid severity level {severity_level}")
        return severity_level
