#!/usr/bin/env python
import sys,random
# usage: ./trivia.py questions.txt
# questions.txt: alternating questions and answers separated by new lines
# license: http://creativecommons.org/licenses/GPL/2.0/

class Question(object):
    def __init__(self):
        super(Question, self).__init__()
        self.q=None
        self.a=None
    def parse_line(self,line):
        """returns True if this question is complete"""
        if line.strip():
            if self.q:
                self.a=line
            else:
                self.q=line
        return self.q and self.a
        
if __name__ == '__main__':
    trivia_rawtext=open(sys.argv[1])
    trivia_questions=[]
    question=Question()
    for l in trivia_rawtext:
        if question.parse_line(l):
            trivia_questions.append(question)
            question=Question()
    print """
        -----------
        Trivia.py
        
        Press any key to get a question. 
        Then press any key when you are ready for the answer. 
        
        Author:   Christine Corbett Moran 
        christine.corbett@gmail.com
        -----------
        """
    while True:
        question=random.choice(trivia_questions)
        print "-----"
        raw_input("")
        print "Q:",question.q
        raw_input("")
        print question.a
        print "-----"