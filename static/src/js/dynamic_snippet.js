odoo.define('latest_blog.dynamic', function (require) {
   var PublicWidget = require('web.public.widget');
   var rpc = require('web.rpc');
   var core=require("web.core")
   var Qweb=core.qweb
   var Dynamic = PublicWidget.Widget.extend({
       selector: '.dynamic_snippet1',
       start: function () {
//       console.log('llllllllllllllllll')
           rpc.query({
               route: '/latest_blogs',
               params: {},
           }).then(function (result) {
               $(".qweb_top").append(Qweb.render('latest_blog.snippet',{result}));
           });
       },
   });

   PublicWidget.registry.dynamic_snippet1 = Dynamic;
   return Dynamic;
});