from datetime import datetime, date
import dateutil.parser
class ViewModel:

    current_date = str(date.today())
    current_date1 = "2020-07-28T14:56:22.343Z"
    covert_time1 = datetime.strptime("2020-08-01T14:56:22.343Z",'%Y-%m-%dT%H:%M:%S.%fZ')
    reformat_time = datetime.strftime(covert_time1, "%Y-%m-%d")

    print("curr date:", current_date)
    print("utc date:", current_date1)

    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    #below is the same as the list comprehension. use yield for iterate items
    #def to_do_items(self):
    #    for item in self._items:
    #        if item.status == "To Do":
    #            yield item
    def to_do_items(self):
        return [item for item in self._items if item.status == "To Do"]
        
    @property
    def doing_items(self):
        return [item for item in self._items if item.status == "Pending"]

    @property
    def done_items(self):
        return [item for item in self._items if item.status == "Done"]

#updated item.update_time is now just a date. No need to convert frmo string to date first)
    @property
    def show_recent_done(self):
        today = self.current_date
        
        for item in self.done_items:
            reformat_time = datetime.strftime(item.update_time, "%Y-%m-%d")
            if reformat_time == today:
                yield item   ##yield creates a generator list. use return instead
        
                        
  # below is same as above but with for loop, this is to see if it helps with testing                  
  #  @property
  #  def show_recent_done(self):
  #      return [item for item in self.done_items if datetime.strftime(datetime.strptime(item.update_time,'%Y-%m-%dT%H:%M:%S.%fZ'), "%Y-%m-%d") == self.current_date ] ## THIS WORKS!
           
    @property
    def show_recent_if_gt_5_all_if_lt_5_done(self):
        print(len(self.done_items))
        if len(self.done_items) > 5:
            return self.show_recent_done
        elif len(self.done_items) <= 5: 
            return self.done_items[0:5]
