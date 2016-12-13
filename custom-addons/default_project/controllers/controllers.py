# -*- coding: utf-8 -*-
from odoo import http

# class DefaultProject(http.Controller):
#     @http.route('/default_project/default_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/default_project/default_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('default_project.listing', {
#             'root': '/default_project/default_project',
#             'objects': http.request.env['default_project.default_project'].search([]),
#         })

#     @http.route('/default_project/default_project/objects/<model("default_project.default_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('default_project.object', {
#             'object': obj
#         })