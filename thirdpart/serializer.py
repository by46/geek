from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)


from flask_restful import fields

MAPPING = {
    'integer': fields.Integer
}


class SerializerMetaclass(type):
    def __new__(cls, name, bases, attributes):
        if name == 'Serializer':
            return type.__new__(cls, name, bases, attributes)

        model = attributes.pop('__model__', None)  # type: User
        class_dict = attributes.copy()
        class_dict['resource_fields'] = resource_fields = {}
        if model:
            for column in model.__table__.columns:
                field_type_name = column.type.__visit_name__
                field_type = MAPPING.get(field_type_name)
                if not field_type:
                    field_type = fields.String
                resource_fields[column.name] = field_type
        return type.__new__(cls, name, bases, class_dict)


class Serializer(object):
    __metaclass__ = SerializerMetaclass


class UserSerializer(Serializer):
    __model__ = User


if __name__ == '__main__':
    user = User()
    print(UserSerializer().resource_fields)
