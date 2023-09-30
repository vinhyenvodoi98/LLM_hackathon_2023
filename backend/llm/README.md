# SETUP

## Environment
1. Recommended to use Python3
2. Run the command below in this folder
`pip install -r requirements.txt`

## API 
1. Create a .env file 
2. Put your API key in the created file in this format
    ```
    ACTIVELOOP_TOKEN=""
    GOOGLE_API_KEY=""
    ```
*Note*: The Activeloop token is for the DeepLake VectorStore API, which we might not need.

## Installation Completion Test
Run the `test.py` file to see if the setup is completed
```
python3 test.py
```
