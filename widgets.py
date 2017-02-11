#encoding=utf-8
from wtforms import fields, widgets

# Define wtforms widget and field
class CKTextAreaWidget(widgets.TextArea):

    def __call__(self, field, **kwargs):
        kwargs.setdefault('class_', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(fields.TextField):
    widget = CKTextAreaWidget()


class SimpleMDEAreaWidget(widgets.TextArea):

    def __call__(self, field, **kwargs):
        kwargs.setdefault('class_', 'simplemde')
        return super(SimpleMDEAreaWidget, self).__call__(field, **kwargs)


class SimpleMDEAreaField(fields.TextField):
    widget = SimpleMDEAreaWidget()
