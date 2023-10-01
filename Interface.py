from PySimpleGUI import PySimpleGUI as sg

tamanho_janela = (800, 400) 
margem_lateral = (20, 5)
tamanho_botao = (15, 2)

# Variáveis de controle de janelas
janela_atual = 'inicial'
janela1, janela2, janela3, janela4, janela5 = None, None, None, None, None

#Criar janelas e estilos(layout)
def janela_Inicial():
    sg.theme('Dark')
 
    layout = [
        [sg.Text('Olá, seja bem vindo(a) à bolaria da Mayra!', pad = (200,5))],
        [sg.Text('O que deseja fazer?', pad=(0,10))],
        [sg.Button('Fazer pedido', key='create', pad=margem_lateral, size=tamanho_botao)],
        [sg.Button('Alterar pedido', key='update', pad=margem_lateral, size=tamanho_botao)],
        [sg.Button('Ver pedidos', key='read', pad=margem_lateral, size=tamanho_botao)],
        [sg.Button('Deletar pedido', key='delete', pad=margem_lateral, size=tamanho_botao)],
        [sg.Button('Sair', key='exit', pad=(350,5), size=tamanho_botao)],
    ]
    return sg.Window('Bolaria da Mayra', layout=layout, finalize=True, size=tamanho_janela)

def janela_CreatePedido():
    sg.theme('Dark')
    layout = [
        [sg.Text('Fazer pedido', pad = (200,5))],
        [sg.Text('Nome do cliente:'), sg.Input('', key='nome_cliente', pad=margem_lateral, size=(30,2))],
        [sg.Text('item:                  '), sg.Input('', key='item', pad=margem_lateral, size=tamanho_botao)],
        [sg.Text('quantidade:        '), sg.Input('', key='quant', pad=margem_lateral, size=tamanho_botao)],
        [sg.Button('Voltar', key='voltar', pad=(20,20), size=tamanho_botao), sg.Button('Create Pedido', key='Create', pad=(20,20), size=tamanho_botao)],
    ]
    return sg.Window('Pedido', layout=layout, finalize=True, size=tamanho_janela)

def janela_UpdatePedido():
    sg.theme('Dark')
    layout = [
        [sg.Text('Alterar pedido', pad = (200,5))],
        [sg.Text('ID pedido:          '), sg.Input('', key='IdPedido', pad=margem_lateral, size=(15,2))],
        [sg.Text('Nome do cliente:'), sg.Input('', key='nome_cliente', pad=margem_lateral, size=(30,2))],
        [sg.Text('item:                  '), sg.Input('', key='item', pad=margem_lateral, size=tamanho_botao)],
        [sg.Text('quantidade:        '), sg.Input('', key='quant', pad=margem_lateral, size=tamanho_botao)],
        [sg.Button('Voltar', key='voltar', pad=(20,20), size=tamanho_botao), sg.Button('Alterar Pedido', key='Update', pad=(20,20), size=tamanho_botao)],
    ]
    return sg.Window('Pedido', layout=layout, finalize=True, size=tamanho_janela)

def janela_ReadPedido():
    sg.theme('Dark')
    layout = [
        [sg.Text('Ver Pedido', pad = (200,5))],
        [sg.Text('ID pedido:          '), sg.Input('', key='IdPedido', pad=margem_lateral, size=(15,2))],
        #[sg.Text('Nome do cliente:'), sg.Input('', key='nome_cliente', pad=margem_lateral, size=(30,2))],
        [sg.Button('Voltar', key='voltar', pad=(20,20), size=tamanho_botao), sg.Button('Ler Pedido', key='Read', pad=(20,20), size=tamanho_botao)],
    ]
    return sg.Window('Pedido', layout=layout, finalize=True, size=tamanho_janela)

def janela_DeletePedido():
    sg.theme('Dark')
    layout = [
        [sg.Text('Deletar Pedido', pad = (200,5))],
        [sg.Text('ID pedido:          '), sg.Input('', key='IdPedido', pad=margem_lateral, size=(15,2))],
        #[sg.Text('Nome do cliente:'), sg.Input('', key='nome_cliente', pad=margem_lateral, size=(30,2))],
        [sg.Button('Voltar', key='voltar', pad=(20,20), size=tamanho_botao), sg.Button('Deletar Pedido', key='Delete', pad=(20,20), size=tamanho_botao)],
    ]
    return sg.Window('Pedido', layout=layout, finalize=True, size=tamanho_janela)




janela1 = janela_Inicial()

while True:
    if janela_atual == 'inicial':
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == 'exit':
            break
        elif event == 'create':
            janela1.hide()
            janela2 = janela_CreatePedido()
            janela_atual = 'create'

        elif event == 'read':
            janela1.hide()
            janela3 = janela_ReadPedido()
            janela_atual = 'read'

        elif event == 'update':
            janela1.hide()
            janela4 = janela_UpdatePedido()
            janela_atual = 'update'

        elif event == 'delete':
            janela1.hide()
            janela5 = janela_DeletePedido()
            janela_atual = 'delete'

    elif janela_atual == 'create':
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'voltar':
            janela2.close()
            janela1.un_hide()
            janela_atual = 'inicial'
        elif event == 'Create':
            nome_cliente = values['nome_cliente']
            item = values['item']
            quant = values['quant']
            print(nome_cliente,'\n', item, '\n',quant)
            sg.popup('Pedido criado com sucesso!')
            janela2.close()
            janela1.un_hide()
            janela_atual = 'inicial'

    elif janela_atual == 'read':
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'voltar':
            janela3.close()
            janela1.un_hide()
            janela_atual = 'inicial'
        elif event == 'Read':
            IdPedido = values['IdPedido']
            print(IdPedido,'Item lido no banco de dados')
            sg.popup('Dados do banco de dados')
            janela3.close()
            janela1.un_hide()
            janela_atual = 'inicial'

    elif janela_atual == 'update':
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'voltar':
            janela4.close()
            janela1.un_hide()
            janela_atual = 'inicial'
        elif event == 'Update':
            IdPedido = values['IdPedido']
            nome_cliente = values['nome_cliente']
            item = values['item']
            quant = values['quant']
            print(IdPedido,'\nDados do banco de dados')

            sg.popup('Pedido alterado com sucesso!')
            janela4.close()
            janela1.un_hide()
            janela_atual = 'inicial'

    elif janela_atual == 'delete':
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'voltar':
            janela5.close()
            janela1.un_hide()
            janela_atual = 'inicial'
        elif event == 'Delete':
            IdPedido = values['IdPedido']
            print(IdPedido, 'Item deleteado do banco de dados')
            sg.popup('Pedido deletado com sucesso!')
            janela5.close()
            janela1.un_hide()
            janela_atual = 'inicial'