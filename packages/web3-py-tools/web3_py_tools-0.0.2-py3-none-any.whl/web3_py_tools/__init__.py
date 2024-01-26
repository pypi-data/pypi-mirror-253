import eth_account_api
import web3.eth.base_eth


web3.eth.base_eth.BaseEth.account = eth_account_api.Account()
