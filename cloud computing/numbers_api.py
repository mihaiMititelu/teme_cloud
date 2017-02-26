import web
import json

tree = open('numbers.json').read()

urls = (
    '/numbers', 'list_numbers',
    '/numbers/(.*)', 'get_number'
)

app = web.application(urls, globals())


class list_numbers:
    def GET(self):
        return json.loads(tree)


class get_number:
    def GET(self, user):
        for child in json.loads(tree):
            if child['id'] == user:
                return str(child['value'])


if __name__ == "__main__":
    app.run()
