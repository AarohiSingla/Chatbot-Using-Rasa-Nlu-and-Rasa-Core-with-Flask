from typing import Dict, Text, Any, List, Union, Optional

from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher
#from rasa_core.actions.action import Action
from rasa_core_sdk import Action
from rasa_core_sdk.forms import FormAction



class Courses(Action):
 def name(self):
  """name of the custom action"""
  return "action_courses"  
 def run(self,dispatcher,tracker,domain):
  
  dispatcher.utter_message("https://www.piford.com/courses.php")
  return []    