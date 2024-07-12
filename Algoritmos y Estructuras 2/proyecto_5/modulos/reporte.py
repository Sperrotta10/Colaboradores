import configparser
from modulos.empresa import GestionEmpresas
from modulos.proyecto import GestionProyectos
from modulos.tareas import GestionTareas
from modulos.sprint import GestionSprints

class Reporte:
    def __init__(self, empresas_file, proyectos_file, tareas_file, sprints_file):
        self.gestion_empresas = GestionEmpresas(empresas_file)
        self.gestion_proyectos = GestionProyectos(proyectos_file)
        self.gestion_tareas = GestionTareas(tareas_file)
        self.gestion_sprints = GestionSprints(sprints_file)

    


