from dao.model.director import Director


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Director).get(bid)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, director_d):
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        try:
            director = self.get_one(rid)
            self.session.delete(director)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False

    def update(self, director_d):
        try:
            director = self.get_one(director_d.get("id"))
            director.name = director_d.get("name")

            self.session.add(director)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False
