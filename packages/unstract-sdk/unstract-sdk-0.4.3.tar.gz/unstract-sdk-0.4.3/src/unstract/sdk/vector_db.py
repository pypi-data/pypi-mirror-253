import logging
from typing import Union

from llama_index.vector_stores.types import BasePydanticVectorStore, VectorStore
from unstract.adapters.constants import Common
from unstract.adapters.vectordb import adapters
from unstract.adapters.vectordb.constants import VectorDbConstants
from unstract.sdk.adapters import ToolAdapter
from unstract.sdk.tool.base import AbstractTool

logger = logging.getLogger(__name__)


class ToolVectorDB:
    """Class to handle VectorDB for Unstract Tools."""

    def __init__(self, tool: AbstractTool):
        self.tool = tool
        self.vector_db_adapters = adapters

    def get_vector_db(
        self,
        adapter_instance_id: str,
        collection_name_prefix: str = None,
        embedding_type: str = None,
    ) -> Union[BasePydanticVectorStore, VectorStore, None]:
        if adapter_instance_id is not None:
            try:
                vector_db_config = ToolAdapter.get_adapter_config(
                    self.tool, adapter_instance_id
                )
                vector_db_adapter_id = vector_db_config.get(Common.ADAPTER_ID)
                if vector_db_adapter_id in self.vector_db_adapters:
                    vector_db_adapter = self.vector_db_adapters[
                        vector_db_adapter_id
                    ][Common.METADATA][Common.ADAPTER]
                    vector_db_metadata = vector_db_config.get(
                        Common.ADAPTER_METADATA
                    )
                    # Adding the collection prefix and embedding type
                    # to the metadata
                    vector_db_metadata[
                        VectorDbConstants.VECTOR_DB_NAME_PREFIX
                    ] = collection_name_prefix
                    vector_db_metadata[
                        VectorDbConstants.EMBEDDING_TYPE
                    ] = embedding_type

                    vector_db_adapter_class = vector_db_adapter(
                        vector_db_metadata
                    )
                    return vector_db_adapter_class.get_vector_db_instance()
                else:
                    return None
            except Exception as e:
                logger.error(f"Unable to get vector_db instance: {e}")
                return None
