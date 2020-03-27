from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.department import DepartmentAdapter
from supply_core.use_cases.department import Department
from flask import jsonify
import json


class ListDepartmentAPI(ResourceBase):
    decorators = [auth.login_required]

    def _init_(self):
        super(ListDepartmentAPI, self)._init_()

    def get(self):
        try:
            bridge = DepartmentAdapter()
            # access = Department(bridge)
            return jsonify(bridge.list())

        except Exception as e:
            return self.handle_error(e)