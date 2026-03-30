# File Organizer with Simple Interface

A simple Python application with a graphical interface that automatically organizes files into specific folders based on their extensions.

## About the Project

This project was developed to make file organization faster and more practical.  
The application allows the user to select a folder, and then automatically sorts the files into predefined categories.

## Features

- Simple graphical interface
- Folder selection window
- Automatic file organization
- Separation by file extension
- Duplicate file name handling

## Technologies Used

- Python
- CustomTkinter
- Tkinter
- OS module

## Project Structure

```bash
project/
│
├── interface.py
├── logic.py
├── extensions.py
├── requirements.txt
├── .gitignore
├── README.md
└── README_PTBR.md
```

## How to Run

1. Clone this repository:
```bash
git clone [YOUR_GITHUB_LINK]
```

2. Enter the project folder:
```bash
cd [PROJECT_FOLDER_NAME]
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python interface.py
```

## How It Works

- The user clicks the button in the interface
- A folder selection window opens
- The program reads the files in the selected folder
- Files are moved to their corresponding folders based on extension

## Future Improvements

- Add support for more file types
- Improve interface design
- Add activity log
- Add custom category support

## Author

Developed by Andrey Souza
