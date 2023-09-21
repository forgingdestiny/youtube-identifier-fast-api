# YouTube URL Identifier FastAPI App

## Overview

This is a FastAPI application that identifies the type of YouTube URL provided. It returns a JSON response containing the type, description, and other meta information about the URL.

## App Structure

youtube-identifier-fast-api/
|-- app.py
|-- patterns.json
|-- requirements.txt
|-- README.md

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/forgingdestiny/youtube-identifier-fast-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd youtube-identifier-fast-api
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Running the App

Run the FastAPI application using Uvicorn:

```bash
uvicorn app:app --reload
```

The application will be available at <http://127.0.0.1:8000>.

## API Endpoint

`POST`` /identify/: Takes a JSON payload with a url field and returns a JSON response identifying the type of YouTube URL.

Example Request

```json
{
  "url": "https://www.youtube.com/watch?v=example"
}
```

## License

MIT License. See LICENSE for more information.
