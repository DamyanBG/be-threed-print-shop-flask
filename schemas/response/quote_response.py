from marshmallow import fields

from schemas.bases import QuoteBaseSchema


class QuoteResponseSchema(QuoteBaseSchema):
    pk = fields.Integer(required=True)
    created_on = fields.DateTime(required=True)
    # Here maybe will be file_url
    file_path = fields.String(required=True)