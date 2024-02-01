
# COMMAND TO RUN= python Assignment2.py 'C:\Users\Readchilly_task\Department_data.csv'
#  "C:\Users\Readchilly_task\Destination_folder" 
# Please change path accordingly for csv file and destination folder

import argparse         #for reading input from cmdline
import csv              # Required To Read csv file
import os               


class MakeFolder:               
    
    # method 'generate_path_Dir' to read csv file then generate path and make directory 
    # for all path at location provided as destination path

    def generate_path_Dir(csvfile,destpath):        

        try:
                
            with open(csvfile,'r') as csv_file:
                file=csv.DictReader(csv_file)
                
                # reading file line by line 
                for line in file:
                    #  if field value is empty defalt value field_name(like Department,Username,Project)
                    #  is provided as value 

                    Department=line['Department'] if line['Department'] !="" else "Department" 
                    Username=line['Username']  if line['Username']!="" else "Username"
                    Project=line['Project'] if line['Project'] !="" else 'Project'
                    
                    # making path as well as directory same time for field provided in csv file
                    os.makedirs('{0}\{1}\{2}\{3}'.format(destpath,Department,Username,Project),exist_ok=True)
        
        # Handling error if file is not exits or path is wrong  
            
        except IOError:
            print("  Please Enter Correct CSV file path ")

if __name__=='__main__':

    parser=argparse.ArgumentParser()

    # Adding number of  requried arguments as input
    parser.add_argument('--csv_file',type=str)
    parser.add_argument('--dest_path',type=str)
    args=parser.parse_args()
    
    # crating object of class and calling function 
    makefolder=MakeFolder()
    makefolder.generate_path_Dir(args.csv_file,args.dest_path)


