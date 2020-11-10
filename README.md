# Naan factory Task

### Summary

TDD bread factory is the latest bread brand in Py Land. It always produces the best bread because it has the best testing strategy!
What they do is before they make any new bread, they make a test to make sure the end output is correct. Then they adjust the recipe until it's just right!

### TDD - test driven development

1. write the test
2. run it, and read the error
3. code and make it pass the test

this helps with:
- Stop over engineering
- Maintainable code
- Reduce technical debt
- Goes well with agile and working code
- errors can be your guide in complex systems

### User Stories 
- 1
  - As a user, I can use the make dough with 'water' and 'flour' to make 'dough'.

- 2
  - As a user, I can use the bake dough with dough to get naan.

- 3
  - As a user, I can user the run factory with water and flour and get naan.
  
### Task
- Create a naan_factory file
- create a naan factory class that will hold specified methods
```python
class NaanFactory:
```
- define a method that makes dough if water and flour is True
```python    
    def make_dough(self, water, flour):
        if water and flour:
            return True
        else:
            return False
```
- Define a method that makes naan if dough is True
```python  
    def make_naan(self, dough):
        if dough:
            return True
        else:
            return False
```
- Define a method that makes naan from water and flour
```python 
    def run_factory(self, water, flour):
        # returns True if naan is made. This depends if make dough returns True
        return self.make_naan(self.make_dough(water, flour))
```
- Now we need to test each method in this class
- make a new file for testing the naan factory
- Import the NaanFactory class
```python
from naan_factory import NaanFactory
```
- Install pytest module in the terminal using `pip install pytest`
- we can then import the relevant test functions we will need
```python
import pytest
import unittest
```
- Create a class now that will hold methods to test each method in NaanFactory
- make sure its a child class of unittest.TestCase so we can use the relevant methods
```python
class TestFactory(unittest.TestCase):
```
- create an object of our naan factory
```python 
    factory_1 = NaanFactory()
```
- make a function that tests the make_dough function
- include test_ in the function name    
```python  
    def test_make_dough(self):
        # If the make dough function works it should return true so the test should pass
        self.assertTrue(self.factory_1.make_dough(True, True)) #assertTrue passes if the outcome of the function is True
```
- Do the same for the make_naan function and the run_factory function
```python  
    def test_make_naan(self):
        self.assertTrue(self.factory_1.make_naan(True))

    def test_run_factory(self):
        self.assertTrue(self.factory_1.run_factory(True, True))
```
- to run the tests on this file enter `python -m pytest`
- If no water or flour, the test will fail
