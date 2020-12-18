import yaml
from collections import defaultdict
#Note this code only works with YAML files where the top section(first 7 lines) of the output YAML file from hydra are manually removed

#The section below is my current attempt at using tokens to skip over these first 7 lines in YAML so my code can run
#The code will not currently run if this is not commented out

with tokenize.open('t1.yaml') as f:
    tokens = tokenize.generate_tokens(f.readline)
    for toknum,tokval, = in tokens:
        if toknum != tokenize.COMMENT:
                print(toknum,tokval)
        
    





#Here is the code that runs well when the first 7 lines are not included

with open('t1.yaml') as file:
    my_file = yaml.load(file, Loader = yaml.FullLoader)
    #variables used to store the urls based off of error message
    #can add/delete different errors based off of what we are looking for 
    errors404 = []
    errors400 = []
    errors302 = []
    other_errors=[]

    #iterates through the entire yaml file
    for index in range(len(my_file)):

        #adds the urls to different lists based off the error code
        if((my_file[index]['code']) == 404):
            errors404.append(my_file[index]['url'])
        elif((my_file[index]['code'] == 400)):
            errors400.append(my_file[index]['url'])
        elif((my_file[index]['code'] == 302)):
            errors302.append(my_file[index]['url'])
        else:
            other_errors.append(my_file[index]['url'] + "\nReason: " + my_file[index]['error'])
            
        

    #output for our interpreter
    print("The following links no longer exist: \n")
    for i in errors404:
        print(i)
    print("\n")
    print("The following links redirect because the url needs to include https:")
    for i in errors400:
        print(i)
    print("\n")
    print("The following links have been temporarily moved and currently redirect you:")
    for i in errors302:
        print(i)
    print("\n")
    print("The following links have miscellaneous errors:")
    for i in other_errors:
        print(i)
        print("\n")
        
          