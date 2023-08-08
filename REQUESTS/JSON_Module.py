import json

data='{"value_1":"adeen","value_2":"ayaan"}'  #It takes a string value 
print(data)
parsed=json.loads(data) #JSON loads the data and makes a sort of virtual dictionary of the data through this we can access contents of a string data seperately without getting errors.  
print(parsed)  
          
data2={
    "python_lib":['TensorFlow','OpenCv','Tkinter'],
    "Identification":('adeen',1234)
    }

json12=json.dumps(data2) # This command converts python different types compatible with Java and can take data of multiple types(string,numbers,..) together in a single tuple 
print(json12)
