# from trello_class import TrelloItem
from todo_item import TodoItem
from view_model import ViewModel
import pytest
from datetime import datetime, timedelta, date
from dotenv import load_dotenv  #to invoke .env file
import os
from user import User, Role

load_dotenv()

def test_filters_by_status(): # first test to see if view model item matches each status
    created_todo = TodoItem(1, "Test in progress Todo", "To Do", datetime.now())
    pending_todo = TodoItem(2, "Test Pending Todo", "Pending", datetime.now())
    done_todo = TodoItem(3, "Test Done Todo", "Done", datetime.now())

    todos = [
        created_todo,
        pending_todo,
        done_todo
    ]

    # added as part of module 10 project
    reader = "ReadOnly"

    view_model = ViewModel(todos, reader)
    
    assert view_model.to_do_items == [created_todo]
    assert view_model.doing_items == [pending_todo]
    assert view_model.done_items == [done_todo]

@pytest.fixture # first way of setting the fixture
def item_view():
    reader = "ReadOnly"

    created_todo = TodoItem(1, "Test in progress Todo", "To Do", date.today())
    created_todo2 = TodoItem(2, "Test in progress Todo", "To Do", date.today())
    created_todo3 = TodoItem(3, "Test in progress Todo", "To Do", date.today())
    pending_todo = TodoItem(4, "Test Pending Todo", "Pending", date.today())
    pending_todo2 = TodoItem(5, "Test Pending Todo", "Pending", date.today())
    done_todo = TodoItem(6, "You're not done", "Done", date.today() - timedelta(days = 2))
    done_todo2 = TodoItem(7, "Are you sure you're done", "Done", date.today() - timedelta(days = 3))
    done_todo3 = TodoItem(8, "Are you sure you're done1", "Done", date.today() - timedelta(days = 4))
    done_todo4 = TodoItem(9, "Are you sure you're done2", "Done", date.today() - timedelta(days = 5))
    done_todo5 = TodoItem(10, "Are you sure you're done3", "Done", date.today())
    done_todo6 = TodoItem(11, "Are you sure you're done4", "Done", date.today())

    todos = [
        created_todo,
        created_todo2,
        created_todo3,
        pending_todo,
        pending_todo2,
        done_todo,
        done_todo2,
        done_todo3,
        done_todo4,
        done_todo5,
        done_todo6
    ]

    return ViewModel(todos, reader)
    
@pytest.fixture # 2nd way of setting the fixture
def items_view2():
    reader = "ReadOnly" # added as part of module 10
    os.environ['LOGIN_DISABLED']='True' 
    return ViewModel([
    TodoItem(1, "Test in progress Todo", "To Do", datetime.now()),
    TodoItem(2, "Test Pending Todo", "Pending", datetime.now()),
    TodoItem(3, "Test Done Todo", "Done", datetime.now())
    ], reader) # added as part of module 10 

# using 1st method to get all cards 
def test_return_all_items(item_view): 
    all_items = item_view.items
    assert len(all_items) == 11

# using 2nd method to get all cards
def test_return_all_items2(items_view2): 
    all_items = items_view2.items
    assert len(all_items) == 3

# add test case for return to do items
def test_return_all_to_do(item_view): 
    to_do = item_view.to_do_items
    assert len(to_do) == 3

# add test case for return doing items
def test_return_all_doing(item_view): 
    doing = item_view.doing_items
    assert len(doing) == 2

# add test case for return done items
def test_return_all_done(item_view): 
    done = item_view.done_items
    assert len(done) == 6

# add test case for return id for specific item from done: done_items[0].id == 5
def test_return_specific_done(item_view): 
    done = item_view.done_items
    assert done[0].title == "You're not done"
    assert done[1].title == "Are you sure you're done"

# add test to show recent done updated is today - THIS now WORKS! 
def test_return_done_today(item_view): 
    recent_done = item_view.show_recent_done
    assert next(recent_done).title == "Are you sure you're done3"
    assert next(recent_done).id == 11


