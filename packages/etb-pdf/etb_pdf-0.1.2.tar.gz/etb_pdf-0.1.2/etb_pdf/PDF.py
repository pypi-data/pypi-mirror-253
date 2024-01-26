from typing import Any, Iterable
from PyPDF2 import PdfReader, PdfWriter


class Pdf:
    '''class for filling out PDF forms'''

    def __init__(self, template_file_path: str, output_dir: str = None):
        self.reader = PdfReader(template_file_path)

        if output_dir is not None:
            self.output_dir = output_dir
        else:
            self.output_dir = ''


    def write(self, rows: list[dict[str, Any]] = None, map: dict[str, str] = None, 
              naming: dict[str, str] = None, required_keys: bool | Iterable = True):
        '''check the README for more info'''

        if map is not None:
            if required_keys:
                if isinstance(required_keys, bool):
                    required_keys = map.values()

                assert all(value in row for value in required_keys for row in rows)
            
            data = [{key : row[value] for key, value in map.items()}
                    for row in rows]

        else:
            data = rows

        static_name = naming.get('static_name', '')
        dynamic_name_key = naming.get('dynamic_name_key', '')

        for row in data:
            writer = PdfWriter()
            page = self.reader.pages[0]

            writer.add_page(page)

            writer.update_page_form_field_values(
                writer.pages[0], row
            )

            output_file_name = f"{self.output_dir}{static_name}_{row.get(dynamic_name_key, '')}.pdf"

            with open(output_file_name, "wb") as output_stream:
                writer.write(output_stream)


    def get_fields(self, text_only: bool = False) -> dict[str, Any]:
        '''get PDF fields (all or text fields only)'''

        if text_only:
            fields = self.reader.get_form_text_fields()
        else:
            fields = self.reader.get_fields()

        return fields