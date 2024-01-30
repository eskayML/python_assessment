## Python Assessment

> **Important Note:** For the type checking, data types excluded from the 4 given in [PROBLEM.md](PROBLEM.md) , e.g boolean(true/false) and also attributes whose 'values are directly in JSON', were ignored in the function and were automatically set to `null` when the schema was generated


### Unittests
I wrote 5 different unittests using the `unittest` library in python

To run the tests
```console

python test.py
```

It  validates the `set_data_type()` function by  checking each of the 4 data types (STRING, INTEGER, ENUM & ARRAY) by passing actual values into them.

It also validates the  `sniff_schema()` function by passing in a entire expected output schema.

