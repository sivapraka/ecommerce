from abc import ABC, abstractmethod
from dataclasses import dataclass
from .model import DocumentType


@dataclass
class DocumentParser(ABC):
    path: str

    @abstractmethod
    def parse_document(self):
        pass

    @abstractmethod
    def supports_type(self):
        pass



@dataclass
class SpreadsheetDocumentParser(DocumentParser):

    def parse_document(self):
        # Parse spreadsheet document
        pass

    def create_parser(self):
        pass

    def supports_type(self):
        return DocumentType.SPREAD_SHEET


@dataclass
class TextDocumentParser(DocumentParser):
    def parse_document(self):
        # Parse text document
        pass

    def supports_type(self):
        return DocumentType.TEXT
