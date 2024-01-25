import requests
from abc import ABC


class TronHttpApiABC(ABC):
    def __init__(self, gateway: str):
        self.gateway = gateway
        if self.gateway is not None and self.gateway.endswith("/"):
            self.gateway = self.gateway[:-1]

    def http_request(self, url: str, query_string: str, json_data):
        if query_string:
            url = url + "?" + query_string

        if json_data is None:
            return self.http_get(url)
        else:
            return self.http_post(url, json_data)

    def final_url(self, url: str):
        return f'{self.gateway}{url}' if url.startswith('/') else f'{self.gateway}/{url}'

    def http_post(self, url: str, json_data: dict):
        response = requests.post(self.final_url(url), json=json_data)
        return response.status_code, response.text

    def http_get(self, url: str):
        response = requests.get(self.final_url(url))
        return response.status_code, response.text


class TronFullNodeHttpApiABC(TronHttpApiABC, ABC):

    def getaccount(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetAccountServlet.java
        """

        url = "/wallet/getaccount"
        return self.http_request(url, query_string, json_data)

    def createtransaction(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/TransferServlet.java
        """

        url = "/wallet/createtransaction"
        return self.http_request(url, query_string, json_data)

    def broadcasttransaction(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/BroadcastServlet.java
        """

        url = "/wallet/broadcasttransaction"
        return self.http_request(url, query_string, json_data)

    def updateaccount(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/UpdateAccountServlet.java
        """

        url = "/wallet/updateaccount"
        return self.http_request(url, query_string, json_data)

    def votewitnessaccount(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/VoteWitnessAccountServlet.java
        """

        url = "/wallet/votewitnessaccount"
        return self.http_request(url, query_string, json_data)

    def createassetissue(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/CreateAssetIssueServlet.java
        """

        url = "/wallet/createassetissue"
        return self.http_request(url, query_string, json_data)

    def updatewitness(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/UpdateWitnessServlet.java
        """

        url = "/wallet/updatewitness"
        return self.http_request(url, query_string, json_data)

    def createaccount(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/CreateAccountServlet.java
        """

        url = "/wallet/createaccount"
        return self.http_request(url, query_string, json_data)

    def createwitness(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/CreateWitnessServlet.java
        """

        url = "/wallet/createwitness"
        return self.http_request(url, query_string, json_data)

    def transferasset(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/TransferAssetServlet.java
        """

        url = "/wallet/transferasset"
        return self.http_request(url, query_string, json_data)

    def participateassetissue(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ParticipateAssetIssueServlet.java
        """

        url = "/wallet/participateassetissue"
        return self.http_request(url, query_string, json_data)

    def freezebalance(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/FreezeBalanceServlet.java
        """

        url = "/wallet/freezebalance"
        return self.http_request(url, query_string, json_data)

    def unfreezebalance(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/UnFreezeBalanceServlet.java
        """

        url = "/wallet/unfreezebalance"
        return self.http_request(url, query_string, json_data)

    def unfreezeasset(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/UnFreezeAssetServlet.java
        """

        url = "/wallet/unfreezeasset"
        return self.http_request(url, query_string, json_data)

    def withdrawbalance(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/WithdrawBalanceServlet.java
        """

        url = "/wallet/withdrawbalance"
        return self.http_request(url, query_string, json_data)

    def updateasset(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/UpdateAssetServlet.java
        """

        url = "/wallet/updateasset"
        return self.http_request(url, query_string, json_data)

    def listnodes(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ListNodesServlet.java
        """

        url = "/wallet/listnodes"
        return self.http_request(url, query_string, json_data)

    def getaccountnet(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetAccountNetServlet.java
        """

        url = "/wallet/getaccountnet"
        return self.http_request(url, query_string, json_data)

    def getassetissuebyname(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetAssetIssueByNameServlet.java
        """

        url = "/wallet/getassetissuebyname"
        return self.http_request(url, query_string, json_data)

    def getassetissuelistbyname(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetAssetIssueListByNameServlet.java
        """

        url = "/wallet/getassetissuelistbyname"
        return self.http_request(url, query_string, json_data)

    def getassetissuebyid(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetAssetIssueByIdServlet.java
        """

        url = "/wallet/getassetissuebyid"
        return self.http_request(url, query_string, json_data)

    def getnowblock(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetNowBlockServlet.java
        """

        url = "/wallet/getnowblock"
        return self.http_request(url, query_string, json_data)

    def getblockbynum(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetBlockByNumServlet.java
        """

        url = "/wallet/getblockbynum"
        return self.http_request(url, query_string, json_data)

    def getblockbyid(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetBlockByIdServlet.java
        """

        url = "/wallet/getblockbyid"
        return self.http_request(url, query_string, json_data)

    def getblockbylimitnext(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetBlockByLimitNextServlet.java
        """

        url = "/wallet/getblockbylimitnext"
        return self.http_request(url, query_string, json_data)

    def getblockbylatestnum(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetBlockByLatestNumServlet.java
        """

        url = "/wallet/getblockbylatestnum"
        return self.http_request(url, query_string, json_data)

    def gettransactionbyid(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetTransactionByIdServlet.java
        """

        url = "/wallet/gettransactionbyid"
        return self.http_request(url, query_string, json_data)

    def listwitnesses(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ListWitnessesServlet.java
        """

        url = "/wallet/listwitnesses"
        return self.http_request(url, query_string, json_data)

    def getassetissuelist(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetAssetIssueListServlet.java
        """

        url = "/wallet/getassetissuelist"
        return self.http_request(url, query_string, json_data)

    def totaltransaction(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/TotalTransactionServlet.java
        """

        url = "/wallet/totaltransaction"
        return self.http_request(url, query_string, json_data)

    def validateaddress(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ValidateAddressServlet.java
        """

        url = "/wallet/validateaddress"
        return self.http_request(url, query_string, json_data)

    def deploycontract(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/DeployContractServlet.java
        """

        url = "/wallet/deploycontract"
        return self.http_request(url, query_string, json_data)

    def triggersmartcontract(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/TriggerSmartContractServlet.java
        """

        url = "/wallet/triggersmartcontract"
        return self.http_request(url, query_string, json_data)

    def triggerconstantcontract(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/TriggerConstantContractServlet.java
        """

        url = "/wallet/triggerconstantcontract"
        return self.http_request(url, query_string, json_data)

    def estimateenergy(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/EstimateEnergyServlet.java
        """

        url = "/wallet/estimateenergy"
        return self.http_request(url, query_string, json_data)

    def getcontract(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetContractServlet.java
        """

        url = "/wallet/getcontract"
        return self.http_request(url, query_string, json_data)

    def getcontractinfo(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetContractInfoServlet.java
        """

        url = "/wallet/getcontractinfo"
        return self.http_request(url, query_string, json_data)

    def clearabi(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ClearABIServlet.java
        """

        url = "/wallet/clearabi"
        return self.http_request(url, query_string, json_data)

    def proposalcreate(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ProposalCreateServlet.java
        """

        url = "/wallet/proposalcreate"
        return self.http_request(url, query_string, json_data)

    def proposalapprove(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ProposalApproveServlet.java
        """

        url = "/wallet/proposalapprove"
        return self.http_request(url, query_string, json_data)

    def proposaldelete(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ProposalDeleteServlet.java
        """

        url = "/wallet/proposaldelete"
        return self.http_request(url, query_string, json_data)

    def listproposals(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ListProposalsServlet.java
        """

        url = "/wallet/listproposals"
        return self.http_request(url, query_string, json_data)

    def getproposalbyid(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetProposalByIdServlet.java
        """

        url = "/wallet/getproposalbyid"
        return self.http_request(url, query_string, json_data)

    def exchangecreate(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ExchangeCreateServlet.java
        """

        url = "/wallet/exchangecreate"
        return self.http_request(url, query_string, json_data)

    def exchangeinject(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ExchangeInjectServlet.java
        """

        url = "/wallet/exchangeinject"
        return self.http_request(url, query_string, json_data)

    def exchangetransaction(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ExchangeTransactionServlet.java
        """

        url = "/wallet/exchangetransaction"
        return self.http_request(url, query_string, json_data)

    def exchangewithdraw(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ExchangeWithdrawServlet.java
        """

        url = "/wallet/exchangewithdraw"
        return self.http_request(url, query_string, json_data)

    def getexchangebyid(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetExchangeByIdServlet.java
        """

        url = "/wallet/getexchangebyid"
        return self.http_request(url, query_string, json_data)

    def listexchanges(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ListExchangesServlet.java
        """

        url = "/wallet/listexchanges"
        return self.http_request(url, query_string, json_data)

    def getchainparameters(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetChainParametersServlet.java
        """

        url = "/wallet/getchainparameters"
        return self.http_request(url, query_string, json_data)

    def getaccountresource(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetAccountResourceServlet.java
        """

        url = "/wallet/getaccountresource"
        return self.http_request(url, query_string, json_data)

    def getsignweight(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetTransactionSignWeightServlet.java
        """

        url = "/wallet/getsignweight"
        return self.http_request(url, query_string, json_data)

    def getapprovedlist(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetTransactionApprovedListServlet.java
        """

        url = "/wallet/getapprovedlist"
        return self.http_request(url, query_string, json_data)

    def accountpermissionupdate(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/AccountPermissionUpdateServlet.java
        """

        url = "/wallet/accountpermissionupdate"
        return self.http_request(url, query_string, json_data)

    def getnodeinfo(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetNodeInfoServlet.java
        """

        url = "/wallet/getnodeinfo"
        return self.http_request(url, query_string, json_data)

    def updatesetting(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/UpdateSettingServlet.java
        """

        url = "/wallet/updatesetting"
        return self.http_request(url, query_string, json_data)

    def updateenergylimit(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/UpdateEnergyLimitServlet.java
        """

        url = "/wallet/updateenergylimit"
        return self.http_request(url, query_string, json_data)

    def getdelegatedresource(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetDelegatedResourceServlet.java
        """

        url = "/wallet/getdelegatedresource"
        return self.http_request(url, query_string, json_data)

    def getdelegatedresourcev2(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetDelegatedResourceV2Servlet.java
        """

        url = "/wallet/getdelegatedresourcev2"
        return self.http_request(url, query_string, json_data)

    def getcandelegatedmaxsize(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetCanDelegatedMaxSizeServlet.java
        """

        url = "/wallet/getcandelegatedmaxsize"
        return self.http_request(url, query_string, json_data)

    def getavailableunfreezecount(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetAvailableUnfreezeCountServlet.java
        """

        url = "/wallet/getavailableunfreezecount"
        return self.http_request(url, query_string, json_data)

    def getcanwithdrawunfreezeamount(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetCanWithdrawUnfreezeAmountServlet.java
        """

        url = "/wallet/getcanwithdrawunfreezeamount"
        return self.http_request(url, query_string, json_data)

    def setaccountid(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/SetAccountIdServlet.java
        """

        url = "/wallet/setaccountid"
        return self.http_request(url, query_string, json_data)

    def getaccountbyid(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetAccountByIdServlet.java
        """

        url = "/wallet/getaccountbyid"
        return self.http_request(url, query_string, json_data)

    def getexpandedspendingkey(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetExpandedSpendingKeyServlet.java
        """

        url = "/wallet/getexpandedspendingkey"
        return self.http_request(url, query_string, json_data)

    def getakfromask(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetAkFromAskServlet.java
        """

        url = "/wallet/getakfromask"
        return self.http_request(url, query_string, json_data)

    def getnkfromnsk(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetNkFromNskServlet.java
        """

        url = "/wallet/getnkfromnsk"
        return self.http_request(url, query_string, json_data)

    def getspendingkey(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetSpendingKeyServlet.java
        """

        url = "/wallet/getspendingkey"
        return self.http_request(url, query_string, json_data)

    def getnewshieldedaddress(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetNewShieldedAddressServlet.java
        """

        url = "/wallet/getnewshieldedaddress"
        return self.http_request(url, query_string, json_data)

    def getdiversifier(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetDiversifierServlet.java
        """

        url = "/wallet/getdiversifier"
        return self.http_request(url, query_string, json_data)

    def getincomingviewingkey(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetIncomingViewingKeyServlet.java
        """

        url = "/wallet/getincomingviewingkey"
        return self.http_request(url, query_string, json_data)

    def getzenpaymentaddress(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetZenPaymentAddressServlet.java
        """

        url = "/wallet/getzenpaymentaddress"
        return self.http_request(url, query_string, json_data)

    def scannotebyivk(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ScanNoteByIvkServlet.java
        """

        url = "/wallet/scannotebyivk"
        return self.http_request(url, query_string, json_data)

    def scannotebyovk(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ScanNoteByOvkServlet.java
        """

        url = "/wallet/scannotebyovk"
        return self.http_request(url, query_string, json_data)

    def getrcm(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetRcmServlet.java
        """

        url = "/wallet/getrcm"
        return self.http_request(url, query_string, json_data)

    def isspend(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/IsSpendServlet.java
        """

        url = "/wallet/isspend"
        return self.http_request(url, query_string, json_data)

    def createspendauthsig(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/CreateSpendAuthSigServlet.java
        """

        url = "/wallet/createspendauthsig"
        return self.http_request(url, query_string, json_data)

    def isshieldedtrc20contractnotespent(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/IsShieldedTRC20ContractNoteSpentServlet.java
        """

        url = "/wallet/isshieldedtrc20contractnotespent"
        return self.http_request(url, query_string, json_data)

    def createshieldedcontractparameters(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/CreateShieldedContractParametersServlet.java
        """

        url = "/wallet/createshieldedcontractparameters"
        return self.http_request(url, query_string, json_data)

    def createshieldedcontractparameterswithoutask(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/CreateShieldedContractParametersWithoutAskServlet.java
        """

        url = "/wallet/createshieldedcontractparameterswithoutask"
        return self.http_request(url, query_string, json_data)

    def scanshieldedtrc20notesbyivk(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ScanShieldedTRC20NotesByIvkServlet.java
        """

        url = "/wallet/scanshieldedtrc20notesbyivk"
        return self.http_request(url, query_string, json_data)

    def scanshieldedtrc20notesbyovk(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ScanShieldedTRC20NotesByOvkServlet.java
        """

        url = "/wallet/scanshieldedtrc20notesbyovk"
        return self.http_request(url, query_string, json_data)

    def gettriggerinputforshieldedtrc20contract(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetTriggerInputForShieldedTRC20ContractServlet.java
        """

        url = "/wallet/gettriggerinputforshieldedtrc20contract"
        return self.http_request(url, query_string, json_data)

    def broadcasthex(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/BroadcastHexServlet.java
        """

        url = "/wallet/broadcasthex"
        return self.http_request(url, query_string, json_data)

    def getBrokerage(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetBrokerageServlet.java
        """

        url = "/wallet/getBrokerage"
        return self.http_request(url, query_string, json_data)

    def getReward(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetRewardServlet.java
        """

        url = "/wallet/getReward"
        return self.http_request(url, query_string, json_data)

    def updateBrokerage(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/UpdateBrokerageServlet.java
        """

        url = "/wallet/updateBrokerage"
        return self.http_request(url, query_string, json_data)

    def createCommonTransaction(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/CreateCommonTransactionServlet.java
        """

        url = "/wallet/createCommonTransaction"
        return self.http_request(url, query_string, json_data)

    def gettransactioninfobyblocknum(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetTransactionInfoByBlockNumServlet.java
        """

        url = "/wallet/gettransactioninfobyblocknum"
        return self.http_request(url, query_string, json_data)

    def net_listnodes(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ListNodesServlet.java
        """

        url = "/net/listnodes"
        return self.http_request(url, query_string, json_data)

    def monitor_getstatsinfo(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/MetricsServlet.java
        """

        url = "/monitor/getstatsinfo"
        return self.http_request(url, query_string, json_data)

    def monitor_getnodeinfo(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetNodeInfoServlet.java
        """

        url = "/monitor/getnodeinfo"
        return self.http_request(url, query_string, json_data)

    def marketsellasset(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/MarketSellAssetServlet.java
        """

        url = "/wallet/marketsellasset"
        return self.http_request(url, query_string, json_data)

    def marketcancelorder(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/MarketCancelOrderServlet.java
        """

        url = "/wallet/marketcancelorder"
        return self.http_request(url, query_string, json_data)

    def getmarketorderbyaccount(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetMarketOrderByAccountServlet.java
        """

        url = "/wallet/getmarketorderbyaccount"
        return self.http_request(url, query_string, json_data)

    def getmarketorderbyid(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetMarketOrderByIdServlet.java
        """

        url = "/wallet/getmarketorderbyid"
        return self.http_request(url, query_string, json_data)

    def getmarketpricebypair(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetMarketPriceByPairServlet.java
        """

        url = "/wallet/getmarketpricebypair"
        return self.http_request(url, query_string, json_data)

    def getmarketorderlistbypair(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetMarketOrderListByPairServlet.java
        """

        url = "/wallet/getmarketorderlistbypair"
        return self.http_request(url, query_string, json_data)

    def getmarketpairlist(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetMarketPairListServlet.java
        """

        url = "/wallet/getmarketpairlist"
        return self.http_request(url, query_string, json_data)

    def getaccountbalance(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetAccountBalanceServlet.java
        """

        url = "/wallet/getaccountbalance"
        return self.http_request(url, query_string, json_data)

    def getblockbalance(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetBlockBalanceServlet.java
        """

        url = "/wallet/getblockbalance"
        return self.http_request(url, query_string, json_data)

    def getburntrx(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetBurnTrxServlet.java
        """

        url = "/wallet/getburntrx"
        return self.http_request(url, query_string, json_data)

    def gettransactionfrompending(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetTransactionFromPendingServlet.java
        """

        url = "/wallet/gettransactionfrompending"
        return self.http_request(url, query_string, json_data)

    def gettransactionlistfrompending(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetTransactionListFromPendingServlet.java
        """

        url = "/wallet/gettransactionlistfrompending"
        return self.http_request(url, query_string, json_data)

    def getpendingsize(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetPendingSizeServlet.java
        """

        url = "/wallet/getpendingsize"
        return self.http_request(url, query_string, json_data)

    def getenergyprices(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetEnergyPricesServlet.java
        """

        url = "/wallet/getenergyprices"
        return self.http_request(url, query_string, json_data)

    def getbandwidthprices(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetBandwidthPricesServlet.java
        """

        url = "/wallet/getbandwidthprices"
        return self.http_request(url, query_string, json_data)

    def getblock(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetBlockServlet.java
        """

        url = "/wallet/getblock"
        return self.http_request(url, query_string, json_data)

    def getmemofee(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetMemoFeePricesServlet.java
        """

        url = "/wallet/getmemofee"
        return self.http_request(url, query_string, json_data)

    def freezebalancev2(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/FreezeBalanceV2Servlet.java
        """

        url = "/wallet/freezebalancev2"
        return self.http_request(url, query_string, json_data)

    def unfreezebalancev2(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/UnFreezeBalanceV2Servlet.java
        """

        url = "/wallet/unfreezebalancev2"
        return self.http_request(url, query_string, json_data)

    def withdrawexpireunfreeze(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/WithdrawExpireUnfreezeServlet.java
        """

        url = "/wallet/withdrawexpireunfreeze"
        return self.http_request(url, query_string, json_data)

    def delegateresource(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/DelegateResourceServlet.java
        """

        url = "/wallet/delegateresource"
        return self.http_request(url, query_string, json_data)

    def undelegateresource(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/UnDelegateResourceServlet.java
        """

        url = "/wallet/undelegateresource"
        return self.http_request(url, query_string, json_data)

    def cancelallunfreezev2(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/CancelAllUnfreezeV2Servlet.java
        """

        url = "/wallet/cancelallunfreezev2"
        return self.http_request(url, query_string, json_data)


class TronSolidityNodeHttpApiABC(TronHttpApiABC, ABC):

    def solidity_getaccount(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetAccountServlet.java
        """

        url = "/walletsolidity/getaccount"
        return self.http_request(url, query_string, json_data)

    def solidity_listwitnesses(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ListWitnessesServlet.java
        """

        url = "/walletsolidity/listwitnesses"
        return self.http_request(url, query_string, json_data)

    def solidity_getassetissuelist(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetAssetIssueListServlet.java
        """

        url = "/walletsolidity/getassetissuelist"
        return self.http_request(url, query_string, json_data)

    def solidity_getpaginatedassetissuelist(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetPaginatedAssetIssueListServlet.java
        """

        url = "/walletsolidity/getpaginatedassetissuelist"
        return self.http_request(url, query_string, json_data)

    def solidity_getassetissuebyname(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetAssetIssueByNameServlet.java
        """

        url = "/walletsolidity/getassetissuebyname"
        return self.http_request(url, query_string, json_data)

    def solidity_getassetissuebyid(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetAssetIssueByIdServlet.java
        """

        url = "/walletsolidity/getassetissuebyid"
        return self.http_request(url, query_string, json_data)

    def solidity_getassetissuelistbyname(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetAssetIssueListByNameServlet.java
        """

        url = "/walletsolidity/getassetissuelistbyname"
        return self.http_request(url, query_string, json_data)

    def solidity_getnowblock(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetNowBlockServlet.java
        """

        url = "/walletsolidity/getnowblock"
        return self.http_request(url, query_string, json_data)

    def solidity_getblockbynum(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetBlockByNumServlet.java
        """

        url = "/walletsolidity/getblockbynum"
        return self.http_request(url, query_string, json_data)

    def solidity_getdelegatedresource(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetDelegatedResourceServlet.java
        """

        url = "/walletsolidity/getdelegatedresource"
        return self.http_request(url, query_string, json_data)

    def solidity_getdelegatedresourcev2(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetDelegatedResourceV2Servlet.java
        """

        url = "/walletsolidity/getdelegatedresourcev2"
        return self.http_request(url, query_string, json_data)

    def solidity_getcandelegatedmaxsize(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetCanDelegatedMaxSizeServlet.java
        """

        url = "/walletsolidity/getcandelegatedmaxsize"
        return self.http_request(url, query_string, json_data)

    def solidity_getavailableunfreezecount(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetAvailableUnfreezeCountServlet.java
        """

        url = "/walletsolidity/getavailableunfreezecount"
        return self.http_request(url, query_string, json_data)

    def solidity_getcanwithdrawunfreezeamount(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetCanWithdrawUnfreezeAmountServlet.java
        """

        url = "/walletsolidity/getcanwithdrawunfreezeamount"
        return self.http_request(url, query_string, json_data)

    def solidity_getdelegatedresourceaccountindex(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetDelegatedResourceAccountIndexServlet.java
        """

        url = "/walletsolidity/getdelegatedresourceaccountindex"
        return self.http_request(url, query_string, json_data)

    def solidity_getdelegatedresourceaccountindexv2(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetDelegatedResourceAccountIndexV2Servlet.java
        """

        url = "/walletsolidity/getdelegatedresourceaccountindexv2"
        return self.http_request(url, query_string, json_data)

    def solidity_getexchangebyid(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetExchangeByIdServlet.java
        """

        url = "/walletsolidity/getexchangebyid"
        return self.http_request(url, query_string, json_data)

    def solidity_listexchanges(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ListExchangesServlet.java
        """

        url = "/walletsolidity/listexchanges"
        return self.http_request(url, query_string, json_data)

    def solidity_getaccountbyid(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetAccountByIdServlet.java
        """

        url = "/walletsolidity/getaccountbyid"
        return self.http_request(url, query_string, json_data)

    def solidity_getblockbyid(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetBlockByIdServlet.java
        """

        url = "/walletsolidity/getblockbyid"
        return self.http_request(url, query_string, json_data)

    def solidity_getblockbylimitnext(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetBlockByLimitNextServlet.java
        """

        url = "/walletsolidity/getblockbylimitnext"
        return self.http_request(url, query_string, json_data)

    def solidity_getblockbylatestnum(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetBlockByLatestNumServlet.java
        """

        url = "/walletsolidity/getblockbylatestnum"
        return self.http_request(url, query_string, json_data)

    def solidity_scanshieldedtrc20notesbyivk(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ScanShieldedTRC20NotesByIvkServlet.java
        """

        url = "/walletsolidity/scanshieldedtrc20notesbyivk"
        return self.http_request(url, query_string, json_data)

    def solidity_scanshieldedtrc20notesbyovk(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/ScanShieldedTRC20NotesByOvkServlet.java
        """

        url = "/walletsolidity/scanshieldedtrc20notesbyovk"
        return self.http_request(url, query_string, json_data)

    def solidity_isshieldedtrc20contractnotespent(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/IsShieldedTRC20ContractNoteSpentServlet.java
        """

        url = "/walletsolidity/isshieldedtrc20contractnotespent"
        return self.http_request(url, query_string, json_data)

    def solidity_gettransactioninfobyblocknum(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetTransactionInfoByBlockNumServlet.java
        """

        url = "/walletsolidity/gettransactioninfobyblocknum"
        return self.http_request(url, query_string, json_data)

    def solidity_getmarketorderbyaccount(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetMarketOrderByAccountServlet.java
        """

        url = "/walletsolidity/getmarketorderbyaccount"
        return self.http_request(url, query_string, json_data)

    def solidity_getmarketorderbyid(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetMarketOrderByIdServlet.java
        """

        url = "/walletsolidity/getmarketorderbyid"
        return self.http_request(url, query_string, json_data)

    def solidity_getmarketpricebypair(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetMarketPriceByPairServlet.java
        """

        url = "/walletsolidity/getmarketpricebypair"
        return self.http_request(url, query_string, json_data)

    def solidity_getmarketorderlistbypair(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetMarketOrderListByPairServlet.java
        """

        url = "/walletsolidity/getmarketorderlistbypair"
        return self.http_request(url, query_string, json_data)

    def solidity_getmarketpairlist(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetMarketPairListServlet.java
        """

        url = "/walletsolidity/getmarketpairlist"
        return self.http_request(url, query_string, json_data)

    def solidity_gettransactionbyid(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/solidity/GetTransactionByIdSolidityServlet.java
        """

        url = "/walletsolidity/gettransactionbyid"
        return self.http_request(url, query_string, json_data)

    def solidity_gettransactioninfobyid(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/solidity/GetTransactionInfoByIdSolidityServlet.java
        """

        url = "/walletsolidity/gettransactioninfobyid"
        return self.http_request(url, query_string, json_data)

    def solidity_gettransactioncountbyblocknum(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetTransactionCountByBlockNumServlet.java
        """

        url = "/walletsolidity/gettransactioncountbyblocknum"
        return self.http_request(url, query_string, json_data)

    def solidity_triggerconstantcontract(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/TriggerConstantContractServlet.java
        """

        url = "/walletsolidity/triggerconstantcontract"
        return self.http_request(url, query_string, json_data)

    def solidity_estimateenergy(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/EstimateEnergyServlet.java
        """

        url = "/walletsolidity/estimateenergy"
        return self.http_request(url, query_string, json_data)

    def getnodeinfo(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetNodeInfoServlet.java
        """

        url = "/wallet/getnodeinfo"
        return self.http_request(url, query_string, json_data)

    def solidity_getnodeinfo(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetNodeInfoServlet.java
        """

        url = "/walletsolidity/getnodeinfo"
        return self.http_request(url, query_string, json_data)

    def solidity_getBrokerage(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetBrokerageServlet.java
        """

        url = "/walletsolidity/getBrokerage"
        return self.http_request(url, query_string, json_data)

    def solidity_getReward(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetRewardServlet.java
        """

        url = "/walletsolidity/getReward"
        return self.http_request(url, query_string, json_data)

    def solidity_getburntrx(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetBurnTrxServlet.java
        """

        url = "/walletsolidity/getburntrx"
        return self.http_request(url, query_string, json_data)

    def solidity_getblock(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetBlockServlet.java
        """

        url = "/walletsolidity/getblock"
        return self.http_request(url, query_string, json_data)

    def solidity_getbandwidthprices(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetBandwidthPricesServlet.java
        """

        url = "/walletsolidity/getbandwidthprices"
        return self.http_request(url, query_string, json_data)

    def solidity_getenergyprices(self, query_string: str = None, json_data: dict = None):
        """
        source file:
                https://github.com/tronprotocol/java-tron/tree/develop/framework/src/main/java/org/tron/core/services/http/GetEnergyPricesServlet.java
        """

        url = "/walletsolidity/getenergyprices"
        return self.http_request(url, query_string, json_data)
