from flask_sqlalchemy import SQLAlchemy
from .models import DBcomment,DBfilm,IMDBcomment,IMDBfilm,Filmid
from flask import render_template,redirect,url_for
from .forms import IDForm,IMDBIDForm
import re,collections
import jieba
def init_views(app):
    @app.route('/',methods=['GET','POST'])
    def index():
        CNinf,CNcom,Overseainf,Overseacom=getData()
        return render_template('index.html',CNinf=CNinf,CNcom=CNcom,Overseainf=Overseainf,Overseacom=Overseacom)

    def getData():
        CNinf=format(DBfilm.query.count(),',')
        CNcom=format(DBcomment.query.count(),',')
        Overseainf=format(IMDBfilm.query.count(),',')
        Overseacom=format(IMDBcomment.query.count(),',')
        return CNinf,CNcom,Overseainf ,Overseacom


    @app.route('/charts',methods=['GET','POST'])
    def charts():
        form=IDForm()
        id=None
        if form.validate_on_submit():
            id=form.id.data
            form.id.data=''
        filminf = DBfilminf()
        ranking=DBRanking(filminf,id)
        cominf=DBcommentinf(id)
        wcount=Wordcount(cominf)
        ratecount=Ratecount(cominf)
        return render_template('charts.html',form=form,id=id,cominf=cominf,count=wcount,ratecount=ratecount,ranking=ranking)

    def DBcommentinf(id):
        DBcommentModel=DBcomment.query.filter(DBcomment.DB_ID ==id).all()
        DBcommentinf=[]
        for item in DBcommentModel:
            DBcommentinf.append(item)
        return DBcommentinf

    def Wordcount(cominf):
        word=''
        stopword=stopwordslist('./app/stopword.txt')
        for i in cominf:
            seglist=jieba.cut(i.DB_CONTENT,cut_all=False)
            for j in seglist:
                if j not in stopword:
                    if j != '\t':
                        word+=j
                        word+=" "
        wordbox=[]
        wordbox.extend(word.strip().split())
        count=collections.Counter(wordbox).most_common(80)
        return count

    def Ratecount(cominf):
        rate=[]
        for i in cominf:
            if i.DB_RATING is not None:
                rate.append(i.DB_RATING)
        ratecount=collections.Counter(rate).most_common()
        return ratecount

    def DBRanking(filminf,id):
        if id is None:
            return 0
        else:
            rating=[]
            for i in filminf:
                if i.id==id:
                    if i.rate is not None:
                        tag=float(i.rate)
                rating.append(i.rate)
            new_rating = [];
            for n in rating:
                if n is not None:
                    new_rating.append(float(n));
            rating = new_rating;
            rating.sort()
            result=rating.index(tag)
            Rank=format((result+1)*100/len(rating),'.2f')
            return Rank


    @app.route('/overseacharts',methods=['GET','POST'])
    def overseacharts():
        form=IMDBIDForm()
        id=None
        if form.validate_on_submit():
            id=form.id.data
            form.id.data=''
        cominf=IMDBcommentinf(id)
        wcount=imdbwordcount(cominf)
        filminf=IMDBfilminf()
        ranking=IMDBRanking(filminf,id)
        ratecount=IMDBRatecount(cominf)
        return render_template('overseacharts.html',form=form,id=id,cominf=cominf,count=wcount,ratecount=ratecount,ranking=ranking)

    def IMDBRatecount(cominf):
        rate=[]
        for i in cominf:
            if i.IMDB_RATING is not None:
                rate.append(i.IMDB_RATING)
        ratecount=collections.Counter(rate).most_common()
        return ratecount

    def IMDBRanking(filminf,id):
        if id is None:
            return 0
        else:
            rating=[]
            for i in filminf:
                if i.IMDB_ID==id:
                    if i.score is not None:
                        tag=float(i.score)
                rating.append(i.score)
            new_rating = [];
            for n in rating:
                if n is not None:
                    new_rating.append(float(n));
            rating = new_rating;
            rating.sort()
            result=rating.index(tag)
            Rank=format((result+1)*100/len(rating),'.2f')
            return Rank


    def IMDBcommentinf(id):
        IMDBcommentModel=IMDBcomment.query.filter(IMDBcomment.IMDB_ID == id).all()
        IMDBcommentinf=[]
        for item in IMDBcommentModel:
            IMDBcommentinf.append(item)
        return IMDBcommentinf

    def imdbwordcount(cominf):
        word=''
        stopword=stopwordslist('./app/enstopword.txt')
        for i in cominf:
            seglist=i.IMDB_CONTENT.strip().split()
            for j in seglist:
                if j.lower() not in stopword:
                    if j != '\t':
                        word+=j
                        word+=" "
        wordbox=[]
        wordbox.extend(word.strip().split())
        count=collections.Counter(wordbox).most_common(50)
        return count


    def stopwordslist(filepath):
        stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
        return stopwords


    @app.route('/tables',methods=['GET','POST'])
    def tables():
        CNfilminf=DBfilminf()
        return render_template('tables.html',filminf=CNfilminf)

    def DBfilminf():
        DBfilmModel=DBfilm.query.all()
        DBfilminf=[]
        for item in DBfilmModel:
            DBfilminf.append(item)
        return DBfilminf

    @app.route('/overseatables', methods=['GET', 'POST'])
    def overseatables():
        Overseafilminf = IMDBfilminf()
        return render_template('overseatables.html', filminf=Overseafilminf)

    def IMDBfilminf():
        IMDBfilmModel=IMDBfilm.query.all()
        IMDBfilminf=[]
        for item in IMDBfilmModel:
            IMDBfilminf.append(item)
        return IMDBfilminf