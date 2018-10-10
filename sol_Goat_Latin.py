
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split(' ')

        cnt = 1
        for i, _ in enumerate(words):
            if words[i][0].lower() in 'aeiou':
                words[i] = words[i] + 'ma' + 'a' * cnt
            else:
                words[i] = words[i][1:] + words[i][0] + 'ma' + 'a' * cnt

            cnt += 1

        return ' '.join(words)
