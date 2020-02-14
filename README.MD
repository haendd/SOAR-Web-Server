Steps to Run webserver in pycharm in windows

1. Open the entire project folder in pycharm

3. In the pycharm terminal run the command: py -m venv webserver_env

3. In the same terminal run the command: .\webserver_env\Scripts\activate

5. then run pip install -r requirements.txt

6. add the virtual environment as the project interpreter
   - under file -> settings -> Project -> Project interpreter

7. create a run configuration with project interpreter and the app.py as the script   