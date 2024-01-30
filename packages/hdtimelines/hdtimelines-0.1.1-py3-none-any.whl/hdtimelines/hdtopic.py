import sys

# -- General idea: improves chances of tests and Sphinx builds working if this is included as a submodule
def add_submodule(path):
    if f"./{path}" not in sys.path:
        sys.path.insert(0,f"../../{path}") # -- Needed for Sphinx builds, usually run in the docs subdirectory
        sys.path.insert(0,f"./{path}")  # -- For normall running. Add second so it will go first in the search order
add_submodule("hdtimelines")

from hdtimelines import hdtimelineutils

class hdTopic():
    '''
    Holds a topic: a list of events and their corresponding ordinals

    Properties:

    * title (str): title of the topic
    * events (list of dict): events in this topic. Dictionary keys are allowed column names in a .csv file as specified in the README
    * ordinals (list of dicts): dictionaries of ordinals corresponding to the dates of events in this topic
    * event_display_lines (list of int): (possible future deprecation): lines on which to display the events
    '''
    def __init__(self, title="", events=None, id=None):
        """
        * title (str) : topic title
        * events (list of dict): events with which to populate the topic
        """
        self.title = title
        self.events = []
        self.ordinals = []
        self.event_display_lines = None
        self.id = id
        if events:
            self.events = events
            self.ordinals = [hdtimelineutils.calc_event_ordinals(event) for event in self.events]
    # ---------    
    def from_dict(self, d):
        """
        Populate existing hdTopic object from a dictionary d as created by *to_dict()*
        """
        self.title = d["title"]
        self.id = d["id"]
        self.events = d["events"]
        self.ordinals = d["ordinals"]
        self.event_display_lines = d["event_display_lines"]
    # ---------    
    def to_dict(self):
        """
        Convert hdTopic to a dictionary
        """
        d = {"title": self.title,
             "id": self.id,
             "events":self.events,
             "ordinals":self.ordinals,
             "event_display_lines":self.event_display_lines}
        return d
    # ---------
    def get_date_range(self):
        """
        Calculate earliest and latest date in this topic, and return them as 
        a duple (earliest, latest) of ordinals
        """
        mindate = min([d["earliest"] for d in self.ordinals])
        maxdate = max([d["latest"] for d in self.ordinals])
        return mindate, maxdate
    # ---------
    def xrange_breakpoints(self):
        bpoints = set()
        for ordset in self.ordinals:
            bpoints = bpoints | {ordset.get("min_xrange_years", None), ordset.get("max_xrange_years", None)}
        return bpoints - {None}

