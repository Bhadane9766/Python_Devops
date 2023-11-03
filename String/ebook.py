import requests
import fitz  # PyMuPDF library

# URL of the PDF you want to extract pages from
pdf_url = "https://www.trainwithshubham.com/s/courses/6406cc4ce4b0d1aea04b434a/take"

# Send a request to the URL and get the content
response = requests.get(pdf_url)
pdf_content = response.content

# Open the PDF using PyMuPDF
pdf_document = fitz.open("pdf", pdf_content)

# Extract and save all pages as separate PDF files
for page_number in range(pdf_document.pageCount):
    page = pdf_document[page_number]
    output_file_name = f"page_{page_number + 1}.pdf"  # Output file name for each page
    page.writePDF(output_file_name)

# Close the PDF document
pdf_document.close()

print("All pages extracted and saved as separate PDF files.")
