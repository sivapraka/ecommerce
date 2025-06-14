from abc import ABC, abstractmethod
from dataclasses import dataclass
from .model import DocumentType


@dataclass
class DocumentProcessor(ABC):
    document_name: str

    @abstractmethod
    def process_document(self):
        pass

    @abstractmethod
    def supports_type(self):
        pass


@dataclass
class SpreadsheetDocumentProcessor(DocumentProcessor):
    def process_document(self):
        # Implement spreadsheet document processing logic
        print("Processing a spreadsheet document:", self.document_name)
        # Additional logic for spreadsheet document processing

    def supports_type(self):
        return DocumentType.SPREAD_SHEET

    def perform_data_analysis(self):
        print("Performing data analysis on the spreadsheet.")


@dataclass
class TextDocumentProcessor(DocumentProcessor):
    def process_document(self):
        # Implement text document processing logic
        print("Processing a text document:", self.document_name)
        # Additional logic for text document processing

    def supports_type(self):
        return DocumentType.TEXT

