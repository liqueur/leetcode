
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letter = 'abcdefghijklmnopqrstuvwxyz'
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        _dict = dict()

        for i in range(len(letter)):
            _dict[letter[i]] = code[i]

        _set = set()

        for word in words:
            s_code = ''
            for w in word:
                s_code += _dict[w]

            _set.add(s_code)

        return len(_set)


sol = Solution()
ret = sol.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
print(ret)
