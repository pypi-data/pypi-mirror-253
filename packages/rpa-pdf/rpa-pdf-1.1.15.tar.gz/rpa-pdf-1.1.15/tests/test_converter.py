import unittest
from rpa_pdf import Converter

CONVERTER = Converter()

class test_converter(unittest.TestCase):
    def test_image_to_pdf(self):
        CONVERTER.convert('c:/temp/input.png')
        CONVERTER.convert('c:/temp/input.jpg', 'c:/temp/output_jpg.pdf')
        CONVERTER.convert('c:/temp/input.bmp', 'c:/temp/output_bmp.pdf')
        CONVERTER.convert('c:/temp/multipage.tif', 'c:/temp/multipage.tif.pdf')

    def test_word_to_pdf(self):
        CONVERTER.convert('c:\\temp\\input.docx', 'c:\\temp\\output_docx.pdf')
        CONVERTER.convert('c:\\temp\\input.doc', 'c:\\temp\\output_doc.pdf')
        CONVERTER.convert('c:/temp/input.txt', 'c:/temp/output_txt.pdf')

    def test_excel_to_pdf(self):
        CONVERTER.convert('c:/temp/input.xlsx', 'c:/temp/output_xlsx.pdf')
        CONVERTER.convert('c:/temp/input.xls', 'c:/temp/output_xls.pdf')
        CONVERTER.convert('c:/temp/input.xlsm', 'c:/temp/output_xlsm.pdf')

    def test_powerpoint_to_pdf(self):
        CONVERTER.convert('c:/temp/input.pptx', 'c:/temp/output_pptx.pdf')
        CONVERTER.convert('c:/temp/input.ppt', 'c:/temp/output_ppt.pdf')
    
    def test_html_to_pdf(self):
        CONVERTER.convert('c:/temp/input.html', 'c:/temp/output_html.pdf')
        CONVERTER.convert('c:/temp/input.htm', 'c:/temp/output_htm.pdf')

    def test_txt_to_pdf(self):
        CONVERTER.convert('c:/temp/input.txt', 'c:/temp/output_txt.pdf')
        CONVERTER.convert('c:/temp/input.csv', 'c:/temp/output_csv.pdf')
        CONVERTER.convert('c:/temp/input.md', 'c:/temp/output_md.pdf')

    def test_email_to_pdf(self):
        CONVERTER.convert('c:/temp/input.msg', 'c:/temp/output_msg.pdf')
        CONVERTER.convert('c:/temp/input.eml', 'c:/temp/output_eml.pdf')

if __name__ == '__main__':
    unittest.main()
