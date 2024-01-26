# Register custom fonts


from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

def regCustomFonts():
    font_folder = os.path.join(os.path.dirname(__file__), "fonts")
    pdfmetrics.registerFont(TTFont('BureauGrotCondensed-Bold', os.path.join(font_folder, 'BureauGrotCondensed-Bold.ttf')))
    pdfmetrics.registerFont(TTFont('LeMondeLivreStd-Demi', os.path.join(font_folder, 'LeMondeLivreStd-Demi.ttf')))
    pdfmetrics.registerFont(TTFont('Typ1451Std-Regular', os.path.join(font_folder, 'Typ1451Std-Regular.ttf')))