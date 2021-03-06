"""
This script is for unit testing purpose.
Usage: python -m unittest
"""

import unittest
from jsonschema import validate
from variables import SchemaDefinition #class defined in python file called variables.py
import datetime
from main import Validation_And_Monitoring

validation_And_Monitoring = Validation_And_Monitoring() #Create an instance of Validation_And_Monitoring class

# class Test inherited from unittest.TestCase
class Test(unittest.TestCase):
	def test_sample_json_instance(self):
		json_instance = {"id": "FB16866D-AE4D-416F-8848-122B07DA42F5", "received_at": "2018-01-30 18:13:52.221000", "anonymous_id": "0A52CDC6-DDDC-4F7D-AA24-4447F6AF2689",  "context_app_version": "1.2.3",  "context_device_ad_tracking_enabled": True,  "context_device_manufacturer": "Apple",   "context_device_model": "iPhone8,4",  "context_device_type": "android",   "context_locale": "de-DE",  "context_network_wifi": True,  "context_os_name": "android",   "context_timezone": "Europe/Berlin", "Event": "submission_success",  "Event_text": "submissionSuccess", "original_Date": "2018-01-30T19:13:43.383+0100",   "sent_at": "2018-01-30 18:13:51.000000",  "Date": "2018-01-30 18:13:43.627000",  "user_id": "18946",  "context_network_carrier": "o2-de",  "context_device_token": '',  "context_traits_taxfix_language": "en-DE"}
		# Test schemaValidator() method
		self.assertTrue(validation_And_Monitoring.schemaValidator(json_instance) == False)

		validation_And_Monitoring.log.append(json_instance)

		# Test if log is written using write_log_file() method
		validation_And_Monitoring.write_log_file('test')

	def test_read_json_file_function(self):
		# Test read_json_file() method
		validation_And_Monitoring.read_json_file('C:/Users/HP/Desktop/TaxfixAssignment/scripts/test_1.json')

	def test_event_count(self):
		json_data = [
			{'Date':'2018-01-30 18:13:43.627000','Event':'registration_Success'},
			{'Date':'2018-01-26 18:13:43.627000','Event':'registration_Success'},
			{'Date':'2019-01-30 18:13:43.627000','Event':'registration_Initiated'},
			{'Date':'2020-01-30 18:13:43.627000','Event':'registration_Failed'},
			{'Date':'2021-01-30 18:13:43.627000','Event':'registration_Initiated'},
			{'Date':'2018-01-30 18:13:43.627000','Event':'registration_Success'}
		]
		validation_And_Monitoring.df=validation_And_Monitoring.df.append(json_data, ignore_index=True, sort=False)
		print(validation_And_Monitoring.df)

		expected_out_df = [{'Date': datetime.date(2018, 1, 26), 'Event': 'registration_Success', 'count': 1}, {'Date': datetime.date(2018, 1, 30), 'Event': 'registration_Success', 'count': 2}, {'Date': datetime.date(2019, 1, 30), 'Event': 'registration_Initiated', 'count': 1}, {'Date': datetime.date(2020, 1, 30), 'Event': 'registration_Failed', 'count': 1}, {'Date': datetime.date(2021, 1, 30), 'Event': 'registration_Initiated', 'count': 1}]

		# Test generateReport() method
		out_dict = validation_And_Monitoring.generateReport('test_data')
		
		self.assertTrue(expected_out_df == out_dict)

if __name__ == '__main__':
	unittest.main()