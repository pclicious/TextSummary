from docx import Document

wordDoc = Document('PoojaCV.docx')

for table in wordDoc.tables:
    for row in table.rows:
        for cell in row.cells:
            print(cell.text)