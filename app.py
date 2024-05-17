from docx import Document
from docx.enum.text import WD_BREAK

# Load the existing Word document
doc = Document('mm.docx')

# Add a page break at the top of each page
for i in range(len(doc.paragraphs)):
    paragraph = doc.paragraphs[i]
    # Check if the paragraph is the first one on a page
    if i != 0 and paragraph.text.strip() == '':
        # Insert a page break before the first paragraph of the page
        run = paragraph.insert_paragraph_before().add_run()
        run.add_break(WD_BREAK.PAGE)

# Save the modified document
doc.save('modified_document.docx')
