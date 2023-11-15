from flask import request
from flask_restful import Resource

from utils.decorators import validate_schema
from managers.quote_manager import QuoteManager
from schemas.request.quote_request import QuoteRequestSchema
from schemas.response.quote_response import QuoteResponseSchema


class QuoteResource(Resource):
    @validate_schema(QuoteRequestSchema)
    def post(self):
        req_body = request.get_json()
        quote = QuoteManager.create_quote(req_body)
        resp_schema = QuoteResponseSchema()
        return resp_schema.dump(quote)

    # @auth.login_required
    # def get(self):
    #     current_user = auth.current_user()
    #     print(current_user)
    #     cat_of_user = CatManager.select_cat_of_user(current_user.pk)
    #     resp_schema = CatResponseSchema()
    #     return resp_schema.dump(cat_of_user)
    