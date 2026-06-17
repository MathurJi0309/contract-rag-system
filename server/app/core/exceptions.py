class BaseException(Exception):
    """Base exception for the application."""


class DocumentNotFoundError(BaseException):
    def __init__(self, document_id: str):
        self.document_id = document_id
        super().__init__(f"Document '{document_id}' not found.")


class UnsupportedFileTypeError(BaseException):
    def __init__(self, filename: str):
        super().__init__(f"Unsupported file type for '{filename}'. Only PDF, DOCX, and TXT are supported.")


class EmptyDocumentError(BaseException):
    def __init__(self, filename: str):
        super().__init__(f"No extractable text found in '{filename}'.")


class NoDocumentsIngestedError(BaseException):
    def __init__(self):
        super().__init__("No documents have been ingested yet. Upload a contract before querying.")
