# Excel File Comparison Web App

This is a web application built with FastAPI that allows users to compare the contents of two Excel files. It provides a user-friendly interface for uploading Excel files, selecting specific sheets, and visualizing the differences between them.

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


3. Install dependencies:

pip install -r requirements.txt


4. Run the application:


5. Open your web browser and go to [http://localhost:8000](http://localhost:8000) to access the application.

## Usage

1. Navigate to the homepage of the web application.
2. Upload two Excel files using the provided form.
3. Optionally, specify the sheet numbers within each file to compare.
4. Click the "Compare" button to view the differences between the selected sheets.
5. Scroll through the comparison result to analyze the differences.

## Technologies Used

- Python
- FastAPI
- Jinja2 Templates
- Pandas
- Openpyxl
- Bootstrap

## Contributing

Contributions are welcome! If you have any ideas for new features, improvements, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
