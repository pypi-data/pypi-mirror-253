"""Format event logs."""

import toolblocks.parsing.address
import toolblocks.parsing.common

# CASTING #####################################################################

to_address_checksum = toolblocks.parsing.address.format_with_checksum
to_hexstr_prefix = lambda __x: toolblocks.parsing.common.to_hexstr(data=__x, prefix=True)
to_bytes_list = lambda __l: [toolblocks.parsing.common.to_bytes(__t) for __t in __l]

# TRACES ######################################################################

def parse_log_data(log: dict) -> dict:
    """Flatten and format all the data in an event log."""
    # common
    __data = {
        'chain_id': '0x01', # TODO
        'block_number': toolblocks.parsing.common.get_field(dataset=log, keys=('block_number', 'blockNumber',), default='0x00', callback=to_hexstr_prefix),
        'block_hash': toolblocks.parsing.common.get_field(dataset=log, keys=('block_hash', 'blockHash',), default='', callback=to_hexstr_prefix),
        'transaction_hash': toolblocks.parsing.common.get_field(dataset=log, keys=('transaction_hash', 'transactionHash',), default='', callback=to_hexstr_prefix),
        'transaction_index': toolblocks.parsing.common.get_field(dataset=log, keys=('transaction_index', 'transactionIndex',), default='0x00', callback=to_hexstr_prefix),
        'log_index': toolblocks.parsing.common.get_field(dataset=log, keys=('log_index', 'logIndex',), default='0x00', callback=to_hexstr_prefix),
        'address': toolblocks.parsing.common.get_field(dataset=log, keys=('address',), default='', callback=to_address_checksum),
        'topics': toolblocks.parsing.common.get_field(dataset=log, keys=('topics',), default=[], callback=to_bytes_list),
        'data': toolblocks.parsing.common.get_field(dataset=log, keys=('data',), default='', callback=to_hexstr_prefix),}
    # aliases
    __data['blockHash'] = __data['block_hash']
    __data['blockNumber'] = __data['block_number']
    __data['transactionHash'] = __data['transaction_hash']
    __data['transactionIndex'] = __data['transaction_index']
    __data['logIndex'] = __data['log_index']
    # output
    return __data
