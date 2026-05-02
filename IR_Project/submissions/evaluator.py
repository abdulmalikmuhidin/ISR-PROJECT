import os
import re

class CranEvaluator:
    def __init__(self, query_file, rel_file):
        self.queries = self._parse_queries(query_file)
        self.qrels = self._parse_qrels(rel_file)

    def _parse_queries(self, filepath):
        queries = {}
        if not filepath or not os.path.exists(filepath):
            return {}
            
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            # This regex captures the ID and the content following it
            items = re.findall(r'\.I\s+(\d+)(.*?)(?=\.I\s+|$)', content, re.DOTALL)
            
            for q_id_str, body in items:
                q_id = q_id_str.lstrip('0') or '0'
                if '.W' in body:
                    # Extract the text specifically under the .W tag
                    text = body.split('.W')[1].strip().replace('\n', ' ')
                    queries[q_id] = ' '.join(text.split())
        return queries

    def _parse_qrels(self, filepath):
        qrels = {} 
        if not filepath or not os.path.exists(filepath):
            return {}
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.split()
                if len(parts) >= 2:
                    q_id = parts[0].lstrip('0') or '0'
                    doc_id = parts[1].lstrip('0') or '0'
                    if q_id not in qrels:
                        qrels[q_id] = []
                    qrels[q_id].append(doc_id)
        return qrels

    def calculate_precision(self, retrieved_ids, relevant_ids, k=10):
        if not relevant_ids: return 0.0
        top_k = retrieved_ids[:k]
        hits = len(set(top_k) & set(relevant_ids))
        return hits / k