from marshmallow import Schema, fields, validate


class QuoteBaseSchema(Schema):
    customer_names = fields.String(required=True, validate=validate.Length(min=2, max=255))
    email = fields.Email(required=True)
    phone_number = fields.String(required=True, validate=validate.Length(min=2, max=255))
    description = fields.String(validate=validate.Length(max=255))