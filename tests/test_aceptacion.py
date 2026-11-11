"""Pruebas de aceptación automatizadas con datos ficticios y almacenamiento temporal.

Estas pruebas recorren los flujos funcionales desde el menú y comprueban
persistencia, radicados, estados y estadísticas sin tocar data/ del proyecto.
"""

import tempfile
import unittest
import subprocess
import sys
from contextlib import redirect_stdout
from datetime import date, timedelta
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from src.archivos import c_archivos
from src.main import c_main
from src.reportes import c_reportes


class TestAceptacionSistema(unittest.TestCase):
    """Valida los recorridos principales de aceptación del sistema."""

    def setUp(self):
        self.temporal = tempfile.TemporaryDirectory()
        self.ruta_datos = Path(self.temporal.name)
        self.archivos = c_archivos(self.ruta_datos)
        self.sistema = c_main()
        # Sustituye el almacenamiento normal por uno temporal y aislado.
        self.sistema.archivos = self.archivos
        self.sistema.reportes = c_reportes(self.archivos)

    def tearDown(self):
        self.temporal.cleanup()

    @staticmethod
    def entradas_registro(tipo, fecha=None):
        """Prepara datos ficticios válidos para recorrer el formulario."""
        return [
            "Ana María Pérez",
            "CC",
            "1037654321",
            "Celular",
            "3001234567",
            "ana.prueba@correo.com",
            "",
            tipo,
            fecha or date.today().isoformat(),
            "Presencial",
            "Consulta veterinaria",
            "Solicito información sobre la atención veterinaria de mi mascota.",
            "Perro",
            "Campus Medellín - Ciudad Universitaria",
        ]

    def registrar_por_menu(self, tipo, entradas=None):
        """Ejecuta el flujo de registro del menú con entradas simuladas."""
        with patch("builtins.input", side_effect=entradas or self.entradas_registro(tipo)):
            with patch("builtins.print"):
                self.sistema.registrar_pqrs()

    def test_registra_los_cuatro_tipos_y_asigna_consecutivos_independientes(self):
        tipos_archivos = {
            "Petición": "Peticion.txt",
            "Queja": "Queja.txt",
            "Reclamo": "Reclamo.txt",
            "Sugerencia": "Sugerencia.txt",
        }

        for tipo in tipos_archivos:
            self.registrar_por_menu(tipo)

        for tipo, nombre in tipos_archivos.items():
            registro = self.archivos.buscar_pqrs(1, tipo)
            self.assertIsNotNone(registro, f"No se encontró la primera {tipo}")
            self.assertEqual(registro["id"], 1)
            self.assertEqual(registro["estado_peticion"], "Registrada")
            self.assertEqual(
                registro["fecha_maxima_respuesta"],
                (date.fromisoformat(registro["fecha_radicacion"]) + timedelta(days=30)).isoformat(),
            )
            self.assertTrue((self.ruta_datos / nombre).is_file())
            radicado = self.ruta_datos / "radicados" / f"{nombre[:-4]}_000001.txt"
            self.assertTrue(radicado.is_file())

        self.assertEqual(len(self.archivos.obtener_todos()), 4)

    def test_validaciones_rechazan_entradas_invalidas_y_vuelven_a_solicitar(self):
        entradas = self.entradas_registro("Petición")
        fecha_futura = (date.today() + timedelta(days=1)).isoformat()
        # Un valor inválido y luego uno válido para cada campo probado.
        entradas_con_errores = [
            "Ana123", entradas[0],
            "XX", entradas[1],
            "10376A321", entradas[2],
            "Fax", entradas[3],
            "30012345AB", entradas[4],
            "correo-sin-arroba", entradas[5],
            entradas[6],
            entradas[7],
            "2026-99-99", fecha_futura, entradas[8],
            "Canal inventado", entradas[9],
            entradas[10],
            entradas[11],
            entradas[12],
            "Campus inexistente", entradas[13],
        ]
        salida = StringIO()
        with patch("builtins.input", side_effect=entradas_con_errores):
            with redirect_stdout(salida):
                self.sistema.registrar_pqrs()

        registro = self.archivos.buscar_pqrs(1, "Petición")
        self.assertIsNotNone(registro)
        self.assertEqual(registro["nombre_completo"], "Ana María Pérez")
        self.assertEqual(registro["numero_documento"], "1037654321")
        self.assertEqual(registro["telefono_contacto"], "3001234567")
        self.assertEqual(registro["correo_electronico"], "ana.prueba@correo.com")
        mensajes_error = salida.getvalue()
        cantidad_errores = sum(
            mensajes_error.count(fragmento)
            for fragmento in ("Use ", "Ingrese ", "no válido", "no sea futura", "debe tener")
        )
        self.assertGreaterEqual(cantidad_errores, 8)

    def test_datos_persisten_al_reabrir_el_gestor_y_consulta_general_funciona(self):
        for tipo in ("Petición", "Queja", "Reclamo", "Sugerencia"):
            self.registrar_por_menu(tipo)

        # Simula cerrar y volver a abrir: una nueva instancia lee los mismos archivos.
        gestor_reabierto = c_archivos(self.ruta_datos)
        self.assertEqual(len(gestor_reabierto.obtener_todos()), 4)

        sistema_reabierto = c_main()
        sistema_reabierto.archivos = gestor_reabierto
        sistema_reabierto.reportes = c_reportes(gestor_reabierto)
        salida = StringIO()
        with patch("builtins.input", side_effect=["Todas", "Queja", "1"]):
            with redirect_stdout(salida):
                sistema_reabierto.consultar_pqrs()

        self.assertIn("REGISTROS ENCONTRADOS", salida.getvalue())
        self.assertIn("Ana María Pérez", salida.getvalue())
        comprobante = self.ruta_datos / "radicados" / "Queja_000001.txt"
        self.assertTrue(comprobante.is_file())

    def test_radica_comprobantes_con_120_caracteres_y_sin_descripcion(self):
        for tipo in ("Petición", "Queja", "Reclamo", "Sugerencia"):
            self.registrar_por_menu(tipo)

        for tipo, archivo in c_archivos.ARCHIVOS.items():
            nombre = f"{archivo[:-4]}_000001.txt"
            contenido = (self.ruta_datos / "radicados" / nombre).read_text(encoding="utf-8")
            self.assertTrue(contenido.splitlines())
            self.assertTrue(all(len(linea) == 120 for linea in contenido.splitlines()))
            self.assertIn("N/A", contenido)
            self.assertIn("Ana María Pérez", contenido)
            self.assertNotIn(
                "Solicito información sobre la atención veterinaria de mi mascota.",
                contenido,
            )

    def test_transiciones_de_estado_y_fecha_de_solucion(self):
        self.registrar_por_menu("Reclamo")
        identificador = 1

        # No se permite saltar directamente de Registrada a Solucionada.
        with self.assertRaises(ValueError):
            self.archivos.cambiar_estado("Reclamo", identificador, "Solucionada")
        self.assertEqual(
            self.archivos.buscar_pqrs(identificador, "Reclamo")["estado_peticion"],
            "Registrada",
        )

        actualizado = self.archivos.cambiar_estado("Reclamo", identificador, "En proceso")
        self.assertEqual(actualizado["estado_peticion"], "En proceso")
        with self.assertRaises(ValueError):
            self.archivos.cambiar_estado("Reclamo", identificador, "Registrada")

        solucionado = self.archivos.cambiar_estado("Reclamo", identificador, "Solucionada")
        self.assertEqual(solucionado["estado_peticion"], "Solucionada")
        self.assertEqual(solucionado["fecha_respuesta"], date.today().isoformat())

    def test_seis_estadisticas_coinciden_con_los_registros_de_prueba(self):
        fecha_resuelta = (date.today() - timedelta(days=5)).isoformat()
        fecha_vencida = (date.today() - timedelta(days=35)).isoformat()
        fecha_proxima = (date.today() - timedelta(days=27)).isoformat()

        id_peticion = self.archivos.guardar_pqrs({
            **self.entradas_a_diccionario("Petición", fecha_resuelta, "Perro")
        })
        self.archivos.cambiar_estado("Petición", id_peticion, "En proceso")
        self.archivos.cambiar_estado("Petición", id_peticion, "Solucionada")

        self.archivos.guardar_pqrs(self.entradas_a_diccionario("Queja", fecha_vencida, "Gato"))
        self.archivos.guardar_pqrs(self.entradas_a_diccionario("Reclamo", fecha_proxima, "Perro"))
        self.archivos.guardar_pqrs(self.entradas_a_diccionario("Sugerencia", date.today().isoformat(), "Gato"))

        reportes = c_reportes(self.archivos)
        self.assertEqual(reportes.calcular_promedio_dias_respuesta(), 5)
        self.assertEqual(
            reportes.cantidad_por_tipo_solicitud(),
            {"Petición": 1, "Queja": 1, "Reclamo": 1, "Sugerencia": 1},
        )
        self.assertEqual(reportes.cantidad_por_tipo_mascota(), {"Perro": 2, "Gato": 2})
        self.assertEqual(
            reportes.cantidad_por_estado(),
            {"Registrada": 3, "En proceso": 0, "Solucionada": 1},
        )
        self.assertEqual(reportes.pqrs_mas_antigua_activa()["tipo_solicitud"], "Queja")
        proximas = reportes.pqrs_proximas_a_vencer()
        self.assertEqual(len(proximas), 2)
        self.assertLess(proximas[0]["dias_restantes"], 0)
        self.assertLessEqual(proximas[-1]["dias_restantes"], 5)

    @classmethod
    def entradas_a_diccionario(cls, tipo, fecha, mascota):
        """Adapta los datos de prueba al esquema que recibe la capa de archivos."""
        entradas = cls.entradas_registro(tipo, fecha)
        return {
            "nombre_completo": entradas[0],
            "tipo_documento": entradas[1],
            "numero_documento": entradas[2],
            "tipo_telefono": entradas[3],
            "telefono_contacto": entradas[4],
            "correo_electronico": entradas[5],
            "direccion": entradas[6],
            "tipo_solicitud": entradas[7],
            "fecha_radicacion": entradas[8],
            "canal_recepcion": entradas[9],
            "asunto_titulo": entradas[10],
            "descripcion_detallada": entradas[11],
            "tipo_mascota": mascota,
            "campus_relacionado": entradas[13],
        }

    def test_estadistica_sin_solucionadas_muestra_sin_datos(self):
        salida = StringIO()
        with redirect_stdout(salida):
            self.sistema.mostrar_estadisticas()
        self.assertIn("Sin datos de PQRS solucionadas", salida.getvalue())
        self.assertNotIn("Promedio de días de respuesta: 0 días", salida.getvalue())

    def test_menu_principal_muestra_las_cinco_opciones(self):
        raiz = Path(__file__).resolve().parents[1]
        resultado = subprocess.run(
            [sys.executable, "-m", "src.main"],
            input="5\n",
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            cwd=raiz,
            timeout=10,
        )
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        for opcion in (
            "1. Registrar PQRS",
            "2. Consultar PQRS",
            "3. Registrar cambio en PQRS",
            "4. Estadísticas",
            "5. Salir",
        ):
            self.assertIn(opcion, resultado.stdout)


if __name__ == "__main__":
    unittest.main()
