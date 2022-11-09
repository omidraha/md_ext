from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTextInlineProcessor
from xml.etree import ElementTree
import re

IMG_WIDTH_RE = r"\{(.*?)\}"
IMG_SRC_RE = r"\((.*?)\)"


class ImgSizeExtension(Extension):

    def __init__(self, **kwargs):
        self.config = {}
        super(ImgSizeExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md):
        md.inlinePatterns.register(ImageSize(IMG_WIDTH_RE, md), 'img_size', 151)


class ImageSize(SimpleTextInlineProcessor):

    def handleMatch(self, m, data):
        img = ElementTree.Element('img')
        src = re.search(IMG_SRC_RE, data).group(1)
        img.set('src', src)
        img.set('width', m.group(1).split('=')[1])
        return img, 0, len(data)


def makeExtension(*args, **kwargs):
    return ImgSizeExtension(*args, **kwargs)
