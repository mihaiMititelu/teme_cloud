import web
import json
import os

os.environ["PORT"] = "80"
tree = open('names.json').read()

urls = (
    '/names', 'list_names',
    '/names/(.*)', 'get_name'
)

app = web.application(urls, globals())


class list_names:
    def GET(self):
        return json.loads(tree)


class get_name:
    def GET(self, user):
        for child in json.loads(tree):
            if child['id'] == user:
                return str(child['value'])


if __name__ == "__main__":
    app.run()
