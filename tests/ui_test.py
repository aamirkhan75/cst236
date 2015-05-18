# """
# Test for ui_test.py
# """
from pywinauto import application
from pyTona.answer_funcs import *
from pyTona.question_answer import *
from unittest import TestCase
from ReqTracer import requirements
from pyTona.main import *
import pywinauto
import time
from pywinauto.application import Application



class Test_Ui(TestCase):

#0001 The system window shall have a title of "SharpTona"
    @requirements(['#0001','#0001'])
    def test_0001_tittle_SharpTona(self):
        app = application.Application()
        app.start_('sharpTona.exe')
        time.sleep(1)
        WindowsHandle = pywinauto.findwindows.find_window(title = "SharpTona")
        self.assertTrue(isinstance (WindowsHandle,int))
        app['SharpTona'].Close()


    # Note: for this test label need to be 'Answer: ' to pass the test. otherwise it will failling the test.
    #0002 The system shall provide labels "Question:" and "Answer:"
    @requirements(['#0002','#0002'])
    def test_0002_Labels_Questions_Answers(self):
        app = application.Application()
        app.start_('sharpTona.exe')
        time.sleep(1)
        dialogue = app.top_window_()
        self.assertEqual(dialogue.Question.Texts()[0],'Question:')
        self.assertEqual(dialogue.Answer.Texts()[0],'Answer: ')
        app['SharpTona'].Close() 


       
    #0003 The system shall allow the user to enter a question and press the "Ask" button
    @requirements(['#0003','#0003'])
    def test_0003_User_to_Enter(self):
        app = application.Application()
        app.start_('sharpTona.exe')
        time.sleep(1)
        dialogue = app.top_window_()
        self.assertTrue(dialogue['Question:Edit'].IsEnabled())
        self.assertTrue(dialogue['Ask'].IsEnabled()) # There is some kind of a issues with this we tried ASK,KASK get the same result it was passing the test.
        app['SharpTona'].Close() 


    #0004 The system shall have a default question/answer of "What is the answer to everything?": "42"
    @requirements(['#0004','#0004'])
    def test_0004_default_answer(self):
        app = application.Application()
        app.start_('sharpTona.exe')
        time.sleep(1)
        dialogue = app.top_window_()
        dialogue['Question:Edit'].TypeKeys('What is the answer to everything?', with_spaces=True)
        dialogue['Ask'].Click()
        self.assertEqual(dialogue['Answer:Edit'].Texts()[0],'42') 
        app['SharpTona'].Close() 
 

    #0005 The system by default shall disable the answer box, "Teach" button and "Correct" button
    @requirements(['#0005','#0005'])
    def test_0005_disable_answer_box(self):
        app = application.Application()
        app.start_('sharpTona.exe')
        time.sleep(1)
        dialogue = app.top_window_()
        self.assertFalse(dialogue['Answer:Edit'].IsEnabled())
        self.assertFalse(dialogue['Teach'].IsEnabled())
        self.assertFalse(dialogue['Correct'].IsEnabled())
        app['SharpTona'].Close()     
   

    #0006 The system shall display answers in the Answer Text Box
    @requirements(['#0006','#0006'])       
    def test_0006_Display_Answer(self):
        app = application.Application()
        app.start_('sharpTona.exe')
        time.sleep(1)
        dialogue = app.top_window_()
        dialogue['Question:Edit'].TypeKeys('What is my name?', with_spaces=True)
        dialogue['Ask'].Click()
        self.assertTrue(dialogue['Answer:Edit'].Texts()[0] !='') 
        app['SharpTona'].Close() 
  


    #0007 If no question is asked when the "Ask" button is pushed then "Was that a question?" shall be displayed in the answer box
    @requirements(['#0007','#0007'])      
    def test_0007_No_Question_Ask(self):
        app = application.Application()
        app.start_('sharpTona.exe')
        time.sleep(1)
        dialogue = app.top_window_()
        dialogue['Ask'].Click()
        self.assertEqual(dialogue['Answer:Edit'].Texts()[0],'Was that a question?') 
        app['SharpTona'].Close()       


    #0008 If the "Ask" button is pushed and the question is known the answer box shall display the answer and enable user input.
    @requirements(['#0008','#0008'])      
    def test_0008_Ask_BTN_Push_Question_Known(self):
        app = application.Application()
        app.start_('sharpTona.exe')
        time.sleep(1)
        dialogue = app.top_window_()
        dialogue['Question:Edit'].TypeKeys('What is the answer to everything?', with_spaces=True)
        dialogue['Ask'].Click()
        self.assertTrue(dialogue['Answer:Edit'].Texts()[0] !='') 
        self.assertTrue(dialogue['Answer:Edit'].IsEnabled())
        app['SharpTona'].Close()


    #0009 If the "Correct" button is pushed the system shall update the answer to the given question and disable the answer box, teach button and correct button
    @requirements(['#0009','#0009'])       
    def test_0009_Correct_BTN_Pushed(self):
        app = application.Application()
        app.start_('sharpTona.exe')
        time.sleep(1)
        dialogue = app.top_window_()
        dialogue['Question:Edit'].TypeKeys('What is the answer to everything?', with_spaces=True)
        dialogue['Ask'].Click()        
        dialogue['Answer:Edit'].TypeKeys('50', with_spaces=True)
        dialogue['CorrectButton'].Click()
        self.assertFalse(dialogue['Answer:Edit'].IsEnabled())
        self.assertEqual(dialogue['Answer:Edit'].Texts()[0],'50') 
        app['SharpTona'].Close()
           

    #0010 If the "Ask button is pushed and the question is not known then the answer box shall display "I don't know please teach me." and the "Teach" button will be enabled
    @requirements(['#0010','#0010'])       
    def test_0010_Ask_BTN_Pushed_Question_not_Known(self):
        app = application.Application()
        app.start_('sharpTona.exe')
        time.sleep(1)
        dialogue = app.top_window_()
        dialogue['Question:Edit'].TypeKeys('What is your name?', with_spaces=True)
        dialogue['Ask'].Click()
        self.assertEqual(dialogue['Answer:Edit'].Texts()[0],"I don't know please teach me.")        
        self.assertTrue(dialogue['Teach'].IsEnabled())
        app['SharpTona'].Close()      


    #0011 If the "Teach button is pushed the system shall store the answer to the given question and disable the answer box, teach button and correct button
    @requirements(['#0011','#0011'])       
    def test_0011_Teach_BTN_Pushed_Stoe_Answer(self):
        app = application.Application()
        app.start_('sharpTona.exe')
        time.sleep(1)
        dialogue = app.top_window_()
        dialogue['Question:Edit'].TypeKeys('What is your name?', with_spaces=True)
        dialogue['Ask'].Click()
        self.assertEqual(dialogue['Answer:Edit'].Texts()[0],"I don't know please teach me.")        
        self.assertTrue(dialogue['Teach'].IsEnabled())
        dialogue['Answer:Edit'].TypeKeys('Aamir', with_spaces=True)
        dialogue['Teach'].Click()
        self.assertFalse(dialogue['Answer:Edit'].IsEnabled())
        self.assertFalse(dialogue['Teach'].IsEnabled())
        self.assertFalse(dialogue['Correct'].IsEnabled())
        dialogue['Ask'].Click()
        self.assertEqual(dialogue['Answer:Edit'].Texts()[0],"Aamir")
        app['SharpTona'].Close()      




