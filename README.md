## CIS3330-CASA6-Reading-a-Plain-File

In this assignment, you are asked to open a file, read its content and search for a keyword to retrieve information. 

* The file you are going to read is a comma separated values file named `'big-mac-full-index.csv'`
* To read the file, use the built-in function `open()` as shown in chapter 7.4 from Severance(2019)
  + The file to open is included in the code repository. I recommend opening the file using the following filename `./big-mac-full-index.csv` (which is included in your casa_6.py)
  + In this CASA assignment, you cannot use CSV, Pandas, or any other external modules to read the document.
* After you read the file, you are asked to traverse through all the lines in the file and print out only the lines that include the word `'USA'`
  + To traverse over the lines in the file, I recommend using a for loop similar to the one shown in the first code snippet in chapter 7.4 from Severance(2019).
  + To search for the keyword, a helpful code statement is `if "word" in line_variable"
  + In your case, you will be looking for the word **'USA'**
  + There is an example of how to search for words in a file in chapter 7.5. However, that example uses the `startswith()` function, which will not be helpful for searching the keyword in the file provided
* Your code should find and print out 37 lines with big-mac information from the USA.
  + I recommend you use a counter variable to verify that your code did find **37 lines** where the word 'USA' appears.
* Your code will not be run against automated testing. However, you need to submit a working program to receive full credit.
## Copyright disclosure

* The file `big-mac-full-index` was obtained from [https://github.com/TheEconomist/big-mac-data] (https://github.com/TheEconomist/big-mac-data). The file is protected under the MIT License [https://github.com/TheEconomist/big-mac-data/blob/master/LICENCE](https://github.com/TheEconomist/big-mac-data/blob/master/LICENCE).