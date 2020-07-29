from trello_class import TrelloItem
from view_model import ViewModel

def test_filters_by_status():
    created_todo = TrelloItem(1, "Test in progress Todo", "To Do")
    pending_todo = TrelloItem(2, "Test Pending Todo", "Pending")
    done_todo = TrelloItem(3, "Test Done Todo", "Done")

    todos = [
        created_todo,
        pending_todo,
        done_todo
    ]

    view_model = ViewModel(todos)
    
    assert view_model.to_do_items == [created_todo]
    assert view_model.doing_items == [pending_todo]
    assert view_model.done_items == [done_todo]

