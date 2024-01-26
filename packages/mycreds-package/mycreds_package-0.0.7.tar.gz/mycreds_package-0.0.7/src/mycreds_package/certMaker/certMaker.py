# This script iterates through each row of the MyCredsCertificate.csv and
# generates PDF certificates in a new folder called newBatch located in MyCreds.


from reportlab.pdfgen import canvas
import os
from .regCustomFonts import regCustomFonts
from .getCertType import getCertType
from .csvReader import csvReader
from .drawCert import drawCert

def certMaker():
    # Call the function to register custom fonts
    regCustomFonts()

    # Prompt user for cert type
    validCertTypes = ['bronze', 'silver', 'gold']
    certType = getCertType(validCertTypes)

    # Read csv and store data in lists
    csv_data = csvReader()

    # Specify the target directory for the output PDF file and create if necessary
    target_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), "newBatch")
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    for i in range(len(csv_data['full names'])):
        # Specify the output PDF file
        output_pdf = os.path.join(target_directory, csv_data['full names'][i] + ".pdf")

        # Create the PDF
        c = canvas.Canvas(output_pdf, pagesize=(792, 612))

        # Draw the certificate
        drawCert(c, certType, csv_data, i)
        c.showPage()
        c.save()