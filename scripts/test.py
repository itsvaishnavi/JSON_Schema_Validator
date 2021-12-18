"""
This script is for unit testing purpose.
Usage: python -m unittest
"""

import unittest
from jsonschema import validate
from variables import SchemaDefinition #class defined in python file called variables.py
import pandas as pd
import datetime
from main import Validation_And_Monitoring

validation_And_Monitoring = Validation_And_Monitoring() #Create an instance of Validation_And_Monitoring class

# class Test inherited from unittest.TestCase
class Test(unittest.TestCase):
	def test_sample_json_instance(self):
		json_instance = {"id": "FB16866D-AE4D-416F-8848-122B07DA42F5", "received_at": "2018-01-30 18:13:52.221000", "anonymous_id": "0A52CDC6-DDDC-4F7D-AA24-4447F6AF2689",  "context_app_version": "1.2.3",  "context_device_ad_tracking_enabled": True,  "context_device_manufacturer": "Apple",   "context_device_model": "iPhone8,4",  "context_device_type": "android",   "context_locale": "de-DE",  "context_network_wifi": True,  "context_os_name": "android",   "context_timezone": "Europe/Berlin", "event": "submission_success",  "event_text": "submissionSuccess", "original_timestamp": "2018-01-30T19:13:43.383+0100",   "sent_at": "2018-01-30 18:13:51.000000",  "timestamp": "2018-01-30 18:13:43.627000",  "user_id": "18946",  "context_network_carrier": "o2-de",  "context_device_token": '',  "context_traits_taxfix_language": "en-DE"}
		self.assertTrue(validation_And_Monitoring.schemaValidator(json_instance) == False)

if __name__ == '__main__':
	unittest.main()