import os
import attrs
from constants import DEFAULT_ENDPOINTS
from bentoml._internal.configuration.helpers import load_config_file
from bentoml._internal.configuration.containers import config_merger
from simple_di import providers


@attrs.define
class ProjectConfig:
    config: dict = attrs.field(factory=dict, init=False)

    def __attrs_post_init__(self):
        """
        Load and merge configuration during initialization.

        This method loads configuration from the file specified in the
        ENV_ENDPOINTS environment variable, or uses the default endpoints if
        the environment variable is not set. It then merges the loaded
        configuration into the `config` attribute.
        """
        endpoints_config = load_config_file(os.getenv("ENV_PROJECT_ENDPOINTS", DEFAULT_ENDPOINTS))
        if len(endpoints_config) > 0:
            config_merger.merge(self.config, endpoints_config)

    @providers.SingletonFactory
    @staticmethod
    def get_instance() -> providers.ConfigDictType:
        """
        Static method to create and return a singleton instance of the configuration.

        This method initializes a new ProjectConfig instance and returns its
        configuration dictionary as a singleton.
        :return: Singleton configuration dictionary
        """
        instance = ProjectConfig()
        return instance.config

# Use ProjectConfig.get_instance to retrieve the singleton configuration
config = ProjectConfig.get_instance.get()