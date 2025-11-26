# -*- coding: utf-8 -*-
# from odoo import http


# class Directory(http.Controller):
#     @http.route('/directory/directory', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/directory/directory/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('directory.listing', {
#             'root': '/directory/directory',
#             'objects': http.request.env['directory.directory'].search([]),
#         })

#     @http.route('/directory/directory/objects/<model("directory.directory"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('directory.object', {
#             'object': obj
#         })
