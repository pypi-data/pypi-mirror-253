"""
Pdf module provides features to work with pdf files: merge pdfs, add stamps, print to the printer
"""
import os.path
from typing import Literal
import subprocess
from pypdf import PdfMerger, PdfReader, PdfWriter
from fpdf import FPDF
from .common import set_x_pos, set_y_pos

class Pdf():
    """ Pdf class """
    def __init__(self) -> None:
        self.__root_dir__: str = os.path.dirname(os.path.abspath(__file__))
        self.__fonts_dir__: str = os.path.join(self.__root_dir__, 'fonts')
        self.__exec_dir__: str = os.path.join(self.__root_dir__, 'exec')

    def compress(self, pdf_file_path: str) -> None:
        """
        Compress pdf file to decrease the file size

        Args:
            pdf_file_path (str): full path of the pdf file

        Raises:
            FileNotFoundError: when the file has not been found
            Exception: other problem occured
        """
        try:
            if os.path.exists(pdf_file_path) is False:
                raise FileNotFoundError(f'{pdf_file_path} does not exist')

            writer = PdfWriter()
            reader = PdfReader(pdf_file_path)
            writer.clone_document_from_reader(reader)
            for page in writer.pages:
                page.compress_content_streams()
            with open(pdf_file_path, 'wb') as pdf:
                writer.write(pdf)
        except Exception as ex:
            raise ex

    def text_to_pdf(
        self,
        text: str,
        output_file_path: str,
        font_family: str = 'DejaVu Sans',
        font_file_path: str | bool = False,
        font_unicode: bool = True,
        font_style: Literal['', 'B', 'I', 'U', 'BU', 'UB', 'BI', 'IB', 'IU', 'UI', 'BIU', 'BUI', 'IBU', 'IUB', 'UBI', 'UIB'] = '',
        font_size: int = 12,
        text_vertical_position: Literal['top', 'center', 'bottom'] = 'top',
        text_horizontal_position: Literal['left', 'center', 'right'] = 'left',
        page_orientation: Literal['portrait', 'landscape'] = 'portrait',
        page_units: Literal['mm', 'pt', 'cm', 'in'] = 'mm',
        page_format: Literal['A3', 'A4', 'A5', 'Letter', 'Legal'] | tuple[float, float] = 'A4',
        page_vertical_margin: int = 10,
        page_horizontal_margin: int = 10
    ) -> None:
        """
        Convert text to pdf file.

        Args:
            text (str): text value
            output_file_path (str): full path of the output file
            font_family (str, optional): you can change default value by providing the font_family (ex. 'Arial') and the font_file_path (ex. 'c:/windows/fonts/Arial.ttf'). Defaults to 'DejaVu Sans'.
            font_file_path (str | bool, optional): font file path; use only with font_family. Defaults to False.
            font_unicode (bool, optional): font code format. Defaults to True.
            font_style (Literal['', 'B', 'I', 'U', 'BU', 'UB', 'BI', 'IB', 'IU', 'UI', 'BIU', 'BUI', 'IBU', 'IUB', 'UBI', 'UIB'], optional): _description_. Defaults to ''.
            font_size (int, optional): font size. Defaults to 12.
            text_vertical_position (Literal['top', 'center', 'bottom'], optional): vertical position of the text. Defaults to 'top'.
            text_horizontal_position (Literal['left', 'center', 'right'], optional): horizontal position of the text. Defaults to 'left'.
            page_orientation (Literal['portrait', 'landscape'], optional): page orientation. Defaults to 'portrait'.
            page_units (Literal['mm', 'pt', 'cm', 'in'], optional): _description_. Defaults to 'mm'.
            page_format (Literal['A3', 'A4', 'A5', 'Letter', 'Legal'] | tuple[float, float], optional): page format. Defaults to 'A4'.
            page_vertical_margin (int, optional): page vertical margin. Defaults to 10.
            page_horizontal_margin (int, optional): page horizontal margin. Defaults to 10.
        """
        try:
            fpdf: FPDF = FPDF(orientation=page_orientation, unit=page_units, format=page_format)
            fpdf.compress = True
            # set style and size of font that you want in the pdf
            fpdf.add_font(font_family, '', font_file_path if isinstance(font_file_path, str) else f'{self.__fonts_dir__}\\DejaVuSans.ttf', font_unicode)
            fpdf.set_font(family=font_family, style=font_style, size=font_size)
            # add a page
            fpdf.add_page()
            # get text width
            string_width: float = fpdf.get_string_width(text)
            # set position of text
            x_pos: float = set_x_pos(text_horizontal_position, page_horizontal_margin, fpdf.w, string_width)
            y_pos: float = set_y_pos(text_vertical_position, page_vertical_margin, fpdf.h, font_size)
            # add text
            fpdf.text(x_pos, y_pos, text)
            # save the pdf with name .pdf
            fpdf.output(output_file_path)
        except Exception as ex:
            raise ex

    def merge(self, pdf_files: list, output_pdf_file_path: str) -> None:
        """
        Merge given pdf files

        Args:
            pdf_files (list): list of paths to pdf files in order
            output_pdf_file_path (str): path of the output pdf file (merged)

        Raises:
            FileNotFoundError: if the file is missing
            FileExistsError: if the output file exists and cannot be overwritten
            Exception: other errors
        """
        try:
            # check if input file exists
            for file_path in pdf_files:
                if os.path.exists(file_path) is False:
                    raise FileNotFoundError(f'{file_path} does not exist')

            # merge_file: PdfMerger = PdfMerger()
            # for pdf_file in pdf_files:
            #     pdf_reader = PdfReader(pdf_file)
            #     merge_file.append(pdf_reader, default_page_orientation=pdf_reader.getPageOrientation())

            # merge_file.write(output_pdf_file_path)
            # merge_file.close()
            
            merge_file = PdfWriter()
            for pdf_file in pdf_files:
                pdf_reader = PdfReader(pdf_file)
                for page in pdf_reader.pages:
                    )

            if os.path.exists(output_pdf_file_path) is False:
                raise FileExistsError(f'{output_pdf_file_path} was not generated.')
        except Exception as ex:
            raise ex

    def print(
        self,
        pdf_file_path: str,
        printer: str = 'default',
        pages: Literal['all', 'first', 'last'] | list = 'all',
        odd_or_even: Literal['odd', 'even'] | bool = False,
        orientation: Literal['portrait', 'landscape'] = 'portrait',
        scale: Literal['noscale', 'shrink', 'fit'] = 'fit',
        color: Literal['color', 'monochrome'] = 'color',
        mode: Literal['duplex', 'duplexshort', 'duplexshort', 'simplex'] = 'simplex',
        paper: Literal['A2', 'A3', 'A4', 'A5', 'A6', 'letter', 'legal', 'tabloid', 'statement'] = 'A4'
    ) -> None:
        """
        Print PDF document.
        Works only on Windows

        Args:
            pdf_file_path (str): full file path
            printer (str, optional): printer name; if empty or default will print on the default printer. Defaults to 'default'.
            pages (Literal["all", "first", "last"] | list, optional): determines which pages should be printed; can select "all", "first", "last" or range of pages, ex. 1,3-5,-1 to print pages: 1, 3, 4, 5 and the last one (-1). Defaults to 'all'.
            odd_or_even (Literal["odd", "even"] | bool, optional): print only odd or even pages from the selected range. Defaults to False.
            orientation (Literal["portrait", "landscape"], optional): page orientation. Defaults to 'portrait'.
            scale (Literal["noscale", "shrink", "fit"], optional): scale. Defaults to 'fit'.
            color (Literal["color", "monochrome"], optional): determine if print in color or monochrome. Defaults to 'color'.
            mode (Literal["duplex", "duplexshort", "duplexshort", "simplex"], optional): print mode. Defaults to 'simplex'.
            paper (Literal["A2", "A3", "A4", "A5", "A6", "letter", "legal", "tabloid", "statement"], optional): paper size. Defaults to 'A4'.

        Raises:
            FileNotFoundError: if file is missing
            Exception: general errors
        """
        # check if input file exists
        if os.path.exists(pdf_file_path) is False:
            raise FileNotFoundError(f'{pdf_file_path} does not exist')

        sumatra_path: str = f'{self.__exec_dir__}\\sumatra.exe'
        printer_mode: str = '-print-to-default' if printer == 'default' else f'-print-to "{printer}"'

        settings: list = []
        # page range to print
        if isinstance(pages, list):
            settings.append(",".join(pages))
        match pages.lower():
            case "first":
                settings.append("1")
            case "last":
                settings.append("-1")
            case "all":
                settings.append("*")
            case _:
                raise ValueError("incorrect range of pages to print; correct vaules: all, first, last, or list (ex. [1,2,3-5,-1])")

        # page to print: odd or even or all
        if isinstance(odd_or_even, str):
            match odd_or_even.lower():
                case 'odd':
                    settings.append('odd')
                case 'even':
                    settings.append('even')
                case _:
                    raise ValueError("incorrect value for odd_or_even attribute; correct values: odd, even")

        # page orientation
        settings.append(orientation)

        # content scale
        settings.append(scale)

        # color
        settings.append(color)

        # print mode
        settings.append(mode)

        # paper size
        settings.append(f'paper={paper}')

        print_settings: str = f'-print-settings "{",".join(settings)}"'

        try:
            subprocess.run(f'{sumatra_path} {printer_mode} {print_settings} -silent "{pdf_file_path}"', check=True)
        except subprocess.CalledProcessError as ex:
            raise ex
