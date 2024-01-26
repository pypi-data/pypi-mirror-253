import json


class StaticCommandsMixin:
    """Mixin class to handle static commands for tools."""

    def _load_json(self, file_to_load: str) -> str:
        """Loads and returns a JSON from a file.

        Args:
            file_to_load (str): Path to the file containing JSON

        Returns:
            str: A compact JSON from the file
        """
        with open(file_to_load) as f:
            loaded_json = json.load(f)
            compact_json = json.dumps(loaded_json, separators=(",", ":"))
            return compact_json

    def spec(self, spec_file: str = "config/spec.json") -> str:
        """Returns the JSON schema of the tool.

        Args:
            spec_file (str): The path to the JSON schema file.
            The default is config/spec.json.
        Returns:
            str: The JSON schema of the tool.
        """
        return self._load_json(spec_file)

    def properties(self, properties_file: str = "config/properties.json") -> str:
        """Returns the properties of the tool.

        Args:
            properties_file (str): The path to the properties file.
            The default is config/properties.json.
        Returns:
            str: The properties of the tool.
        """
        return self._load_json(properties_file)

    def variables(self, variables_file: str = "config/runtime_variables.json") -> str:
        """Returns the JSON schema of the runtime variables.

        Args:
            variables_file (str): The path to the JSON schema file.
            The default is config/runtime_variables.json.
        Returns:
            str: The JSON schema for the runtime variables.
        """

        return self._load_json(variables_file)

    def icon(self, icon_file: str = "config/icon.svg") -> str:
        """Returns the icon of the tool.

        Args:
            icon_file (str): The path to the icon file. The default is config/icon.svg.
        Returns:
            str: The icon of the tool.
        """
        with open(icon_file) as f:
            icon = f.read()
            return icon
