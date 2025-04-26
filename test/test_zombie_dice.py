import sys
import os
import pytest

# Adiciona o caminho do src ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.main import resetarcopo

def test_resetar_copo():
    dados = resetarcopo()
    assert len(dados) == 13
    assert dados.count('dVerde') == 6
    assert dados.count('dAmarelo') == 4
    assert dados.count('dVermelho') == 3