# war_or_peace_python
## Implementation
### `Python 3.7.3`
### `Unittest`

## Testing
### To run all test run `python -m unittest discover test "*_test.py"`
### Note: When tests are run the War class will be instantiated twice. This is due to the fact that the war class is a runner file and should be able to run independently of calling the War.start() function. Yet the test will have to instantiate War() to test whether it can be won or not
