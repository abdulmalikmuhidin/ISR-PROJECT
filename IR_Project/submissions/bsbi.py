import os
import heapq
import itertools
import math
from collections import Counter
from IR_Project.submissions.inverted_index import InvertedIndexMapper, InvertedIndexWriter

class BSBIIndex:
    def __init__(self, data_dir, output_dir):
        self.data_dir = data_dir
        self.output_dir = output_dir
        self.postings_dict = {}
        self.terms = []

    def parse_block(self, block_file_path):
        """Fixed: More robust parsing to ensure documents are found."""
        td_pairs = []
        if not os.path.exists(block_file_path): return []
        
        with open(block_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Split by .I followed by a space or newline
            docs = content.split('.I ')
            for doc in docs:
                if not doc.strip(): continue
                lines = doc.split('\n')
                
                # Get the first part which should be the ID
                doc_id_str = lines[0].strip()
                try:
                    # Clean the ID string (remove non-digits just in case)
                    doc_id = int(''.join(filter(str.isdigit, doc_id_str)))
                except (ValueError, IndexError):
                    continue

                if '.W' in doc:
                    text_content = doc.split('.W')[1].split('.I')[0].strip()
                    for token in text_content.split():
                        clean_token = token.strip('.,()[]{}:;"\'').lower()
                        if clean_token:
                            term_id = self.term_id_map[clean_token]
                            td_pairs.append((term_id, doc_id))
        return td_pairs

    def invert_write(self, td_pairs, index):
        td_pairs.sort()
        current_term = None
        doc_counts = Counter() 
        for term_id, doc_id in td_pairs:
            if term_id != current_term:
                if current_term is not None:
                    index.append(current_term, sorted(doc_counts.items()))
                current_term = term_id
                doc_counts = Counter()
            doc_counts[doc_id] += 1
        if current_term is not None:
            index.append(current_term, sorted(doc_counts.items()))

    def merge(self, indices, merged_index):
        """Fixed: Removed the 'from main import' to prevent ImportError."""
        iters = [iter(idx) for idx in indices]
        for term_id, group in itertools.groupby(heapq.merge(*iters), key=lambda x: x[0]):
            combined_postings = []
            for _, p_list in group:
                combined_postings = self._sorted_union(combined_postings, p_list)
            merged_index.append(term_id, combined_postings)

    def _sorted_union(self, list1, list2):
        """Helper for merging postings lists."""
        res = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            id1, f1 = list1[i]; id2, f2 = list2[j]
            if id1 == id2:
                res.append((id1, f1 + f2)); i += 1; j += 1
            elif id1 < id2:
                res.append(list1[i]); i += 1
            else:
                res.append(list2[j]); j += 1
        res.extend(list1[i:]); res.extend(list2[j:])
        return res

    def retrieve(self, query):
        tokens = [t.strip('.,()[]{}:;"\'').lower() for t in query.split()]
        if not tokens: return []
        scores = {} 
        N = 1400 
        with InvertedIndexMapper(self.index_file_path, postings_dict=self.postings_dict, terms=self.terms) as mapper:
            for token in tokens:
                term_id = self.term_id_map.str_to_id.get(token)
                if term_id is None: continue
                postings = mapper[term_id] 
                if not postings: continue
                
                df = len(postings)
                idf = math.log10(N / df)
                for doc_id, freq in postings:
                    tf = 1 + math.log10(freq)
                    scores[doc_id] = scores.get(doc_id, 0) + (tf * idf)
        
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return [str(doc_id) for doc_id, score in ranked]