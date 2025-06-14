from documenteditor.document_parser import *
from documenteditor.printer import *
from documenteditor.processor import *
from abc import ABC, abstractmethod


class DocumentFactory(ABC):

    @abstractmethod
    def create_parser(self, path: str) -> DocumentParser:
        pass

    @abstractmethod
    def create_processor(self, name: str) -> DocumentProcessor:
        pass

    @abstractmethod
    def create_printer(self, processor: DocumentProcessor) -> DocumentPrinter:
        pass

    @abstractmethod
    def supports_type(self) -> DocumentType:
        pass


class TextDocumentFactory(DocumentFactory):

    def create_processor(self, name: str) -> DocumentProcessor:
        return TextDocumentProcessor(name)

    def create_printer(self, processor: DocumentProcessor) -> DocumentPrinter:
        return TextDocumentPrinter(processor)

    def create_parser(self,path: str) -> DocumentParser:
        return TextDocumentParser(path)

    def supports_type(self) -> DocumentType:
        return DocumentType.TEXT


class SpreadsheetDocumentFactory(DocumentFactory):
    def create_parser(self, path: str) -> DocumentParser:
        return SpreadsheetDocumentParser(path)

    def create_processor(self, name: str) -> DocumentProcessor:
        return SpreadsheetDocumentProcessor(name)

    def create_printer(self, processor: DocumentProcessor) -> DocumentPrinter:
        return SpreadsheetDocumentPrinter(processor)

    def supports_type(self) -> DocumentType:
        return DocumentType.SPREAD_SHEET
