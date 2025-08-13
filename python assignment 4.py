#Task 1
try:
   with open("my_file.txt","r")as file1:
        print("Reading file contain:")
        for line in file1:
         print(line .strip())
except FileNotFoundError:
    print("Error: The File 'my_file.txt ' was not found")

#Task 2
user_input = input("Enter text to write to the file:")
try:
    with open("output.txt","a") as file:
     file.write(user_input)
     print ("Data written successfully to output.txt")
except IDError:
    print("Error:Could not write to the file")

append=input("Enter additional text to append:")
try:
    with open("output.txt","w") as file:
     file.write("\n" +append)
     print("data successfully appended")
except IDError:
     print("Error could not append to the file:")
try:
    with open("output.txt","r") as file:
     print("\nfinal content of output.txt:")
     print(file.read())
except FileNotFoundError:
    print("File 'output.txt not found")
except IDError :
    print("Error : could not read the file")