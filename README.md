# 💊 DrogaLaugh - Sistema de Autoatendimento em Farmácias

![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)
![Licença](https://img.shields.io/badge/License-CC%20BY--NC%204.0-blue)
![Tecnologias](https://img.shields.io/badge/Tecnologias-Python%20%7C%20PostgreSQL%20%7C%20Docker%20%7C%20Docker%20Compose%20%7C%20PyQT5-green)

---

## 📄 Descrição
DrogaLaugh é um sistema de autoatendimento desenvolvido com o objetivo de **reduzir a superlotação**, **eliminar longas filas** e **otimizar o gerenciamento de estoque em farmácias**. Focado na experiência do cliente, o sistema permite que os usuários busquem, reservem medicamentos e se comuniquem diretamente com atendentes por meio de um **chat online**.

Embora inspirado em um cenário real, DrogaLaugh é uma aplicação **acadêmica**, criada para ilustrar como soluções tecnológicas podem resolver problemas comuns enfrentados por farmácias. 

---

## 🌟 Objetivo principal
Reduzir filas e melhorar a experiência de compra, proporcionando atendimento ágil e controlado.

---

## ⚙️ Funcionalidades Principais

### Para os Clientes:
- 🔍 **Busca de Medicamentos**: Pesquise medicamentos cadastrados no sistema.
- 🛒 **Sistema de Reservas**: Reserve medicamentos com prazo limitado para retirada.
- 💬 **Chat Online**: Receba suporte direto de atendentes para esclarecer dúvidas e obter informações sobre medicamentos.
- 💳 **Pagamento no Local**: Pague via Pix, cartão ou dinheiro ao retirar os medicamentos.

### Para os Funcionários:
- 🗃️ **Gerenciamento de Estoque**: Adicione, edite ou remova medicamentos em tempo real.
- 📢 **Promoções Semanais**: Cadastre ofertas promocionais visíveis para os clientes.
- 💻 **Atendimento via Chat**: Forneça suporte aos clientes pelo chat integrado.

---

## 🛠️ Tecnologias Aplicadas

Este projeto foi desenvolvido utilizando uma combinação de tecnologias modernas para garantir eficiência, escalabilidade futura e desempenho. Abaixo estão as principais tecnologias aplicadas:

| Tecnologia           | Descrição                                                                 |
|-----------------------|---------------------------------------------------------------------------|
| 🐍 **Python 3.12**    | Linguagem de programação principal utilizada para construir o sistema.   |
| 🐋 **Docker**         | Ferramenta de contêinerização para padronizar e simplificar a execução.  |
| 📦 **Docker Compose** | Gerenciador de múltiplos contêineres para uma configuração simplificada. |
| 🖥️ **PyQt5**          | Biblioteca para desenvolvimento de interfaces gráficas de usuário (GUIs) em Python. |

---

## 🏗️ Estrutura do Sistema

### 🔒 Arquitetura
- **Banco de Dados**: PostgreSQL, armazenando medicamentos, reservas e promoções.
- **Componentes**:
  - **Interface do Cliente**: Busca, reservas e chat online.
  - **Interface do Funcionário**: Gerenciamento de produtos e atendimento.
  - **Camada de Segurança**: Proteção de dados sensíveis, como CPF.

### 🎨 Design de Interface
- Interface intuitiva, com foco em **facilidade de uso**.
- O design foi criado para proporcionar uma navegação intuitiva e fácil para o usuário, com uma **organização clara** das funcionalidades.

---

## 🛠️ Instalação e configuração
### Pré-requisitos
* Python 3.12 ou superior
* Docker e Docker Compose instalados
* PostgreSQL instalado
* Acesso à internet para clonar o repositório e instalar dependências

### Passos para configurar
1. Clone o repositório:
```bash
git clone https://github.com/Malujoro/POO_II-Trabalho_Final.git
cd POO_II-Trabalho_Final
```
2. Crie o ambiente virtual e instale as dependencias:
```bash
python -m venv drogaLaugh
source drogaLaugh/bin/activate
pip install -r requirements.txt
```
3. Construa e instale o pacote `postgresdb` localmente:
 * Acesse o diretório do pacote:
```bash
cd postgres_package
```
 * Construa o pacote:
```bash
poetry build
```
 * Instale o pacote gerado:
```bash
pip install dist/postgresdb-0.1.0-py3-none-any.whl --force-reinstall
```
4. execute o programa

---

## 👥 Contribuidores
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/149737667?v=4" width=115><br><sub>Alef Cauan Sousa Rodrigues</sub>](https://github.com/alefCauan) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/157396271?v=4" width=115><br><sub>Áurea Letícia Carvalho Macedo</sub>](https://github.com/aureamcd) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/110724864?v=4" width=115><br><sub>Gabriel Alves de Freitas</sub>](https://github.com/gabreudev) |
| :---: | :---: | :---: |
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/157633101?v=4" width=115><br><sub>Márcio Roberto de Brito Rodrigues</sub>](https://github.com/MarcioRobt0) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/45736178?v=4" width=115><br><sub>Mateus da Rocha Sousa</sub>](https://github.com/Malujoro) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/77069795?v=4" width=115><br><sub>Viviany da Silva Araújo</sub>](https://github.com/VivySilva) |

---



---

## 📜 Licença
Este projeto está licenciado sob a [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).  
Isso significa que você pode usar, modificar e compartilhar o projeto, mas **não é permitido utilizá-lo para fins comerciais** sem nossa permissão prévia.  
Consulte a licença para mais informações.

---

## 📬 Contato
Caso tenha dúvidas ou sugestões, você pode entrar em contato diretamente com os contribuidores do projeto:

| Contribuidor                              | GitHub Link                                                             |
|-------------------------------------------|-------------------------------------------------------------------------|
| Alef Cauan Sousa Rodrigues                | [Perfil no GitHub](https://github.com/alefCauan)                        |
| Áurea Letícia Carvalho Macedo             | [Perfil no GitHub](https://github.com/aureamcd)                         |
| Gabriel Alves de Freitas                  | [Perfil no GitHub](https://github.com/gabreudev)                        |
| Márcio Roberto de Brito Rodrigues         | [Perfil no GitHub](https://github.com/MarcioRobt0)                      |
| Mateus da Rocha Sousa                     | [Perfil no GitHub](https://github.com/Malujoro)                         |
| Viviany da Silva Araújo                   | [Perfil no GitHub](https://github.com/VivySilva)                        |

Ou visite diretamente o repositório do projeto no GitHub:  
👉 [DrogaLaugh system - Repositório Oficial](https://github.com/Malujoro/POO_II-Trabalho_Final)
