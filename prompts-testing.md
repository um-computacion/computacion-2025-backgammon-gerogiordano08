- ChatGPT 5:
    - Input: "hay alguna manera simple de assert any call para varias lineas?"
    - Output: 
        "Sí—hay varias formas simples. Estas son las más comunes:
        1) Con mock usando assert_has_calls (varias líneas a la vez)
        Útil si querés validar llamadas a print (con o sin orden).
        from unittest.mock import patch, call

        @patch('builtins.print')
        def test_imprime_varias_lineas(mock_print):
            show_board()

            esperadas = [call("Línea A"), call("Línea B"), call("Línea C")]
            # Sin importar el orden:
            mock_print.assert_has_calls(esperadas, any_order=True)

            # Y si además querés que no haya impresiones extra:
            # assert mock_print.call_count == len(esperadas)
        Para respetar el orden exacto, poné any_order=False (o simplemente omitilo).
        2) Con mock iterando assert_any_call
        Sencillo y explícito.
        from unittest.mock import patch

        @patch('builtins.print')
        def test_imprime_varias_lineas(mock_print):
            show_board()
            for linea in ["Línea A", "Línea B", "Línea C"]:
                mock_print.assert_any_call(linea)
        3) Sin mock: capturar stdout y chequear todas
        Mejor cuando te importa el texto final (y no las llamadas).
        import io, contextlib, unittest

        class TestSalida(unittest.TestCase):
            def test_varias_lineas(self):
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    show_board()

                out_lines = buf.getvalue().splitlines()
                esperadas = {"Línea A", "Línea B", "Línea C"}
                self.assertTrue(esperadas.issubset(set(out_lines)))
                # o: for l in esperadas: self.assertIn(l, out_lines)
        Tips rápidos
        print("x") en el mock es call("x") (el \n no aparece en los args).
        Si usás print(..., end="") o múltiples argumentos, reflejalo en el call, ej. call("a", "b", end="").
        Si tu función “arma” una línea en varias llamadas (p. ej., varios print(..., end="")), capturar stdout suele ser más fiable que mockear."
    - Uso: use la primera sugerencia para checkear que se imprime correctamente el tablero con un test. Lo use en tests/board_tests.py