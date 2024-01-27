"""Format addresses."""

import eth_utils.address

import toolblocks.parsing.common

# FORMAT ######################################################################

def format_with_checksum(address: str) -> str:
    """Format an address as a HEX string of length 40 with the "0x" prefix and a checksum."""
    __address = toolblocks.parsing.common.to_hexstr(data=address, prefix=False) # remove prefix
    return (
        eth_utils.address.to_checksum_address('0x{0:0>40x}'.format(int(__address, 16))) if __address
        else '')
