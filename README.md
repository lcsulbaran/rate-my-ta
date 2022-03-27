# RateMyTA

Repository for SENG 401 Final Project

Project Name: RateMyTA

## Contributors: 
- Adam Abouelhassan
- Brian Chen
- Kenny Jeon
- John McMurtry
- Harrison Mondragon
- Luis Sulbaran
- Jaxson Waterstreet
              
## Instructions to Run Program:

1. Create a new folder on your computer to hold the project contents

2. Within the folder, create a new Python virtual environment using the command line

3. Once the virtual environment has been created and activated, use **'pip install'** to install the following packages:
  **'Django'**, **'pymongo'**, **'pymongo[srv]'**,**'certifi'**, **'fuzzywuzzy'**, **'levenshtein'**
 
4. Once these packages are installed, git clone the repository into the folder

5. After cloning, navigate into the 'src' folder and run the command **'py manage.py migrate'**

To run the program use the command **'py manage.py runserver'** and open http://127.0.0.1:8000/ on your browser

To run the program tests use the command **'py manage.py test'** and the tests will execute within the terminal
