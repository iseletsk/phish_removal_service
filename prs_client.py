import requests
import base64
import json

class PhishRemovalServiceClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {'Authorization': f'Bearer {api_key}'}

    def submit_phish_report(self, report_id, phish_url, timestamp, review_type, screenshot=None, match_text=None, match_regex=None, callback_url=None):
        data = {
            "reportId": report_id,
            "phishURL": phish_url,
            "timestamp": timestamp,
            "reviewType": review_type,
            "screenshot": screenshot,
            "matchText": match_text,
            "matchRegex": match_regex,
            "callbackURL": callback_url
        }
        response = requests.post(f'{self.base_url}/submitPhishReport', headers=self.headers, json=data)
        return response.json()

    def check_status(self, report_id):
        params = {"reportId": report_id}
        response = requests.get(f'{self.base_url}/checkStatus', headers=self.headers, params=params)
        return response.json()


# Usage
# client = PhishRemovalServiceClient(api_key="your_api_key")
# print(client.submit_report(report_id="report1234", phish_url="https://example.com", timestamp="2023-05-24T14:30:00Z", review_type="automated"))
# print(client.check_status(report_id="report1234"))

