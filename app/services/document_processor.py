import os
import uuid
from pathlib import Path
from typing import List

from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from app.core.config import settings
from app.core.exceptions import UnsupportedFileTypeError, EmptyDocumentError

DOCUMENT_TYPES = {
    ".pdf": PyPDFLoader,
    ".docx": Docx2txtLoader,
    ".txt": TextLoader,
}


class DocumentProcessor:
    """
     Here we do loading of file from where it store and extracting content
     and after storing it we load the data and split into the chunks.


    using RecursiveCharacterTextSplitter we can do chunking  .
    """

    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap,
        )

    def save_upload(self, filename: str, content: bytes) -> str:
        os.makedirs(settings.upload_dir, exist_ok=True)
        extension = Path(filename).suffix.lower()
        if extension not in DOCUMENT_TYPES:
            raise UnsupportedFileTypeError(filename)

        document_id = str(uuid.uuid4())
        stored_path = os.path.join(settings.upload_dir, f"{document_id}{extension}")
        with open(stored_path, "wb") as f:
            f.write(content)
        return stored_path, document_id

    def load_and_split(
        self, filepath: str, document_id: str, filename: str
    ) -> List[Document]:
        extension = Path(filepath).suffix.lower()
        loader_cls = DOCUMENT_TYPES.get(extension)
        if loader_cls is None:
            raise UnsupportedFileTypeError(filename)

        raw_docs = loader_cls(filepath).load()
        full_text = "\n".join(d.page_content for d in raw_docs).strip()

        if not full_text:
            raise EmptyDocumentError(filename)

        chunks = self.splitter.split_text(full_text)

        return [
            Document(
                page_content=chunk,
                metadata={
                    "document_id": document_id,
                    "filename": filename,
                    "chunk_index": idx,
                },
            )
            for idx, chunk in enumerate(chunks)
        ]
