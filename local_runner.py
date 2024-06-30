from index import handler
from mock_event import scheduler_event as mock_event

if __name__ == "__main__":
    print('-------- running locally --------')
    handler(mock_event)
    print('------------ finish! ------------')
