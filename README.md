# :bank: :chart_with_upwards_trend: Sistema Bancário

## O que foi desenvolvido
Neste projeto foi desenvolvido um Sistema Bancário em Python.<br>
Para a primeira versão desse sistema foram implementadas funcionalidades que permitem ao usuário realizar depósitos, saques e consultar o extrato da conta.

## Como funciona o sistema
1. **Variáveis principais**:
- saldo: armazena o saldo atual da conta.
- depositos: lista que guarda todos os depósitos feitos.
- saques: lista que guarda todos os saques realizados.
- limite_saque_diario: define o máximo de saques permitidos por dia.
- saque_maximo: define o valor máximo por saque (R$ 500).
- saques_diarios_realizados: conta quantos saques o usuário já fez no dia.

2. **Depósito**:<br>
O sistema pede um valor de depósito. Se for um valor positivo, ele é adicionado ao saldo e armazenado na lista "depositos".

3. **Saque**:<br>
O sistema verifica se o usuário já realizou o número máximo de saques no dia e se o valor do saque é válido (não maior que o saldo ou o limite de R$ 500). 
Se estiver tudo certo, o saque é realizado.

4. **Extrato**:<br>
O sistema exibe todos os depósitos e saques realizados até o momento e o saldo atual da conta.

5. **Sair**:<br>
O loop é interrompido quando o usuário escolhe a opção "4. Sair".

## Exemplo de Uso
----- Sistema Bancário -----
1. Depositar
2. Sacar
3. Extrato
4. Sair<br>
Escolha uma opção: 1<br>
Digite o valor do depósito: R$ 1000<br>
Depósito de R$ 1000.00 realizado com sucesso.<br>

----- Sistema Bancário -----
1. Depositar
2. Sacar
3. Extrato
4. Sair<br>
Escolha uma opção: 2<br>
Digite o valor do saque: R$ 300<br>
Saque de R$ 300.00 realizado com sucesso.<br>

----- Sistema Bancário -----
1. Depositar
2. Sacar
3. Extrato
4. Sair<br>
Escolha uma opção: 3

--- Extrato da Conta ---<br>
Depósitos:<br>
R$ 1000.00

Saques:<br>
R$ 300.00

Saldo atual: R$ 700.00

## Linguagens, Ferramentas e Bibliotecas Utilizadas
- Python
