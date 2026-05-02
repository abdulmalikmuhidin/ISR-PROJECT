# Information Retrieval Project Report

## Group Members

## Name .......................ID

## 1.Abdellah Nuruhussein ....UGR/5973/17

## 2.Abdulmalik Muhidin ......UGR/2859/17

## 3.Abdunasir Hassen........ UGR/4133/17

## 4.Alazr Wondifraw......... UGR/2894/17

## 5.Amin Ahmed ..............UGR/6904/17

## 6.Aymen Muhammed.......... UGR/7906/17

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

The project was executed in the following stages:

### Step 1: Environment Setup

Python environment was prepared and required libraries installed.

### Step 2: Data Preparation

The Cranfield dataset files were extracted and placed in the project folder.

### Step 3: Index Construction

The BSBI algorithm processed all documents and created the inverted index.

### Step 4: Query Processing

Queries from the benchmark set were tokenized and submitted to the search engine.

### Step 5: Ranking

TF-IDF scores were calculated for matching documents.

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
