import logging
from typing import Optional

from llama_index.embeddings.base import BaseEmbedding
from unstract.adapters.constants import Common
from unstract.adapters.embedding import adapters
from unstract.sdk.adapters import ToolAdapter
from unstract.sdk.tool.base import AbstractTool

logger = logging.getLogger(__name__)


class ToolEmbedding:
    def __init__(self, tool: AbstractTool):
        self.tool = tool
        self.max_tokens = 1024 * 16
        self.embedding_adapters = adapters

    def get_embedding(
        self, adapter_instance_id: str
    ) -> Optional[BaseEmbedding]:
        if adapter_instance_id is not None:
            try:
                embedding_config_data = ToolAdapter.get_adapter_config(
                    self.tool, adapter_instance_id
                )
                embedding_adapter_id = embedding_config_data.get(
                    Common.ADAPTER_ID
                )
                if embedding_adapter_id in self.embedding_adapters:
                    embedding_adapter = self.embedding_adapters[
                        embedding_adapter_id
                    ][Common.METADATA][Common.ADAPTER]
                    embedding_metadata = embedding_config_data.get(
                        Common.ADAPTER_METADATA
                    )
                    embedding_adapter_class = embedding_adapter(
                        embedding_metadata
                    )
                    return embedding_adapter_class.get_embedding_instance()
                else:
                    return None
            except Exception as e:
                logger.error(f"Error getting embedding: {e}")
                return None
        else:
            return None
