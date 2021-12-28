# members-club-test

## Members club application

### Installation
In terminal:

```git clone https://github.com/arttre/members-club-test.git -b master``` -- installing repository

```cd members-club-test``` -- moving to a _main directory_

```pip install -r requirements.txt``` -- installing all requirements

*_pip_ must be installed.

### Run

Inside _main directory_:
```python3 -m uvicorn main:app```
to run our local server.

After that open ```index.html``` file.
Here it is, you can work with application.

*of course, _python3_ must be installed.

### Testing

Simply use ```pytest``` command in a _main directory_.

To export testing results to a file use ```pytest > test_results.log``` command.
