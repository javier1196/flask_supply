from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.support_department_problem_type import SupportDepartmentProblemType
from supply_core.use_cases.support_department import SupportDepartment
from flask import jsonify
import json


class ListSupportDepartmentProblemTypeAPI(ResourceBase):
    decorators = [auth.login_required]

    def _init_(self):
        super(ListSupportDepartmentProblemTypeAPI, self).init()

    def get(self):
        try:
            bridge = SupportDepartmentProblemType()
            # access = Department(bridge)
            return jsonify(bridge.list())

        except Exception as e:
            return self.handle_error(e)
