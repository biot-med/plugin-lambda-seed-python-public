from index import handler
from mock_event import notification_mock_event as mock_event

if __name__ == "__main__":
    print('-------- running locally --------')
    handler(mock_event)
    print('------------ finish! ------------')
