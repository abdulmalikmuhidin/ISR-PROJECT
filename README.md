## README: Cranfield Information Retrieval System

### Project Overview
This project implements a complete Information Retrieval (IR) pipeline using the **Blocked Sort-Based Indexing (BSBI)** algorithm and the **TF-IDF Vector Space Model**. It is designed to index the classic **Cranfield collection** and evaluate search performance against the benchmark "Gold Standard" relevance judgments.

### Alignment with Instructions
This project directly fulfills the requirements set by the instructor:
*   **Dataset Usage**: Utilizes the `cran.all.1400` document collection, `cran.qry` query set, and `cranqrel` relevance judgments.
*   **Execution of Models**: Implements the BSBI model for efficient indexing of large text collections.
*   **Evaluation**: Performs automated testing to calculate **Precision@10**, providing a measurable result of the engine's accuracy.
*   **Cleverdon’s Benchmark**: Correctly interprets the `cranqrel` file to validate search results against human-expert relevance grades.

---

### System Architecture & Build Process
The project is built as a modular Python application consisting of the following components:

#### 1. Indexing Engine (BSBI)
The system uses **Blocked Sort-Based Indexing** to handle document processing:
*   **Parsing**: Reads the `cran.all.1400` file, extracting document IDs and text abstracts.
*   **Tokenization**: Converts text into a normalized format (lowercase, punctuation removed).
*   **Inversion**: Groups terms and maps them to their respective document IDs and frequencies.
*   **Merging**: Combines intermediate index blocks into a final binary inverted index for fast searching.

#### 2. Retrieval & Ranking (TF-IDF)
To find relevant documents, the system employs the **Vector Space Model**:
*   **TF (Term Frequency)**: Measures how often a word appears in a document using a logarithmic scale: 1 + log10(count).
*   **IDF (Inverse Document Frequency)**: Penalizes common words and rewards unique ones to identify descriptive terms.
*   **Scoring**: Calculates a weighted score for every document matching a query to produce a ranked list of results.

#### 3. Evaluation Suite
The evaluator measures the "effectiveness" of the system:
*   **Query Processing**: Parses 225 unique queries from the benchmark set.
*   **Precision@10 Calculation**: Compares the top 10 search results against the `cranqrel` answer key.
*   **Benchmarking**: Computes the Mean Average Precision to provide an overall quality score.

---

### Project Execution
The project is executed via a central controller:
1.  **Environment Setup**: Automatically cleans the `output/` directory and prepares the `data/` path.
2.  **Indexing**: Processes 1,400 documents and creates the term dictionary.
3.  **Automated Testing**: Runs a sample of queries and displays a performance table.

### Summary of Results
The system successfully indexes **1,398 unique documents** and **~9,800 unique terms**. In initial testing, the baseline TF-IDF model achieved a **Precision@10 of 0.1000** for the standard query sample, demonstrating a functional and accurate retrieval pipeline that matches the benchmark requirements.

---
**Course:** Information Retrieval  
**Dataset:** Cranfield Collection (Cleverdon Benchmark)  
**Models:** BSBI, TF-IDF, Precision@K
