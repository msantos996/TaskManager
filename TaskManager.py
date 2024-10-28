status = {
            'c': "Concluído", #posicao 0, ponto de situação da tarefa
            'p': "Pendente" #posicao 1, ponto de situação da tarefa
        }
class Tarefas:
    def __init__(self, titulo, descricao, categoria, prazo) -> None: #declaração das variaveis a serem utilizadas para o programa
        self.titulo = titulo #variavel aplicavel ao titulo
        self.descricao = descricao #variavel aplicavel à descrição
        self.categoria = categoria #variavel aplicavel à categoria
        self.prazo = prazo #variavel aplicavel ao prazo
        self.status = "p" 
        

    def __str__(self):
        return f"Tarefa: {self.titulo}, Descrição: {self.descricao}, Categoria: {self.categoria}, Prazo: {self.prazo}, Status: {status[self.status]}"

class Categorias:
    def __init__(self, titulo):
        self.titulo = titulo

    def __str__(self):
        return f"Categoria: {self.titulo}"

class GestordeTarefas:
    def __init__(self):
        self.tarefas = []

    def criar_tarefa(self, titulo, descricao, categoria, prazo, status="p"): # Added status parameter with default value
        if titulo and descricao and categoria and prazo:
            nova_tarefa = Tarefas(titulo, descricao, categoria, prazo)
            nova_tarefa.status = status  # Set the status
            self.tarefas.append(nova_tarefa)
            print(f"Tarefa '{titulo}' criada com sucesso!")
        else:
            print("Dados invalidos, preencha uma nova tarefa e com dados válidos, por favor")
        #criar uma tarefa sem nome devia dar uma mensagem de que não é possivel criar sem nome
    def editar_tarefa(self, index, new_titulo=None, new_descricao=None, new_categoria=None, new_prazo=None): #edicao de uma tarefa
        if 0 <= index < len(self.tarefas):
            tarefa = self.tarefas[index]
            tarefa.titulo = new_titulo if new_titulo else tarefa.title
            tarefa.descricao = new_descricao if new_descricao else tarefa.descricao
            tarefa.categoria = new_categoria if new_categoria else tarefa.categoria
            if (new_prazo):
                try:
                    tarefa.prazo = int(new_prazo)
                except ValueError:
                    print("Prazo inválido! O prazo deve ser um valor numérico.")
                    return

            tarefa.prazo = new_prazo if new_prazo else tarefa.prazo
            print(f"Tarefa '{tarefa.titulo}' editada com sucesso!")
        else:
            print("Índice de tarefa inválido!")

    def eliminar_tarefa(self, index):
        if 0 <= index < len(self.tarefas):
            tarefa = self.tarefas.pop(index)
            print(f"Tarefa '{tarefa.titulo}' eliminada com sucesso!")
        else:
            print("Índice de tarefa inválido!")

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa encontrada.")
            return False
        for i, tarefa in enumerate(self.tarefas):
            print(f"{i}: {tarefa}")
        return True

    def mudar_status(self, index, novo_status): #mudar o estado, de pendente para concluido, mostrando ao utilizador a mensagem
        if 0 <= index < len(self.tarefas):
            tarefa = self.tarefas[index]
            if novo_status in ["c", "p"]:
                tarefa.status = novo_status
                print(f"Status da tarefa '{tarefa.titulo}' alterado para '{status[novo_status]}'!")
            else:
                print("Status inválido! Use 'p - pendente' ou 'c - concluido'.")
        else:
            print("Índice de tarefa inválido!")

    def criar_categoria(self, titulo):

        nova_categoria = Categorias(titulo)

        if (titulo in [categoria.titulo for categoria in self.categorias]):
            print("Categoria já existe!")
            return


        self.categorias.append(nova_categoria)
        print(f"Categoria '{titulo}' criada com sucesso!")

    def listar_categorias(self):
        if not self.categorias:
            print("Nenhuma categoria encontrada.")
            return False
        for i, categoria in enumerate(self.categorias):
            print(f"{i}: {categoria}")
        return True

    #TODO: Se existir uma categoria com tarefas associadas, não deve ser possível eliminar a categoria
    def eliminar_categoria(self, index):
        if 0 <= index < len(self.categorias):
            categoria = self.categorias.pop(index)
            print(f"Categoria '{categoria.titulo}' eliminada com sucesso!")
        else:
            print("Índice de categoria inválido!")


def menu():
    gestor = GestordeTarefas()

    def criar():
        titulo = input("Título: ")
        descricao = input("Descrição: ")
        categoria = input("Categoria: ")
        #valor_numerico = input("Prazo: ") #restringir para valores numericos
        while True:
            try:
                prazo=int(input("Prazo: "))
                break
            except ValueError:
                print ("Por favor preencha com um valor inteiro") #criação do prazo em minutos, e um aviso se for tentado o utilizador escrever valores que não sejam numericos
        gestor.criar_tarefa(titulo, descricao, categoria, prazo)
    def editar():
        if not gestor.listar_tarefas():
            return
        index = input("Índice da tarefa a editar (ou 'm' para voltar ao menu): ")
        if index.lower() == 'm':
            return
        index = int(index)
        new_titulo = input("Novo Título (deixe em branco para manter o atual): ")
        new_descricao = input("Nova Descrição (deixe em branco para manter a atual): ")
        new_categoria = input("Nova Categoria (deixe em branco para manter a atual): ")
        new_prazo = input("Novo Prazo (deixe em branco para manter o atual): ")
        gestor.editar_tarefa(index, new_titulo, new_descricao, new_categoria, new_prazo)

    def eliminar():
        if not gestor.listar_tarefas():
            return
        index = input("Índice da tarefa a eliminar (ou 'm' para voltar ao menu): ")
        if index.lower() == 'm':
            return
        index = int(index)
        gestor.eliminar_tarefa(index)

    def listar():
        gestor.listar_tarefas()

    def mudar_status():
        if not gestor.listar_tarefas():
            return
        index = input("Índice da tarefa para mudar o status (ou 'm' para voltar ao menu): ")
        if index.lower() == 'm':
            return
        index = int(index)
        novo_status = input("Novo status (p - pendente/c - concluido): ")
        gestor.mudar_status(index, novo_status)

    def sair():
        print("A Sair do Programa...")
        exit()

    options = {
        "1": criar,
        "2": editar,
        "3": eliminar,
        "4": listar,
        "5": mudar_status,
        "6": sair
    }

    while True:
        print("\n -- Trabalho Realizado por Fátima Esteves, João Nogueira e Miguel Santos --") #menu principal de acesso ao programa, onde o utilizador pode escolher as opções
        print("\n -- Menu Task Manager --")
        print("1 - Criar Tarefa")
        print("2 - Editar Tarefa")
        print("3 - Eliminar Tarefa")
        print("4 - Listar Tarefas")
        print("5 - Mudar Status da Tarefa")
        print("6 - Sair")

        escolha = input("Escolha a tarefa: ")
        action = options.get(escolha)
        if action:
            action()
        else:
            print("Escolha inválida! Tente novamente.") #se o utilizador não escolher a opção correta é dado uma mensagem para tentar novamente

if __name__ == "__main__":
    menu()
