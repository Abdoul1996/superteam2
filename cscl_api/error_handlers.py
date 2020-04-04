from flask import Blueprint, abort
from werkzeug import exceptions as w_exceptions
blueprint = Blueprint('error_handlers', __name__)

@blueprint.app_errorhandler(w_exceptions.BadRequest)
def error_bad_request(err):
    abort(400, err)

@blueprint.app_errorhandler(w_exceptions.NotFound)
def not_found(err):
    abort(404, err)
