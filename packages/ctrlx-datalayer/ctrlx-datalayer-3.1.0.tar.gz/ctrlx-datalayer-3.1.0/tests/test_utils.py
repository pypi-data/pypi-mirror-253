import os

# export INTEGRATION=1
# unset INTEGRATION


def is_integration_test() -> bool:
    """ is_integration_test """
    return os.getenv("INTEGRATION") is not None

# port 443 is needed


def client_connection() -> str:
    """ client_connection """
    addr = os.getenv("CTRLX_ADDRESS")
    port = os.getenv("CTRLX_SSL_PORT")
    if addr is None or addr == "":
        addr = "127.0.0.1"
    if port is None or port == "":
        port = "443"
    return "tcp://boschrexroth:boschrexroth@{}:2069?sslport={}".format(addr, port)


def provider_connection() -> str:
    """ client_connection """
    addr = os.getenv("CTRLX_ADDRESS")
    port = os.getenv("CTRLX_SSL_PORT")
    if addr is None or addr == "":
        addr = "127.0.0.1"
    if port is None or port == "":
        port = "443"
    return "tcp://boschrexroth:boschrexroth@{}:2070?sslport={}".format(addr, port)


def client_timeout() -> int:
    """ client_timeout """
    t = os.getenv("CTRLX_TIMEOUT")
    if t is None or t == "":
        return 2000
    return int(t)


def root_node_alldata_provider() -> str:
    """ root_node_alldata_provider """
    t = os.getenv("ALLDATA_PROVIDER")
    if t is None or t == "":
        return ""
    return t  # "sdk-cpp-alldata"
