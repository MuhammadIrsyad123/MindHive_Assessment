## Setup Instructions


### Prerequisites
- Python 3.8 to 3.11 
- SQLite3

### Command to run the application
```bash
git clone https://github.com/yourusername/subway-outlets-api.git
winget install Python.Python.3.11 --override "/quiet InstallAllUsers=1 PrependPath=1 TargetDir=C:\Your\Custom\Path" # If python 3.11 is not in your machine yet
cd subway-outlets-api
py -3.11 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt


uvicorn main:app --reload
###


