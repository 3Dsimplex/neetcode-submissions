class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            end = len(word)
            encoded_str = encoded_str + str(end) + "." + word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        is_index = True
        word_len_str = ""
        word = ""
        word_len = None

        for letter in s:
            if is_index:
                if letter == '.': 
                    is_index = False
                    word_len = int(word_len_str)
                else: word_len_str += letter
            elif word_len == 0: 
                decoded_strs.append(word)
                word = ""
                word_len_str = "" + letter
                is_index = True
            else: 
                word += letter
                word_len -= 1
        decoded_strs.append(word)

        if s: return decoded_strs
        else: return []
