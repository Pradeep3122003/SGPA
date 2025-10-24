from marshmallow import Schema, fields, validate, ValidationError

class RegisterSchema(Schema):
    first_name = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    last_name = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))
