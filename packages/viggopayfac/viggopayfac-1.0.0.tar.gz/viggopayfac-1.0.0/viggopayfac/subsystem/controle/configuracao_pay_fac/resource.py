from enum import Enum

import sqlalchemy

from viggocore.common.subsystem import entity
from viggocore.database import db


class ConfiguracaoPayFacTipo(Enum):
    HOMOLOGACAO = 'HOMOLOGACAO'
    PRODUCAO = 'PRODUCAO'


class ConfiguracaoPayFac(entity.Entity, db.Model):

    attributes = ['client_id', 'client_secret', 'tipo']
    attributes += entity.Entity.attributes

    client_id = db.Column(db.String(100), nullable=False)
    client_secret = db.Column(db.String(100), nullable=False)
    tipo = db.Column(sqlalchemy.Enum(ConfiguracaoPayFacTipo),
                     nullable=False)

    def __init__(self, id, client_id, client_secret, tipo,
                 active=True, created_at=None, created_by=None,
                 updated_at=None, updated_by=None, tag=None):
        super().__init__(id, active, created_at, created_by,
                         updated_at, updated_by, tag)
        self.client_id = client_id
        self.client_secret = client_secret
        self.tipo = tipo

    @classmethod
    def individual(self):
        return 'configuracao_pay_fac'
