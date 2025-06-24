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
            
            # #---------------- Dealer Car Search ------------------
            # #----------------------------------------------------- 
            
            #     'IMPORT_INDEX_ID': row.get('IMPORT_INDEX_ID', None),
            #     'IMPORT_INDEX_TYPE': row.get('LeadType', None),
            #     'IMPORT_INDEX_FIRSTNAME': row.get('FirstName', None),
            #     'IMPORT_INDEX_LASTNAME': row.get('LastName', None),
            #     'IMPORT_INDEX_STREET': row.get('LeadAddress', None),
            #     'IMPORT_INDEX_APTNO': row.get('IMPORT_INDEX_APTNO', None),
            #     'IMPORT_INDEX_CITY': row.get('LeadCity', None),
            #     'IMPORT_INDEX_COUNTY': row.get('IMPORT_INDEX_COUNTY', None),
            #     'IMPORT_INDEX_STATE': row.get('LeadState', None),
            #     'IMPORT_INDEX_ZIP': row.get('LeadZip', None),
            #     'IMPORT_INDEX_PHONE_WORK': row.get('WorkPhone', None),
            #     'IMPORT_INDEX_PHONE_CELL': row.get('MobilePhone', None),
            #     'IMPORT_INDEX_PHONE_HOME': row.get('PhoneNumber', None),
            #     'IMPORT_INDEX_EMAIL': row.get('EmailAddress', None),
            #     'IMPORT_INDEX_ADD_AGENT': row.get('IMPORT_INDEX_ADD_AGENT', None),
            #     'IMPORT_INDEX_ADD_DATE': f"{currDate}", 
            #     #'IMPORT_INDEX_ADD_DATE': row.get('Date', None),
            #     'IMPORT_INDEX_LAST_AGENT': row.get('IMPORT_INDEX_LAST_AGENT', None),
            #     'IMPORT_INDEX_LAST_TOUCHED': f"{currDate}", #"2024-10-01 00:00:00", 
            #     #'IMPORT_INDEX_LAST_TOUCHED': row.get('Date', None),
            #     'IMPORT_INDEX_DL': row.get('IMPORT_INDEX_DL', None),
            #     'IMPORT_INDEX_DOB': row.get('IMPORT_INDEX_DOB', None),
            #     'IMPORT_INDEX_COMMENTS': row.get('IMPORT_INDEX_COMMENTS', None),
            #     'IMPORT_INDEX_SOURCE': "Web Lead" 
            #     #'IMPORT_INDEX_SOURCE': row.get('Lead Source', None),
            #      IMPORT_INDEX_STATUS': row.get('leadStatus', None)

            # #---------------- Dealer Car Search ------------------
            # #----------------------------------------------------- 
            
            # #---------------- ASN  ------------------
            # #----------------------------------------------------- 

                # 'IMPORT_INDEX_ID': row.get('IMPORT_INDEX_ID', None),
                # 'IMPORT_INDEX_TYPE': row.get('IMPORT_INDEX_TYPE', None),
                # 'IMPORT_INDEX_FIRSTNAME': row.get('Firstname', None),
                # 'IMPORT_INDEX_LASTNAME': row.get('Lastname', None),
                # 'IMPORT_INDEX_STREET': row.get('Address', None),
                # 'IMPORT_INDEX_APTNO': row.get('IMPORT_INDEX_APTNO', None),
                # 'IMPORT_INDEX_CITY': row.get('City', None),
                # 'IMPORT_INDEX_COUNTY': row.get('IMPORT_INDEX_COUNTY', None),
                # 'IMPORT_INDEX_STATE': row.get('State', None),
                # 'IMPORT_INDEX_ZIP': row.get('Zip', None),
                # 'IMPORT_INDEX_PHONE_WORK': row.get('IMPORT_INDEX_PHONE_WORK', None),
                # 'IMPORT_INDEX_PHONE_CELL': row.get('MobilePhone', None),
                # 'IMPORT_INDEX_PHONE_HOME': row.get('HomePhone', None),
                # 'IMPORT_INDEX_EMAIL': row.get('Email', None),
                # 'IMPORT_INDEX_ADD_AGENT': row.get('IMPORT_INDEX_ADD_AGENT', "AZIELROQUE5@GMAIL.COM"),
                # #'IMPORT_INDEX_ADD_DATE': f"{currDate}", 
                # 'IMPORT_INDEX_ADD_DATE': row.get('inDate', None),
                # 'IMPORT_INDEX_LAST_AGENT': row.get('IMPORT_INDEX_LAST_AGENT', "AZIELROQUE5@GMAIL.COM"),
                # 'IMPORT_INDEX_LAST_TOUCHED': f"{currDate}", #"2024-10-01 00:00:00", 
                # #'IMPORT_INDEX_LAST_TOUCHED': row.get('inDate', None),
                # 'IMPORT_INDEX_DL': row.get('DriversLicNo', None),
                # 'IMPORT_INDEX_DOB': row.get('DOB', None),
                # 'IMPORT_INDEX_COMMENTS': row.get('IMPORT_INDEX_COMMENTS', None),
                # #'IMPORT_INDEX_SOURCE': "Web Lead" 
                # 'IMPORT_INDEX_SOURCE': row.get('Source', None),
                # 'IMPORT_INDEX_STATUS': row.get('leadStatus', "ACTIVE")
            
            # #---------------- ASN ------------------
            # #----------------------------------------------------- 
            
            # #---------------- Selly Automotive ------------------
            # #----------------------------------------------------- 
            
            #     'IMPORT_INDEX_ID': row.get('IMPORT_INDEX_ID', None),
            #     'IMPORT_INDEX_TYPE': row.get('IMPORT_INDEX_TYPE', None),
            #     'IMPORT_INDEX_FIRSTNAME': row.get('FirstName', None),
            #     'IMPORT_INDEX_LASTNAME': row.get('LastName', None),
            #     'IMPORT_INDEX_STREET': row.get('Address', None),
            #     'IMPORT_INDEX_APTNO': row.get('IMPORT_INDEX_APTNO', None),
            #     'IMPORT_INDEX_CITY': row.get('City', None),
            #     'IMPORT_INDEX_COUNTY': row.get('IMPORT_INDEX_COUNTY', None),
            #     'IMPORT_INDEX_STATE': row.get('State', None),
            #     'IMPORT_INDEX_ZIP': row.get('ZipCode', None),
            #     'IMPORT_INDEX_PHONE_WORK': row.get('WorkPhone', None),
            #     'IMPORT_INDEX_PHONE_CELL': row.get('CellPhone', None),
            #     'IMPORT_INDEX_PHONE_HOME': row.get('HomePhone', None),
            #     'IMPORT_INDEX_EMAIL': row.get('Email', None),
            #     'IMPORT_INDEX_ADD_AGENT': (row.get('Salesperson', None) or "").upper(),
            #     #'IMPORT_INDEX_ADD_DATE': f"{currDate}", 
            #     'IMPORT_INDEX_ADD_DATE': row.get('CreatedOn', None),
            #     'IMPORT_INDEX_LAST_AGENT': (row.get('Salesperson', None) or "").upper(),
            #     #'IMPORT_INDEX_LAST_TOUCHED': "2024-12-03 00:00:00", #f"{currDate}", 
            #     'IMPORT_INDEX_LAST_TOUCHED': row.get('CreatedOn', None),
            #     'IMPORT_INDEX_DL': row.get('LicenseNo', None),
            #     'IMPORT_INDEX_DOB': row.get('BirthDate', None),
            #     'IMPORT_INDEX_COMMENTS': row.get('IMPORT_INDEX_COMMENTS', None),
            #     #'IMPORT_INDEX_SOURCE': "Web Lead" 
            #     'IMPORT_INDEX_SOURCE': row.get('MarketingSource', None),
            #      IMPORT_INDEX_STATUS': row.get('leadStatus', None)
            
            # #---------------- Selly Automotive ------------------
            # #-----------------------------------------------------
            
            #---------------- Vin Solution ------------------
            #----------------------------------------------------- 
            
                # 'IMPORT_INDEX_ID': row.get('IMPORT_INDEX_ID', None),
                # 'IMPORT_INDEX_TYPE': row.get('IMPORT_INDEX_TYPE', None),
                # 'IMPORT_INDEX_FIRSTNAME': unidecode(row.get('firstname', None)),
                # 'IMPORT_INDEX_LASTNAME': unidecode(row.get('lastname', None)),
                # 'IMPORT_INDEX_STREET': row.get('address', None),
                # 'IMPORT_INDEX_APTNO': row.get('IMPORT_INDEX_APTNO', None),
                # 'IMPORT_INDEX_CITY': row.get('city', None),
                # 'IMPORT_INDEX_COUNTY': row.get('IMPORT_INDEX_COUNTY', None),
                # 'IMPORT_INDEX_STATE': row.get('state', None),
                # 'IMPORT_INDEX_ZIP': row.get('postalcode', None),
                # 'IMPORT_INDEX_PHONE_WORK': row.get('IMPORT_INDEX_PHONE_WORK', None),
                # 'IMPORT_INDEX_PHONE_CELL': row.get('cellphone', None),
                # 'IMPORT_INDEX_PHONE_HOME': row.get('cellphone', None),
                # 'IMPORT_INDEX_EMAIL': row.get('email', None),
                # 'IMPORT_INDEX_ADD_AGENT': row.get('IMPORT_INDEX_ADD_AGENT', None),
                # #'IMPORT_INDEX_ADD_DATE': f"{currDate}", 
                # 'IMPORT_INDEX_ADD_DATE': row.get('LeadCreatedUTC', None),
                # 'IMPORT_INDEX_LAST_AGENT': row.get('IMPORT_INDEX_LAST_AGENT', None),
                # #'IMPORT_INDEX_LAST_TOUCHED': f"{currDate}", #"2024-10-01 00:00:00", 
                # 'IMPORT_INDEX_LAST_TOUCHED': row.get('LeadCreatedUTC', None),
                # 'IMPORT_INDEX_DL': row.get('IMPORT_INDEX_DL', None),
                # 'IMPORT_INDEX_DOB': row.get('IMPORT_INDEX_DOB', None),
                # 'IMPORT_INDEX_COMMENTS': row.get('IMPORT_INDEX_COMMENTS', None),
                # #'IMPORT_INDEX_SOURCE': "Web Lead" 
                # 'IMPORT_INDEX_SOURCE': row.get('leadsourcename', None),
                # 'IMPORT_INDEX_STATUS': row.get('leadstatustypename', "ACTIVE")

            #---------------- Vin Solution ------------------
            #-----------------------------------------------------  
            
            # ---------------- CarGurus ------------------
            # ----------------------------------------------------- 
            
                # 'IMPORT_INDEX_ID': row.get('IMPORT_INDEX_ID', None),
                # 'IMPORT_INDEX_TYPE': row.get('IMPORT_INDEX_TYPE', None),
                # 'IMPORT_INDEX_FIRSTNAME': row.get('Name', None) if row.get('Name') != "" else "NONAME",
                # 'IMPORT_INDEX_LASTNAME': row.get('IMPORT_INDEX_LASTNAME', None),
                # 'IMPORT_INDEX_STREET': row.get('IMPORT_INDEX_STREET', None),
                # 'IMPORT_INDEX_APTNO': row.get('IMPORT_INDEX_APTNO', None),
                # 'IMPORT_INDEX_CITY': row.get('IMPORT_INDEX_CITY', None),
                # 'IMPORT_INDEX_COUNTY': row.get('IMPORT_INDEX_COUNTY', None),
                # 'IMPORT_INDEX_STATE': row.get('IMPORT_INDEX_STATE', None),
                # 'IMPORT_INDEX_ZIP': row.get('IMPORT_INDEX_ZIP', None),
                # 'IMPORT_INDEX_PHONE_WORK': row.get('IMPORT_INDEX_PHONE_WORK', None),
                # 'IMPORT_INDEX_PHONE_CELL': row.get('Phone', None),
                # 'IMPORT_INDEX_PHONE_HOME': row.get('Phone', None),
                # 'IMPORT_INDEX_EMAIL': row.get('Email', None),
                # 'IMPORT_INDEX_ADD_AGENT': row.get('IMPORT_INDEX_ADD_AGENT', None),
                # #'IMPORT_INDEX_ADD_DATE': f"{currDate}", 
                # 'IMPORT_INDEX_ADD_DATE': row.get('Date', None),
                # 'IMPORT_INDEX_LAST_AGENT': row.get('IMPORT_INDEX_LAST_AGENT', None),
                # #'IMPORT_INDEX_LAST_TOUCHED': f"{currDate}", #"2024-10-01 00:00:00", 
                # 'IMPORT_INDEX_LAST_TOUCHED': row.get('Date', None),
                # 'IMPORT_INDEX_DL': row.get('IMPORT_INDEX_DL', None),
                # 'IMPORT_INDEX_DOB': row.get('IMPORT_INDEX_DOB', None),
                # 'IMPORT_INDEX_COMMENTS': row.get('IMPORT_INDEX_COMMENTS', None),
                # #'IMPORT_INDEX_SOURCE': "Web Lead" 
                # 'IMPORT_INDEX_SOURCE': row.get('Lead Source', None),
                # 'IMPORT_INDEX_STATUS': row.get('IMPORT_INDEX_STATUS', "ACTIVE")

            # ---------------- CarGurus ------------------
            # -----------------------------------------------------  
            
            #---------------- Cars For Sale ------------------
            #----------------------------------------------------- 
            
                # 'IMPORT_INDEX_ID': row.get('IMPORT_INDEX_ID', None),
                # 'IMPORT_INDEX_TYPE': row.get('IMPORT_INDEX_TYPE', None),
                # 'IMPORT_INDEX_FIRSTNAME': (row.get('First Name', None)) if row.get('First Name') != "" else "NONAME",
                # 'IMPORT_INDEX_LASTNAME': (row.get('Last Name',None)),
                # 'IMPORT_INDEX_STREET': row.get('IMPORT_INDEX_STREET', None),
                # 'IMPORT_INDEX_APTNO': row.get('IMPORT_INDEX_APTNO', None),
                # 'IMPORT_INDEX_CITY': row.get('IMPORT_INDEX_CITY', None),
                # 'IMPORT_INDEX_COUNTY': row.get('IMPORT_INDEX_COUNTY', None),
                # 'IMPORT_INDEX_STATE': row.get('State', None),
                # 'IMPORT_INDEX_ZIP': row.get('IMPORT_INDEX_ZIP', None),
                # 'IMPORT_INDEX_PHONE_WORK': row.get('IMPORT_INDEX_PHONE_WORK', None),
                # 'IMPORT_INDEX_PHONE_CELL': row.get('Phone Number', None),
                # 'IMPORT_INDEX_PHONE_HOME': row.get('IMPORT_INDEX_PHONE_HOME', None),
                # 'IMPORT_INDEX_EMAIL': row.get('Email', None),
                # 'IMPORT_INDEX_ADD_AGENT': row.get('IMPORT_INDEX_ADD_AGENT', None),
                # #'IMPORT_INDEX_ADD_DATE': f"{currDate}", 
                # 'IMPORT_INDEX_ADD_DATE': row.get('Submission Date', None),
                # 'IMPORT_INDEX_LAST_AGENT': row.get('Assigned To', None),
                # #'IMPORT_INDEX_LAST_TOUCHED': f"{currDate}", #"2024-10-01 00:00:00", 
                # 'IMPORT_INDEX_LAST_TOUCHED': row.get('Submission Date', None),
                # 'IMPORT_INDEX_DL': row.get('IMPORT_INDEX_DL', None),
                # 'IMPORT_INDEX_DOB': row.get('IMPORT_INDEX_DOB', None),
                # 'IMPORT_INDEX_COMMENTS': row.get('IMPORT_INDEX_COMMENTS', None),
                # #'IMPORT_INDEX_SOURCE': "Web Lead" 
                # 'IMPORT_INDEX_SOURCE': row.get('Submission Type Name', None),
                # 'IMPORT_INDEX_STATUS': row.get('IMPORT_INDEX_STATUS', "ACTIVE")

            #---------------- Cars For Sale ------------------
            #-----------------------------------------------------  
            
            # #---------------- Dominion DMS ------------------
            # #----------------------------------------------------- 
            
            #     'IMPORT_INDEX_ID': row.get('IMPORT_INDEX_ID', None),
            #     'IMPORT_INDEX_TYPE': row.get('IMPORT_INDEX_TYPE', None),
            #     'IMPORT_INDEX_FIRSTNAME': unidecode(row.get('CustomerFirstName', None)),
            #     'IMPORT_INDEX_LASTNAME': unidecode(row.get('CustomerLastName', None)),
            #     'IMPORT_INDEX_STREET': row.get('Address', None),
            #     'IMPORT_INDEX_APTNO': row.get('IMPORT_INDEX_APTNO', None),
            #     'IMPORT_INDEX_CITY': row.get('City', None),
            #     'IMPORT_INDEX_COUNTY': row.get('IMPORT_INDEX_COUNTY', None),
            #     'IMPORT_INDEX_STATE': row.get('StateorProvince', None),
            #     'IMPORT_INDEX_ZIP': row.get('PostalCode', None),
            #     'IMPORT_INDEX_PHONE_WORK': row.get('IMPORT_INDEX_PHONE_WORK', None),
            #     'IMPORT_INDEX_PHONE_CELL': row.get('DayPhone', None),
            #     'IMPORT_INDEX_PHONE_HOME': row.get('EveningPhone', None),
            #     'IMPORT_INDEX_EMAIL': row.get('EmailAddress', None),
            #     'IMPORT_INDEX_ADD_AGENT': row.get('IMPORT_INDEX_ADD_AGENT', None),
            #     #'IMPORT_INDEX_ADD_DATE': f"{currDate}", 
            #     'IMPORT_INDEX_ADD_DATE': row.get('TimeStamp', None),
            #     'IMPORT_INDEX_LAST_AGENT': row.get('Salesperson', None),
            #     #'IMPORT_INDEX_LAST_TOUCHED': f"{currDate}", #"2024-10-01 00:00:00", 
            #     'IMPORT_INDEX_LAST_TOUCHED': row.get('ModifiedDate', None),
            #     'IMPORT_INDEX_DL': row.get('IMPORT_INDEX_DL', None),
            #     'IMPORT_INDEX_DOB': row.get('IMPORT_INDEX_DOB', None),
            #     'IMPORT_INDEX_COMMENTS': row.get('IMPORT_INDEX_COMMENTS', None),
            #     #'IMPORT_INDEX_SOURCE': "Web Lead" 
            #     'IMPORT_INDEX_SOURCE': row.get('Source', None),
            #     'IMPORT_INDEX_STATUS': row.get('IMPORT_INDEX_STATUS', "ACTIVE")

            # #---------------- Dominion DMS ------------------
            # #-----------------------------------------------------  
            
            #---------------- Manual ------------------
            #----------------------------------------------------- 
            
                'IMPORT_INDEX_ID': row.get('IMPORT_INDEX_ID', None),
                'IMPORT_INDEX_TYPE': row.get('LeadType', None),
                'IMPORT_INDEX_FIRSTNAME': unidecode(row.get('FirstName', None)),
                'IMPORT_INDEX_LASTNAME': unidecode(row.get('LastName', None)),
                'IMPORT_INDEX_STREET': row.get('LeadAddress', None),
                'IMPORT_INDEX_APTNO': row.get('IMPORT_INDEX_APTNO', None),
                'IMPORT_INDEX_CITY': row.get('LeadCity', None),
                'IMPORT_INDEX_COUNTY': row.get('IMPORT_INDEX_COUNTY', None),
                'IMPORT_INDEX_STATE': row.get('LeadState', None),
                'IMPORT_INDEX_ZIP': row.get('LeadZip', None),
                'IMPORT_INDEX_PHONE_WORK': row.get('WorkPhone', None),
                'IMPORT_INDEX_PHONE_CELL': row.get('PhoneNumber', None),
                'IMPORT_INDEX_PHONE_HOME': row.get('IMPORT_INDEX_PHONE_HOME', None),
                'IMPORT_INDEX_EMAIL': row.get('EmailAddress', None),
                'IMPORT_INDEX_ADD_AGENT': row.get('IMPORT_INDEX_ADD_AGENT', None),
                #'IMPORT_INDEX_ADD_DATE': f"{currDate}", 
                'IMPORT_INDEX_ADD_DATE': row.get('CreateDate') if row.get('CreateDate') != "" else currDate,
                'IMPORT_INDEX_LAST_AGENT': row.get('Assigned To', None),
                #'IMPORT_INDEX_LAST_TOUCHED': f"{currDate}", #"2024-10-01 00:00:00", 
                'IMPORT_INDEX_LAST_TOUCHED': row.get('LastModifiedDate', None) if row.get('LastModifiedDate') != "" else currDate,
                'IMPORT_INDEX_DL': row.get('IMPORT_INDEX_DL', None),
                'IMPORT_INDEX_DOB': row.get('IMPORT_INDEX_DOB', None),
                'IMPORT_INDEX_COMMENTS': row.get('IMPORT_INDEX_COMMENTS', None),
                #'IMPORT_INDEX_SOURCE': "Web Lead" 
                'IMPORT_INDEX_SOURCE': row.get('IMPORT_INDEX_SOURCE', "Imported Lead"),
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
