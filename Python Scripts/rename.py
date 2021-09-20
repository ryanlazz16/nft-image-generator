# Pythono3 code to rename multiple 
# files in a directory or folder
  
# importing os module
import os
  
# Function to rename multiple files
def main():
     dirName = "/Users/ryanlazzareschi 1/Desktop/NFTs/Collection Filtered/"
     files = os.listdir(dirName)
     files.sort()
     for count, filename in enumerate(files, start=0):
          dst = str(count).zfill(4) + filename[4: -4] + ".png"
          src = dirName + filename
          dst = dirName + dst
               
          # rename() function will
          # rename all the files
          os.rename(src, dst)
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()