class Solution:
    def reorderSpaces(self, text: str) -> str:
        #First attempt
        strings = text.split()
        spaceLength = text.count(" ")
        if len(strings) == 1:
            return strings[0] + " "*spaceLength
        else:
            spaceLength_per_word, spaceLength_extra = divmod(spaceLength, len(strings)-1)
            return (" "*spaceLength_per_word).join(strings) + " "*spaceLength_extra
