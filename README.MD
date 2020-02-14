Project Info

- This projected was created by group 1 in SE 3810 031 Winter Quarter 2/14/2020
- The project is a flask app that has an api call at /api/V1.0/get_building_info/<string>.
This api call takes in a building name as the string and returns the json object of the building or building not found  



Steps to Run webserver in pycharm on windows

1. Open the entire project folder in pycharm

3. In the pycharm terminal run the command: py -m venv webserver_env

3. In the same terminal run the command: .\webserver_env\Scripts\activate

5. then run pip install -r requirements.txt

6. add the virtual environment as the project interpreter
   - under file -> settings -> Project -> Project interpreter

7. create a run configuration with project interpreter and the app.py as the script   