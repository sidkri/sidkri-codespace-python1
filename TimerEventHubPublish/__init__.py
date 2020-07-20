import datetime
import logging

import azure.functions as func

def main(timer: func.TimerRequest) -> str:
    if timer.past_due:
        logging.info('The timer is past due!')
    for i in range(1,10):
        utc_timestamp = datetime.datetime.utcnow().replace(
            tzinfo=datetime.timezone.utc).isoformat()
        msg = 'Message created at: {}'.format(utc_timestamp)
        logging.info('>>>>> Publishing to Event Hub Message: %s', msg)
    return msg