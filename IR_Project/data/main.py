import os
import shutil
import time
from IR_Project.submissions.id_map import IdMap
from IR_Project.submissions.bsbi import BSBIIndex
from IR_Project.submissions.evaluator import CranEvaluator 

class MyBSBI(BSBIIndex):
    def __init__(self, data_dir, output_dir):
        super().__init__(data_dir, output_dir)
        self.term_id_map = IdMap()
        self.doc_id_map = IdMap() 
        self.index_file_path = os.path.join(output_dir, 'final_index.bin')

def setup_output_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        return
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
            else:
                os.unlink(file_path)
        except Exception:
            try:
                os.rename(file_path, os.path.join(directory, f"old_{int(time.time())}_{filename}"))
            except:
                pass

def run_project():
    data_folder = 'data'
    output_dir = 'output'
    
    doc_file = os.path.join(data_folder, 'cran.all.1400')
    
    # ADDED 'cran.qry' to the check list
    possible_queries = ['cran.qry', 'cran.query', 'crane.query']
    query_file = None
    for p in possible_queries:
        path = os.path.join(data_folder, p)
        if os.path.exists(path):
            query_file = path
            break
        
    rel_file = os.path.join(data_folder, 'cranqrel')

    setup_output_directory(output_dir)
    indexer = MyBSBI('.', output_dir)

    print("--- Step 1: Parsing & Indexing Doc Collection ---")
    td_pairs = indexer.parse_block(doc_file)
    unique_doc_count = len(set([pair[1] for pair in td_pairs]))
    print(f"Successfully indexed {unique_doc_count} documents.")

    from IR_Project.submissions.inverted_index import InvertedIndexWriter, InvertedIndexIterator
    block_path = os.path.join(output_dir, 'block_0.bin')
    with InvertedIndexWriter(block_path) as writer:
        indexer.invert_write(td_pairs, writer)
    
    with InvertedIndexIterator(block_path, writer.postings_dict, writer.terms) as reader:
        with InvertedIndexWriter(indexer.index_file_path) as final_writer:
            indexer.merge([reader], final_writer)
    
    indexer.postings_dict, indexer.terms = final_writer.postings_dict, final_writer.terms

    print("\n--- Step 2: Automated Evaluation ---")
    evaluator = CranEvaluator(query_file, rel_file)
    
    print(f"System loaded {len(evaluator.queries)} queries.")

    sample_queries = list(evaluator.queries.keys())[:10] 
    
    if not sample_queries:
        print(f"ERROR: Still no queries found in {query_file}.")
        return

    print(f"{'Q_ID':<5} | {'P@10':<6} | {'Query Snippet'}")
    print("-" * 75)
    total_p10 = 0
    for q_id in sample_queries:
        results = indexer.retrieve(evaluator.queries[q_id])
        p10 = evaluator.calculate_precision(results, evaluator.qrels.get(q_id, []), k=10)
        total_p10 += p10
        print(f"{q_id:<5} | {p10:<6.2f} | {evaluator.queries[q_id][:55]}...")

    print("-" * 75)
    print(f"Average Precision@10 for sample: {total_p10/len(sample_queries):.4f}")

if __name__ == "__main__":
    run_project()