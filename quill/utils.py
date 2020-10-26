
def make_response(
    success: bool,
    message: str,
    data: dict = None,
    errors: list = None):

    if success:
        if not data:
            raise Exception("Successful response must have a payload")
        return {
            'success': True,
            'message': message,
            'data': data
        }
    if not success:
        if not errors:
            raise Exception("Failed response must have a list of errors")
        return {
            'success': False,
            'message': message,
            'errors': errors
        }
