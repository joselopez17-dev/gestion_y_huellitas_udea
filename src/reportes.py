# Cálculo de estadísticas y reportes.

from datetime import date

try:
    from .archivos import c_archivos
except ImportError:
    from archivos import c_archivos

class c_reportes:

    def __init__(self, gestor_archivos=None):
        self.gestor_archivos = gestor_archivos or c_archivos()

    def _registros(self):
        return self.gestor_archivos.obtener_todos()

    def calcular_promedio_dias_respuesta(self):
        dias = [
            (date.fromisoformat(registro["fecha_respuesta"])
             - date.fromisoformat(registro["fecha_radicacion"])).days
            for registro in self._registros()
            if registro.get("estado_peticion") == "Solucionada"
            and registro.get("fecha_respuesta")
            and registro.get("fecha_radicacion")
        ]
        return round(sum(dias) / len(dias)) if dias else None

    def cantidad_por_tipo_solicitud(self):
        registros = self._registros()
        tipos = ("Petición", "Queja", "Reclamo", "Sugerencia")
        return {
            tipo: sum(1 for registro in registros if registro.get("tipo_solicitud") == tipo)
            for tipo in tipos
        }

    def cantidad_por_tipo_mascota(self):
        registros = self._registros()
        return {
            mascota: sum(1 for registro in registros if registro.get("tipo_mascota") == mascota)
            for mascota in ("Perro", "Gato")
        }

    def cantidad_por_estado(self):
        registros = self._registros()
        estados = ("Registrada", "En proceso", "Solucionada")
        return {
            estado: sum(1 for registro in registros if registro.get("estado_peticion") == estado)
            for estado in estados
        }

    def pqrs_mas_antigua_activa(self):
        activas = [
            registro for registro in self._registros()
            if registro.get("estado_peticion") != "Solucionada"
            and registro.get("fecha_radicacion")
        ]
        return min(activas, key=lambda registro: registro["fecha_radicacion"]) if activas else None

    def pqrs_proximas_a_vencer(self, dias=5):
        hoy = date.today()
        proximas = []
        for registro in self._registros():
            if registro.get("estado_peticion") == "Solucionada":
                continue
            fecha_limite = registro.get("fecha_maxima_respuesta")
            if not fecha_limite:
                continue
            restantes = (date.fromisoformat(fecha_limite) - hoy).days
            if restantes <= dias:
                copia = dict(registro)
                copia["dias_restantes"] = restantes
                proximas.append(copia)
        return sorted(proximas, key=lambda registro: registro["dias_restantes"])

    def resumen_estadistico(self):
        proximas = self.pqrs_proximas_a_vencer()
        return {
            "promedio_dias_respuesta": self.calcular_promedio_dias_respuesta(),
            "por_tipo_solicitud": self.cantidad_por_tipo_solicitud(),
            "por_tipo_mascota": self.cantidad_por_tipo_mascota(),
            "por_estado": self.cantidad_por_estado(),
            "mas_antigua_activa": self.pqrs_mas_antigua_activa(),
            "proximas_a_vencer": proximas,
        }
