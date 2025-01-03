BASENAMES_REGISTRAR_CONTROLLER_ADDRESS_MAINNET = "0x4cCb0BB02FCABA27e82a56646E81d8c5bC4119a5"
BASENAMES_REGISTRAR_CONTROLLER_ADDRESS_TESTNET = "0x49aE3cC2e3AA768B1e5654f5D3C6002144A59581"
L2_RESOLVER_ADDRESS_MAINNET = "0xC6d566A56A1aFf6508b41f6c90ff131615583BCD"
L2_RESOLVER_ADDRESS_TESTNET = "0x6533C94869D28fAA8dF77cc63f9e2b2D6Cf77eBA"

DAOHAUS_GRAPH_URLS = {
    "0x2105": "/subgraphs/id/7yh4eHJ4qpHEiLPAk9BXhL5YgYrTrRE6gWy8x4oHyAqW",
}

SUMMON_CONTRACTS = {
    "HIGHER_HOS_SUMMONER": {
        "0xaa36a7": "",  
        "0x2105": "0x4050E747Ed393e1Fd89783662C48373421fD0647"  
    },
    "YEET24_SUMMONER": {
        "0xaa36a7": "0xde65e8b424438b361d8f4a8896f92956510b08dc",  # "0x78cf150b2E684562C0510C0b699edE1DCD69b983"
        "0x2105": "0xe6eB99FaB27bE81D5F5F4dC44fCdf508a1B97Cd3"  # "0x788C55D87a416F391E93a986AbB1e2b2960d0079"
    },
    "YEETER_SINGLETON": {
        "0xaa36a7": "0x62ff4ca410e9e58f5ce8b2ad03695ef0ad990381",
        "0x2105": "0x8D60971eFf778966356c1cADD76d525E7B25cc6b"
    },
    "YEET24_SINGLETON": {
        "0xaa36a7": "0x9CA5ABC37BE4716A494E958d7404DE19cad9d858",  # "0x59a7C71221d05e30b9d7981AB83f0A1700e51Af8"
        "0x2105": "0xcbcdce90ddaf50739dfb90b84e9b84a312b0a4e5"  # "0x2f3637757875414c938EF80A5aD197aAaCDaA924"
    },
    "YEET24_CLAIM_MODULE": {
        "0xaa36a7": "0xDC38DB792fFf0d7E321411DC03D80d8C9c0AC836",
        "0x2105": "0xc5ec2eabfd8d1a1e38896ad2ec1d452f66dac761"
    },
    "GOV_LOOT_SINGLETON": {
        "0xaa36a7": "0x8a4a9e36106ee290811b89e06e2fafe913507965",
        "0x2105": "0x59a7C71221d05e30b9d7981AB83f0A1700e51Af8"
    },
    "DH_TOKEN_SINGLETON": {
        "0xaa36a7": "0x8a4a9e36106ee290811b89e06e2fafe913507965",
        "0x2105": "0xD2bA2c50D16D35d6B8642A06b2C882F9fe790EDD"
    },
    "GNOSIS_SAFE_PROXY_FACTORY": {
        "0xaa36a7": "0xc22834581ebc8527d974f8a1c97e1bea4ef910bc",
        "0x2105": "0xC22834581EbC8527d974F8a1c97E1bEA4EF910BC"
    },
    "GNOSIS_SAFE_MASTER_COPY": {
        "0xaa36a7": "0x69f4d1788e39c87893c980c06edf4b7f686e2938",
        "0x2105": "0x69f4D1788e39c87893C980c06EdF4b7f686e2938"
    },
    "UNISWAP_V3_NF_POSITION_MANAGER": {
        "0xaa36a7": "0x1238536071E1c677A632429e3655c799b22cDA52",
        "0x2105": "0x03a520b32C04BF3bEEf7BEb72E919cf822Ed34f1"
    },
    "WETH": {
        "0xaa36a7": "0xfFf9976782d46CC05630D1f6eBAb18b2324d6B14",
        "0x2105": "0x4200000000000000000000000000000000000006"
    },
    "POSTER": {
        "0xaa36a7": "0x000000000000cd17345801aa8147b8d3950260ff",
        "0x2105": "0x000000000000cd17345801aa8147b8d3950260ff"
    },
    "GNOSIS_MULTISEND": {
        "0xaa36a7": "0x998739BFdAAdde7C933B942a68053933098f9EDa",
        "0x2105": "0x998739BFdAAdde7C933B942a68053933098f9EDa",
    },
}


DEFAULT_MEME_YEETER_VALUES = {
 "poolFee": 10000,
  "boostRewardFees": 90000,
}
MEME_SHAMAN_PERMISSIONS = 3
YEET_SHAMAN_PERMISSIONS = 2

DEFAULT_YEETER_VALUES = {
    "isShares": True,
    "feeRecipients": [
        "0xD0f8720846890a7961945261FE5012E4cA39918e",
        "0x4a9a27d614a74ee5524909ca27bdbcbb7ed3b315",
    ],  # yeeter team, daohaus eco fund 
    "feeAmounts": [5000, 5000],  # .5% fees
    "multiplier": 100000,
    "minThresholdGoal": 10000000000000000,  # .01
    "price": 1000000000000000, # .0069
}

DEFAULT_SUMMON_VALUES = {
  "votingPeriodInSeconds": 259200,
  "gracePeriodInSeconds": 172800,
  "newOffering": 10000000000000000, # .1
  "quorum": 15,
  "sponsorThreshold": 100000000000000000000, # 100
  "minRetention": 33,
  "votingTransferable": False,
  "nvTransferable": True,
}

DEFAULT_FORM_VALUES = {
    "form": "0x"
}

DEFAULT_START_DATE_OFFSET = 600 # 10 minutes

DEFAULT_DURATION = 1800 # 30 minutes

DEFAULT_DAO_PARAMS = {
    "NAME": "YEET DAO",
    "SYMBOL": "YEET",
}