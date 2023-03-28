class ErrorApp(Exception):
    """Class Default to Error in application."""
    status = 400


class ErrorPartnerGreaterEqual500(ErrorApp):
    status = 500


class ErrorPartnerGreaterEqual400(ErrorApp):
    status = 400


class ErrorRequests(ErrorApp):
    status = 500


class ErrorStartServer(ErrorApp):
    status = 500
