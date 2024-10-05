CSV Uploader Tool

A web application that allows users to upload CSV files containing student data and displays the data in a user-friendly interface.

### Features

- Upload CSV files with any data.
- It looks for Header 1 and Header 2 feild and creates 2 instances for header as Header with both values
- It combines and First Name and Last Name.
- Parse and store data in a SQLite database.
- Display data in a user-friendly interface.

### Running the Application

You can run the application in two ways:

1. Using Docker (Recommended)
2. Manually

### 1. Running with Docker

#### Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installed.

#### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/wpn10/csv_app.git
   cd csv_uploader_tool
   ```

2. **Build and run the containers:**

   ```bash
   docker-compose up --build
   ```

3. **Access the application:**

   - Frontend: Open [http://localhost:3000](http://localhost:3000) in your web browser.
   - Backend API: Accessible at [http://localhost:8000/api/](http://localhost:8000/api/)


### 2. Running Manually

#### Prerequisites

- **Python 3.8+**
- **Node.js 14+** and **npm**
- **Git**

#### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/csv_uploader_tool.git
   cd csv_uploader_tool
   ```

2. **Backend Setup:**

   ```bash
   cd backend
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```

3. **Frontend Setup:**

   In a new terminal window:

   ```bash
   cd frontend
   npm install
   ```

4. **Modify `package.json`:**

   In `frontend/package.json`, change the `"proxy"` setting to:

   ```json
   "proxy": "http://localhost:8000"
   ```

   This ensures the frontend can communicate with the backend when running locally.

5. **Start the frontend development server:**

   ```bash
   npm start
   ```

6. **Access the application:**

   - Frontend: Open [http://localhost:3000](http://localhost:3000) in your web browser.
   - Backend API: Accessible at [http://localhost:8000/api/](http://localhost:8000/api/)

**Note:** When running manually, the frontend communicates with the backend at `localhost:8000`. Ensure the `"proxy"` setting in `package.json` is set accordingly.


## Contact

For any questions or feedback, please contact:

- **Paritosh Wankhade**
- **Email:** [paritosh21w@gmail.com](mailto:paritosh21w@gmail.com)
