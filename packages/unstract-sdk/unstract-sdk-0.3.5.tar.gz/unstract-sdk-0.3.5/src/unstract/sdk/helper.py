import logging
import os

logger = logging.getLogger(__name__)


class SdkHelper:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_platform_base_url(platform_host: str, platform_port: str) -> str:
        """Make base url from host and port.

        Args:
            platform_host (str): Host of platform service
            platform_port (str): Port of platform service

        Returns:
            str: URL to the platform service
        """
        if platform_host[-1] == "/":
            return f"{platform_host[:-1]}:{platform_port}"
        return f"{platform_host}:{platform_port}"

    @staticmethod
    def get_env_or_die(env_key: str) -> str:
        """Returns the value of an env variable.

        If its empty or None, raises an error and exits

        Args:
            env_key (str): Key to retrieve

        Returns:
            str: Value of the env
        """
        env_value = os.environ.get(env_key)
        if env_value is None or env_value == "":
            logger.error("Env variable %s is required", env_key)
            exit(1)
        return env_value
