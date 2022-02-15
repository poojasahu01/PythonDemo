import requests
import pandas as pd

bashapi = "http://toolseng-infra-prd.corp.pep.pvt/toolseng-prd/rest/AssetAnalysis?QUERY=((ANAL_CFGM_BF_AGT_STAT[EQ]INSTALL)[OR](ANAL_CFGM_BF_AGT_STAT[EQ]AGT_ERROR))[AND]((ANAL_OPSYS[EQ]WIN*)[AND]([NOT]ANAL_OPSYS[EQ]WIN%202003*))&GET=host_name,anal_scope,ANAL_CFGM_BF_AGT_STAT,ANAL_OPSYS"

response = requests.get(bashapi)

response1 = response.json()
print(response1)
