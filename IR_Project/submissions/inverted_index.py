from IR_Project.submissions.compressed_postings import CompressedPostings

class InvertedIndex:
    def __init__(self, index_file_path, postings_dict=None, terms=None):
        self.index_file_path = index_file_path
        self.metadata_file_path = index_file_path + '.dict'
        self.postings_dict = postings_dict if postings_dict is not None else {}
        self.terms = terms if terms is not None else []

    def __enter__(self):
        # Open with 'a+' or 'rb+' depending on the child class
        self.index_file = open(self.index_file_path, 'rb+')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # CRITICAL: This is what releases the Windows Lock
        if hasattr(self, 'index_file'):
            self.index_file.close()

class InvertedIndexWriter(InvertedIndex):
    def __enter__(self):
        self.index_file = open(self.index_file_path, 'wb+')
        return self

    def append(self, term, postings_list):
        encoded = CompressedPostings.encode(postings_list)
        start_offset = self.index_file.tell()
        self.postings_dict[term] = (start_offset, len(postings_list), len(encoded))
        self.terms.append(term)
        self.index_file.write(encoded)

class InvertedIndexIterator(InvertedIndex):
    def __enter__(self):
        super().__enter__()
        self.current_term_idx = 0
        return self

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_term_idx >= len(self.terms):
            raise StopIteration
        term = self.terms[self.current_term_idx]
        offset, count, byte_len = self.postings_dict[term]
        self.index_file.seek(offset)
        encoded_data = self.index_file.read(byte_len)
        postings_list = CompressedPostings.decode(encoded_data)
        self.current_term_idx += 1
        return term, postings_list

class InvertedIndexMapper(InvertedIndex):
    def _get_postings_list(self, term):
        if term not in self.postings_dict: return []
        offset, count, byte_len = self.postings_dict[term]
        self.index_file.seek(offset)
        encoded_data = self.index_file.read(byte_len)
        return CompressedPostings.decode(encoded_data)

    def __getitem__(self, key):
        return self._get_postings_list(key)