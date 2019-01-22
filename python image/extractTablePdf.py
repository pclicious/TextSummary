import tabula

# Read pdf into DataFrame
df = tabula.read_pdf("PoojaCV.pdf")

# Read remote pdf into DataFrame
#df2 = tabula.read_pdf("table.pdf")

# convert PDF into CSV
tabula.convert_into("PoojaCV.pdf", "output.csv", output_format="csv")

# convert all PDFs in a directory
#tabula.convert_into_by_batch("input_directory", output_format='csv')