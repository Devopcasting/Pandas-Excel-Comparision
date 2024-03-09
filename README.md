# Excel File Comparison Web App

This is a web application built with FastAPI that allows users to compare the contents of two Excel files.

## Features

- Upload two Excel files for comparison.
- Select specific sheets within each Excel file.
- View the differences between the selected sheets side by side.
- Highlight rows with differing values or rows present only in one file.
- Responsive layout for different screen sizes.

## Setup

1. Clone the repository:

git clone https://github.com/yourusername/excel-comparison-app.git


2. Navigate to the project directory:

cd excel-comparison-app

3. Create Python environment

python -m virtualenv env

4. Activate environment

.\env\Scripts\activate.ps1

5. Install dependencies:

pip install -r requirements.txt


6. Run the application:

python main.py

## Technologies Used

- Python
- FastAPI
- Jinja2 Templates
- Pandas
- Openpyxl
- Bootstrap