class CompressedPostings:
    @staticmethod
    def encode(postings_list):
        """
        Encodes a list of (doc_id, frequency) tuples.
        Uses Gap Encoding for doc_ids to keep them small.
        """
        data_to_encode = []
        last_id = 0
        
        for doc_id, freq in postings_list:
            gap = doc_id - last_id
            data_to_encode.append(gap)
            data_to_encode.append(freq) # Store the frequency right after the gap
            last_id = doc_id

        result = bytearray()
        for val in data_to_encode:
            bytes_list = []
            temp_val = val
            while True:
                bytes_list.insert(0, temp_val % 128)
                if temp_val < 128:
                    break
                temp_val //= 128
            bytes_list[-1] += 128 
            result.extend(bytes_list)
        return bytes(result)

    @staticmethod
    def decode(encoded_postings_list):
        """
        Decodes the byte stream back into a list of (doc_id, frequency) tuples.
        """
        numbers = []
        n = 0
        for b in encoded_postings_list:
            if b < 128:
                n = 128 * n + b
            else:
                n = 128 * n + (b - 128)
                numbers.append(n)
                n = 0
        
        postings = []
        current_id = 0
        # Iterate by 2 because we stored (gap, frequency) pairs
        for i in range(0, len(numbers), 2):
            gap = numbers[i]
            freq = numbers[i+1]
            current_id += gap
            postings.append((current_id, freq))
        return postings