import boto3
import pandas as pd
from io import StringIO


class data_handler():
    def __init__(self):
        self.s3 = boto3.client('s3')
        print()


    def read_data(self):      
        # Specify your bucket and file key
        bucket_name = 'emailclassification'
        file_key = 'complaints_processed.csv'

        # Get the object
        obj = self.s3.get_object(Bucket=bucket_name, Key=file_key)

        # Read data into a pandas DataFrame
        df = pd.read_csv(StringIO(obj['Body'].read().decode('utf-8')))

        # Display the DataFrame
        # print(df)
        return df



if __name__ == '__main__':
    dh = data_handler()
    dh.read_data()