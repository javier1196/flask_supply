from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.admin_support import AdminSupportAdapter
from flask import jsonify
import json


class DeleteAdminSupportAPI(ResourceBase):
    decorators = [auth.login_required]

    def _init_(self):
        super(DeleteAdminSupportAPI, self).init()

    def get(self, id):
        try:
            bridge = AdminSupportAdapter()
            return jsonify(bridge.delete(str(id)))

        except Exception as e:
            return self.handle_error(e)
