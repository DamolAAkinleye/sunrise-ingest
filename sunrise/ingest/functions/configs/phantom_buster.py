from enum import Enum


class PhantomsAgent(str, Enum):
    LINKEDIN_FOLLOWERS = "8321478019160429"
    SALES_NAVIGATOR = "1927480176628162"
    LINKEDIN_COMPANY_FOLLOWERS = "2097137271922468"


class PhantomStorageFolder(str, Enum):
    LINKEDIN_FOLLOWERS = "74UWogzQ1SglwovSV9uK1g"
    LINKEDIN_COMPANY_FOLLOWERS = "YCQE7GaHmhVOYCR5yQUb1g"
    SALES_NAVIGATOR = "lD88imUnaS6rq4NakPlMFA"


PHANTOM_ORG_FOLDER = "SUweCmfqhIg"
PHANTOM_RESULT_BLOB = "result.json"
