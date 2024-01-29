"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Scope , String
from xblock.core import XBlock
from django.template import Template, Context
try:
    from xblock.utils.resources import ResourceLoader
except ModuleNotFoundError:  # For backward compatibility with releases older than Quince.
    from xblockutils.resources import ResourceLoader
resource_loader = ResourceLoader(__name__)

@XBlock.needs("i18n")
class LabXBlock(XBlock):
   
    icon_class = 'problem'
    total_score = Integer(
        default=1,
        scope=Scope.settings
    )

    
    @property
    def has_score(self):
        return True
    
    @property
    def _(self):
        i18nServer = self.runtime.service(self, 'i18n')
        return i18nServer.ugettext
    
    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the LabXBlock, shown to students
        when viewing courses.
        """
        # html = self.resource_string("templates/html/labxblock.html")
        
    
        # template_str = self.resource_string('templates/labxblock.html')
        # template = Template(template_str)
        # rendered_html = template.render(Context(''))
        frag = Fragment()
        frag.add_content(resource_loader.render_django_template(
            'templates/labxblock.html',
            # i18n_service=self.runtime.service(self, 'i18n')
        ))
        frag.add_css(self.resource_string("static/css/labxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/labxblock.js"))
        frag.initialize_js('LabXBlock')
        return frag

    def studio_view(self, context):
        """
        The view for editing the AudioXBlock parameters inside Studio.
        """
        html = self.resource_string("static/html/labxblock_edit.html")
        frag = Fragment(html.format(self=self))
        frag.add_javascript(self.resource_string("static/js/src/labxblock_edit.js"))
        frag.initialize_js('LabEditBlock')
        return frag   

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        
        self.runtime.publish(self, "grade", { "value": 1, "max_value": 1})
       
        return {"message": 'success'}

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("LabXBlock",
             """<labxblock/>
             """),
            ("Multiple LabXBlock",
             """<vertical_demo>
                <labxblock/>
                <labxblock/>
                <labxblock/>
                </vertical_demo>
             """),
        ]
