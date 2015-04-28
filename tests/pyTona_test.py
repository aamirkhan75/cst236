"""
Test for pyTona
"""
from pyTona.question_answer import *
from unittest import TestCase
from ReqTracer import requirements
from pyTona.main import *
import re
import getpass

def answerGenerator():
    return "This is the Answer!"

class TestPyTona(TestCase):

    #0001 The system shall accept questions in the form of strings and attempt to answer them
    @requirements(['#0001','#0001'])
    def test_0001_string(self):
        question = "question string"
        #question = 1
        answer = ""
        result = QA(question, answer)
        #self.assertEqual(result,"a")
        self.assertTrue(isinstance(question, str))
        self.assertTrue(isinstance(result.value,str))


    @requirements(['#0001','#0001'])
    def test_0001_nonstring(self):
        question = 1
        dream = Interface()
        try:
            answer = dream.ask(question)
        except Exception as e:
            self.assertEqual(str(e),"Not A String!")

    #0002 The system shall answer questions that begin with one of the following valid question keywords: "How", "What", "Where", "Why" and "Who"
    @requirements(['#0002','#0002'])
    def test_0002(self):
        dream = Interface()
        answer = dream.ask("How about a valid question?")
        self.assertTrue(isinstance(answer,str))
        self.assertNotEqual(answer, NOT_A_QUESTION_RETURN)


       
    #0003 If the system does not detect a valid question keyword it shall return "Was that a question?"
    @requirements(['#0003','#0003'])
    def test_0003(self):
        dream = Interface()
        question = "Invalide question?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, NOT_A_QUESTION_RETURN)


    #0004 If the system does not detect a question mark at end of the string it shall return "Was that a question?" 
    @requirements(['#0004','#0004'])       
    def test_0004(self):
        dream = Interface()
        question = "Invalide question without question mark"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, NOT_A_QUESTION_RETURN)    

    #0005 The system shall break a question down into words separated by space
    @requirements(['#0005','#0005'])        
    def test_0005(self):
        question = "The system shall break a question down into words separated by space"
        words=question.split()
        for word in words:
            self.assertEqual(re.search(' ',word),None)
   

    #0006 The system shall determine an answer to a question as a correct if the keywords provide a 90% match and return the answer  
    @requirements(['#0006','#0006'])       
    def test_0006(self):
        dream = Interface()
        question = "How many seconds since 1942"
        try:
            answer = dream.ask(question)
            self.assertTrue(isinstance(answer,str))
            self.assertNotEqual(answer, NOT_A_QUESTION_RETURN)    
            slef.assertEqual(answer, "42 seconds")
        except Exception:
            self.assertNotEqual(str(Exception),"Too many extra parameters")

    #0007 The system shall exclude any number value from match code and provide the values to generator function (if one exists)   
    @requirements(['#0007','#0007'])      
    def test_0007(self):
        # Not exists in code
        self.assertTrue(0)   

    #0008 When a valid match is determined the system shall return the answer 
    @requirements(['#0008','#0008'])      
    def test_0008(self):
        dream = Interface()
        question = "How about a valid match?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertNotEqual(answer, NOT_A_QUESTION_RETURN)    

    #0009 When no valid match is determined the system shall return "I don't know, please provide the answer"   
    @requirements(['#0009','#0009'])       
    def test_0009(self):
        dream = Interface()
        question = "How about an unknown question?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, UNKNOWN_QUESTION)    

    #0010 The system shall provide a means of providing an answer to the previously asked question.  
    @requirements(['#0010','#0010'])       
    def test_0010(self):
        dream = Interface()
        question = "How about an unknown question?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, UNKNOWN_QUESTION) 
        newAnswer = "This is a known answer"
        dream.teach(newAnswer)   
        answer = dream.ask(question)
        self.assertEqual(answer, newAnswer) 



    #0011 The system shall accept and store answers to previous questions in the form of a string or a function pointer and store it as the generator function.
    @requirements(['#0011','#0011'])           
    def test_0011(self):
        dream = Interface()
        question = "How about an unknown question?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, UNKNOWN_QUESTION) 
        funcdict = {'answerGenerator': answerGenerator}
        newAnswer = funcdict['answerGenerator']()  
        dream.teach(newAnswer)   
        answer = dream.ask(question)
        self.assertEqual(answer, newAnswer) 
        


    #0012 If no previous question has been asked the system shall respond with "Please ask a question first"  
    @requirements(['#0012','#0012'])       
    def test_0012(self):
        dream = Interface()
        newAnswer = "This is the answer without any question"
        answer = dream.teach(newAnswer)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, NO_QUESTION)    

    #0013 If an attempt is made to provide an answer to an already answered question the system shall respond with "I don\'t know about that. I was taught differently" and not update the question        
    @requirements(['#0013','#0013']) 
    def test_0013(self):
        dream = Interface()
        question = "Why don't you understand me?"
        answer = dream.ask(question)
        newAnswer = "This is an unacceptable answer"
        teach_result = dream.teach(newAnswer)   
        self.assertEqual(teach_result, NO_TEACH)   

    #0014 The system shall provide a means of updating an answer to the previously asked question.     
    @requirements(['#0014','#0014'])  
    def test_0014(self):
        dream = Interface()
        question = "How to updating an answer to the previously asked question?"
        answer = dream.ask(question)
        newAnswer = "This is the updated answer"
        self.assertTrue(hasattr(dream, 'correct'))


    #0015 The system shall accept and store answers to previous questions in the form of a string or a function pointer and store it as the generator function.
    @requirements(['#0015','#0015'])         
    def test_0015(self):
        dream = Interface()
        question = "How to updating an answer to the previously asked question?"
        answer = dream.ask(question)
        newAnswer = "This is the updated answer"
        dream.correct(newAnswer)
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, newAnswer)    

    #0016 If no previous question has been asked the system shall respond with "Please ask a question first" 
    @requirements(['#0016','#0016'])     
    def test_0016(self):
        dream = Interface()
        newAnswer = "No previous question has been asked"
        correct_result = dream.correct(newAnswer)
        self.assertEqual(correct_result, NO_QUESTION)    

    #0017 The system shall respond to the question "What is <float> feet in miles" with the the float value divided by 5280 and append "miles" to the end of  the return.        
    @requirements(['#0017','#0017']) 
    def test_0017(self):
        dream = Interface()
        question = "What is 5280 feet in miles?"
        answer = dream.ask(question)
        self.assertEqual(answer, '1.0 miles')    

    #0018 The system shall respond to the question "How many seconds since <date time>" with the number of seconds from that point of day till now. 
    @requirements(['#0018','#0018'])        
    def test_0018(self):
        dream = Interface()
        question = "How many seconds since 1982?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertNotEqual(answer, UNKNOWN_QUESTION)    
        self.assertNotEqual(answer, '42 seconds') 

    #0019 The system shall respond to the question "Who invented Python" with "Guido Rossum(BFDL)"    
    @requirements(['#0019','#0019'])      
    def test_0019(self):
        dream = Interface()
        question = "Who invented Python?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, 'Guido Rossum(BFDL)')    

    #0020 The system shall respond to the question "Why don't you understand me" with "Because you do not speak 1s and 0s"  
    @requirements(['#0020','#0020'])       
    def test_0020(self):
        dream = Interface()
        question = "Why don't you understand me?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, 'Because you do not speak 1s and 0s')    

    #0021 The system shall respond to the question "Why don't you shutdown" with "I'm afraid I can't do that <username>" 
    @requirements(['#0021','#0021'])        
    def test_0021(self):
        dream = Interface()
        question = "Why don't you shutdown?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, "I'm afraid I can't do that {0}".format(getpass.getuser()) )   

                  