# InterCollege Placement Web App

Welcome to the InterCollege Placement WebApp! This application is designed to empower college administrators to efficiently manage and contribute placement data for individual students. By centralizing this information, the project aims to provide the stakeholders with valuable insights into the state of placements across the colleges in India.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Tech Stack](#tech-stack)
- [License](#license)

## Features

1. **User-friendly Interface**: Intuitive design to make it easy for college administrators to add and manage placement data.

2. **Secure Authentication**: Ensure data integrity and privacy with secure authentication mechanisms for authorized access.

3. **Placement Data Entry**: Streamlined forms for administrators to enter/update student data.

4. **Data Visualization**: Dashboards to visualize placement trends and statistics.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/kunalagra/InterCollege-Placement-WebApp.git
   ```

2. Install the required dependencies:

   ```bash
   cd InterCollege-Placement-WebApp
   pip install -r requirements.txt
   ```

3. Configure the database connection by updating the `database.py` file and creating ServiceAccount with required permission.

4. Start the application:

   ```bash
    python app.py
   ```

## Tech Stack

- Backend: Flask, gspread (Google Sheets), pandas
- Frontend: HTML, CSS, Bootstrap, jQuery

## License

This project is licensed under the [GNU AGPL v3](LICENSE.md). See the [LICENSE.md](LICENSE.md) file for details.
Based on [Flask SB Admin](https://github.com/app-generator/flask-sb-admin)
