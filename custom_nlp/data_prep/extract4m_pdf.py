# first script to use to extract data. The script will run through a list of PDFs and provide as output 
# text of all the stories that can then be used as basis for json data containing story content and titles
# 12/5/2023: Providing output in a saved text format.
# Possible next steps: Process data to identify titles and content without user intervention.
import os
import PyPDF2
import json

# Function to read titles from a text file
def read_titles_from_file(file_path):
    with open(file_path, 'r') as file:
        titles = json.load(file)  # Assuming the titles are stored in JSON format
    return titles

# Function to extract text from a single PDF file
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Directory containing your PDF files
pdf_directory = './Children Stories/3'
#Read titles from the text file. Current json file is stored at the root directory
#titles_file_path = './story_titles.json'
#titles = read_titles_from_file(titles_file_path)

content_file_path = './story_content.json'
content = (content_file_path)

# List to store extracted text and titles from all PDFs
all_texts_with_titles = []

# Loop through all PDF files in the directory
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_directory, filename)
        extracted_text = extract_text_from_pdf(pdf_path)
        # Associate title with the PDF file
        #if len(titles) > 0:
        #    title = titles.pop(0)  # Get the next title from the list
        #else:
        #    title = "No title available"  # Handle case if titles are fewer than PDFs
        # Create a dictionary entry eith title and content
        #pdf_with_title = {
        #    "Title": title,
        #    "Content": extracted_text,
        #}
        all_texts_with_titles.append(extracted_text)

# Write extracted text to a text file
#with open('all_texts_with_titles_2.txt','w') as file:
#    for line in all_texts_with_titles:
#        file.write(line + '\n--- Next PDF --- \n')

# Display extracted text (for demonstration)
for text in all_texts_with_titles:
    print(text)
    print('\n--- Next PDF ---\n')
