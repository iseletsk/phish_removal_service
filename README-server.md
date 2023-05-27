# Phish Removal Service - Server Implementation

This FastAPI application implements the Phish Removal Service API. 

## Setup

This application uses SQLite as a database and SQLAlchemy as an ORM. Ensure you have these installed. You also need to create a database file named `phish.db`.

## Database Setup

The database setup code can be found in `database.py`. Run this file to create the necessary tables in the SQLite database.

## Running the Server

To run the server, use the following command:

```
uvicorn main:app --reload
```

Replace `main` with the filename of your FastAPI application if it's different.

## API Endpoints

The application has the following endpoints:

### 1. `/submitPhishReport` (POST)

This endpoint accepts a phishing report. The data should be provided as a JSON object in the request body. The `Authorization` header should contain the API key for the organization.

### 2. `/checkStatus` (GET)

This endpoint checks the status of a phishing report. The `reportId` should be provided as a query parameter, and the `Authorization` header should contain the API key for the organization.

### 3. `/unprocessedReports` (GET)

This endpoint returns all unprocessed phishing reports. It is intended for internal use and does not require the `Authorization` header.

### 4. `/updateReport/{reportId}` (PATCH)

This endpoint updates the status of a phishing report. The `status` and `processor` should be provided as JSON in the request body. It is intended for internal use and does not require the `Authorization` header.

## Notes

For simplicity, this application uses the `Authorization` header value as the organization ID. In a real-world application, you would want to validate the API key provided in the `Authorization` header and map it to an organization.

The models for the SQLAlchemy ORM can be found in `models.py`. Please ensure that this file is present in your application's directory. 

The status of a report can have the following values: `new`, `processed`, `not_applicable`, `not_found`.

The processing timestamp (`processingTimestamp`) is generated by the server at the time of the status change.