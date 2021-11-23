import os
from dotenv import load_dotenv
from web3 import Web3
import requests

load_dotenv() 

VOTING_MACHINE_0 = '0x1C18bAd5a3ee4e96611275B13a8ed062B4a13055'
VOTING_MACHINE_1 = '0x332B8C9734b4097dE50f302F7D9F273FFdB45B84' 

def fetch(endpoint, schemes):
    w3 = Web3(Web3.HTTPProvider(os.getenv(f'ENDPOINT_{endpoint}')))
    for s in schemes:
        scheme = w3.eth.contract(address=s, )



def fetch_all():
    nets = ['MAINNET', 'XDAI', 'ARBITRUM']

    pass