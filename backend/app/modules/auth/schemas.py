from marshmallow import Schema, fields, validate

class RegisterSchema(Schema):
    email = fields.Email(required=True, validate=validate.Length(max=255))
    password = fields.String(required=True, load_only=True, validate=validate.Length(min=8, max=255))
    first_name = fields.String(required=True, validate=validate.Length(max=255))
    last_name = fields.String(required=True, validate=validate.Length(max=255))
    phone = fields.String(required=False, allow_none=True,validate=validate.Length(max=20))