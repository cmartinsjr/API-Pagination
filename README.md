# API-Pagination
information on prismacloud API pagination

You need to check the "Total Count" header and compare it to the sum of offset+limit after each API call as shown in the if statement at the end of my script. The total count is returned as a response header on any endpoint that returns large numbers of results, as stated in this python library: https://github.com/PaloAltoNetworks/prismacloud-api-python/blob/ceda70141d16e65eb2952af378e7c5a8a42e8fca/prismacloud/api/cwpp/cwpp.py#L40 


also important to note that this is different per API:
Cloud Security: https://github.com/PaloAltoNetworks/prismacloud-api-python/blob/ceda70141d16e65eb2952af378e7c5a8a42e8fca/prismacloud/api/cspm/cspm.py#L78C12-L78C101
Application Security: https://github.com/PaloAltoNetworks/prismacloud-api-python/blob/ceda70141d16e65eb2952af378e7c5a8a42e8fca/prismacloud/api/pccs/pccs.py#L24
