from typing import List
import logging

import azure.functions as func

def main(events: List[func.EventHubEvent]):
    for event in events:
        logging.info('<<<<< Python EventHub trigger processed an event: %s',
                        event.get_body().decode('utf-8'))
        logging.info('  EnqueuedTimeUtc = %s', event.enqueued_time)
        logging.info('  SequenceNumber = %s', event.sequence_number)
        logging.info('  Offset = %s', event.offset)
