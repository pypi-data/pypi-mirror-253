#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from doctext.Capabilities import Capabilities
from doctext.textextract import extract_text

class Processor:
    def __init__(self, openai_api_key=None):
        """
        Constructor for the Processor class.
        If no API for OpenAI is provided, we will not make use of Whisper for audio to text.
        """
        self.openai_api_key = openai_api_key
            
        self.capabilities = Capabilities(self.openai_api_key is not None)


    def run(self, file_path: str|Path) -> str:
        return extract_text(str(file_path), self.openai_api_key)