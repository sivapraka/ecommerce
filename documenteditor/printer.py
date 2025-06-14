from abc import ABC, abstractmethod
from dataclasses import dataclass

from .model import DocumentType
from .processor import DocumentProcessor

@dataclass
class DocumentPrinter(ABC):
    processor: DocumentProcessor

    @abstractmethod
    def print_document(self):
        pass

    @abstractmethod
    def supports_type(self):
        pass


@dataclass
class TextDocumentPrinter(DocumentPrinter):
    def print_document(self):
        # Print text document
        print("Printing text document")

    def supports_type(self):
        return DocumentType.TEXT


@dataclass
class SpreadsheetDocumentPrinter(DocumentPrinter):
    def print_document(self):
        # Print spreadsheet document
        print("Printing spreadsheet document")

    def supports_type(self):
        return DocumentType.SPREAD_SHEET
