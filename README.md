# Patient Health Record Query System

This project is a web application that allows users to upload PDF files containing patient health records and ask questions related to the data. The application processes the PDF, extracts relevant information, and provides answers using OpenAI's GPT-based model in a hierarchical approach with multiple agents. The app is built with Streamlit for simplicity and user-friendliness.

---

## Features
1. **Upload Patient Health Records**: Upload PDF files containing patient health records.
2. **Ask Questions**: Use a query bar to ask specific questions about the uploaded records.
3. **View Extracted Data**: See the text extracted from the PDF in a readable format.
4. **Get Answers**: Receive detailed answers generated by OpenAI's GPT model.
5. **Hierarchical Processing**: The application uses three agents to extract, process, and analyze the data.

---

## File Structure
```
project_directory/
│
├── app.py                 # Main Streamlit application
├── agents/
│   ├── agent1.py          # Extracts text from PDFs
│   ├── agent2.py          # Processes extracted data
│   ├── agent3.py          # Queries OpenAI's GPT model
│
├── utils/
│   ├── pdf_utils.py       # Utilities for handling PDF files
│   ├── openai_utils.py    # Utilities for interacting with OpenAI API
│
├── css/
│   └── styles.css         # Custom CSS for UI styling
│
├── requirements.txt       # List of Python dependencies
├── README.md              # Detailed project documentation
```

---

## Prerequisites
1. **Python (>= 3.8)**: Ensure Python is installed on your system.
   - Download Python from [python.org](https://www.python.org/downloads/).
2. **OpenAI API Key**: Sign up at [OpenAI](https://platform.openai.com/signup/) and generate an API key. **This is a mandatory step, as you need this key to authenticate this app.**
3. **Streamlit**: Framework to build the web application. You will be able to install this framework while installing the dependencies in the 3rd step of `Installation` given below.

---

## Installation
Follow these steps to set up the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/patient-health-query-system.git
   cd patient-health-query-system
   ```

2. **Set Up a Virtual Environment** (Optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   

4. **Set OpenAI API Key**:
   Create an environment variable for your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-api-key"     # Linux/Mac
   set OPENAI_API_KEY="your-api-key"       # Windows
   ```

---

## How to Run the Application
1. **Start the Streamlit Application**:
   ```bash
   streamlit run app.py
   ```

2. **Upload a PDF**:
   - Use the "Upload Patient Health Record" button to upload a PDF.

3. **Ask Questions**:
   - Enter your question in the query bar and press enter.

4. **View Results**:
   - The extracted text and the generated answer will appear below the query bar.

---

## How It Works
The application uses a **hierarchical processing approach** with three agents:

### Agent 1: Text Extraction
- Extracts text from the uploaded PDF using the `PyPDF2` library.
- Handles multi-page PDFs and consolidates the text for further processing.

### Agent 2: Query Data Processing
- Processes the extracted text for relevance based on the user's query.
- Prepares data to be passed to the OpenAI model.

### Agent 3: Answer Generation
- Uses OpenAI's GPT-based `ChatCompletion` API to generate answers based on the processed data.
- Incorporates user queries and the extracted text into the prompt for accurate responses.

---

## Styling
The application includes custom CSS for a clean and user-friendly interface:
- Background color: Soft grey.
- Text area: Highlighted for clarity.
- Buttons and inputs: Styled for usability.

CSS is stored in the `css/styles.css` file and is applied using Streamlit's `st.markdown` function.

---

## Dependencies
The project uses the following Python libraries:
- `streamlit`: For building the web application.
- `PyPDF2`: For extracting text from PDF files.
- `openai`: For interacting with OpenAI's GPT models.

All dependencies are listed in the `requirements.txt` file.

---

## Example Usage
### Input
1. Upload a PDF containing patient health records.
2. Ask a question like:
   - "What medications are listed in the record?"
   - "Is there a history of diabetes?"

### Output
- The text extracted from the PDF.
- The AI-generated answer based on the query.

---

## Troubleshooting
1. **Missing OpenAI API Key**:
   Ensure your API key is set as an environment variable.
   ```bash
   export OPENAI_API_KEY="your-api-key"   # Linux/Mac
   set OPENAI_API_KEY="your-api-key"     # Windows
   ```

2. **Invalid PDF**:
   - Ensure the uploaded file is a valid PDF.
   - If the text extraction fails, check if the PDF is scanned (image-based) and convert it to a text-based PDF.

3. **Dependency Issues**:
   - Run `pip install -r requirements.txt` to reinstall dependencies.
   - Use a virtual environment to avoid conflicts.

---

## Future Improvements
1. Add OCR support for image-based PDFs using libraries like `pytesseract`.
2. Enhance query handling with more robust NLP techniques.
3. Deploy the application using Streamlit Cloud or similar services.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgements
- OpenAI for the GPT model.
- Streamlit for the web application framework.
- PyPDF2 for PDF text extraction.

---

## Authors
Developed by **VIJVAL VEMULA** and **ANAMIKA REKHA**. For questions or support, contact vemulavijval1@gmail.com or anamikarekha1999@gmail.com.
