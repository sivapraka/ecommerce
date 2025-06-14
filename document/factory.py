from document.products import DocumentType, DocumentProcessor, PresentationDocumentProcessor, SpreadsheetDocumentProcessor, TextDocumentProcessor


class DocumentFactory:
    @staticmethod
    def create_document(format_: DocumentType, name: str) -> DocumentProcessor:
        format = format_.value.lower()
        if format == "presentation":
            return PresentationDocumentProcessor(name)
        elif format == "text":
            return TextDocumentProcessor(name)
        elif format == "spreadsheet":
            return SpreadsheetDocumentProcessor(name)
        else:
            raise ValueError(f"Unsupported document format: {format}")


if __name__ == '__main__':
    doc1 = DocumentFactory.create_document(DocumentType.TEXT, "resume.txt")
    print(doc1.process_document())