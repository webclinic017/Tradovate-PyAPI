##-----------------------------##
## Tradovate PyAPI             ##
## Written By: Ryan Smith      ##
##-----------------------------##
## URL Endpoints               ##
##-----------------------------##

## Constants
# -Base URLs
base_live = "https://live.tradovateapi.com/v1/"
base_demo = "https://demo.tradovateapi.com/v1/"
market_live = "https://md.tradovateapi.com/v1/"
market_demo = "https://md-demo.tradovateapi.com/v1/"
# -Authorization Endpoints
auth_oauth = "auth/oauthtoken"
auth_request = "auth/accesstokenrequest"
auth_renew = "auth/renewaccesstoken"
auth_me = "auth/me"
# -Account Endpoints
account_list = "account/list"
account_get_by_id = "account/item"
account_get_by_ids = "account/items"
account_get_by_name = "account/find"
account_dependents_by_id = "account/deps"
account_dependents_by_ids = "account/ldeps"
account_suggest = "account/suggest"
# -Account: Cash Balance Endpoints
cashbalance_list = "cashbalance/list"
cashbalance_by_id = "cashbalance/item"
cashbalance_by_ids = "cashbalance/items"
cashbalance_dependents_by_id = "cashbalance/deps"
cashbalance_dependents_by_ids = "cashbalance/ldeps"
cashbalance_snapshot_by_id = "cashbalance/getcashbalancesnapshot"
# -Account: Cash Balance Log Endpoints
# -Account: Margin Endpoints
# -Account: Permission Endpoints
# -Order Endpoints
order_create = "order/placeorder"
# -Position Endpoints
position_list = "position/list"
