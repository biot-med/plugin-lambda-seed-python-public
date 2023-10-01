from lambda_function import lambda_handler
from mock_event import mock_event

print('-------- running locally --------')
lambda_handler(mock_event)
print('------------ finish! ------------')