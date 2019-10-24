from app import db
class DBcomment(db.Model):
    __tablename__='dbcomment'
    DBCommentID=db.Column(db.Integer,primary_key=True)
    TIME=db.Column(db.VARCHAR)
    DB_ID=db.Column(db.VARCHAR)
    DB_RATING=db.Column(db.VARCHAR)
    DB_CONTENT=db.Column(db.Text)
    CREATOR=db.Column(db.VARCHAR)
    ADD_TIME=db.Column(db.VARCHAR)

    def __repr(self):
        return '<DBcomment %r>' % self.name

class DBfilm(db.Model):
    __tablename__='dbfilm'
    key=db.Column(db.Integer,primary_key=True)
    director=db.Column(db.VARCHAR)
    rate=db.Column(db.VARCHAR)
    star=db.Column(db.VARCHAR)
    name=db.Column(db.VARCHAR)
    url=db.Column(db.VARCHAR)
    cast=db.Column(db.VARCHAR)
    cover = db.Column(db.VARCHAR)
    id = db.Column(db.VARCHAR)

    def __repr(self):
        return '<DBfilm %r>' % self.name


class Filmid(db.Model):
    __tablename__='filmid'
    key=db.Column(db.Integer,primary_key=True)
    DB_ID=db.Column(db.VARCHAR)
    IMDB_ID=db.Column(db.VARCHAR)

    def __repr(self):
        return '<Filmid %r>' % self.name

class IMDBcomment(db.Model):
    __tablename__='imdbcomment'
    id=db.Column(db.Integer,primary_key=True)
    helpfulness=db.Column(db.VARCHAR)
    IMDB_ID=db.Column(db.VARCHAR)
    IMDB_RATING=db.Column(db.VARCHAR)
    SUMMARY=db.Column(db.Text)
    IMDB_CONTENT=db.Column(db.Text)
    TIME=db.Column(db.VARCHAR)
    userName = db.Column(db.VARCHAR)

    def __repr(self):
        return '<IMDBcomment %r>' % self.name


class IMDBfilm(db.Model):
    __tablename__='imdbfilm'
    key=db.Column(db.Integer,primary_key=True)
    actors=db.Column(db.Text)
    country=db.Column(db.VARCHAR)
    directors=db.Column(db.VARCHAR)
    IMDB_ID=db.Column(db.VARCHAR)
    language=db.Column(db.VARCHAR)
    name=db.Column(db.VARCHAR)
    onTime=db.Column(db.VARCHAR)
    posterURL=db.Column(db.VARCHAR)
    ratingNum=db.Column(db.VARCHAR)
    score=db.Column(db.VARCHAR)
    scriptKeyWords=db.Column(db.VARCHAR)
    summary=db.Column(db.Text)
    tagLine=db.Column(db.VARCHAR)
    tags=db.Column(db.VARCHAR)
    cast = db.Column(db.Text)

    def __repr(self):
        return '<IMDBfilm %r>' % self.name