# Information Retrieval Project Report

## Group Members

## Name .......................ID

## 1.Abdulmalik Muhidin ......UGR/2859/17

## 2.Abdunasir Hassen........ UGR/4133/17

## 3.Alazar Wondifraw......... UGR/2894/17

## 4.Amin Ahmed ..............UGR/6904/17

## 5.Aymen Muhammed.......... UGR/7906/17

## Title

Implementation of an Information Retrieval System using BSBI and TF-IDF on the Cranfield Collection

## Course

Information Retrieval Systems

## 1. Introduction

The purpose of this project was to design and implement a complete Information Retrieval (IR) pipeline using Python. The system was developed to index documents, process user queries, rank relevant results, and evaluate retrieval effectiveness using a standard benchmark dataset. The project demonstrates the practical application of indexing and ranking algorithms commonly used in search engines.

---

## 2. Objectives

The major objectives of the project were:

- To understand how Information Retrieval systems work.
- To implement an indexing algorithm for document collections.
- To rank retrieved documents using TF-IDF weighting.
- To evaluate system performance using benchmark relevance judgments.
- To gain practical experience using real-world IR datasets.

---

## 3. Dataset Used

The project used the **Cranfield Collection**, one of the classic benchmark datasets in Information Retrieval research.

The dataset contains three major files:

### a) `cran.all.1400`

Contains 1,400 technical documents related to aeronautical engineering.

### b) `cran.qry`

Contains user search queries used to test the system.

### c) `cranqrel`

Contains relevance judgments indicating which documents are relevant to each query.

This benchmark was originally developed by Cleverdon and is widely used to evaluate retrieval systems.

---

## 4. Models and Techniques Used

## 4.1 Blocked Sort-Based Indexing (BSBI)

The indexing component used the BSBI algorithm. This method is efficient for large collections because it processes documents in blocks.

Main steps:

- Parse documents
- Tokenize text
- Create term-document pairs
- Sort terms
- Merge blocks into final inverted index

### Benefits:

- Efficient memory usage
- Suitable for large-scale indexing
- Faster retrieval preparation

---

## 4.2 TF-IDF Vector Space Model

The ranking component used TF-IDF weighting.

### Term Frequency (TF)

Measures how often a term appears in a document.

### Inverse Document Frequency (IDF)

Gives lower weight to common words and higher weight to rare informative words.

### Final Ranking

Documents are scored according to relevance to the query, and top results are returned.

---

## 5. Execution Process
1.  **Block Parsing**: The collection is split into manageable "blocks" (e.g., 500 documents at a time) [cite: 12].
2.  **ID Mapping**: Each unique term encountered is mapped to a `term_id`, and each document is mapped to a `doc_id`. This reduces the memory footprint by replacing long strings with integers [cite: 12].
3.  **In-Memory Sorting**: For each block, the system generates a list of `(term_id, doc_id)` pairs. This list is sorted primarily by `term_id` and secondarily by `doc_id` [cite: 12].
4.  **Local Inversion**: The sorted pairs are transformed into a local inverted list (a "postings list") for that specific block [cite: 12].
5.  **Disk Write**: These blocks are saved as temporary binary files to disk [cite: 12].
6.  **Multi-Way Merge**: The final step involves reading all temporary blocks simultaneously. The system uses a **Min-Heap** to efficiently merge these sorted lists into one final, global inverted index [cite: 12].

---

## Python Module Deep Dive

### A. `bsbi.py` (The Construction Engine)
This script is responsible for transforming raw text into the search engine's "brain" [cite: 12].

*   **Functionality**: Coordinates the block-based parsing and the final merge operation [cite: 12].
*   **Execution Trace**:
    *   Initialize the `term_dictionary` [cite: 12].
    *   Process Documents $1 \to 500$, creating `block_0.bin` [cite: 12].
    *   Process Documents $501 \to 1000$, creating `block_1.bin` [cite: 12].
    *   Run the merge function to produce the final `index.bin` [cite: 12].

### B. `main.py` (The Retrieval & Evaluation Engine)
This is the operational interface of the system, handling queries and performance benchmarking [cite: 12].

*   **Functionality**: It loads the index, processes queries using the **Vector Space Model**, and calculates accuracy against the `cranqrel` file [cite: 12].
*   **Ranking Mechanism**: It calculates the **TF-IDF** (Term Frequency-Inverse Document Frequency) weights for terms and ranks documents based on **Cosine Similarity** [cite: 12].

---

## Ranking Mathematics: The Vector Space Model
The system does not just find documents that contain a word; it ranks them by relevance [cite: 12].

### TF-IDF Weighting
Each term $t$ in document $d$ is assigned a weight $w$ to prioritize words that are frequent in a specific document but rare across the entire collection of $N$ documents [cite: 12]:

$$w_{t,d} = \text{tf}_{t,d} \times \log\left(\frac{N}{\text{df}_t}\right)$$

### Cosine Similarity
To rank document $D$ against query $Q$, the system treats both as vectors in a high-dimensional space and calculates the cosine of the angle between them [cite: 12]:

$$\text{score}(Q, D) = \frac{\sum Q_i D_i}{\sqrt{\sum Q_i^2} \sqrt{\sum D_i^2}}$$

Documents with higher scores are returned at the top of the search results [cite: 12].

---

### Step 6: Evaluation

Retrieved results were compared with the benchmark relevance judgments.

---

## 6. Evaluation Results

The implemented system successfully indexed approximately:

- 1,398 documents
- Around 9,800 unique terms

Initial experiments produced:

- **Precision@10 = 0.1000**

This means that, on average, 1 out of the top 10 returned documents was relevant in the tested baseline setup.

---

## 7. Discussion

The project successfully demonstrated all major stages of an Information Retrieval system.

### Strengths:

- Functional indexing pipeline
- Fast retrieval using inverted index
- Standard benchmark evaluation
- Clear modular design

### Limitations:

- Baseline TF-IDF model can be improved
- No stemming or advanced preprocessing
- Precision can be increased with better ranking methods

### Possible Improvements:

- BM25 ranking model
- Stopword removal
- Stemming / Lemmatization
- Query expansion
- Better evaluation metrics (MAP, Recall)

---

## 8. Challenges Faced

During implementation, some practical challenges were encountered:

- Dataset extraction and file handling
- Environment setup
- Understanding notebook execution flow
- Running experiments correctly

These challenges were solved through debugging and proper configuration.

---

## 9. Conclusion

This project provided practical experience in building a complete search engine pipeline using standard IR methods. By combining BSBI indexing and TF-IDF ranking, the system was able to retrieve documents from the Cranfield benchmark and measure performance scientifically. The project strengthened understanding of indexing, ranking, evaluation, and real-world Information Retrieval systems.

---

## 10. References

- Cranfield Collection Benchmark Dataset
- Information Retrieval course materials
- Python documentation
- TF-IDF and Inverted Index literature
