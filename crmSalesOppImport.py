import csv
import json
import string
import os
from datetime import datetime
import time
import math
import pandas as pd
import ast
from unidecode import unidecode
from dotenv import load_dotenv

def read_and_pair_data(csv_file_path):
    """
    Reads a CSV file and pairs data into a list of dictionaries based on specified columns.

    Parameters:
    - csv_file_path: str, path to the CSV file.

    Returns:
    - list of dictionaries, where each dictionary contains specified data fields.
    """
    paired_data = []

    # Open the CSV file and read data
    # with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    with open(csv_file_path, mode='r', newline='', encoding='latin1') as file:
        
        currDate = datetime.today()
        currDate = currDate.strftime("%Y-%m-%d %H:%M:%S")
        print(currDate)
        reader = csv.DictReader(file)
        
        # Check if required columns are in the CSV
        # required_columns = {'inDate'}
        # if not required_columns.issubset(reader.fieldnames):
        #     raise ValueError("CSV does not contain all required columns.")

        # Create a list of dictionaries for each row
        count = 2
        
        for row in reader:
            
            record = {
            # Create a dictionary for the specific fields
            # print(row)
            
            #---------------- Manual ------------------
            #----------------------------------------------------- 
            
                'IMPORT_INDEX_ID': row.get('IMPORT_INDEX_ID', None),
                'IMPORT_INDEX_TYPE': row.get('IMPORT_INDEX_TYPE', None),
                'IMPORT_INDEX_FIRSTNAME': unidecode(row.get('IMPORT_INDEX_FIRSTNAME', None)),
                'IMPORT_INDEX_LASTNAME': unidecode(row.get('IMPORT_INDEX_LASTNAME', None)),
                'IMPORT_INDEX_STREET': row.get('IMPORT_INDEX_STREET', None),
                'IMPORT_INDEX_APTNO': row.get('IMPORT_INDEX_APTNO', None),
                'IMPORT_INDEX_CITY': row.get('IMPORT_INDEX_CITY', None),
                'IMPORT_INDEX_COUNTY': row.get('IMPORT_INDEX_COUNTY', None),
                'IMPORT_INDEX_STATE': row.get('IMPORT_INDEX_STATE', None),
                'IMPORT_INDEX_ZIP': row.get('IMPORT_INDEX_ZIP', None),
                'IMPORT_INDEX_PHONE_WORK': row.get('IMPORT_INDEX_PHONE_WORK', None),
                'IMPORT_INDEX_PHONE_CELL': row.get('IMPORT_INDEX_PHONE_CELL', None),
                'IMPORT_INDEX_PHONE_HOME': row.get('IMPORT_INDEX_PHONE_HOME', None),
                'IMPORT_INDEX_EMAIL': row.get('IMPORT_INDEX_EMAIL', None),
                'IMPORT_INDEX_ADD_AGENT': row.get('IMPORT_INDEX_ADD_AGENT', None),
                'IMPORT_INDEX_ADD_DATE': row.get('IMPORT_INDEX_ADD_DATE') if row.get('IMPORT_INDEX_ADD_DATE') != "" else currDate,
                'IMPORT_INDEX_LAST_AGENT': row.get('IMPORT_INDEX_LAST_AGENT', None),
                'IMPORT_INDEX_LAST_TOUCHED': row.get('IMPORT_INDEX_LAST_TOUCHED', None) if row.get('IMPORT_INDEX_LAST_TOUCHED') != "" else currDate,
                'IMPORT_INDEX_DL': row.get('IMPORT_INDEX_DL', None),
                'IMPORT_INDEX_DOB': row.get('IMPORT_INDEX_DOB', None),
                'IMPORT_INDEX_COMMENTS': row.get('IMPORT_INDEX_COMMENTS', None),
                'IMPORT_INDEX_SOURCE': row.get('IMPORT_INDEX_SOURCE', None) if row.get('IMPORT_INDEX_SOURCE') != "" else "Imported Lead",
                'IMPORT_INDEX_STATUS': row.get('IMPORT_INDEX_STATUS', "ACTIVE")

            #---------------- Manual ------------------
            #-----------------------------------------------------  
            
            
            
            
            
            # print(count)
            # count= count + 1
            }
            paired_data.append(record)
            # print(row)

    return paired_data

def save_to_csv(data, output_csv_path, dealerName):
    """
    Saves a list of dictionaries to a CSV file.

    Parameters:
    - data: list of dictionaries to save.
    - output_csv_path: str, path to the output CSV file.
    """
    chunkSize = 5000
    numRows = len(data)
    print(f"This DataSet has {numRows} records.")
    splitCount = math.ceil((numRows / chunkSize))
    print(f"This DataSet will be split {splitCount} times.")
    load_dotenv()
    template_file_path = os.getenv("OUTPUT_FILE_PATH")  # Specify the path to your output CSV file
    output_file_path = template_file_path.format(dealerName=dealerName)
    
    for i in range (splitCount):
        startIndex = i*chunkSize
        endIndex = min(startIndex+chunkSize, len(data))
        newData = data[startIndex:endIndex]
        
        newOutPutFile = f'{output_file_path}{output_csv_path}_{i}.csv'
        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(newData)
    
        # Write the DataFrame to a CSV file
        df.to_csv(newOutPutFile, index=False)
        print(f"Data successfully saved to {newOutPutFile}")


dealerName = os.getenv("DEALER_NAME")
# Example usage
load_dotenv()
file_name = os.getenv("FILE_NAME")
file_path_template = os.getenv("FILE_PATH") # Specify the path to your input CSV file
csv_file_path = file_path_template.format(dealerName=dealerName, fileName=file_name)
output_csv_path = f'{dealerName}_output_file'  # Specify the path to your output CSV file

try:
    data = read_and_pair_data(csv_file_path)
    #print(data)
    save_to_csv(data, output_csv_path, dealerName)
    #print(f"Data successfully saved to {output_csv_path}")
except Exception as e:
    print("An error occurred:", e)
