# This program draws the certificate


import os
from reportlab.platypus import Image
from datetime import datetime
from .splitLongString import splitLongString

def drawCert(c, certType, csv_data, i):
    # Modify data for cert use
    studentName = csv_data['full names'][i].upper()
    courseName = csv_data['course names'][i].upper()
    completionDate = csv_data['completion dates'][i]

    # Specify the folder containing template images and choose template image
    templates_folder = os.path.join(os.path.dirname(__file__), "templates")
    template_image = certType + "CertTemp.jpg"
    image_path = os.path.join(templates_folder, template_image)

    # Load and draw the image
    img = Image(image_path, width=792, height=612)
    img.drawOn(c, 0, 0) # Adjust the coordinates as needed

    # Set the font for the first text element
    c.setFont("BureauGrotCondensed-Bold", 42)
    c.drawCentredString(396, 364, studentName)

    # Set the font for the second text element
    c.setFont("LeMondeLivreStd-Demi", 33)
    if len(courseName) < 21:
        c.drawCentredString(396, 280, courseName)
    else:
        if len(courseName) > 60:
            c.setFont("LeMondeLivreStd-Demi", 20)
        courseLines = splitLongString(courseName)
        c.drawCentredString(396, 283, courseLines[0])
        c.drawCentredString(396, 249, courseLines[1])

    # Set the font for the third text element
    c.setFont("Typ1451Std-Regular", 10)
    formattedDate = datetime.strptime(completionDate, "%Y-%b-%d").strftime("%B %Y").upper()
    c.drawCentredString(396, 213, formattedDate)