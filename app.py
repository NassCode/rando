from docx import Document
from docx.enum.section import WD_SECTION

# Load an existing document
doc = Document('your_document.docx')

# Count the number of pages (assuming each 'Enter' or paragraph return is a new page)
number_of_pages = len(doc.paragraphs)

# Add a section break for each new page
for _ in range(number_of_pages - 1):  # -1 because the first page is already a section
    # Add a section break at the end of the document
    new_section = doc.add_section(WD_SECTION.NEW_PAGE)
    # Set your specific section properties here if needed

# Save the document with the new sections
doc.save('your_document_with_sections.docx')
