# Phish Removal Service Client Library

This is a Python client library for interacting with the Phish Removal Service API. 

## Installation

No special installation is required as this is a single Python class that you can import into your project.

## Usage

First, import the `PhishRemovalServiceClient` class from its location in your project. Then, create an instance of the client using your API base URL and the API key provided by the Phish Removal Service. 

```python
from prs_client import PhishRemovalServiceClient

client = PhishRemovalServiceClient('http://api.your-service.com', 'your_api_key')
```

The Phish Removal Service client currently supports two operations:

### Submit Phishing Report

To submit a phishing report, use the `submit_phish_report` method. This method accepts the following parameters:

- `reportId` (string): A unique identifier for the report.
- `phishURL` (string): The URL of the phishing website.
- `timestamp` (string, ISO 8601 datetime format): The timestamp of when the phish was detected.
- `reviewType` (string): The type of the review done on the page. Possible values are `human` and `automated`.
- `screenshot` (string, Base64 encoded PNG image, optional): A screenshot of the phishing website.
- `matchText` (string, optional): Text that matches part of the content on the page.
- `matchRegex` (string, optional): Regex that would match part of the content on the page.
- `callbackURL` (string, optional): A URL that the service will call back when the phish report has been processed.

Here is an example:

```python
response = client.submit_phish_report(
    "report1", 
    "http://phishy.com", 
    "2023-01-01T00:00:00Z", 
    "human", 
    None, 
    "Phishy text", 
    None, 
    "http://callback.com"
)
```

### Check Status

To check the status of a previously submitted report, use the `check_status` method. This method accepts the following parameter:

- `reportId` (string): The unique identifier of the report.

Here is an example:

```python
status = client.check_status("report1")
```

These methods will return a Python dictionary with the response from the Phish Removal Service API.

Remember to replace `'http://api.your-service.com'` and `'your_api_key'` with your actual base URL and API key.