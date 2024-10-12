# DashboardDjango
Develop an interactive dashboard in Django that features a pie chart, doughnut chart, and bar graph. The dashboard will read data from a CSV file and generate a line graph based on this data. Users will have the ability to modify the data, and the graphs will update accordingly to reflect these changes.

Interactive Graphs :
one line graph which reads a csv file (downloaded from : https://data.worldbank.org/ ) which you can see on clicking file data in the sidebar.
doughnut chart, bar chart and pie chart are in Reports section of sidebar.
all the services are in products (user can perform all crud operations and this would be reflected in the plots of Report section.
CSV file is stored in media folder of project directory

APIs :
urls.py file of apps contains the API calls.
API fetching is done through fetch library of JS

Authentication :
only logged in users can access the dashboard page (@login_required decorator is used).
users can register (make new accounts too).
signout button in the sidebar allows user to log out.

How to run the project?
Virtual environment (optional)
create a virtual environment and activate it outside the project directory and download the requirements specified in requirements.txt "pip install -r requirements.txt"
then run in the project directory (i.e deepqtask/) run "python manage.py runserver"
project should run successfully on the local host

Tech stack used :
Frontend : HTML CSS JS 
Backend : Django
for plots : chart.js and plotly

Design choices/help from : 
Booststrap, youtube, chatgpt
