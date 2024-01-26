# Unstract SDK

### Tools

#### Create a  scaffolding for a new tool

Example

```bash
unstract-tool-gen --command NEW --tool-name <name of tool> \
 --location ~/path_to_repository/unstract-tools/ --overwrite false
```

Supported commands:

- `NEW` - Create a new tool


#### Llama Index support

Unstract SDK 0.3.2 uses the following version of Llama 
Index Version **0.9.28** as on January 14th, 2024

#### Environment variables required for all Tools

- `PLATFORM_SERVICE_HOST`
- `PLATFORM_SERVICE_PORT`
- `PLATFORM_SERVICE_API_KEY`

#### Environment variables required for various LLMs

- Azure OpenAI
    - `OPENAI_API_KEY`
    - `OPENAI_API_BASE`
    - `OPENAI_API_VERSION`
    - `OPENAI_API_ENGINE`
    - `OPENAI_API_MODEL`
