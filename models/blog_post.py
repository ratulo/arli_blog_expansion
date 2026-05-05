from odoo import models, fields


class BlogPost(models.Model):
    _inherit = 'blog.post'

    front_page = fields.Boolean(
        string='Front Page Blog Post',
        default=False,
    )
    front_page_testimonial = fields.Boolean(
        string='Front Page Testimonial',
        default=False,
    )
    # testimonial_author stays non-translatable — proper name of the
    # quoted person doesn't change between languages. Position and the
    # project description do (e.g. "CEO" → "konateľ", a longer narrative
    # paragraph wants its own SK rewrite).
    testimonial_author = fields.Char(string='Testimonial Author')
    testimonial_author_position = fields.Char(string='Testimonial Author Position', translate=True)
    project_description = fields.Text(string='Project Description', translate=True)
    product_ids = fields.Many2many(
        'product.template',
        'blog_post_product_template_rel',
        'blog_post_id',
        'product_template_id',
        string='Products',
    )
