import os
from dotenv import load_dotenv
from web3 import Web3
import requests
import datetime
from brownie import Wei

load_dotenv() 

VOTING_MACHINE_0 = '0x1C18bAd5a3ee4e96611275B13a8ed062B4a13055'
VOTING_MACHINE_1 = '0x332B8C9734b4097dE50f302F7D9F273FFdB45B84'

mainnet_avatar = '0x519b70055af55A007110B4Ff99b0eA33071c720a'

def fetch_mainnet():
    net = 'MAINNET'
    w3 = Web3(Web3.HTTPProvider(os.getenv(f'ENDPOINT_MAINNET')))
    
    # Contribution Proposals
    cp_scheme = '0x08cC7BBa91b849156e9c44DEd51896B38400f55B'
    abi = get_abi(cp_scheme, net)
    scheme = w3.eth.contract(address=cp_scheme, abi=abi)
    proposals = scheme.events.NewContributionProposal.createFilter(fromBlock=get_block(net), argument_filters={'_avatar': mainnet_avatar})
    proposal_events = proposals.get_all_entries()

    for p in proposal_events:
        p = p['args']
        print(scheme.functions.getProposalExecutionTime('0x' + p['_proposalId'].hex(), mainnet_avatar).call())
        print(get_title(p['_descriptionHash']))
        print('0x' + p['_proposalId'].hex())
        if p['_rewards'][1] > 0:
            print('ETH:', Wei(p['_rewards'][1]).to('ether'))
        if p['_rewards'][2] > 0:
            print('ERC20:', Wei(p['_rewards'][2]).to('ether'))
        if p['_reputationChange'] > 0:
            print('REP:', Wei(p['_reputationChange']).to('ether'))
        print('\n')




def fetch_all():
    nets = ['MAINNET', 'XDAI', 'ARBITRUM']

    pass

def get_abi(address, network):
    if network == 'MAINNET':
        req = requests.get(f"https://api.etherscan.io/api?module=contract&action=getabi&address={address}&apikey={os.getenv('ETHERSCAN_KEY')}")
        abi = req.json()['result']
        return abi

def get_title(proposal_hash):
    req = requests.get('https://gateway.pinata.cloud/ipfs/' + proposal_hash)
    title = req.json()['title']
    return title

def get_block(network):
    now = datetime.datetime.now()
    then = now - datetime.timedelta(days=60)
    ts = int(then.timestamp())
    if network == 'MAINNET':
        req = requests.get(f"https://api.etherscan.io/api?module=block&action=getblocknobytime&timestamp={ts}&closest=before&apikey={os.getenv('ETHERSCAN_KEY')}")
        block = int(req.json()['result'])
    elif network == 'XDAI':
        raise NotImplementedError
    elif network == 'ARBITRUM':
        raise NotImplementedError
    else:
        raise NotImplementedError
    return block

if __name__ == '__main__':
    fetch_mainnet()