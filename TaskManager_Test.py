import unittest
from TaskManager import Tarefas, GestordeTarefas

class TaskManagerTest(unittest.TestCase):  # Corrected class name
    def setUp(self):
        self.gestor = GestordeTarefas()  # Corrected instance name

#Testes Validos
    def test_criar_tarefa(self):
        self.gestor.criar_tarefa("Ramo de Flores", "Ramo de Flores para casamento", "Ramos", 30, "p")
        self.assertEqual(len(self.gestor.tarefas), 1)
        self.assertEqual(self.gestor.tarefas[0].titulo, "Ramo de Flores")
        self.assertEqual(self.gestor.tarefas[0].descricao, "Ramo de Flores para casamento")
        self.assertEqual(self.gestor.tarefas[0].categoria, "Ramos")
        self.assertEqual(self.gestor.tarefas[0].prazo, 30)

    def test_editar_tarefa(self):
        self.gestor.criar_tarefa("Ramo de Flores", "Ramo de Flores para casamento", "Ramos", 30, "p")
        self.gestor.editar_tarefa(0, "Vaso de Rosas", "Vaso de Rosas para funeral", "Vasos", 20)
        self.assertEqual(self.gestor.tarefas[0].titulo, "Vaso de Rosas")
        self.assertEqual(self.gestor.tarefas[0].descricao, "Vaso de Rosas para funeral")
        self.assertEqual(self.gestor.tarefas[0].categoria, "Vasos")
        self.assertEqual(self.gestor.tarefas[0].prazo, 20)

    def test_eliminar_tarefa(self):
        self.gestor.criar_tarefa("Ramo de Flores", "Ramo de Flores para casamento", "Ramos", 30, "p")
        self.gestor.eliminar_tarefa(0)
        self.assertEqual(len(self.gestor.tarefas), 0)

    def test_listar_tarefas(self):
        self.gestor.criar_tarefa("Ramo de Flores", "Ramo de Flores para casamento", "Ramos", 30, "p")
        self.gestor.criar_tarefa("Vaso de tulipas", "Vaso de flores com tulipas", "Vasos", 20, "p")
        self.gestor.criar_tarefa("Flores ornamentais", "Ramos de Flores ornamentais", "Ramos", 15, "p")
        self.gestor.listar_tarefas()
        self.assertEqual(len(self.gestor.tarefas), 3)
        self.assertEqual(self.gestor.tarefas[0].titulo, "Ramo de Flores")
        self.assertEqual(self.gestor.tarefas[1].titulo, "Vaso de tulipas")
        self.assertEqual(self.gestor.tarefas[2].titulo, "Flores ornamentais")

    def test_mudar_status(self):
        self.gestor.criar_tarefa("Ramo de Flores", "Ramo de Flores para casamento", "Ramos", 30, "p")
        self.gestor.mudar_status(0, "c")
        self.assertEqual(self.gestor.tarefas[0].status, "c")

    def test_criar_categoria(self):
        self.gestor.criar_categoria("Ramos")
        self.assertEqual(len(self.gestor.categorias), 1)
        self.assertEqual(self.gestor.categorias[0].titulo, "Ramos")


    def test_listar_categorias(self):
        self.gestor.criar_categoria("Ramos")
        self.gestor.criar_categoria("Vasos")
        self.gestor.criar_categoria("Arranjos Ornamentais")
        self.gestor.listar_categorias()
        self.assertEqual(len(self.gestor.categorias), 3)
        self.assertEqual(self.gestor.categorias[0].titulo, "Ramos")
        self.assertEqual(self.gestor.categorias[1].titulo, "Vasos")
        self.assertEqual(self.gestor.categorias[2].titulo, "Arranjos Ornamentais")

    def test_eliminar_categoria(self):
        self.gestor.criar_categoria("Ramos")
        self.gestor.eliminar_categoria(0)
        self.assertEqual(len(self.gestor.categorias), 0)

# Testes invalidos

    def test_criar_tarefa_invalido(self):
        self.gestor.criar_tarefa("Ramo de Flores", "Ramo de Flores para casamento", "Ramos", "23", "p")
        self.assertEqual(self.gestor.tarefas[0].prazo, "23")

    def test_editar_tarefa_invalido(self):
        self.gestor.criar_tarefa("Ramo de Flores", "Ramo de Flores para casamento", "Ramos", 30, "p")
        self.gestor.editar_tarefa(0, "Vaso de Rosas", "Vaso de Rosas para funeral", "Vasos", "20")
        self.assertEqual(self.gestor.tarefas[0].prazo, "20")

    def test_eliminar_tarefa_invalido(self):
        self.gestor.criar_tarefa("Ramo de Flores", "Ramo de Flores para casamento", "Ramos", 30, "p")
        self.gestor.eliminar_tarefa(1)
        self.assertEqual(len(self.gestor.tarefas), 1)

    def test_mudar_status_invalido(self):
        self.gestor.criar_tarefa("Ramo de Flores", "Ramo de Flores para casamento", "Ramos", 30, "p")
        self.gestor.mudar_status(0, "x")
        self.assertEqual(self.gestor.tarefas[0].status, "p")

    def test_criar_categoria(self):
        self.gestor.criar_categoria("Ramos")
        self.assertEqual(len(self.gestor.categorias), 1)
        self.assertEqual(self.gestor.categorias[0].titulo, "Ramos")

    def test_listar_categorias(self):
        self.gestor.criar_categoria("Ramos")
        self.gestor.criar_categoria("Vasos")
        self.gestor.criar_categoria("Arranjos Ornamentais")
        self.gestor.listar_categorias()
        self.assertEqual(len(self.gestor.categorias), 3)
        self.assertEqual(self.gestor.categorias[0].titulo, "Ramos")
        self.assertEqual(self.gestor.categorias[1].titulo, "Vasos")
        self.assertEqual(self.gestor.categorias[2].titulo, "Arranjos Ornamentais")

    def test_eliminar_categoria(self):
        self.gestor.criar_categoria("Ramos")
        self.gestor.eliminar_categoria(0)
        self.assertEqual(len(self.gestor.categorias), 0)

    def test_criar_categoria_duplicada(self):
        self.gestor.criar_categoria("Ramos")
        self.gestor.criar_categoria("Ramos")
        self.assertEqual(len(self.gestor.categorias), 1)

    def test_eliminar_categoria_invalida(self):
        self.gestor.criar_categoria("Ramos")
        self.gestor.eliminar_categoria(1)
        self.assertEqual(len(self.gestor.categorias), 1)

if __name__ == "__main__":
    unittest.main()