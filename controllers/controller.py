from odoo.addons.http_routing.models.ir_http import slug
from odoo import http
from odoo.http import request


class LatestBlog(http.Controller):
    @http.route(['/latest_blogs'], type="json", auth="public")
    def latest_blog(self):
        blog = request.env['blog.post'].search([], order='published_date desc', limit=4)
        blog_list = [[i.name, i.id, slug(i), slug(i.blog_id)] for i in blog]
        return blog_list
