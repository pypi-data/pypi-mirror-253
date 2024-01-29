#

BACKEND_ENDPOINT = {
    "dev": "http://127.0.0.1:8000",
    "prod": "http://xprompt-server-env.eba-yvum4nem.us-west-2.elasticbeanstalk.com",
}


def get_backend_endpoint(debug=False):
    """
    Get backend endpoint based on debug mode
    Args:
        debug: Local host if True

    Returns:
    backend endpoint
    """
    return BACKEND_ENDPOINT["dev" if debug else "prod"]
