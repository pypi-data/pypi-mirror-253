"""Format transaction traces."""

import toolblocks.parsing.address
import toolblocks.parsing.common

# CASTING #####################################################################

to_address_checksum = toolblocks.parsing.address.format_with_checksum
to_hexstr_prefix = lambda __x: toolblocks.parsing.common.to_hexstr(data=__x, prefix=True)
to_bytes_list = lambda __l: [toolblocks.parsing.common.to_bytes(__t) for __t in __l]

# TRACES ######################################################################

def parse_trace_data(trace: dict) -> dict:
    """Flatten and format all the data in a transaction trace."""
    # common
    __action = toolblocks.parsing.common.get_field(dataset=trace, keys=('action',), default=trace)
    __result = toolblocks.parsing.common.get_field(dataset=trace, keys=('result',), default=trace)
    # flatten
    return {
        # trace root
        'chain_id': '0x01', # TODO
        'block_hash': toolblocks.parsing.common.get_field(dataset=trace, keys=('block_hash', 'blockHash',), default='', callback=to_hexstr_prefix),
        'block_number': toolblocks.parsing.common.get_field(dataset=trace, keys=('block_number', 'blockNumber',), default='0x00', callback=to_hexstr_prefix),
        'transaction_hash': toolblocks.parsing.common.get_field(dataset=trace, keys=('transaction_hash', 'transactionHash',), default='', callback=to_hexstr_prefix),
        'transaction_index': toolblocks.parsing.common.get_field(dataset=trace, keys=('transaction_index', 'transactionIndex', 'transaction_position', 'transactionPosition'), default='0x00', callback=to_hexstr_prefix),
        'error': toolblocks.parsing.common.get_field(dataset=trace, keys=('error',), default='',),
        'subtraces': toolblocks.parsing.common.get_field(dataset=trace, keys=('subtraces',), default='', callback=to_hexstr_prefix),
        'trace_address': toolblocks.parsing.common.get_field(dataset=trace, keys=('trace_address', 'traceAddress',), default=[],), # supposed to be a list
        # trace action
        'action_type': toolblocks.parsing.common.get_field(dataset=__action, keys=('type', 'action_type', 'actionType',), default=toolblocks.parsing.common.get_field(dataset=trace, keys=('type', 'action_type', 'actionType',), default='')),
        'action_call_type': toolblocks.parsing.common.get_field(dataset=__action, keys=('call_type', 'callType', 'action_call_type', 'actionCallType',), default=''),
        'action_reward_type': '', # TODO
        'action_gas': '0x00', # TODO
        'action_from': toolblocks.parsing.common.get_field(dataset=__action, keys=('from', 'from_', 'action_from', 'actionFrom',), default='', callback=to_address_checksum),
        'action_to': toolblocks.parsing.common.get_field(dataset=__action, keys=('to', 'action_to', 'actionTo',), default='', callback=to_address_checksum),
        'action_input': toolblocks.parsing.common.get_field(dataset=__action, keys=('input', 'action_input', 'actionInput',), default='', callback=to_hexstr_prefix),
        'action_init': toolblocks.parsing.common.get_field(dataset=__action, keys=('init', 'action_init', 'actionInit',), default='', callback=to_hexstr_prefix),
        'action_value': toolblocks.parsing.common.get_field(dataset=__action, keys=('value', 'action_value', 'actionValue',), default='0x00', callback=to_hexstr_prefix),
        # trace result
        'result_address': toolblocks.parsing.common.get_field(dataset=__result, keys=('address', 'result_address', 'resultAddress',), default='', callback=to_address_checksum),
        'result_gas_used': toolblocks.parsing.common.get_field(dataset=__result, keys=('gas_used', 'gasUsed', 'result_gas_used', 'resultGasUsed',), default='', callback=to_hexstr_prefix),
        'result_code': toolblocks.parsing.common.get_field(dataset=__result, keys=('code', 'result_code', 'resultCode',), default='', callback=to_hexstr_prefix),
        'result_output': toolblocks.parsing.common.get_field(dataset=__result, keys=('output', 'result_output', 'resultOutput',), default='', callback=to_hexstr_prefix),}
