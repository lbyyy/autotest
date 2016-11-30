
node1 = 'core1.diqi.us_5566_11224_/home/skz/.gcoin'
node2 = 'core1.diqi.us_55888_11114_/home/skz/.gcoin1'
node3 = 'core1.diqi.us_10000_11221_/home/skz/.gcoin2'
node4 = 'core1.diqi.us_5580_11223_/home/skz/.gcoin3'

node5 = 'core2.diqi.us_5566_11224_/home/skz/.gcoin'
node6 = 'core2.diqi.us_55888_11221_/home/skz/.gcoin1'
node7 = 'core2.diqi.us_5522_11222_/home/skz/.gcoin2'
node8 = 'core2.diqi.us_5533_11223_/home/skz/.gcoin3'

roledefs = {
    'alliance':[node1, node2, node3, node4, node5, node6, node7, node8],
    'issuer': [node1, node2, node3, node4, node5, node6, node7, node8],
    'others': [node1, node2, node3, node4, node5, node6, node7, node8],
    'monitor': [],
}

remote_user = 'skz'
ssh_key_filename = '/home/skz/.ssh/id_rsa.pub'

# bitcoind configuration
rpcthreads = 20

NUM_ADDRESS_PER_NODE = 30
NUM_COLOR = 1000 # num of color you want to use
MAX_NUM_MEMBERS_PER_ISSUER = 10
MAX_TRANSACTION_NUM_ALLOWED_PER_MEMBER_PER_COLOR = 100000
MAX_AMOUNT_PER_PAYMENT = 100
NUM_ATTEMPT_CREATE_PAYMENT = 1000000

INITIAL_AMOUNT_PER_ISSUER = 10**10 # should can be 10^10
MAX_COIN = 10**10
MIN_ACTIVATION_BTC = 1
LICENSE_MATURITY = 10
COINBASE_MATURITY = 10

FAKE_LICENSE_HEX_STRING = "72110100046e616d6503646573046164647201000000000000000000000000046164647200000000000000000000000001046c696e6b0000000000000000000000000000000000000000000000000000000000000000"

"""
FAKE_LICENSE_INFO = {
    "version": 1,
    "name": "",
    "description": "description",
    "issuer": "",
    "divisibility": True,
    "fee_type": "fixed",
    "fee_rate": 0.0,
    "fee_collector": "",
    "mint_schedule": "free",
    "member_control": True,
    "metadata_link": "hyperlink",
    "metadata_hash": "hash"
}
"""

