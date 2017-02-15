routes = [
    ['GET', '/', 'www.home.main', 'html'],
    ['GET', '/sub', 'www.home.sub', 'html'],
    ['GET', '/users', 'www.user.main'],
    ['GET', '/user/<name>/<city>', 'www.user.main', 'html'],
    ['GET', '/api/users', 'api.users.main', 'json']
]