from connexion.problem import problem
from connexion import decorators
from jsonschema import ValidationError


class RequestBodyValidator(decorators.validation.RequestBodyValidator):
    """
    This class overrides the default connexion RequestBodyValidator
    so that it returns the complete string representation of the
    error, rather than just returning the error message.

    Prev Err message: "detail": "None is not of type 'object'",

    Code Retrieved from:
    https://github.com/zalando/connexion/issues/879#issuecomment-561158597
    """

    def validate_schema(self, data, url):
        if self.is_null_value_valid:
            return None

        try:
            self.validator.validate(data)
        except ValidationError as exception:
            return problem(400, "Bad Request", str(exception))

        return None
