import uuid
from datetime import datetime

tarefas = []

def adicionar_tarefas(descricao, prazo, urgencia):
  '''
  Adiciona uma nova tarefa à lista de tarefas.

  Parâmetros:
  descricao (str): Descrição da tarefa.
  prazo (str): Prazo final da tarefa no formato 'dd/mm/aaaa'
  urgencia (str): Nível de urgência da tarefa (Ex: 'Alta', 'Média', 'Baixa').

  Retorna:
  None
  '''
  tarefa = {
    'id': str(uuid.uuid4())[:8],
    'descricao': descricao,
    'data_criacao': datetime.now().strftime('%d/%m/%Y'),
    'status': 'Pendente',
    'prazo': prazo,
    'urgencia': urgencia
  }
  tarefas.append(tarefa)
  print(f'\nTarefa "{descricao}" com ID: "{tarefa['id']}" adicionada com sucesso')

def listar_tarefas():
  '''
  Lista todas as tarefas pendentes, mostrando ID, descrição, status e data de criação.

  Retorna:
  None
  '''
  if not tarefas:
    print('Nenhuma tarefa encontrada.')
    return
  
  print('\n--- Lista de Tarefas ---')
  for tarefa in tarefas:
    print(f'ID: {tarefa['id']} | Descrição: {tarefa['descricao']} | Status: {tarefa['status']} | Data de Criação: {tarefa['data_criacao']}')

def marcar_concluida(tarefa_id):
  '''
  Marca uma tarefa específica como concluída.
  
  Parâmetros:
  tarefas_id (str): ID da tarefa a ser marcada como concluída.

  Retorna:
  None
  '''
  for tarefa in tarefas:
    if tarefa['id'] == tarefa_id:
      tarefa['status'] = "Concluída"
      print(f'\nTarefa "{tarefa['descricao']}" marcada como concluída.')
      return
  print('\nTarefa não encontrada.')

def remover_tarefa(tarefa_id):
  '''
  Remoce uma tarefa da lista com base no ID.
  
  Parâmetros:
  tarefa_id (str): ID da tarefa a ser removida.
  
  Retorna:
  None
  '''
  for tarefa in tarefas:
    if tarefa['id'] == tarefa_id:
      tarefas.remove(tarefa)
      print(f'\nTarefa "{tarefa['descricao']}" removida com sucesso.')
      return
  print('\nTarefa não encontrada.')

def menu():
  '''
  Apresenta um menu de opções para o usuário e executa a função correspondente com base na escolha.
  
  Retorna:
  None
  '''
  while True:
    print('\n--- Menu de Tarefas ---')
    print('1. Adicionar Tarefa')
    print('2. Listar Tarefa')
    print('3. Marcar Tarefa como concluída')
    print('4. Remover Tarefa')
    print('5. Sair')

    escolha = input('Escolha uma opção: ')

    if escolha == '1':
      descricao = input('Digite a descrição da tarefa: ')
      prazo = input('Digite o prazo da tarefa (dd/mm/aaaa): ')
      urgencia = input('Digite o nível de urgência (Alta, Média, Baixa): ')
      adicionar_tarefas(descricao, prazo, urgencia)

    elif escolha == '2':
      listar_tarefas()

    elif escolha == '3':
      tarefa_id = input('Digite o ID da tarefa a ser marcada como concluída: ')
      marcar_concluida(tarefa_id)
    
    elif escolha == '4':
      tarefa_id = input('Digite o ID da tarefa a ser removida: ')
      remover_tarefa(tarefa_id)

    elif escolha == '5':
      print('\nSaindo do programa...')
      break

    else:
      print('\nOpção inválida. Por favor, escolha um número entra 1 e 5')


menu()