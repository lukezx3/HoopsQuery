# NBA-Shot-Projection

## Description

As an avid NBA fan, I’m passionate about exploring detailed shot statistics of NBA players. This project is a full-stack application designed to provide dynamic insights into NBA shot data. It leverages React.js, HTML, and CSS for a responsive and user-friendly frontend, while Flask and Python handle backend operations. PostgreSQL serves as the robust database for storing extensive datasets, and OpenAI's GPT-3.5 Turbo model powers the intelligent query processing.

The application works by allowing users to input queries related to NBA shot statistics. These queries are processed by GPT-3.5 Turbo to dynamically generate the appropriate SQL commands. The backend then executes these queries against the PostgreSQL database and returns the results, which are displayed on a separate page, providing users with precise and actionable data insights.

### Prerequisites
- Python3
- PostGreSQL
- React
Packages/Libraries:
- OpenAI
- Psycopg2-binary
- Flask
- react-router-dom

### Setup

1.Install Prerequisites
2. **Clone the repository:**
   ```git clone(https://github.com/lukezx3/NBA-Shot-Projection.git```
3. ```cd <your project directory>```
4. run ```npm start from project directory``` to run react script
5. cd server
6. run ```python3 app.py``` to start backend server

### Demo

### Acknowledgements

Credit to DomSamangy for datasets: https://github.com/DomSamangy/NBA_Shots_04_24

