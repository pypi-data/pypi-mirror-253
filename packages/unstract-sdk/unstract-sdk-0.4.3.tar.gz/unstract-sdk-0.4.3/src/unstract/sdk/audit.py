import logging

import requests
from llama_index.callbacks import TokenCountingHandler
from llama_index.callbacks.schema import CBEventType
from unstract.sdk.constants import ToolEnv
from unstract.sdk.helper import SdkHelper

logger = logging.getLogger(__name__)


class Audit:
    """The 'Audit' class is responsible for pushing usage data to the platform
    service.

    Methods:
        - push_usage_data: Pushes the usage data to the platform service.

    Attributes:
        None

    Example usage:
        audit = Audit()
        audit.push_usage_data(
            token_counter,
            workflow_id,
            execution_id,
            external_service,
            event_type)
    """

    @staticmethod
    def push_usage_data(
        token_counter: TokenCountingHandler = None,
        workflow_id: str = "",
        execution_id: str = "",
        external_service: str = "",
        event_type: CBEventType = None,
    ) -> None:
        """Pushes the usage data to the platform service.

        Args:
            token_counter (TokenCountingHandler, optional): The token counter
              object. Defaults to None.
            workflow_id (str, optional): The ID of the workflow. Defaults to "".
            execution_id (str, optional): The ID of the execution. Defaults
              to "".
            external_service (str, optional): The name of the external service.
              Defaults to "".
            event_type (CBEventType, optional): The type of the event. Defaults
              to None.

        Returns:
            None

        Raises:
            requests.RequestException: If there is an error while pushing the
            usage details.
        """
        platform_host = SdkHelper.get_env_or_die(ToolEnv.PLATFORM_HOST)
        platform_port = SdkHelper.get_env_or_die(ToolEnv.PLATFORM_PORT)

        base_url = SdkHelper.get_platform_base_url(
            platform_host=platform_host, platform_port=platform_port
        )
        bearer_token = SdkHelper.get_env_or_die(ToolEnv.PLATFORM_API_KEY)

        data = {
            "usage_type": event_type,
            "external_service": external_service,
            "workflow_id": workflow_id,
            "execution_id": execution_id,
            "embedding_tokens": token_counter.total_embedding_token_count,
            "prompt_tokens": token_counter.prompt_llm_token_count,
            "completion_tokens": token_counter.completion_llm_token_count,
            "total_tokens": token_counter.total_llm_token_count,
        }

        url = f"{base_url}/usage"
        headers = {"Authorization": f"Bearer {bearer_token}"}

        try:
            response = requests.post(
                url, headers=headers, json=data, timeout=30
            )
            if response.status_code != 200:
                logger.error(
                    "Error while pushing usage details: %d %s",
                    response.status_code,
                    response.reason,
                )
            else:
                logger.info("Successfully pushed usage details")

        except requests.RequestException as e:
            logger.error("Error while pushing usage details: %s", str(e))
