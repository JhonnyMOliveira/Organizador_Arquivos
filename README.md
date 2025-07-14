# 🗂️ Organizador de Arquivos por Extensão

Este projeto em Python automatiza a organização de arquivos em um diretório, separando-os em subpastas conforme a **extensão do arquivo** (ex.: `.txt`, `.pdf`, `.jpg`).

---

## 🎯 Objetivo

Facilitar a organização de diretórios com grande volume de arquivos, agrupando-os automaticamente em pastas de acordo com o seu tipo, mantendo o ambiente de trabalho limpo e organizado.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.x**
- Módulo padrão `os`

---

## 🚀 Como Executar

1. **Clone ou baixe este repositório** no seu computador.

2. **Altere o diretório no script** (`os.chdir`) para o caminho da pasta que deseja organizar:

   ```python
   os.chdir(r"C:\Users\SeuUsuario\Caminho\Para\Sua\Pasta")

3. **Execute o script:** python organizador_arquivos.py


## 📂 Funcionamento do Script

O processo é realizado em quatro etapas:

1. **Leitura do diretório**

- Lista todos os arquivos no diretório escolhido.
- Converte os nomes dos arquivos para minúsculo para evitar duplicação de pastas (ex.: TXT e txt).

2. **Identificação de tipos**

- Extração das extensões dos arquivos.

3. **Criação das pastas**

- Cria automaticamente uma pasta para cada extensão (caso não exista).

4. **Movimentação dos arquivos**

- Move cada arquivo para a pasta correspondente ao seu tipo.


## 💡 Exemplo de Resultado

Antes da execução:

  Downloads/
  ├── documento.pdf
  ├── imagem.jpg
  ├── arquivo.txt
  ├── apresentação.pptx

Depois da execução:

  Downloads/
  ├── pdf/
  │   └── documento.pdf
  ├── jpg/
  │   └── imagem.jpg
  ├── txt/
  │   └── arquivo.txt
  ├── pptx/
  │   └── apresentação.pptx


## ⚠️ Observações Importantes

- O script move os arquivos, não cria cópias.
- Arquivos sem extensão não serão organizados automaticamente.
- Tenha certeza de estar no diretório correto antes de executar.


## ✨ Melhorias Futuras

- Tratar arquivos sem extensão.
- Permitir escolha do diretório por argumento de linha de comando.
- Implementar logs detalhados da execução.


#### 👨‍💻 Autor

Jhonny Marcelo de Oliveira
Engenheiro Eletricista com Ênfase em Telecomunicações | Especialista em Redes | Entusiasta por soluções em Python e Automações.


