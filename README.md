# :bank: :chart_with_upwards_trend: Sistema Bancário

## O que foi desenvolvido
Neste projeto foi desenvolvido um Sistema Bancário em Python.<br>
Para a primeira versão desse sistema foram implementadas funcionalidades que permitem ao usuário realizar depósitos, saques e consultar o extrato da conta.
Para a segunda versão o sistema está otimizado para ser mais modular. As operações de saque, depósito e extrato foram separadas em funções e foram criadas mais duas funções: criar usuário e criar conta corrente vinculando com o usuário.

## Como funciona o sistema
1. **Função criar_usuario**:<br>
- Cadastra um novo usuário no sistema.
- Verifica se o CPF já existe na lista de usuários, evitando duplicidade.
- Usuário é composto por nome, data de nascimento, CPF e endereço.

2. **Função criar_conta_corrente**:<br>
- Cria uma conta corrente vinculada a um usuário existente.
- Verifica o CPF do usuário e associa a conta a esse CPF.
- O número da conta é sequencial, e a agência é sempre "0001".

3. **Função saque**:<br>
- Realiza saques com limite de R$ 500 por saque e até 3 saques diários.
- Recebe argumentos apenas por nome (keyword-only).
- Retorna o saldo atualizado e o extrato.

4. **Função deposito**:<br>
- Realiza depósitos na conta.
- Recebe argumentos apenas por posição (positional-only).
- Retorna o saldo atualizado e o extrato.

5. **Função exibir_extrato**:<br>
- Exibe todas as transações realizadas, além do saldo atual.
- Recebe o saldo por posição e o extrato por nome.

## Linguagens, Ferramentas e Bibliotecas Utilizadas
<img align='left' src="https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python" style='max-width: 100%;'/>
