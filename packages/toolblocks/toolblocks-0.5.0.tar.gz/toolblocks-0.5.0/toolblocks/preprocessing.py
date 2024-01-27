"""Preprocess the inputs of the Forta "handle" functions."""

import collections.abc
import functools

import toolblocks.parsing.common
import toolblocks.parsing.logs
import toolblocks.parsing.traces
import toolblocks.parsing.transaction

# PARSE FORTA OBJECTS #########################################################

def _parse_logs(logs: collections.abc.Iterable) -> list:
    """Iterate over the logs and parse each log."""
    return [toolblocks.parsing.logs.parse_log_data(log=__l) for __l in logs]

def _parse_traces(traces: collections.abc.Iterable) -> list:
    """Iterate over the traces and parse each trace."""
    return [toolblocks.parsing.traces.parse_trace_data(trace=__t) for __t in traces]

# PARSE ARGS ##################################################################

def _extract_transaction_event(*args, **kwargs) -> 'TransactionEvent':
    """Extracts the composite object handed by the Forta node."""
    return args[0] if args else toolblocks.parsing.common.get_field(dataset=kwargs, keys=('transaction', 'tx', 'log'), default=None)

# WRAP HANDLE TX ##############################################################

def parse_forta_arguments(func: callable) -> callable:
    """Creates a decorator for handle_transaction to parse the compositte object handed by the Forta node."""

    @functools.wraps(func)
    def __wrapper(*args, **kwargs):
        """Main function called on the logs gathered by the Forta network."""
        # find the transaction event in the nameless arguments
        __data = _extract_transaction_event(*args, **kwargs)
        # parse forta objects
        __tx = toolblocks.parsing.common.get_field(dataset=__data, keys=('transaction',), default={}, callback=toolblocks.parsing.transaction.parse_transaction_data)
        __logs = toolblocks.parsing.common.get_field(dataset=__data, keys=('logs',), default=[], callback=_parse_logs)
        __traces = toolblocks.parsing.common.get_field(dataset=__data, keys=('traces',), default=[], callback=_parse_traces)
        # call handle_transaction
        return func(transaction=__tx, logs=__logs, traces=__traces)

    return __wrapper
