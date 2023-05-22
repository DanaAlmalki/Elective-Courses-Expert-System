from experta import *

class Attribute(Fact):
  """Info about the students preference."""
  pass

class Matched(Fact):
  """Info about the rules executed."""
  pass

class SubjectSelector(KnowledgeEngine):
  @Rule(AND(Attribute(ar = ('y'), ts = ('y'), ns = ('y'), art = ('y'))))
  def Flower(self):
    engine.declare(Matched(flower = 't'))
    print('HHM-223: Ornamental Plants & Flower Assortment')
  @Rule(AND(Attribute(eng = ('y'), ts = ('y'), hs = ('y'), art = ('y'))))
  def Work(self):
    print('CPIT-490: Workplace Skills')
    engine.declare(Matched(work = 't'))
  @Rule(AND(Attribute(ar = ('y'), ex = ('y'), ts = ('y'), hs = ('y'))))
  def Elderly(self):
    print('HHM-246: Elderly Care')
    engine.declare(Matched(elderly = 't'))
  @Rule(AND(Attribute(ar = ('y'), ex = ('y'), ts = ('y'), ns = ('y'), hs = ('y'))))
  def Nutrition(self):
    print('FNU111: Principles of Nutrition ')
    engine.declare(Matched(nutrition = 't'))
  @Rule(AND(Attribute(eng = ('y'), ex = ('y'), ts = ('y'), hs = ('y'))))
  def English(self):
    print('ELAN-213: English for Communication')
    engine.declare(Matched(english = 't'))
  @Rule(AND(Attribute(eng = ('y'), ex = ('y'), ts = ('y'), ns = ('y'))))
  def Astronomy(self):
    print('ASTR-201: General Astronomy ')
    engine.declare(Matched(astronomy = 't'))
  @Rule(AND(Attribute(eng = ('y'), ex = ('y'), ts = ('y'), ht = ('y'), hs = ('y'))))
  def Tourism(self):
    print('HIST-431: Touristic Text in English')
    engine.declare(Matched(tourism = 't'))
  @Rule(AND(Attribute(ar = ('y'), ex = ('y'), ht = ('y'))))
  def KSAhistory(self):
    print('HIST-410: History of Saudi Arabia')
    engine.declare(Matched(ksaHistory = 't'))
  @Rule(AND(Attribute(ar = ('y'), ex = ('y'), ts = ('y'), ht = ('y'))))
  def Biography(self):
    print('HIST-221: Prophetic Biography ')
    engine.declare(Matched(biography = 't'))
  @Rule(AND(Attribute(ar = ('y'), ex = ('y'), ts = ('y'), hs = ('y'))))
  def Listening(self):
    print('ARAB290: Listening and Comprehension Skills')
    engine.declare(Matched(listening = 't'))
  @Rule(NOT(OR(Matched(flower = ('t')), Matched(work = ('t')), Matched(elderly = ('t')), Matched(nutrition = ('t')), Matched(english = ('t')), \
  Matched(astronomy = ('t')), Matched(tourism = ('t')), Matched(ksaHistory = ('t')), Matched(biography = ('t')), Matched(listening = ('t')) )))
  def default(self):
    print('Sorry, seems like no elective course match your preferences available...')  

print('Welcome to the Elective Courses Selector Program')
engine = SubjectSelector()
engine.reset()

cont = 'y'
while cont == 'y':
 print('\nDear student, please answer the following questions with y(yes) or n(no) \nto help us find the most suitable elective course/s for you:')
 u_eng = input('Do you prefer courses in english language? (y/n)').lower()
 u_ar = input('Do you prefer courses in arabic language? (y/n)').lower()
 u_ex = input('Do you prefer courses with exams? (y/n)').lower()
 u_ts = input('Do you prefer courses with tasks? (y/n)').lower()
 u_ns = input('Do you prefer courses in Natural Science? (y/n)').lower()
 u_ht = input('Do you prefer courses in History? (y/n)').lower()
 u_hs = input('Do you prefer courses in Human Science? (y/n)').lower()
 u_art = input('Do you prefer courses in Art? (y/n)').lower()
 engine.declare(Attribute(eng = u_eng, ar = u_ar, ex = u_ex, ts = u_ts, ns =    u_ns, ht = u_ht, hs = u_hs, art = u_art))
 print('\nMost suitable course/s:')
 engine.run()
 cont = input('\nWould you like to take the test again? (y/n)').lower() 
print('Thank you for using the Elective Courses Selector Program!')