from marshmallow import fields

from schemas.bases import QuoteBaseSchema


class QuoteRequestSchema(QuoteBaseSchema):
    cad_file = fields.String(required=True)