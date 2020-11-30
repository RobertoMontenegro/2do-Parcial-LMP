from peewee import *

database = MySQLDatabase('marveluniverso',
                         **{'charset': 'utf8',
                            'sql_mode': 'PIPES_AS_CONCAT',
                            'use_unicode': True, 'host': 'localhost',
                            'user': 'root',
                            'password': '1234'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class Marvels(BaseModel):
    id = AutoField(column_name='ID')
    alignment = TextField()
    durability = IntegerField()
    energy_projection = IntegerField(column_name='energy_Projection')
    fighting_skills = IntegerField(column_name='fighting_Skills')
    gender = TextField()
    height_m = DecimalField()
    hometown = TextField()
    intelligence = IntegerField()
    name = TextField()
    popularity = IntegerField()
    speed = IntegerField()
    strength = IntegerField()
    weight_kg = DecimalField()

    def agregar(self, obj):
        Marvels.insert(
            id=obj.id,
            name=obj.name,
            popularity=obj.popularity,
            alignment=obj.alignment,
            gender=obj.gender,
            height_m=obj.height_m,
            weight_kg=obj.weight_kg,
            hometown=obj.hometown,
            intelligence=obj.intelligence,
            strength=obj.strength,
            speed=obj.speed,
            durability=obj.durability,
            energy_projection=obj.energy_projection,
            fighting_skills=obj.fighting_skills
        ).execute()

    def actualizar(self, id, nombreAtributo, nuevoValor):
        try:
            superheroe = (Marvels
                          .select()
                          .where(Marvels.id == id))
            setattr(superheroe[0], nombreAtributo, nuevoValor)
            (Marvels
             .update({nombreAtributo: nuevoValor})
             .where(Marvels.name == superheroe[0].name)
             .execute())
        except IndexError:
            print("No se ha encontrado el id")
        for sp in superheroe:
            print(nombreAtributo, '-> {}'
                  .format(getattr(sp, nombreAtributo)))

    def eliminar(self, id):
        try:
            res = Marvels.delete_by_id(id)
            return res
        except IndexError:
            return "No se ha encontrado el id"

    def obtener(self, id):
        try:
            superheroe = (Marvels
                          .select()
                          .where(Marvels.id == id))
            return Marvels().formatearSalida(superheroe[0])
        except IndexError:
            return "No se ha encontrado el id"

    def formatearSalida(self, obj):
        attrib = 'name, popularity, alignment, gender, height_m, weight_kg, hometown, intelligence, strength, speed, ' \
                 'durability, energy_projection, fighting_skills'.split(', ')
        texto = ''
        for at in attrib:
            atConFormato = str(at) + ': '
            texto = texto + atConFormato + str(getattr(obj, at)) + '\n'
        return texto

    class Meta:
        table_name = 'marvels'
