from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Flask RESTplus', description='Simple Flask-RESTplus-API by Jan Macenka')
ns = api.namespace('languages', description='Known programming languages')

a_language = api.model('Language', {
    'language' : fields.String(description='Programming language')
})

a_language_full = api.model('Language', {
    'id' : fields.Integer(description='Language Identifyer', readOnly=True),
    'language' : fields.String(description='Programming language')
})

languages = []
python = {'language' : 'Python', 'id' : 1}
languages.append(python)

@ns.route('/')
class Language(Resource):
    @ns.doc('list_languages')
    @ns.marshal_list_with(a_language_full)
    def get(self):
        return languages

    @ns.doc('create_language')
    @ns.expect(a_language)
    @ns.marshal_list_with(a_language, code=201)
    def post(self):
        new_language = api.payload
        new_language['id'] = len(languages) + 1
        languages.append(new_language)
        return {'result' : 'Language added'}, 201

    @ns.doc('update_language')
    @ns.expect(a_language_full)
    @ns.marshal_with(a_language_full)
    def put(self, id):
        languages[id] = api.payload
        return {'updated' : languages[id]}

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
