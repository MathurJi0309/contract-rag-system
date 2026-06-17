from app.services.document_processor import DocumentProcessor
from app.services.vector_store import VectorStoreService
from app.core.exceptions import BaseException


class DocumentService:

    def __init__(
        self,
        processor: DocumentProcessor,
        vector_db: VectorStoreService,
    ):
        self.processor = processor
        self.vector_db = vector_db

    async def upload_documents(self, files):
        if len(files) > 5:
            raise BaseException("Maximum 5 files per request.")

        results = []

        for file in files:
            content = await file.read()

            stored_path, document_id = self.processor.save_upload(
                file.filename,
                content
            )

            chunks = self.processor.load_and_split(
                stored_path,
                document_id,
                file.filename
            )

            self.vector_db.add_documents(chunks)

            results.append(
                {
                    "document_id": document_id,
                    "filename": file.filename,
                    "chunks_indexed": len(chunks),
                }
            )

        return results