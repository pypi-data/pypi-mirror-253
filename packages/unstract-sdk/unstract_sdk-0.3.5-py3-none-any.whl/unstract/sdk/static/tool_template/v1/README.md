### TODO: Replace the contents of this file with the README for your tool

## Your Tool Name

Description of your tool

### Required environment variables

| Variable           | Description                                       |
| ------------------ | ------------------------------------------------- |
| `PLATFORM_SERVICE_HOST`    | The host in which the platform service is running |
| `PLATFORM_SERVICE_PORT`    | The port in which the service is listening        |
| `PLATFORM_SERVICE_API_KEY` | The API key for the platform                      |

_TODO: Add more variables here if required_

### Testing the tool locally

Setup a virtual environment and install the requirements:

```commandline
python -m venv .venv
```

Once a virtual environment is created or if you already have created one, activate it:

```commandline
source .venv/bin/activate
```

Install the requirements:

> If you want to use the local sdk, make sure you comment out the `unstract-sdk` line in the `requirements.txt` file.

```commandline
pip install -r requirements.txt
```

To use the local development version of the _unstract sdk_ install it from the local repository. Replace the path with
the path to your local repository:

```commandline
pip install ~/path_to_repo/sdks/.
```

Load the environment variables:

Make a copy of the `sample.env` file and name it `.env`. Fill in the required values.
They get loaded with python-dotenv through the SDK.

#### Run SPEC command

```commandline
python main.py --command SPEC
```

#### Run PROPERTIES command

```commandline
python main.py --command PROPERTIES
```

#### Run ICON command

```commandline
python main.py --command ICON
```

#### Run VARIABLES command

```commandline
python main.py --command VARIABLES
```

#### Run RUN command to index a document

#### TODO: Update the example below with the correct parameters

The format of the jsons required for settings and params can be found by running the SPEC command and the PROPERTIES
command respectively. Alternatively if you have access to the code base, it is located in the `config` folder
as `spec.json` and `properties.json`.

```commandline
python main.py \
    --command RUN \
    --params '{
        }' \
    --settings '{
        }' \
    --workflow-id '00000000-0000-0000-0000-000000000000' \
    --log-level DEBUG

```

### Testing the tool from its docker image

To test the tool from its docker image, run the following command:

```commandline
docker run \
    unstract-tool-example:0.1 \
    python main.py \
    --command RUN \
    --params '{
        }' \
    --settings '{
        }' \
    --workflow-id '00000000-0000-0000-0000-000000000000' \
    --log-level DEBUG

```
