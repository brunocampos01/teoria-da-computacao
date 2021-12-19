# Teoria da Computação
![License](https://img.shields.io/badge/Code%20License-MIT-blue.svg)
![java](https://img.shields.io/badge/UFSC-Teoria_da_Computação-blue.svg)


## Theory of Computation
A teoria da computação é dividida em 3 partes:
- Teoria da computabilidade
- Teoria da complexidade
- Teoria dos autômatos e linguagens: usa técnica para reconhecer padrões, define gramáticas.


## Chomsky's Hierarchy

<img src="images/hierarquia.png" align="center" height=auto width=60%/>

<br/>

## Regular Languages
São as linguagens mais simples na Hierarquia de Chomsky.
<br/>
Exemplos:
- Analisador léxico
- Pesquisar por ocorrência de um padrão em uma palavra

### Regular Expressions
Expressão regular (ER) é outra forma de representar linguagens regulares.


## Context-Free Grammars
São linguagens mais poderosas que as linguagens regulares.
<br/>
Exemplos:
- Analisador sintático
- Processador de texto

## Finite Automata
- É um modelo computacional que reconhece classes de linguagens regulares. Para fazer isso, só mantem o estado atual.

<img src="images/automato.png" align="center" height=auto width=40%/>

<br/>

#### Exemplo de ADF
<img src="images/afd.png" align="center" height=auto width=70%/>

<br/>

#### Exemplo de AFND
<img src="images/afnd.png" align="center" height=auto width=70%/>

<br/>

## Turing Machine
Alan Turing criou a _Turing Machine_ para compreender a computabilidade.

> Note: Computador quântico não invalida a tese de Church-Turing

#### Representation
<img src="images/turing_machine_def.png" align="center" height=auto width=50%/>

- Fita infinita é dividida em células
- Cabeçote lê e escreve símbolos na fita
Cabeçote move para a esquerda e para a direita exatamente uma posição
- Cabeçote armazena um estado
- Células da fita contém exatamente um símbolo
- Células não inicialmente preenchidas possuem um símbolo de vazio

#### Turing Machine Example
<img src="images/turing_machine.png" align="center" height=auto width=70%/>

<br/>

[Aqui](exercicios/mestrado/resolucao_maquina_turing.pdf) tem um exemplo de resolução de questões sobre _Turing Machine_.


## Pumping Lema
O Pumping Lema serve para provar que algo não pertence a uma linguagem/gramática

## References
- [1] Michael Sipser, Introduction to the Theory of Computation


---

<p  align="left">
<br/>
<a href="mailto:brunocampos01@gmail.com" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/email.png" alt="Gmail" width="30">
</a>
<a href="https://stackoverflow.com/users/8329698/bruno-campos" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/stackoverflow.png" alt="GitHub" width="30">
</a>
<a href="https://www.linkedin.com/in/brunocampos01" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/linkedin.png" alt="LinkedIn" width="30"></a>
<a href="https://github.com/brunocampos01" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/github.png" alt="GitHub" width="30"></a>
<a href="https://brunocampos01.netlify.app/" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/blog.png" alt="Website" width="30">
</a>
<a href="https://medium.com/@brunocampos01" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/medium.png" alt="GitHub" width="30">
</a>
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png",  align="right" /></a><br/>
</p>
