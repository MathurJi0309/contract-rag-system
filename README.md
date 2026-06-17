# AI-Based Contract Analysis System

## Overview

AI-Based Contract Analysis System is a Retrieval-Augmented Generation (RAG) application designed to analyze legal and contract documents and answer user questions based on their content.

The system allows authenticated users to upload contract documents, process them into vector embeddings, and interact with the documents through an AI-powered chat interface. Responses are generated using relevant document context retrieved from a vector database, ensuring answers remain grounded in the uploaded documents rather than general knowledge.

---

## Features

* User Registration and Authentication
* Contract Document Upload
* Automatic Document Processing and Chunking
* OpenAI Embedding Generation
* Semantic Search using ChromaDB
* AI-Powered Question Answering
* React Frontend
* FastAPI Backend
* MongoDB Integration
* Local Vector Storage

---

## Tech Stack

### Frontend

* React.js
* Bootstrap

### Backend

* FastAPI
* Python

### Database

* MongoDB

### Vector Database

* ChromaDB (Local Storage)

### AI & NLP

* OpenAI
* LangChain

---


# Frontend Setup

Navigate to the frontend directory:

```bash
cd frontend
```

### Create Environment File

Copy the example environment file:

```bash
cp .env.example .env
```

Update the values if required.

### Install Dependencies

```bash
npm install
```

### Run Frontend

```bash
npm run dev
```

The frontend application will start and connect to the backend APIs.

---

# Backend Setup

Navigate to the server directory:

```bash
cd server
```

### Create Virtual Environment

```bash
python3 -m venv venv
```

### Activate Virtual Environment

Linux / Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file using `.env.example`.

Example:

```env
OPENAI_API_KEY=your_openai_api_key
MONGODB_URL=your_mongodb_connection_string
DATABASE_NAME=contract_analysis
```

### Required Variables

| Variable       | Description               |
| -------------- | ------------------------- |
| OPENAI_API_KEY | OpenAI API Key            |
| MONGODB_URL    | MongoDB Connection String |
| DATABASE_NAME  | MongoDB Database Name     |

Other variables can remain unchanged unless customization is required.

---

## Storage Directories

The application automatically creates the required storage directories during runtime:

```text
data/uploads
data/vectorstore
```

No manual setup is required.

---

## Run Backend

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

# Usage

### Step 1

Register a new account.

### Step 2

Login using your credentials.

### Step 3

Upload one or more legal or contract documents.

### Step 4

Wait for document processing and indexing to complete.

### Step 5

Ask questions related to the uploaded documents.

### Step 6

Receive answers generated from the retrieved document context.


---

## Current Limitations

### No User-Specific Document Isolation

Documents uploaded by one authenticated user are currently available to all authenticated users.

Document ownership and access control have not yet been implemented.

### No Conversational Memory

Each question is processed independently.

Previous questions and responses are not retained as conversational context.

### Local Vector Storage

ChromaDB is stored locally inside the project and is not configured as a distributed or managed vector database.



## Evaluation Objectives

This project demonstrates:

* Document Understanding
* Semantic Retrieval
* Retrieval-Augmented Generation (RAG)
* FastAPI Backend Development
* Authentication & Authorization
* Vector Search Implementation
* AI-Powered Contract Question Answering

---

## Assumptions

* Documents are primarily legal or contract-based.
* OpenAI API access is available.
* Uploaded documents are processed before querying.
* Authentication is required before accessing protected endpoints.


---


## System Architecture

```text
User
 │
 ▼
React Frontend
 │
 ▼
FastAPI Backend
 │
 ▼
routes/
 │
 ▼
modules/
 │
 ├── users
 │
 ├── documents
 │      │
 │      ▼
 │   document_processor.py
 │      │
 │      ▼
 │   vector_store.py
 │
 └── query
        │
        ▼
   vector_store.py
        │
        ▼
     llm_chain.py
        │
        ▼
    OpenAI API

MongoDB
 │
 └── User & Application Data

ChromaDB (Local)
 │
 └── Document Embeddings
```

---

## Project Structure

```text
contract-rag-system/
│
├── frontend/
│
└── server/
    │
    ├── app/
    │   │
    │   ├── core/
    │   │
    │   ├── modules/
    │   │   │
    │   │   ├── documents/
    │   │   │   ├── controller.py
    │   │   │   ├── dependencies.py
    │   │   │   ├── router.py
    │   │   │   └── service.py
    │   │   │
    │   │   ├── query/
    │   │   │   ├── controller.py
    │   │   │   ├── dependencies.py
    │   │   │   ├── dto.py
    │   │   │   ├── router.py
    │   │   │   └── service.py
    │   │   │
    │   │   ├── users/
    │   │   └── health/
    │   │
    │   ├── routes/
    │   │
    │   ├── services/
    │   │   ├── document_processor.py
    │   │   ├── llm_chain.py
    │   │   └── vector_store.py
    │   │
    │   └── main.py
    │
    ├── data/
    │   ├── uploads/
    │   └── vectorstore/
    │
    ├── requirements.txt
    ├── .env.example
    └── .env
```

---

## Backend Architecture

The backend follows a modular architecture to ensure scalability, maintainability, and separation of concerns.

### Core Layer

Contains shared application configurations and utilities such as:

* Database configuration
* Environment settings
* Authentication helpers
* Shared utilities

### Routes Layer

Acts as the centralized routing layer responsible for registering all API routes.

### Modules Layer

#### Users Module

Responsible for:

* User Registration
* User Login
* Authentication

#### Documents Module

Responsible for:

* File Upload
* Document Validation
* Document Processing
* Embedding Creation
* Vector Storage

#### Query Module

Responsible for:

* Similarity Search
* Context Retrieval
* Answer Generation

#### Health Module

Responsible for:

* Health Check APIs

### Services Layer

Contains reusable business logic:

#### document_processor.py

Handles:

* Text Extraction
* Text Chunking
* Pre-processing

#### vector_store.py

Handles:

* Embedding Storage
* Similarity Search
* ChromaDB Operations

#### llm_chain.py

Handles:

* Prompt Construction
* Context Injection
* OpenAI Response Generation

---

## Application Flow

### Document Upload Flow

```text
User Uploads Contract
        │
        ▼
Document Module
        │
        ▼
Document Processor
        │
        ▼
Chunk Creation
        │
        ▼
OpenAI Embeddings
        │
        ▼
ChromaDB Storage
```

### Query Flow

```text
User Question
        │
        ▼
Query Module
        │
        ▼
Convert Question to Embedding
        │
        ▼
Retrieve Relevant Chunks
        │
        ▼
Build Prompt with Context
        │
        ▼
OpenAI LLM
        │
        ▼
Generate Answer
        │
        ▼
Return Response
```

---


## Design Decisions

### Why FastAPI?

* High performance
* Automatic OpenAPI documentation
* Excellent async support
* Clean and maintainable architecture

### Why MongoDB?

* Flexible schema design
* Easy integration with FastAPI
* Suitable for user and application metadata

### Why ChromaDB?

* Lightweight
* Open source
* Easy local deployment
* No additional infrastructure required

### Why Retrieval-Augmented Generation (RAG)?

RAG ensures:

* Answers remain grounded in uploaded documents
* Reduced hallucinations
* Better contextual accuracy
* Improved trustworthiness of responses

---

## Author

Developed as part of the AI-Based Contract Analysis System By Anilesh Mathur.
