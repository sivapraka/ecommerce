import unittest

from documenteditor import *
from documenteditor.abstract_factory import TextDocumentFactory, SpreadsheetDocumentFactory
from documenteditor.model import DocumentType
from documenteditor.printer import DocumentPrinter
from documenteditor.processor import DocumentProcessor
from documenteditor.document_parser import DocumentParser


class TestDocumentFactory(unittest.TestCase):

    def test_methods(self):
        text_factory = TextDocumentFactory()
        spreadsheet_factory = SpreadsheetDocumentFactory()
        methods = [
            "create_processor",
            "create_parser",
            "create_printer",
            "supports_type",
        ]
        for method in methods:
            self.assertTrue(
                hasattr(text_factory, method),
                f"If the abstract factory is correctly implemented, DocumentFactory should have a method named {method}.",
            )
            self.assertTrue(
                hasattr(spreadsheet_factory, method),
                f"If the abstract factory is correctly implemented, DocumentFactory should have a method named {method}.",
            )

    def test_text_document_factory(self):
        text_factory = TextDocumentFactory()

        # Check supported type
        self.assertEqual(
            text_factory.supports_type(),
            DocumentType.TEXT,
            "If the factory supports TEXT type, it should return DocumentType.TEXT.",
        )

        # Create mock data
        document_name = "test_document.txt"
        path = "/path/to/test_document.txt"

        # Create objects using the factory
        processor = text_factory.create_processor(document_name)
        parser = text_factory.create_parser(path)
        printer = text_factory.create_printer(processor)

        # Check types of created objects
        self.assertIsInstance(
            processor,
            DocumentProcessor,
            "If the create_processor method is called, it should return an object of type DocumentProcessor.",
        )
        self.assertIsInstance(
            parser,
            DocumentParser,
            "If the create_parser method is called, it should return an object of type DocumentParser.",
        )
        self.assertIsInstance(
            printer,
            DocumentPrinter,
            "If the create_printer method is called, it should return an object of type DocumentPrinter.",
        )

    def test_spreadsheet_document_factory(self):
        spreadsheet_factory = SpreadsheetDocumentFactory()

        # Check supported type
        self.assertEqual(
            spreadsheet_factory.supports_type(),
            DocumentType.SPREAD_SHEET,
            "If the factory supports SPREAD_SHEET type, it should return DocumentType.SPREAD_SHEET.",
        )

        # Create mock data
        document_name = "test_spreadsheet.xlsx"
        path = "/path/to/test_spreadsheet.xlsx"

        # Create objects using the factory
        processor = spreadsheet_factory.create_processor(document_name)
        parser = spreadsheet_factory.create_parser(path)
        printer = spreadsheet_factory.create_printer(processor)

        # Check types of created objects
        self.assertIsInstance(
            processor,
            DocumentProcessor,
            "If the create_processor method is called, it should return an object of type DocumentProcessor.",
        )
        self.assertIsInstance(
            parser,
            DocumentParser,
            "If the create_parser method is called, it should return an object of type DocumentParser.",
        )
        self.assertIsInstance(
            printer,
            DocumentPrinter,
            "If the create_printer method is called, it should return an object of type DocumentPrinter.",
        )


if __name__ == "__main__":
    unittest.main()
