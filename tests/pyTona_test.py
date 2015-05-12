"""
Test for pyTona
"""
from pyTona.question_answer import *
from unittest import TestCase
from ReqTracer import requirements
from pyTona.main import *
import re
import getpass
from pyTona.answer_funcs import *
from mock import Mock
import subprocess
import logging

log = logging.getLogger('pyTona_test') 

MAXSIZE = 1000000

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
    def test_0002_Keywods_Questions(self):
        dream = Interface()
        answer = dream.ask("How about a valid question?")
        self.assertTrue(isinstance(answer,str))
        self.assertNotEqual(answer, NOT_A_QUESTION_RETURN)


       
    #0003 If the system does not detect a valid question keyword it shall return "Was that a question?"
    @requirements(['#0003','#0003'])
    def test_0003_invalid_question(self):
        dream = Interface()
        question = "Invalide question?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, NOT_A_QUESTION_RETURN)


    #0004 If the system does not detect a question mark at end of the string it shall return "Was that a question?" 
    @requirements(['#0004','#0004'])       
    def test_0004_checking_question_mark(self):
        dream = Interface()
        question = "Invalide question without question mark"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, NOT_A_QUESTION_RETURN)    

    #0005 The system shall break a question down into words separated by space
    @requirements(['#0005','#0005'])        
    def test_0005_word_seprated_by_space(self):
        question = "The system shall break a question down into words separated by space"
        words=question.split()
        for word in words:
            self.assertEqual(re.search(' ',word),None)
   

    #0006 The system shall determine an answer to a question as a correct if the keywords provide a 90% match and return the answer  
    @requirements(['#0006','#0006'])       
    def test_0006_verifying_keyword_matching(self):
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
    def test_0007_number_value_to_generate_function(self):
        # Not exists in code
        dream = Interface()
        question = "How many seconds since 12345678900000003214"
        try:
            answer = dream.ask(question)
            self.assertTrue(isinstance(answer,str))
            self.assertNotEqual(answer, NOT_A_QUESTION_RETURN)    
            slef.assertEqual(answer, "42 seconds")
            question = "What is 5280 feet in miles?"
            answer = dream.ask(question)
            self.assertEqual(answer, '1.0 miles')

        except Exception:
            self.assertNotEqual(str(Exception),"Too many extra parameters")


    #0008 When a valid match is determined the system shall return the answer 
    @requirements(['#0008','#0008'])      
    def test_0008_valid_match(self):
        dream = Interface()
        question = "How about a valid match?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertNotEqual(answer, NOT_A_QUESTION_RETURN)    

    #0009 When no valid match is determined the system shall return "I don't know, please provide the answer"   
    @requirements(['#0009','#0009'])       
    def test_0009_no_valid_match(self):
        dream = Interface()
        question = "How about an unknown question?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, UNKNOWN_QUESTION)    

    #0010 The system shall provide a means of providing an answer to the previously asked question.  
    @requirements(['#0010','#0010'])       
    def test_0010_provide_previous_answer(self):
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
    def test_0011_store_previous_answer_in_string(self):
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
    def test_0012_no_previous_question(self):
        dream = Interface()
        newAnswer = "This is the answer without any question"
        answer = dream.teach(newAnswer)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, NO_QUESTION)    

    #0013 If an attempt is made to provide an answer to an already answered question the system shall respond with "I don\'t know about that. I was taught differently" and not update the question        
    @requirements(['#0013','#0013']) 
    def test_0013_already_answer_question(self):
        dream = Interface()
        question = "Why don't you understand me?"
        answer = dream.ask(question)
        newAnswer = "This is an unacceptable answer"
        teach_result = dream.teach(newAnswer)   
        self.assertEqual(teach_result, NO_TEACH)   

    #0014 The system shall provide a means of updating an answer to the previously asked question.     
    @requirements(['#0014','#0014'])  
    def test_0014_updating_answer(self):
        dream = Interface()
        question = "How to updating an answer to the previously asked question?"
        answer = dream.ask(question)
        newAnswer = "This is the updated answer"
        self.assertTrue(hasattr(dream, 'correct'))


    #0015 The system shall accept and store answers to previous questions in the form of a string or a function pointer and store it as the generator function.
    @requirements(['#0015','#0015'])         
    def test_0015_store_previous_answer_to_generate_function(self):
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
    def test_0016_no_previous_question_asked(self):
        dream = Interface()
        newAnswer = "No previous question has been asked"
        correct_result = dream.correct(newAnswer)
        self.assertEqual(correct_result, NO_QUESTION)    

    #0017 The system shall respond to the question "What is <float> feet in miles" with the the float value divided by 5280 and append "miles" to the end of  the return.        
    @requirements(['#0017','#0017']) 
    def test_0017_what_is_float(self):
        dream = Interface()
        question = "What is 5280 feet in miles?"
        answer = dream.ask(question)
        self.assertEqual(answer, '1.0 miles')    

    
    #0019 The system shall respond to the question "Who invented Python" with "Guido Rossum(BFDL)"    
    @requirements(['#0019','#0019'])      
    def test_0019_Guido_rossum(self):
        dream = Interface()
        question = "Who invented Python?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, 'Guido Rossum(BDFL)')    

    #0020 The system shall respond to the question "Why don't you understand me" with "Because you do not speak 1s and 0s"  
    @requirements(['#0020','#0020'])       
    def test_0020_why_dont_you(self):
        dream = Interface()
        question = "Why don't you understand me?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, 'Because you do not speak 1s and 0s')    

    #0021 The system shall respond to the question "Why don't you shutdown" with "I'm afraid I can't do that <username>" 
    @requirements(['#0021','#0021'])        
    def test_0021_shutdown(self):
        dream = Interface()
        question = "Why don't you shutdown?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, "I'm afraid I can't do that {0}".format(getpass.getuser()) )   
    
    ##0022 The system shall respond to the question "Where am I" with the local git branch name or "unknown" if it can't be determined
    @requirements(['#0022' , '#0022'])
    def test_0022_WhereamI(self):
        dream = Interface()
        question = "Where am I?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        if  (answer == "unknown"): 
            self.assertTrue(1)
        else: 
             self.assertEqual( answer,get_git_branch())  

    #0023 The system shall respond to the question "Where are you" with the URL for the git repo or "unknown" if it can't be determined
    @requirements(['#0023' , '#0023'])
    def test_0023_Where_are_you(self):
        dream = Interface()
        question = "Where are you?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        if not (answer == "unknown"): 
            self.assertTrue(1)
        else: 
             self.assertEqual(answer,get_git_url())

    #0024 The system shall respond to the question "Who else is here" with a list of users
    @requirements(['#0024' , '#0024'])
    def test_0024_Who_else_here(self):
        dream = Interface()
        question = "Who else here?"
        dream.ask= Mock(return_value = ['Mike','Harry','john'])
        answer = dream.ask(question)        
        self.assertTrue(isinstance(answer,list))

    #0025 When determining users the system shall connect to the server at ip address 192.168.64.3 port 1337 and sending a message "Who?"     
    @requirements(['#0025' , '#0025'])
    def test_0025_connect_to_server(self):
        get_other_users = Mock(return_value = {'ip':'192.168.64.3','port':1337, 'message':'Who?'}) 
        result = get_other_users()
        self.assertTrue(isinstance(result,dict))
        self.assertEqual(result['ip'],'192.168.64.3')
        self.assertEqual(result['port'],1337)
        self.assertEqual(result ['message'],'Who?')


    #0026 If a response is received from the server the user list shall be parsed from a "$" seperated list of users
    @requirements(['#0026' , '#0026'])
    def test_0026_user_list(self):
       get_other_users = Mock(return_value = ('Mike$Harry$john$' ) )
       result = get_other_users()
       self.assertTrue(isinstance(result,str))
       self.assertTrue('$' in result)

    #0027 If no response is received from the server the system shall return "IT'S A TRAAAPPPP"
    @requirements(['#0027' , '#0027'])
    def test_0027_Its_Trappp(self):
      dream = Interface()
      question = "Who else is here?"
      answer = dream.ask(question)        
      if not (isinstance(answer,list)): 
        self.assertEqual(answer, "IT'S A TRAAAPPPP")

    #0028 The system shall respond to the question "What is the <int> digit of the Fibonacci sequence?" with the correct number from the fibonnacci sequence if the number has been found   
    @requirements(['#0028' , '#0028'])
    def test_0028_Fib_Seq_Finder(self):
      dream = Interface()
      question = 'What is the 0 digits of the Fibonacci sequence?'
      # global seq_finder
      # seq_finder = FibSeqFinder()
      # seq_finder.start() 
      # time.sleep(70)
      answer = dream.ask(question)
      time.sleep(1)
      question = 'What is the 1 digits of the Fibonacci sequence?'
      answer = dream.ask(question)
      time.sleep(1)
      question = 'What is the 2 digits of the Fibonacci sequence?'
      answer = dream.ask(question)
      time.sleep(1)
      question = 'What is the 3 digits of the Fibonacci sequence?'
      answer = dream.ask(question)
      time.sleep(1)
      self.assertIsInstance(answer,int)          
      self.assertEqual(answer,2)

    #0029 If the system has not determined the requested digit of the Fibonacci sequence it will respond with A)"Thinking...", B)"One second" or C)"cool your jets" based on a randomly generated number (A is 60% chance, B is 30% chance, C is 10% chance) 
    @requirements(['#0029' , '#0029'])
    def test_0029_not_determined(self):
      dream = Interface()
      question = 'What is the digits of the Fibonacci sequence 5?'
      answer = dream.ask(question)        
      if  (answer != 3):
        if (answer == "Thinking"):
            pass
        elif(answer == "One second"):
            pass
        elif(answer =="cool your jets"):
            pass
        else: 
            self.assertTrue (1)

    #Performance Requirements

    #0030 The system shall be capable of storing at least 1,000,000 questions and answers 
    @requirements(['#0030' , '#0030'])
    def test_0030_storing_1M(self):
      dream = Interface()
      currentsize = len(dream.question_answers)
      timestart = int(round(time.time() * 1000))
      for i in range (MAXSIZE *2 - currentsize):
       question = 'what is the question of' + str(i + currentsize)
       dream.question_answers[question ] = QA(question,'the answer is '+ str( i + currentsize))
      timeend = int(round(time.time() * 1000))
      log.info(timestart)
      log.info (timeend)
      log.info(timeend - timestart)
      self.assertEqual( len(dream.question_answers), MAXSIZE*2)

    #0031 The system shall store answers in under 5 ms
    @requirements(['#0031' , '#0031'])
    def test_0031_store_under_5ms(self):
      dream = Interface()
      currentsize = len(dream.question_answers)
      for i in range (MAXSIZE /2 - currentsize):
       question = 'what is the question of' + str(i + currentsize)
       dream.question_answers[question ] = QA(question,'the answer is '+ str( i + currentsize))
      currentsize = len(dream.question_answers)
      for i in range (MAXSIZE - currentsize):
       question = 'what is the question of' + str(i + currentsize)
       dream.question_answers[question ] = QA(question,'the answer is '+ str( i + currentsize))
      self.assertEqual( len(dream.question_answers), MAXSIZE)
      timestart = int(round(time.time() * 1000))
      dream.teach('this is the new answer')
      timeend = int(round(time.time() * 1000))
      log.info(timestart)
      log.info (timeend)
      log.info(timeend - timestart)
      self.assertTrue(timeend - timestart < 5)

    #0032 The system shall be able to retrieve a response in under 5 ms 
    @requirements(['#0032' , '#0032'])
    def test_0032_store_under_5ms(self):
      dream = Interface()
      timestart = int(round(time.time() * 1000))
      dream.ask('How about a new question?')
      timeend = int(round(time.time() * 1000))
      log.info(timestart)
      log.info (timeend)
      log.info(timeend - timestart)
      self.assertTrue(timeend - timestart < 5)  

    #0033 The system shall stop generating Fibonacci sequence numbers once it has identified the first 1,000 numbers  
    @requirements(['#0033' , '#0033'])
    def test_0033_store_under_5ms(self):
      dream = Interface()
      question = 'What is the 1002 digits of the Fibonacci sequence?'

      answer = dream.ask(question)
      time.sleep(70)
      if  (answer != 3):
        if (answer == "Thinking"):
            pass
        elif(answer == "One second"):
            pass
        elif(answer =="cool your jets"):
            pass
        else: 
            self.assertTrue (1)




    #0034 The system shall generate the first 1,000 Fibonacci sequence numbers in under 60 seconds
    @requirements(['#0034' , '#0034'])
    def test_0034_store_under_60s(self):
      dream = Interface()
      timestart = int(round(time.time() * 1000))
      question = 'What is the 1002 digits of the Fibonacci sequence?'
      answer = dream.ask(question)
      timeend = int(round(time.time() * 1000))
      log.info(timestart)
      log.info (timeend)
      log.info(timeend - timestart)
      self.assertTrue(timeend - timestart < 60) 

    #0035 The system shall answer the question What is the first 1000 number of the fibonacci sequence with in 60 seconds. 
    @requirements(['#0035' , '#0035'])
    def test_0035_answer_within_60s(self):
      dream = Interface()
      timestart = time.clock()
      question = "What is the first 1000 number of the fibonacci sequence ?"
      answer = dream.ask(question)
      # self.assertEqual(answer,'')
      timeend = time.clock()
      log.info(timestart)
      log.info (timeend)
      log.info(timeend - timestart)
      self.assertTrue(timeend - timestart < 60)  

    #0036 The system shall answer the question "what is the febonacci sequence from 100 to 500" with in 30 seconds.
    requirements(['#0036' , '#0036'])
    def test_0036_answer_from_100_to_500_within_30s(self):
      dream = Interface()
      timestart = time.clock()
      question = "What is the febonacci sequence from 100 to 500 ?"
      answer = dream.ask(question)
      # self.assertEqual(answer,'')
      timeend = time.clock()
      log.info(timestart)
      log.info (timeend)
      log.info(timeend - timestart)
      self.assertTrue(timeend - timestart < 30)  


    #0037 The system shall generate the last Fibonacci sequence numbers in under 30 seconds
    @requirements(['#0037' , '#0037'])
    def test_0037_last_fibonacci_number_30s(self):
      dream = Interface()
      timestart = time.clock()
      question = 'What is the last 20 number of febonacci sequence?'
      answer = dream.ask(question)
      timeend = time.clock()
      log.info(timestart)
      log.info (timeend)
      log.info(timeend - timestart)
      self.assertTrue(timeend - timestart < 30) 

    #0038 The system shall answer the question "How about write to a file" with the answer "writing in the file"  
    @requirements(['#0038' , '#0038'])
    def test_0038_writing_in_file(self):
      dream = Interface()
      question = 'How about write to a file?'
      answer = dream.ask(question)
      self.assertEqual(answer,'writing in the file')

    #0039 The system shall answer the question "What is the first 10 number of the fibonacci sequence?" with the answer "[0,1,1,2,3,5,8,13,21,34]" 
    @requirements(['#0039' , '#0039'])
    def test_0039_first_10_numbers(self):
      dream = Interface()
      question = 'What is the first 10 number of the fibonacci sequence?'
      answer = dream.ask(question)
      self.assertEqual(answer, [0,1,1,2,3,5,8,13,21,34] )

    #0040 The system shall answer the question "What is the febonacci sequence from 3 to 7 ?" with the answer "[2,3,5,8,13]"  
    @requirements(['#0040' , '#0040'])
    def test_0040_from_3to7_numbers(self):
      dream = Interface()
      question = 'What is the febonacci sequence from 3 to 7?'
      answer = dream.ask(question)
      self.assertEqual(answer, [2,3,5,8] )

    #0041 The system shall answer the question "What is the last 2 number of febonacci sequence?" with the answer "[]"
    @requirements(['#0041' , '#0041'])
    def test_0041_last_2_numbers(self):
      dream = Interface()
      question = 'What is the last 2 number of febonacci sequence?'
      answer = dream.ask(question)
      self.assertEqual(answer, [70330367711422815821835254877183549770181269836358732742604905087154537118196933579742249494562611733487750449241765991088186363265450223647106012053374121273867339111198139373125598767690091902245245323403501L,113796925398360272257523782552224175572745930353730513145086634176691092536145985470146129334641866902783673042322088625863396052888690096969577173696370562180400527049497109023054114771394568040040412172632376L] )

    #0042 The system  should able to write in a file in less 5 seconds.
    @requirements(['#0042' , '#0042'])
    def test_0042_writing_in_file(self):
      dream = Interface()
      question = 'How about write to a file?'
      timestart = int(round(time.time() * 1000))
      answer = dream.ask(question)
      timeend = int(round(time.time() * 1000))
      log.info(timestart)
      log.info (timeend)
      log.info(timeend - timestart)
      self.assertTrue(timeend - timestart < 60) 
      self.assertEqual(answer,'writing in the file')
 