from sqlalchemy import Column, Integer, ForeignKey, UnicodeText
from reahl.sqlalchemysupport import Session, Base
from sqlalchemy.orm import relationship
from reahl.domain.systemaccountmodel import LoginSession, EmailAndPasswordSystemAccount

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)

    system_account_id = Column(Integer, ForeignKey(EmailAndPasswordSystemAccount.id), nullable=False)
    system_account = relationship(EmailAndPasswordSystemAccount)

    name = Column(UnicodeText)
    surname = Column(UnicodeText)

        
class PersonFactory:

    @classmethod
    def person_for_current_session(cls):
        login_session = LoginSession.for_current_session()
        if not login_session:
            return None

        system_account = login_session.account
        person = Session.query(Person).filter_by(system_account_id=system_account.id).one()
        return person

    @classmethod
    def create_person_for_account(cls, system_account):
        #TODO: make sure system account is not already used...
        person = Person()
        Session.add(person)
        person.system_account = system_account
        return person

        
