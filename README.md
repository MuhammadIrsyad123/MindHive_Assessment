## Setup Instructions


### Prerequisites

- SQLite3
- Python 3.8 to 3.11 
```bash
winget install Python.Python.3.11 --override "/quiet InstallAllUsers=1 PrependPath=1 TargetDir=C:\Your\Custom\Path" # If python 3.11 is not in your machine yet
```

### Clone the repository

```bash
git clone https://github.com/MuhammadIrsyad123/MindHive_Assessment.git
cd MindHive_Assessment
```

### Command to run the application

```bash
py -3.11 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```

In the same directory, execute this line in two separate terminals.

```bash
source env/bin/activate  # On Windows use `env\Scripts\activate`
python -m http.server 8080
```
```bash
source env/bin/activate  # On Windows use `env\Scripts\activate`
uvicorn main:app --reload
```

Run the server on 

http://localhost:8080
or
http://127.0.0.1:8080
