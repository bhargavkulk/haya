from mako.template import Template
from mako.lookup import TemplateLookup
from docutils.writers.html4css1 import Writer, HTMLTranslator
from pathlib import Path
from docutils.core import publish_parts
from docutils import nodes
from docutils.transforms import Transform

class MoveFootnotesToEnd(Transform):
    default_priority = 850

    def apply(self):
        footnotes = []
        for node in self.document.traverse(nodes.footnote):
            footnotes.append(node)
            node.parent.remove(node)

        if footnotes:
            # Create section with 'footnotes' class
            footnote_section = nodes.section(classes=['footnotes'])
            self.document += footnote_section
            for footnote in footnotes:
                footnote_section += footnote

class HayaHTMLTranslator(HTMLTranslator):
    def __init__(self, document):
        super().__init__(document)
        self.metadata = {}  # Dictionary to store metadata fields
        self.documenttag_args = {'tagname' : 'div'}

    def visit_meta(self, node):
        """Handle meta nodes and add `<%inherit file="..." />` for templates."""
        name = node.get('name', None)
        content = node.get('content', None)
        if name and content:
            self.metadata[name] = content

            # Check if the "template" field is present
            if name == "template":
                # Add the Mako template inheritance directive
                self.body_pre_docinfo.insert(0, f'<%inherit file="{content}" />\n')

        # Call the base implementation to allow further processing if needed
        super().visit_meta(node)

    def depart_document(self, node) -> None:
        self.fragment.extend(self.body)  # self.fragment is the "naked" body
        self.html_body.extend(self.body_prefix[1:] + self.body_pre_docinfo
                              + self.docinfo + self.body
                              + self.body_suffix[:-1])
        assert not self.context, f'len(context) = {len(self.context)}'

    def visit_admonition(self, node) -> None:
        self.body.append(self.starttag(node, 'div', classes=['admonition']))

    def depart_admonition(self, node=None) -> None:
        self.body.append('</div>\n')

class HayaHTMLWriter(Writer):
    def __init__(self):
        super().__init__()
        self.translator_class = HayaHTMLTranslator

    def get_transforms(self):
            return super().get_transforms() + [MoveFootnotesToEnd]

    def translate(self):
        """Override to store metadata into the `parts` dictionary."""
        super().translate()
        self.parts['metadata'] = self.visitor.metadata

class PageWriter:
    input_dir: Path
    output_dir: Path
    lookup: TemplateLookup
    file_name: str

    def __init__(self, input_dir: str,
                 output_dir: str,
                 template_dir: str,
                 file_name: str):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.lookup = TemplateLookup(directories=[template_dir])
        self.file_name = file_name

    def write_page(self):
        input_file = self.input_dir / Path(f'{self.file_name}.rst')
        output_file = self.output_dir / Path(f'{self.file_name}.html')

        with input_file.open() as file:
            source = file.read()

        parts = publish_parts(source, writer=HayaHTMLWriter(), settings_overrides={'footnote_references': 'superscript'})
        html_body = parts['html_body']

        mytemplate = Template(html_body, lookup=self.lookup)

        with output_file.open('w') as file:
            file.write(mytemplate.render())
