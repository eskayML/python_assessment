## Python Assessment


The program `main.py` contains the main script that runs the program and sniffs the schema from the data folder. 


> **Important Note:**  For the type checking, data types excluded from the 4 given in [PROBLEM.md](PROBLEM.md) , e.g boolean(true/false), empty arrays [] and also attributes whose values are JSON objects , were ignored in the function and were automatically set to `null` when the schema was generated


### Unittests
I wrote 4 different unittests using the `unittest` library in python

To run the tests
```console

python test.py
```

The test script runs test cases for the different information , these include:
- padding 
- excluding the attributes key 
- setting required=False
- setting the 4 different datatypes 


# Showing Inputs and expected outputs (via the 'type'key)

#### data_1.json
```json
"message":{
    // SHOWING THE IMMEDIATE KEYS ONLY.
    "battle": {
        ... //since its directly a JSON object , and not a JSON object in an array , it maps to null
    },

    "joiner": {
        ... // same thing with above, it gets mapped to null
    },

    "participantsIds": [
        "ABCDEFGHIJKLMNOPQRST",
        "ABCDEFGHIJKLMNOPQRST"
        ]  // it gets mapped to ENUM since it contains strings in an array.

}
```



#### data_2.json

```json
"message": {
    // SHOWING THE IMMEDIATE KEYS ONLY
    "user":{
        ...  // it gets mapped to null , since its not a JSON inside a list
    }, 
    "time":890, // gets mapped to INTEGER
    "acl":[],  // gets mapped to null 
    "publicFeed":false,  // gets mapped to null since its a boolean
    "internationalCountries":["...","...","..."], // gets mapped to ENUM , string inside an array
    "topTraderFeed":true,  // gets mapped to null since its a boolean
}
```