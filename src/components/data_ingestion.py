#reading the data
import os #path related work we should use os because In linux kind of machine it will be important
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation


## initialize data ingestion configuratiom
## inside this we will define train and test path
@dataclass
class DataIngestionconfig:
     #here we dont need to write init class inside this because we are not going tp write any finction inside this
     train_data_path:str=os.path.join('artifacts','train.csv')
     test_data_path:str=os.path.join('artifacts','test.csv')
     raw_data_path:str=os.path.join('artifacts','raw.csv')
     
    

#create our data ingestion class
class DataIngestion:
     def __init__(self):
          self.ingestion_config=DataIngestionconfig()
          
     def initiate_data_ingestion(self):
          logging.info("Data Ingestion Methods starts")

          try:
               df=pd.read_csv(os.path.join('notebooks/data','train.csv'))
               logging.info('DataSet read as pandas DataFrame')
               os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
               df.to_csv(self.ingestion_config.raw_data_path,index=False)
               logging.info("We are started doing train test split")
               train_set,test_set=train_test_split(df,test_size=30)

               logging.info("we are storing it into the path we create")
               train_set.to_csv(self.ingestion_config.train_data_path,header=True,index=False)
               test_set.to_csv(self.ingestion_config.test_data_path,header=True,index=False)
               logging.info("Ingestion of data is completed")

               return(
                    self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path
               )

          except Exception as e:
               logging.info("Exception occured at Data Ingestion stage")
               raise CustomException(e,sys)

#To run the data ingestion function

if __name__=='__main__':
     obj=DataIngestion()
     train_data_path,test_data_path=obj.initiate_data_ingestion()
     print(train_data_path,test_data_path)
     data_transformation=DataTransformation()
     train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)
