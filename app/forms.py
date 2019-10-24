from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


class IDForm(FlaskForm):
    id=StringField('请输入要查询的豆瓣ID',validators=[DataRequired()])
    submit=SubmitField('查询')

class IMDBIDForm(FlaskForm):
    id=StringField('请输入要查询的IMDBID',validators=[DataRequired()])
    submit=SubmitField('查询')
