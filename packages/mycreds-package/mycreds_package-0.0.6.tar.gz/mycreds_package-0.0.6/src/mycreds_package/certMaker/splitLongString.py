# Function to split long strings without breaking words


def splitLongString(str):
    def charCount(los):
        return len(' '.join(los))
    
    charHalf = len(str) // 2
    words = str.split()
    line1 = []
    line2 = []
    index = 0
    
    while charCount(line1) < charHalf:
        line1.append(words[index])
        index = index + 1
    line2 = words[index:]
    return(' '.join(line1), ' '.join(line2))