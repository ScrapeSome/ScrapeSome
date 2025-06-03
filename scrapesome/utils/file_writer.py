"""
file_writer.py

A utility module for writing data to files in various formats.

Supported formats:
- JSON
- Markdown
- Plain Text
- HTML

If the target file path does not include an extension, one will be added based on the selected format.

Usage Example:
    from file_writer import write

    data = {"name": "Open Source", "type": "Library"}
    write(data, "output", "json")  # Writes to output.json
"""

import json
import os
from scrapesome.logging import get_logger
from scrapesome.config import Settings

settings = Settings()

logger = get_logger()

def write(data, file_name, output_format_type):
    """
    Writes data to a file in the specified format. Adds file extension if missing.

    Parameters:
        data (any): The data to write. Can be dict, list, or str.
        file_name (str): Name to the output file.
        output_format_type (str): Format type. One of 'json', 'markdown', 'text', 'html'.

    Raises:
        ValueError: If an unsupported format is provided.
    """
    output_format_type = output_format_type.lower()
    extensions = settings.file_extensions

    if output_format_type not in extensions:
        raise ValueError(f"Unsupported format: {output_format_type}")

    # create file_path based on file_name and output_format_type
    file_path = file_name + extensions.get(output_format_type,"")

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            if output_format_type == 'json':
                json.dump(data, f, indent=4)
            else:
                f.write(str(data))

        logger.info(f"writing scraped data into file {file_path} completed.")
        return file_path
    except Exception as e:
       logger.error(f"Error writing file: {e}")
