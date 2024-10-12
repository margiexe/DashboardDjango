Develop an interactive dashboard in Django that features a pie chart, doughnut chart, and bar graph. The dashboard will read data from a CSV file (downloaded from: https://data.worldbank.org/) and generate a line graph based on this data. Users will have the ability to modify the data, and the graphs will update accordingly to reflect these changes.

Interactive Graphs
One line graph reads a CSV file (downloaded from: https://data.worldbank.org/) which you can access by clicking "File Data" in the sidebar.
The doughnut chart, bar chart, and pie chart are located in the "Reports" section of the sidebar.
All services are in "Products," where users can perform CRUD operations, and these changes will be reflected in the plots of the "Reports" section.
The CSV file is stored in the media folder of the project directory.
APIs
The urls.py file of the app contains the API calls. API fetching is done through the Fetch API of JavaScript.

Authentication
Only logged-in users can access the dashboard page (the @login_required decorator is used). Users can also register to create new accounts. The sign-out button in the sidebar allows users to log out.

How to Run the Project
Virtual Environment (optional): Create a virtual environment and activate it outside the project directory. Download the requirements specified in requirements.txt using the command:

command to install all necessary packages : 
"pip install -r requirements.txt"
Run the following command in the project directory (i.e., deepqtask/):

command to run project : 
"python manage.py runserver"
The project should run successfully on the localhost.

Tech Stack Used
Frontend: HTML, CSS, JavaScript
Backend: Django
For Plots: Chart.js and Plotly
Design Choices/Help From
Bootstrap, YouTube, ChatGPT
