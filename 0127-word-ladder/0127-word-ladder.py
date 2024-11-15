'''
beginWord에서 endWord로 변환하는 가장 짧은 단어 변환 과정을 찾는 문제.
변환 과정은 wordList 안에 있는 단어들을 사용해야하며, 변환 규칙은 각 변환마다 한 글자만 달라야 한다는 것

Test Cases
hit -> hot -> dot -> dog -> cog

beginWord 는 wordList에 있을 필요가 없지만 endWord는 wordList에 있어야한다. 
ouptut: 변환 과정에서 거치는 단어의 수 출력. 변환이 불가능하다면 0 반환

'''
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        queue = deque([(beginWord, 1)]) # (단어, 변환 횟수)
        alphabet = 'abcdefghijklmnopqrstuvwxyz' 

        while queue:
            curr_word, length = queue.popleft()

            if curr_word == endWord:
                return length
            
            for i in range(len(curr_word)):
                original_char = curr_word[i]
                for char in alphabet:
                    new_word = curr_word[:i] + char + curr_word[i+1:]
                    if new_word in word_set:
                        queue.append((new_word, length + 1))
                        word_set.remove(new_word) # 방문한 단어는 set에서 제거
        return 0


        
        