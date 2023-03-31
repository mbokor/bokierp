from extensions import db
todo_list = []

def get_last_id():
    last_todo = 1

    if todo_list:
        last_todo = todo_list[-1].id + 1

    return last_todo

class Todo(db.Model):

    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True)
    betreff = db.Column(db.String(100),nullable=False)
    beschreibung = db.Column(db.String(500),nullable=True)
    termin = db.Column(db.String(15),nullable=True)
    firma = db.Column(db.String(20),nullable=True)
    projekt = db.Column(db.String(20),nullable=True)
    sammelaufgabe = db.Column(db.Integer,nullable=True)
    status = db.Column(db.String(20),nullable=False, default="angelegt")

    @property
    def data(self):
        return {
            "id": self.id,
            "betreff": self.betreff,
            "beschreibung": self.beschreibung,
            "termin": self.termin,
            "firma": self.firma,
            "projekt": self.projekt,
            "sammelaufgabe": self.sammelaufgabe,
             "status": self.status
            }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    #aktuelle_id = 0

    #def __init__(self, betreff, beschreibung, termin, firma, projekt, sammelaufgabe , status):
    #    Todo.aktuelle_id += 1
    #    self.id = Todo.aktuelle_id
    #    self.betreff = betreff
    #    self.beschreibung = beschreibung
    #    self.termin = termin
    #    self.firma = firma
    #    self.projekt = projekt
    #    self.sammelaufgabe = sammelaufgabe
    #    self.status = status

    #@property
    #def data(self):
    #    return {
    #        "id": self.id,
    #        "betreff": self.betreff,
    #        "beschreibung": self.beschreibung,
    #        "termin": self.termin,
    #        "firma": self.firma,
    #        "projekt": self.projekt,
    #        "sammelaufgabe": self.sammelaufgabe,
    #        "status": self.status
    #    }