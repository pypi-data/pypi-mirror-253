# Python Grooper Wrapper

This wrapper encapsulates the functionality provided in the grooper API.

## Usage

```python
import grooper.core import API, Batch

API.key = <API Key>
API.url = <API URL>

batch = Batch.find(<Batch ID>)
print(batch)
```

## Testing

To run the tests, you need to have `pytest` and `coverage` installed. To run the tests and generate a coverage report, run the following commands:

```bash
coverage run --source=. -m pytest
coverage report
```

Before committing, make sure you are styling appropriately your code. For that, you can run the following command (assuming you have installed `black`, `isort` and `pylint`):

```bash
black .
isort .
pylint grooper tests
```
