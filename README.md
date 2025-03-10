# Game Review Analysis

This project focuses on game review data analysis, where I have performed an in-depth exploration and analysis of game review data. The repository contains code to analyze game reviews, build a Django application for data entry, and visualize the data with downloadable reports.

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Description
This project includes:
- **Data Analysis**: Analyzing game review data such as critic scores, user scores, sales data, and more.
- **Django Application**: A fully functional Django application for managing game reviews, where users can add game data, view analyses, and download the results in various formats.
- **Data Visualization**: Visualizing the game review data with interactive graphs and charts to identify trends and insights.

## Features
- **Game Data Entry**: A form to submit game data (name, year of release, sales data, reviews, etc.).
- **Data Analysis**: Statistical and machine learning-based analysis on game reviews.
- **Visualization**: Heatmaps and other plots for analyzing correlations and trends.
- **Downloadable Reports**: Export your game review data as CSV files for further use.
- **Django Admin**: A built-in admin panel to manage all the game data.

## Technologies Used
- **Python**: The main programming language used for analysis and backend development.
- **Django**: A high-level Python web framework to build the data entry and management interface.
- **pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations and support for data manipulation.
- **Seaborn & Matplotlib**: For data visualization (heatmaps, charts).
- **Scikit-learn**: For implementing machine learning models (if applicable).
- **SQLite**: Default database used for storing game data in the Django app.

## Setup and Installation

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Clone the Repository
To get started, first clone the repository to your local machine:
```bash
git clone https://github.com/Kami80/Game-review-analysis.git
cd Game-review-analysis
```
Create a Virtual Environment (optional but recommended)
```bash

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Install Dependencies
Use pip to install the necessary libraries:

```bash

pip install -r requirements.txt
```
### Apply Database Migrations
Run the following command to set up the database:

```bash

python manage.py migrate
```
### Create a Superuser (optional)
To access the Django admin panel, create a superuser account:

```bash

python manage.py createsuperuser
```
### Start the Development Server
Run the Django server to view the project locally:

```bash

python manage.py runserver
```
You can access the app at http://127.0.0.1:8000/.

## Usage
Once the project is running, you can:

- **Enter Game Data:** Go to the game data entry page and fill out the form with the game’s details.
- **View Data:** Analyze game review data and visualize trends using built-in graphs.
- **Download Data:** Export the game review data as CSV files.
- **Admin Interface:** Manage game data using the Django admin panel at http://127.0.0.1:8000/admin/.
Contributing
Contributions are always welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request. Here's how you can contribute:

## Fork the repository.
- Create a new branch (git checkout -b feature-name).
- Make your changes and commit (git commit -am 'Add new feature').
- Push to your branch (git push origin feature-name).
- Open a pull request.
## License
This project is licensed under the MIT License – see the LICENSE file for details.

## Contact
Feel free to reach out for any questions or suggestions regarding the project.

GitHub: @Kami80
Email: Kamyabsafaie80@gmail.com
