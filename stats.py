def get_num_words (contents):
        return len(contents.split())

def get_character_frequency (contents):
        frequency_map = {}
        for ch in contents:
                curr_ch = ch.lower()
                curr_freq = frequency_map.get(curr_ch, 0)
                frequency_map[curr_ch] = curr_freq + 1
        return frequency_map

def sort_freq (item):        
        return item[1]

def sort_char_frequency (char_frequency):
        freq = list(char_frequency.items())
        freq.sort(reverse=True, key=sort_freq)
        return freq