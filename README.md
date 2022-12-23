
# FlickR Image Tagger

This project uses the Flickr API, Azure Vision API, and OpenAI GPT-3 to fetch the title, tags, and the URL of an 400 pixel wide image version with the Flickr API, generate a description for the image with Azure Vision and OpenAI GPT-3, and optionally sets the title and description with the Flickr API.

## Installation

Install FlickR Image Tagger using pip from the github repo address: https://github.com/clemensv/imagetagger

```
pip install git+https://github.com/clemensv/imagetagger
```

## Usage

To run the FlickR Image Tagger, provide the `photo_id` argument with the ID of the photo on Flickr and the `--api-key`, `--api-secret`, `--azure-key`, `--azure-endpoint`, `--openai-api-key`, and `--gpt3-engine` arguments with the values for the Flickr API, Azure Vision API, and OpenAI GPT-3.

```
imagetagger <photo_id> --api-key <flickr_api_key> --api-secret <flickr_api_secret> --azure-key <azure_api_key> --azure-endpoint <azure_api_endpoint> --openai-api-key <openai_api_key> --gpt3-engine <gpt3_engine>
```

If the `--store` argument is provided, the configuration file will be written and the program will end. The keys are stored in the config file and don't need to be provided in subsequent runs.

```
imagetagger --store --api-key <flickr_api_key> --api-secret <flickr_api_secret> --azure-key <azure_api_key> --azure-endpoint <azure_api_endpoint> --openai-api-key <openai_api_key> --gpt3-engine <gpt3_engine>
```
