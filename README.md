# APTIMATE-BOT
In this project you can chat with your pdf with no time limit.
SYSTEM SPECIFICATIONS
Hardware Specifications
Processor (CPU): : Intel Core i7
Ram : 4GB DDR4
Software Specifications
Operating System : Windows 11
Technology Used : Python 3.11.5
 Platform : Visual Studio Code(Terminal)
 Package
The provided code utilizes several Python packages for various functionalities. Here are the
packages used in the code:
1. NLTK (Natural Language Toolkit):
 - Used for text tokenization.
 - Specifically, the `sent_tokenize()` function from the `nltk.tokenize` module is used to
tokenize sentences.
2. PyPDF2:
 - Used for reading and parsing PDF files.
 - Specifically, the `PdfReader` class from the `PyPDF2` module is used to read PDF files
and extract text from them.
5
3. Streamlit:
 - Used for building the web application interface.
 - The `st` module from Streamlit is used to create elements such as titles, file uploaders,
text input fields, buttons, and text displays within the web application.
4. dotenv:
 - Used for loading environment variables from a `.env` file.
 - The `load_dotenv()` function from the `dotenv` module is used to load environment
variables from the `.env` file.
5. langchain:
 - Used for language detection.
 - The `langchain` module is used to detect the language of the text content extracted from
PDF files.
6. Python Built-in Modules:
 - Additionally, the code utilizes built-in Python modules such as `os`, `sys`, and `io` for
various functionalities like file operations and system interactions.
 SYSTEM DESIGN
5.1 Application Design
The application design for the "APTIMATE BOT" code involves several components
working together to create a web-based interface for interacting with PDF documents. Here's an
overview of the application design:
1. Frontend Interface:
 - The frontend interface is developed using Streamlit, a Python library for building web
applications.
 - It includes elements such as file uploaders, text input fields, buttons, and text displays.
 - Users interact with the frontend interface through their web browser.
2. Backend Logic:
 - The backend logic of the application is implemented using Python code.
 - It handles tasks such as PDF parsing, text processing, question matching, and output
presentation.
3. PDF Parsing and Text Processing:
 - Upon uploading a PDF file, the application uses the PyPDF2 library to read and extract
text from the document.
 - The extracted text is then tokenized into sentences using NLTK's `sent_tokenize()`
function for further processing.
4. Question Processing:
 - Users input questions related to the content of the PDF documents using a text input
field.
 - The application matches these questions against the tokenized sentences extracted from
the PDF text to identify relevant information.
 - Matching sentences are identified based on simple keyword matching.
7
5. Output Presentation:
 - If matching sentences are found, the application displays them to the user as relevant
information.
 - The output is presented within the frontend interface, allowing users to view and interact
with the displayed information.
6. User Interaction:
 - Users interact with the application by uploading PDF files, inputting questions, and
viewing the displayed output.
 - The application provides a user-friendly and intuitive interface, enabling users to access
information within PDF documents through natural language queries.
7. Integration and Deployment:
 - The application can be integrated with various deployment platforms and services for
hosting and accessibility.
 - Once deployed, users can access the application through a web browser, allowing them
to interact with PDF documents from any device with internet access.


*************** for futher reference mail me at srpaabinaya80529@gmail.com or my linkedin profile https://www.linkedin.com/in/pakiyalakshmi-s-9647211bb/ ***************
