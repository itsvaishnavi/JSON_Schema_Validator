"""
Usage:
python main.py <filename>

Eg.
python main.py sample_3.json
"""

# Importing the essential libraries
import json
import ijson as ijson
from jsonschema import validate
from variables import SchemaDefinition #class defined in python file called variables.py
import pandas as pd
import datetime
from memory_profiler import profile
import sys
import os

class Validation_And_Monitoring():
	def __init__(self):
		"""
		This constructor initializes the values for schema, log and dataframe with column names Date and Event.
		"""
		self.schema = SchemaDefinition().schema #contains schema for json validation
		self.log = [] #list to record the json item if there is data field error or missing value(empty string)
		self.df = pd.DataFrame(columns=['Date','Event']) #DataFrame
		self.path_parent = os.path.dirname(os.getcwd())
		os.chdir(self.path_parent)
		self.path_parent = os.getcwd()
		self.path_parent = self.path_parent.replace('\\','/')

	@profile
	def read_json_file(self,file:str):
		"""
		This function reads the user json file.
		Parameter(s):
		file: filename
		"""
		with open(file,'rb') as json_file:
			json_data = ijson.items(json_file, 'item')
			for item in json_data:
				# Call schemaValidator to validate item
				bool_val = self.schemaValidator(item)
				try:
					self.df.loc[len(self.df)] = [item['timestamp'],item['event']]
				except:
					pass

	def schemaValidator(self, json_item:dict) -> bool:
		"""
		This function checks if the json_item follows the JSON schema as defined in the 'schema' in variables.py.
		If the error is thrown, json_item is appended to the 'log' variable.
		"""
		try:
			validate(instance=json_item, schema=self.schema)
			return True
		except:
			self.log.append(json_item)
			return False

	@profile
	def write_log_file(self,fileName:str):
		"""
		This function writes self.log to the output json file.
		This file contains the data which is recorded as 'wrong data type' or 'missing data value'.
		"""
		with open(self.path_parent+SchemaDefinition().output_json_log_folder_path+fileName+'_log_file.json','w') as f_output:
			json.dump(self.log,f_output)
	
	@profile	
	def generateReport(self,fileName:str):

		# Since the Date column in dataframe contains the string value, we need to convert it into datetime format.
		self.df['Date'] = [datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S.%f") for d in self.df["Date"]]

		# After converting the Date column into datetime format, we are storing only the date in the 'Date' column.
		self.df['Date'] = [datetime.datetime.date(d) for d in self.df['Date']]

		# To generate the report containing 3 columns: Date, Event, count
		out_dataframe = pd.DataFrame({'count' : self.df.groupby(['Date','Event']).size()}).reset_index()
		
		# print(self.df.groupby(['Date','Event']).size())

		# Converting out_dataframe to csv
		out_dataframe.to_csv(self.path_parent+SchemaDefinition().csv_generated_report_folder_path+fileName+'_Generated_report.csv')

def main():
	if len(sys.argv)==2:
		fileName = sys.argv[1] #Takes the file name from the command line
		f_name = fileName.split('/')[-1].split('.json')[0] #Extract the file name
		validation_And_Monitoring = Validation_And_Monitoring() #Create an instance of Validation_And_Monitoring class
		validation_And_Monitoring.read_json_file(fileName) #Call read_json_file method of the Validation_And_Monitoring class
		validation_And_Monitoring.write_log_file(f_name) #Call write_log_file method of the Validation_And_Monitoring class
		validation_And_Monitoring.generateReport(f_name) #Call generateReport method of the Validation_And_Monitoring class
	else:
		print("Insufficient arguments provided.")

if __name__ == '__main__':
	main()