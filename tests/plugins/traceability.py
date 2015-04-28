import logging
import os

from nose2.events import Plugin

log = logging.getLogger('nose2.plugins.traceability')


class Traceability(Plugin):
    configSection = 'traceability'
    commandLineSwitch = (None, 'traceability', 'trace!')


    # def getTestCaseNamesEvent(self, event):
    #     print "+++++",event.testcase.id()

    def startTestRun(self, event):
        log.info("check requirement!")
        # for r in self.requirements:
        # 	log.info(r)
    def testOutCome(self, event):
    	log.info('outcome++++++++' + event.outcome)

    def startTest(self, event):
        log.info('startTest++++++++' + event.test)    	

    def stopTest(self, event):
        log.info("stop test")        

	def outcomeDetail(self, event):
		log.info("outcome detail")        

"""
	def reportFailure(self, event):
		log.info("test failed!")
"""		

