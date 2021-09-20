# Pythono3 code to rename multiple 
# files in a directory or folder
  
# importing os module
import os
import csv
  
# data rows of csv file 
fields = ['Index', 'Word']
rows = [] 
  
# Function to rename multiple files
def main():
     dirName = "/Users/ryanlazzareschi 1/Desktop/NFTs/Collection Filtered/"
     files = os.listdir(dirName)
     files.sort()
     for _, filename in enumerate(files):
          rows.append([filename[:4], filename[5: -4]])

       
     with open('./../data/wordIndexes.csv', 'w') as f:
          # using csv.writer method from CSV package
          write = csv.writer(f)
          write.writerow(fields)
          write.writerows(rows)
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()


