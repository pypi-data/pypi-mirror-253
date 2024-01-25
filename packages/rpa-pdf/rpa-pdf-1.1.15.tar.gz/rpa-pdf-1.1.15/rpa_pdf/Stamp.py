import os
from typing import Literal
import tempfile
from pypdf import PdfReader, PdfWriter
from fpdf import FPDF
from barcode import Code39
from barcode.writer import ImageWriter
from .Pdf import Pdf
from .common import set_x_pos, set_y_pos

pdf = Pdf()

class Stamp():
    """ Stamp class """
    def __init__(self) -> None:
        self.__root_dir__: str = os.path.dirname(os.path.abspath(__file__))
        self.__fonts_dir__: str = os.path.join(self.__root_dir__, 'fonts')
        self.__exec_dir__: str = os.path.join(self.__root_dir__, 'exec')

    def generate_code39_stamp(self,
        code: str,
        output_file_path: str,
        output_file_format: Literal['pdf', 'png'] = 'pdf',
        width: float = 40.0,
        height: float = 20.0,
        vertical_position: Literal['top', 'center', 'bottom'] = 'top',
        horizontal_position: Literal['left', 'center', 'right'] = 'left',
        page_orientation: Literal['portrait', 'landscape'] = 'portrait',
        page_units: Literal['mm', 'pt', 'cm', 'in'] = 'mm',
        page_format: Literal["a3", "A3", "a4", "A4", "a5", "A5", "letter", "Letter", "legal", "Legal"] | tuple[float, float] = 'A4',
        page_vertical_margin: int = 0,
        page_horizontal_margin: int = 0
    ):
        """
        Generates CODE39 stamp as image (png) or pdf file.

        Args:
            code (str): text value
            output_file_path (str): full path of the output file
            output_file_format (Literal["pdf", "png"], optional): output file format. Defaults to 'pdf'.
            width (float, optional): width of the barcode. Defaults to 40.0.
            height (float, optional): height of the barcode. Defaults to 20.0.
            vertical_position (Literal['top', 'center', 'bottom'], optional): vertical position of the barcode. Defaults to 'top'.
            horizontal_position (Literal['left', 'center', 'right'], optional): horizontal position of the barcode. Defaults to 'left'.
            page_orientation (Literal['portrait', 'landscape'], optional): page orientation. Defaults to 'portrait'.
            page_units (Literal['mm', 'pt', 'cm', 'in'], optional): page units. Defaults to 'mm'.
            page_format (Literal["a3", "A3", "a4", "A4", "a5", "A5", "letter", "Letter", "legal", "Legal"] | tuple[float, float], optional): page format. Defaults to 'A4'.
            page_vertical_margin (int, optional): vertial margin; can be used to move the barcode up or down. Defaults to 0.
            page_horizontal_margin (int, optional): horizontal position; can be used to move the barcode left or right. Defaults to 0.
        """
        # render barcode image
        barcode_image_path: str = tempfile.gettempdir() + '\\barcode.png' if output_file_format == 'pdf' else output_file_path
        Code39(code=code, writer=ImageWriter(), add_checksum=False).write(barcode_image_path)
        if output_file_format == 'png':
            return

        # generate a stamp pdf file
        fpdf: FPDF = FPDF(orientation=page_orientation, unit=page_units, format=page_format)
        fpdf.compress = False
        fpdf.add_page()
        fpdf.image(
            name=barcode_image_path,
            x=set_x_pos(horizontal_position, page_horizontal_margin, fpdf.w, width),
            y=set_y_pos(vertical_position, page_vertical_margin, fpdf.h, height),
            w=width,
            h=height,
            type='PNG'
        )
        fpdf.output(output_file_path)

    def add_code39_stamp(
        self,
        input_pdf_file_path: str,
        output_pdf_file_path: str,
        code: str,
        width: float = 40,
        height: float = 20,
        apply_for_pages: Literal['all', 'first', 'last'] | list[int] = 'first',
        remove_input_file: bool = False,
        vertical_position: Literal['top', 'center', 'bottom'] = 'top',
        horizontal_position: Literal['left', 'center', 'right'] = 'left',
        page_orientation: Literal['portrait', 'landscape'] = 'portrait',
        page_units: Literal['mm', 'pt', 'cm', 'in'] = 'mm',
        page_format: Literal["a3", "A3", "a4", "A4", "a5", "A5", "letter", "Letter", "legal", "Legal"] | tuple[float, float] = 'A4',
        page_vertical_margin: int = 0,
        page_horizontal_margin: int = 0
    ) -> None:
        """
        Add CODE39 barcode to the pdf file and save the output as a new pdf file.
        
        Args:
            input_pdf_file_path (str): input pdf file path (to which the barcode will be added)
            output_pdf_file_path (str): output pdf file path
            code (str): text value
            width (float, optional): width of the barcode. Defaults to 40.
            height (float, optional): height of the barcode. Defaults to 20.
            apply_for_pages (Literal["all", "first", "last"] | list[int], optional): The barcode can be applied to all pages, only to the first or the last page, or to specified pages (ex. [0,3,5]). Defaults to 'first'.
            remove_input_file (bool, optional): flag to determine if the input file should be removed. Defaults to False.
            vertical_position (Literal["top", "center", "bottom"], optional): barcode vertical position. Defaults to 'top'.
            horizontal_position (Literal["left", "center", "right"], optional): baarcode horizontal position. Defaults to 'left'.
            page_orientation (Literal["portrait", "landscape"], optional): page orientation. Defaults to 'portrait'.
            page_units (Literal["mm", "pt", "cm", "in"], optional): page units. Defaults to 'mm'.
            page_format (Literal["a3", "A3", "a4", "A4", "a5", "A5", "letter", "Letter", "legal", "Legal"] | tuple[float, float], optional): page format. Defaults to 'A4'.
            page_vertical_margin (int, optional): vertical margin. Defaults to 0.
            page_horizontal_margin (int, optional): horizontal margin. Defaults to 0.

        Raises:
            Exception: throws error message
        """
        try:
            # check if input file exists
            if os.path.exists(input_pdf_file_path) is False:
                raise FileNotFoundError(f'{input_pdf_file_path} doesn\'t exist')
            
            # render barcode pdf file
            stamp: str = f'{tempfile.gettempdir()}\\stamp.pdf'
            self.generate_code39_stamp(
                code=code,
                output_file_path=stamp,
                output_file_format='pdf',
                width=width,
                height=height,
                vertical_position=vertical_position,
                horizontal_position=horizontal_position,
                page_orientation=page_orientation,
                page_units=page_units,
                page_format=page_format,
                page_vertical_margin=page_vertical_margin,
                page_horizontal_margin=page_horizontal_margin
            )

            # check if stamp file was generated
            if os.path.exists(stamp) is False:
                raise FileNotFoundError(f'file {stamp} has not been generated')

            # get watermark page
            watermark_reader = PdfReader(stamp)
            watermark = watermark_reader.pages[0]

            # get input pdf file
            pdf_document = PdfReader(input_pdf_file_path)

            # get indexes of pages where the stamp should be added
            if not isinstance(apply_for_pages, list):
                match apply_for_pages:
                    case 'all':
                        apply_for_pages = list(range(0, len(pdf_document.pages)))
                    case 'last':
                        apply_for_pages = [-1]
                    case 'first':
                        apply_for_pages = [0]
                    case _:
                        raise ValueError('incorrect value of apply_for_pages argument')

            # prepare output pdf
            output = PdfWriter()
            
            for index, page in enumerate(pdf_document.pages):
                if index in apply_for_pages:
                    page.merge_page(watermark)
                output.add_page(page)

            # save the output file
            output.write(output_pdf_file_path)

            # try to clean out temp files
            try:
                if os.path.exists(stamp):
                    os.remove(stamp)
                if remove_input_file and os.path.exists(input_pdf_file_path):
                    os.remove(input_pdf_file_path)
            except (FileNotFoundError) as ex:
                print(ex)
        except Exception as ex:
            raise ex

    def add_text_stamp(
        self,
        input_pdf_file_path: str,
        output_pdf_file_path: str,
        text: str, *,
        apply_for_pages: Literal['all', 'first', 'last'] | list[int] = 'first',
        remove_input_file: bool = False,
        font_family: str = 'DejaVu',
        font_file_path: str | bool = False,
        font_unicode: bool = True,
        font_style: Literal["", "B", "I", "U", "BU", "UB", "BI", "IB", "IU", "UI", "BIU", "BUI", "IBU", "IUB", "UBI", "UIB"] = '',
        font_size: int = 12,
        text_vertical_position: Literal['top', 'center', 'bottom'] = 'top',
        text_horizontal_position: Literal['left', 'center', 'right'] = 'left',
        page_orientation: Literal['portrait', 'landscape'] = 'portrait',
        page_units: Literal['mm', 'pt', 'cm', 'in'] = 'mm',
        page_format: Literal["a3", "A3", "a4", "A4", "a5", "A5", "letter", "Letter", "legal", "Legal"] | tuple[float, float] = 'A4',
        page_vertical_margin: int = 10,
        page_horizontal_margin: int = 10
    ) -> None:
        """
        Add text (watermark/stamp) to the pdf document.
        Possible font formats: B - bold, I - italic, U - underline, and combinations: BI, BU, UIB, etc.\n\r
        Default font size is 12.\n\r
        Position of the text is determined by text_vertical_position: top (default), center, bottom and text_horizontal_position: left (default), center, right.\n\r
        The barcode can be applied to all pages, only to the first (default) or the last page, or to specified pages (ex. [0,3,5]).\n\r

        Args:
            input_pdf_file_path (str): full path of the input pdf file
            output_pdf_file_path (str): full path of the output pdf file
            text (str): text value
            apply_for_pages (Literal["all", "first", "last"] | list[int], optional): _description_. Defaults to 'first'.
            remove_input_file (bool, optional): _description_. Defaults to False.
            font_family (str, optional): You can change default font by providing the font_family (ex. 'Arial') and the font_file_path (ex. 'c:/windows/fonts/Arial.ttf'). Defaults to 'DejaVu'.
            font_file_path (str | bool, optional): font file path; use together with font_family. Defaults to False.
            font_unicode (bool, optional): charcode of font. Defaults to True.
            font_style (Literal["", "B", "I", "U", "BU", "UB", "BI", "IB", "IU", "UI", "BIU", "BUI", "IBU", "IUB", "UBI", "UIB"], optional): font style. Defaults to ''.
            font_size (int, optional): font size. Defaults to 12.
            text_vertical_position (Literal["top", "center", "bottom"], optional): vertical postion of the text. Defaults to 'top'.
            text_horizontal_position (Literal["left", "center", "right"], optional): horizontal position of the text. Defaults to 'left'.
            page_orientation (Literal["portrait", "landscape"], optional): page orientation. Defaults to 'portrait'.
            page_units (Literal["mm", "pt", "cm", "in"], optional): page units. Defaults to 'mm'.
            page_format (Literal["a3", "A3", "a4", "A4", "a5", "A5", "letter", "Letter", "legal", "Legal"] | tuple[float, float], optional): page format. Defaults to 'A4'.
            page_vertical_margin (int, optional): vertical margin. Defaults to 10.
            page_horizontal_margin (int, optional): horizontal margin. Defaults to 10.

        Raises:
            FileNotFoundError: when the file is missing
            Exception: general issues
        """
        try:
            # check if input file exists
            if os.path.exists(input_pdf_file_path) is False:
                raise FileNotFoundError

            # generate watermark pdf
            watermark_pdf_file_path = tempfile.gettempdir() + '\\stamp.pdf'
            pdf.text_to_pdf(
                text=text,
                output_file_path=watermark_pdf_file_path,
                font_family=font_family,
                font_file_path=font_file_path,
                font_unicode=font_unicode,
                font_style=font_style,
                font_size=font_size,
                text_vertical_position=text_vertical_position,
                text_horizontal_position=text_horizontal_position,
                page_orientation=page_orientation,
                page_units=page_units,
                page_format=page_format,
                page_vertical_margin=page_vertical_margin,
                page_horizontal_margin=page_horizontal_margin
            )

            # get watermark page
            watermark_reader = PdfReader(watermark_pdf_file_path)
            watermark = watermark_reader.pages[0]

            # get input pdf file
            pdf_document = PdfReader(input_pdf_file_path)

            # get indexes of pages where the stamp should be added
            if not isinstance(apply_for_pages, list):
                match apply_for_pages:
                    case 'all':
                        apply_for_pages: list[int] = list(range(0, len(pdf_document.pages)))
                    case 'last':
                        apply_for_pages = [-1]
                    case _:
                        apply_for_pages = [0]

            # prepare output pdf
            output = PdfWriter()
            # add a stamps
            for index, page in enumerate(pdf_document.pages):
                if index in apply_for_pages:
                    page.merge_page(watermark)
                output.add_page(page)

            # save the output file
            output.write(output_pdf_file_path)

            # try to clean out temp files
            try:
                if os.path.exists(watermark_pdf_file_path):
                    os.remove(watermark_pdf_file_path)
                if remove_input_file and os.path.exists(input_pdf_file_path):
                    os.remove(input_pdf_file_path)
            except (FileNotFoundError, FileExistsError) as ex:
                print(ex)

        except Exception as ex:
            raise ex
