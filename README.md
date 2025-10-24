
<p align="center">
  <img src="httpsT://raw.githubusercontent.com/joaogaabdev/RemindProject/main/app/static/assets/images/Favicon.png" alt="RemindMe Logo" width="120">
</p>

<h1 align="center">RemindMe</h1>

<p align="center">
  Um sistema inteligente de lembretes com OCR para reconhecimento automático de texto.
  <br />
  <br />
  <img src="https://img.shields.io/github/license/joaogaabdev/RemindProject" alt="License">
  <img src="https://img.shields.io/github/last-commit/joaogaabdev/RemindProject" alt="Last Commit">
  <img src="https://img.shields.io/badge/Python-3.9-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Django-3.2-darkgreen.svg" alt="Django">
  <img src="https://img.shields.io/badge/Docker-blue" alt="Docker">
</p>

---

## 📖 Sobre o Projeto

O **RemindMe** é um sistema web de código aberto projetado para resolver um problema comum: esquecer datas importantes escondidas em documentos. Quantas vezes você já perdeu o prazo de uma fatura, a data de vencimento de um contrato ou uma data de renovação?

Este projeto utiliza tecnologia **OCR (Reconhecimento Óptico de Caracteres)** para escanear automaticamente documentos (como PDFs e imagens) que você envia. Ele identifica datas e informações-chave, permitindo que você crie lembretes inteligentes e automatizados.

É a ferramenta perfeita para pequenas equipes, agentes de atendimento ou qualquer pessoa que precise gerenciar lembretes de forma mais eficiente.

### ✨ Principais Funcionalidades

* **📄 Reconhecimento Automático com OCR:** Faça upload de contratos, faturas, relatórios e deixe o sistema extrair o texto para você.
* **🤖 Agendamento Inteligente:** O sistema sugere datas encontradas no texto para criar lembretes de forma rápida.
* **🔔 Sistema de Notificação:** Seja alertado antes que datas importantes expirem.
* **👥 Gestão de Equipe:** (Em desenvolvimento) Um dashboard para gestores administrarem usuários e lembretes da equipe.
* **🐳 100% Dockerizado:** Configuração e deploy simplificados com Docker e Docker Compose.

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3
* **Banco de Dados:** PostgreSQL
* **DevOps:** Docker, Docker Compose
* **OCR Engine:** (Defina a biblioteca que você está usando, ex: Tesseract, EasyOCR)

---

## 🚀 Começando

Siga estas instruções para ter uma cópia do projeto rodando localmente para desenvolvimento e testes.

### Pré-requisitos

Você vai precisar ter as seguintes ferramentas instaladas na sua máquina:
* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/products/docker-desktop/)
* [Docker Compose](https://docs.docker.com/compose/install/)

### ⚙️ Instalação Local

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/joaogaabdev/RemindProject.git](https://github.com/joaogaabdev/RemindProject.git)
    cd RemindProject
    ```

2.  **Construa e suba os contêineres:**
    O `docker-compose` cuidará de tudo: construir a imagem do Django, baixar a imagem do Postgres e rodar as migrações do banco de dados (como definido no `command`).

    ```bash
    docker-compose up --build
    ```

3.  **Acesse a aplicação:**
    Após os contêineres estarem rodando, abra seu navegador e acesse:
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

    Você deverá ver a página inicial do RemindMe!

### 🔒 Configuração de Produção (Importante)

O arquivo `docker-compose.yml` atual está configurado para **desenvolvimento** (com `DEBUG=True` e senhas expostas). Para um ambiente de produção:

* Altere `DEBUG=True` para `DEBUG=False` no `settings.py`.
* Configure uma `SECRET_KEY` segura.
* **Nunca** use senhas "hardcoded". Use variáveis de ambiente (com `env_file` no Docker Compose) para todas as credenciais sensíveis (Secret Key, senhas de banco de dados, etc.).

---

## Usage

1.  Acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
2.  Crie uma conta na tela de "Sign up".
3.  Faça "Login".
4.  No seu dashboard, clique em "Novo Lembrete".
5.  Faça o upload de um documento (PDF ou imagem).
6.  O sistema processará o arquivo com OCR.
7.  Confirme os dados (como título e data) e salve o lembrete.
8.  Você verá seus lembretes pendentes no dashboard "Meus Lembretes".

---

## 🤝 Como Contribuir

Contribuições são o que tornam a comunidade de código aberto um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito bem-vinda**.

1.  Faça um **Fork** do projeto.
2.  Crie uma nova **Branch** (`git checkout -b feature/MinhaFeatureIncrivel`).
3.  Faça **Commit** das suas mudanças (`git commit -m 'Adicionando MinhaFeatureIncrivel'`).
4.  Faça **Push** para a Branch (`git push origin feature/MinhaFeatureIncrivel`).
5.  Abra um **Pull Request**.

---

## ⚖️ Licença

Distribuído sob a licença MIT. Veja `LICENSE.txt` para mais informações.
(Você precisará criar um arquivo `LICENSE.txt` e adicionar o texto da licença MIT nele).

---

## 👤 Contato

**João Gabriel**
* **GitHub:** [@joaogaabdev](https://github.com/joaogaabdev)
* **LinkedIn:** (Adicione o link do seu LinkedIn aqui)

**Link do Projeto:** [https://github.com/joaogaabdev/RemindProject](https://github.com/joaogaabdev/RemindProject)