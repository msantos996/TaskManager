import unittest
from TaskManager import Tarefas, GestordeTarefas

class TaskManagerTest(unittest.TestCase):  # Corrected class name
    def setUp(self):
        self.gestor = GestordeTarefas()  # Corrected instance name

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

if __name__ == "__main__":
    unittest.main()