from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
import os

from dotenv import load_dotenv

load_dotenv()

instructor_embeddings = HuggingFaceInstructEmbeddings(
    model_name="hkunlp/instructor-large")
vectordb_file_path = os.environ['EMBEDDINGS_VECTOR_DB_DIRECTORY']


def create_vector_db():
    # Load data from FAQ sheet
    loader = CSVLoader(file_path='data/faqs.csv',
                       source_column="prompt")
    data = loader.load()

    # Create a FAISS instance for vector database from 'data'
    vectordb = FAISS.from_documents(documents=data,
                                    embedding=instructor_embeddings)

    # Save vector database locally
    vectordb.save_local(vectordb_file_path)


if __name__ == "__main__":
    create_vector_db()
