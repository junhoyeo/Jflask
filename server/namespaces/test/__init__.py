from flask_restplus import Namespace

test_ns = Namespace('test', description='API test')

# models
import server.namespaces.test.models

# resources
import server.namespaces.test.resources.test
