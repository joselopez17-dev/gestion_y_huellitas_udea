"""Pruebas automatizadas de validación, almacenamiento y reportes."""

import tempfile
import unittest
from unittest.mock import patch
from datetime import date, timedelta
from pathlib import Path

from src.archivos import c_archivos
from src.reportes import c_reportes
from src.main import c_main
from src.validaciones import c_validaciones


class TestValidaciones(unittest.TestCase):
    def test_nombre(self):
        self.assertTrue(c_validaciones.validar_nombre("Juan David Pérez Gómez"))
        self.assertTrue(c_validaciones.validar_nombre("María José O'Connor"))
        self.assertFalse(c_validaciones.validar_nombre("Juan123"))
        self.assertFalse(c_validaciones.validar_nombre("A"))

    def test_documento_y_telefono(self):
        self.assertTrue(c_validaciones.validar_numero_documento("1037654321"))
        self.assertFalse(c_validaciones.validar_numero_documento("10376A321"))
        self.assertFalse(c_validaciones.validar_numero_documento("１２３"))
        self.assertTrue(c_validaciones.validar_telefono("3001234567", "Celular"))
        self.assertFalse(c_validaciones.validar_telefono("300123456", "Fijo"))
        self.assertFalse(c_validaciones.validar_telefono("٣٠٠١٢٣٤٥٦٧", "Celular"))

    def test_correo_y_direccion(self):
        self.assertTrue(c_validaciones.validar_correo("usuario@correo.com"))
        self.assertFalse(c_validaciones.validar_correo("usuariocorreo.com"))
        self.assertTrue(c_validaciones.validar_direccion(""))
        self.assertTrue(c_validaciones.validar_direccion("Avenida 10 #20-30"))
        self.assertFalse(c_validaciones.validar_direccion("abc"))
        self.assertFalse(c_validaciones.validar_direccion("Avenida\\\\Norte 10"))
        self.assertTrue(c_validaciones.validar_asunto("Solicitud de consulta veterinaria."))
        self.assertFalse(c_validaciones.validar_asunto("😊😊😊😊😊😊"))

    def test_opciones_y_fecha(self):
        self.assertTrue(c_validaciones.validar_tipo_solicitud("peticion"))
        self.assertTrue(c_validaciones.validar_campus("campus medellin - ciudad universitaria"))
        self.assertTrue(c_validaciones.validar_fecha_radicacion(date.today().isoformat()))
        futura = (date.today() + timedelta(days=1)).isoformat()
        self.assertFalse(c_validaciones.validar_fecha_radicacion(futura))
        self.assertFalse(c_validaciones.validar_fecha_radicacion(date.today().strftime("%Y%m%d")))


class TestArchivosYReportes(unittest.TestCase):
    def setUp(self):
        self.temporal = tempfile.TemporaryDirectory()
        self.gestor = c_archivos(Path(self.temporal.name))

    def tearDown(self):
        self.temporal.cleanup()

    @staticmethod
    def datos(tipo="Petición", fecha=None, mascota="Perro"):
        return {
            "nombre_completo": "Juan David Pérez Gómez",
            "tipo_documento": "CC",
            "numero_documento": "1037654321",
            "tipo_telefono": "Celular",
            "telefono_contacto": "3001234567",
            "correo_electronico": "usuario@correo.com",
            "direccion": "",
            "tipo_solicitud": tipo,
            "fecha_radicacion": fecha or date.today().isoformat(),
            "canal_recepcion": "Presencial",
            "asunto_titulo": "Atención veterinaria",
            "descripcion_detallada": "Solicito información sobre la atención veterinaria para mi mascota.",
            "tipo_mascota": mascota,
            "campus_relacionado": "Campus Medellín - Ciudad Universitaria",
        }


    def test_registro_completo_desde_el_menu(self):
        sistema = c_main()
        sistema.archivos = self.gestor
        entradas = [
            "Juan123",  # Debe rechazarse y volver a solicitar el nombre.
            "Juan David Pérez Gómez",
            "CC",
            "1037654321",
            "Celular",
            "3001234567",
            "usuario@correo.com",
            "",  # Dirección opcional.
            "Petición",
            date.today().isoformat(),
            "Presencial",
            "Atención veterinaria",
            "Solicito información sobre la atención veterinaria para mi mascota.",
            "Perro",
            "Campus Medellín - Ciudad Universitaria",
        ]
        with patch("builtins.input", side_effect=entradas), patch("builtins.print"):
            sistema.registrar_pqrs()

        registro = self.gestor.buscar_pqrs(1, "Petición")
        self.assertIsNotNone(registro)
        self.assertEqual(registro["nombre_completo"], "Juan David Pérez Gómez")
        self.assertEqual(registro["estado_peticion"], "Registrada")
        self.assertEqual(registro["direccion"], "")
        ruta_radicado = self.gestor.carpeta_radicados / "Peticion_000001.txt"
        self.assertTrue(ruta_radicado.exists())

    def test_consecutivos_independientes(self):
        primero = self.gestor.guardar_pqrs(self.datos("Petición"))
        segundo = self.gestor.guardar_pqrs(self.datos("Petición"))
        primero_queja = self.gestor.guardar_pqrs(self.datos("Queja"))
        self.assertEqual((primero, segundo, primero_queja), (1, 2, 1))
        self.assertTrue((Path(self.temporal.name) / "Peticion.txt").exists())
        self.assertTrue((Path(self.temporal.name) / "Queja.txt").exists())

    def test_flujo_de_estado_y_promedio(self):
        fecha = (date.today() - timedelta(days=5)).isoformat()
        identificador = self.gestor.guardar_pqrs(self.datos("Petición", fecha))
        with self.assertRaises(ValueError):
            self.gestor.cambiar_estado("Petición", identificador, "Solucionada")
        self.gestor.cambiar_estado("Petición", identificador, "En proceso")
        registro = self.gestor.cambiar_estado("Petición", identificador, "Solucionada")
        self.assertEqual(registro["estado_peticion"], "Solucionada")
        self.assertEqual(registro["fecha_respuesta"], date.today().isoformat())
        self.assertEqual(c_reportes(self.gestor).calcular_promedio_dias_respuesta(), 5)

    def test_radicado_de_120_caracteres(self):
        identificador = self.gestor.guardar_pqrs(self.datos())
        registro = self.gestor.buscar_pqrs(identificador, "Petición")
        radicado = self.gestor.construir_radicado(registro)
        lineas = radicado.splitlines()
        self.assertTrue(lineas)
        self.assertTrue(all(len(linea) == 120 for linea in lineas))
        self.assertIn("N/A", radicado)
        self.assertNotIn(registro["descripcion_detallada"], radicado)
        ruta = self.gestor.generar_radicado(registro)
        self.assertTrue(ruta.exists())


    def test_cinco_estadisticas_complementarias(self):
        hoy = date.today()
        fecha_peticion = (hoy - timedelta(days=6)).isoformat()
        fecha_queja_vencida = (hoy - timedelta(days=35)).isoformat()
        fecha_queja_proxima = (hoy - timedelta(days=27)).isoformat()
        fecha_reclamo_antiguo = (hoy - timedelta(days=50)).isoformat()

        id_peticion = self.gestor.guardar_pqrs(
            self.datos("Petición", fecha_peticion)
        )
        self.gestor.cambiar_estado("Petición", id_peticion, "En proceso")
        self.gestor.cambiar_estado("Petición", id_peticion, "Solucionada")

        self.gestor.guardar_pqrs(
            self.datos("Queja", fecha_queja_vencida, "Gato")
        )
        self.gestor.guardar_pqrs(
            self.datos("Queja", fecha_queja_proxima, "Perro")
        )
        self.gestor.guardar_pqrs(
            self.datos("Reclamo", fecha_reclamo_antiguo, "Gato")
        )

        reportes = c_reportes(self.gestor)

        self.assertEqual(
            reportes.cantidad_por_tipo_solicitud(),
            {"Petición": 1, "Queja": 2, "Reclamo": 1, "Sugerencia": 0},
        )
        self.assertEqual(
            reportes.cantidad_por_tipo_mascota(),
            {"Perro": 2, "Gato": 2},
        )
        self.assertEqual(
            reportes.cantidad_por_estado(),
            {"Registrada": 3, "En proceso": 0, "Solucionada": 1},
        )
        antigua = reportes.pqrs_mas_antigua_activa()
        self.assertEqual(antigua["tipo_solicitud"], "Reclamo")
        vencidas = reportes.pqrs_proximas_a_vencer()
        self.assertEqual(len(vencidas), 3)
        self.assertEqual(vencidas[0]["tipo_solicitud"], "Reclamo")
        self.assertLess(vencidas[0]["dias_restantes"], 0)


    def test_consulta_y_generacion_de_radicado_desde_menu(self):
        identificador = self.gestor.guardar_pqrs(self.datos("Petición"))
        sistema = c_main()
        sistema.archivos = self.gestor
        sistema.reportes = c_reportes(self.gestor)

        with patch("builtins.input", side_effect=["Petición", str(identificador)]), patch("builtins.print"):
            sistema.consultar_pqrs()

        ruta = self.gestor.carpeta_radicados / "Peticion_000001.txt"
        self.assertTrue(ruta.exists())
        self.assertIn("Juan David Pérez Gómez", ruta.read_text(encoding="utf-8"))

    def test_cambio_de_estado_desde_menu(self):
        identificador = self.gestor.guardar_pqrs(self.datos("Queja"))
        sistema = c_main()
        sistema.archivos = self.gestor
        sistema.reportes = c_reportes(self.gestor)

        with patch("builtins.input", side_effect=["Queja", str(identificador), "En proceso"]), patch("builtins.print"):
            sistema.cambiar_estado_pqrs()

        registro = self.gestor.buscar_pqrs(identificador, "Queja")
        self.assertEqual(registro["estado_peticion"], "En proceso")

    def test_fecha_maxima_y_reporte_por_tipo(self):
        identificador = self.gestor.guardar_pqrs(self.datos("Queja"))
        registro = self.gestor.buscar_pqrs(identificador, "Queja")
        esperado = (date.fromisoformat(registro["fecha_radicacion"]) + timedelta(days=30)).isoformat()
        self.assertEqual(registro["fecha_maxima_respuesta"], esperado)
        self.assertEqual(c_reportes(self.gestor).cantidad_por_tipo_solicitud()["Queja"], 1)


if __name__ == "__main__":
    unittest.main()


class TestMenuAplicacion(unittest.TestCase):
    def test_menu_principal_abre_y_cierra(self):
        raiz = Path(__file__).resolve().parents[1]
        resultado = __import__("subprocess").run(
            [__import__("sys").executable, str(raiz / "src" / "main.py")],
            input="5\n",
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            cwd=raiz,
            timeout=10,
        )
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertIn("Gracias por utilizar Gestión y Huellitas UdeA", resultado.stdout)
