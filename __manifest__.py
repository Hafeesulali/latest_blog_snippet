{'name': 'Latest Blog',
 'installable': True,
 'auto_install': False,
 'version': '16.0.1.0.0',
 'depends': ['base', 'website'],
 'data': [
     'views/q_web.xml',
     'views/snippet_inherit_view.xml'],
 'assets': {
     'web.assets_frontend': [
         '/latest_blog/static/src/js/dynamic_snippet.js',
         '/latest_blog/static/src/xml/snippet_view.xml',
         '/latest_blog/static/src/css/snippet.scss',
     ]}

 }
