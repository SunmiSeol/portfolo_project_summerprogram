# portfolo_project_summerprogram


 1. I would like to develop a  "Summer Program Registration System" for my project and actually there is a website like 'citypark' that I used to search some programs for my kids makes me to create this system.  This registration system will provides free activities list for user or parents and, the users are able to register the activity programs through creating an account. 

 2. I have created my project from starting with the Django appication of first workshop as a starting and modified this to "Summer Programs Registration System". It has an implement a 3-tier architecture that includes a Postgres database, pg Admin and the web-based application that interacts with the database. Docker Compose used 
 to define and manage the tiers. 

 3. 2. Endpoints
  - GET, '/' -> Show base html page with program titles.
  - GET, api/program/  -> def index : get a list all available activity programs.
  - GET, api/program/:id -> get a detailed of program list.
  - GET, api/program/open -> get a registration open list which is available.
  - POST, api/program/  -> add a program as request of JSON body type.
  - POST, api/program/:id -> update an information of program as request of JSON body type.
  - DELETE, api/program/:id -> delete a program from the list.

 