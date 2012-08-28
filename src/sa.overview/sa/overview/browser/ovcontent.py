from five import grok
from sa.overview.content.ovcontent import IOvContent


class View(grok.View):
    grok.context(IOvContent)
    grok.require('zope2.View')
    grok.name('view')
