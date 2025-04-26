import sys
import os
import pytest
from unittest.mock import patch

# Adiciona o caminho do src ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Usando patch para evitar que o input() do main.py quebre o teste
with patch('builtins.input', return_value='2'):
    from src.main import resetarcopo

def test_resetar_copo():
    dados = resetarcopo()
    assert len(dados) == 13
    assert dados.count('dVerde') == 6
    assert dados.count('dAmarelo') == 4
    assert dados.count('dVermelho') == 3

