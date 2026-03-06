# 📄 Atualização NUP
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Status](https://img.shields.io/badge/status-active-success)
![Google Sheets](https://img.shields.io/badge/google--sheets-API-green)
![API](https://img.shields.io/badge/API-REST-orange)
![GitHub stars](https://img.shields.io/github/stars/BrennoReboucas/atualizacao_nup)


> Automação criada porque alguém pediu atualização automática das planilhas…  
> ...sem recurso, sem n8n.
```
                         ⇦⇦⇨⇨⇨⇨⇨⇨⇨⇨⇨⇦⇦                         
                    ⇦⇨⇨←←←←→→→→→→→→→→←←←⇨⇨⇦                    
                ⇦⇨←←→→→↑↑↑↑↑↑↓↓↓↓↓↑↑↑↑↑↑→→→←←⇨⇦                
             ⇨⇨←←→→↑↑↓↕↱↲↲↲↲↲↲↲↲↲↲↲↲↲↲↲↱↔↑↑↑→→→←⇨⇦             
          <⇨⇨←→→↑↓↔↱↱↲↲↲↱↲↲↲↲↱↲↲↲↱↲↲↲↲↱↲↲↲↱↱↔↓↑↑→←⇨⇨<          
        <⇨⇨←→↑↑↓↕↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↕↓↑↑→←⇨⇨<        
       ⇨⇨←→↑↑↓↕↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↕↓↑↑→←⇨⇦       
     ⇦⇨←→→↑↓↔↕↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↱↕↔↓↑→→←⇨⇦     
     ⇨←→↑↑↓↔↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↓↑↑→←⇦     
    ⇨←→↑↑↓↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↓↑↑→←⇨    
   ⇨←→↑↑↓↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↓↓↑→←⇦   
  ⇦⇨→↑↑↓↓↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↓↓↑↑→⇨⇦  
 ⇦⇨←→↑↓↓↓↔↔↔↔↔↔↔↔↔↑>-↔↓↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔-/↑↔↔↔↔↔↔↔↔↔↓↓↓↑→←⇨⇦ 
 ⇨←→↑↑↓↓↓↓↓↓↓↓↔↕⇦\^^⇧↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓⇧~^/⇦↕↔↓↓↓↓↓↓↓↓↓↑→←⇨ 
⇦⇨←→↑↓↓↓↓↓↔↕→⇧<<<<\↑↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↑\^<<<⇧→↕↓↓↓↓↓↓↑→←⇨⇦
⇦⇨→↑↑↓↓↑|/~^<<^~←←↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓→←~^<<^~/|↑↓↓↑↑→⇨⇦
⇨⇨→↑↓↓↓↓↓↓↑→↑↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↑↑↑↓↓↓↓↓↓↑→⇨⇨
⇨←→↑↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↑→⇨⇨
⇨⇨→↑↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↑→⇨⇨
⇦⇨→→↑↓↓↓↓↓↓↑→↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↑↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↑↑→⇨⇦
⇨⇨←→↑↓↓↓↓↓↓←-^⇧⇩↔↓↓↓↓↓↑⇦⇩~~↓↓↓↓↓↓↓↓⇩-~⇦⇨↑↓↓↓↓↓↓⇩⇧<-←↓↓↓↓↓↓↑→←⇨⇨
 ⇨←→↑↑↓↓↓↓↓↓⇨>^^<^^^^^^^^^⇦↓↓↓↓↓↓↓↓↓⇦^<^^^^^^^^^^^⇦↓↓↓↓↓↓↓↑→←⇨ 
 ⇦⇨←→↑↓↓↓↓↓↓↓→⇧>///////>⇩↓↓↓↓↓↓↓↓↓↓↓↓↓⇦>///////>⇩→↓↓↓↓↓↓↓↑→←⇨⇦ 
  ⇦←→↑↑↓↓↓↓↓↓↓↓↓↑→\<⇧↑↑↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↑↑↑/<⇩↑→↓↓↓↓↓↓↓↓↓↑↑→⇨⇦  
   ⇨←→↑↑↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↑→←⇦   
    ⇨←→↑↑↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↑→←⇦    
     ⇦←→↑↑↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↑↑→←⇦     
     ⇦⇨⇨→→↑↓↓↓↓↓↓↓↓↓↓↓↓↓↓↔↑↑↑↑↑↑↑↑↑↑↑↔↓↓↓↓↓↓↓↓↓↓↓↓↓↓↑→→⇨⇨←     
       ⇦⇨←→↑↑↓↓↓↓↓↓↓↓↓↓↓⇦^^^^^~~~^^^^<↔↓↓↓↓↓↓↓↓↓↓↓↑↑→←⇨⇦       
        <⇨⇨←→↑↑↓↓↓↓↓↓↓↓↓↓→⇦⇦⇦⇦⇦⇦⇦⇦⇦⇦⇦→↓↓↓↓↓↓↓↓↓↓↑↑→←⇨⇨<        
          <⇨⇨←→→↑↑↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↑↑↑→←⇨⇨<          
             ⇦⇨←←→→↑↑↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↑↑→→→←⇨⇦             
                ⇦⇨←←→→→↑↑↑↑↑↓↓↓↓↓↓↓↑↑↑↑↑→→→←←⇨⇦                
                    ⇦⇨⇨←←←→→→→→→→→→→→←←←⇨⇨⇦                    
                         ⇦⇦⇨⇨⇨⇨⇨⇨⇨⇨⇦⇦⇦                         
                                
```

---

# 🇧🇷 Sobre o projeto

O **Atualização NUP** é um script em Python que automatiza o processo de atualização de planilhas.

Ele basicamente:

1. Realiza requisições para coletar dados.
2. Processa as informações recebidas.
3. Atualiza automaticamente uma planilha no Google Sheets.

A ideia surgiu para evitar o trabalho manual de atualizar planilhas repetidamente.

Em resumo:  
👉 alguém queria automação  
👉 não tinha ferramenta  
👉 então nasceu um script.

---

# ⚙️ Funcionalidades

- 🔎 Coleta automática de dados via requisição HTTP
- 📊 Atualização automática de planilhas Google
- ⏱ Execução programada em horários específicos
- 🧩 Código simples e fácil de adaptar

---

# 🧰 Tecnologias utilizadas

- Python
- Requests
- gspread
- Google API
- uv (gerenciador de ambiente)

---

# 🚀 Como executar

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/BrennoReboucas/atualizacao_nup.git
cd atualizacao_nup
```
### 2️⃣ Instale as dependências
```bash
uv sync
```

### 3️⃣ Configure suas credenciais

Adicione os arquivos necessários da API do Google (credenciais) para permitir acesso ao Google Sheets.

### 4️⃣ Execute o script
```bash
uv run sheets.py
```

# ⏰ Automação

O script foi projetado para rodar automaticamente em horários específicos do dia.

Exemplo:

  - 07:00

  - 12:30

Isso pode ser configurado usando:

  - schedule (Python)

  - cron

  - ou um serviço de automação.


# 🇺🇸 About

Atualização NUP is a Python automation script designed to update spreadsheets automatically.

It works by:

  - Sending requests to collect data

  - Processing the response

  - Updating a Google Sheet automatically

The goal is simple: eliminate manual spreadsheet updates.

Because sometimes the best solution is just automating the problem.

## 📂 Project structure
```
.
├── sheets.py
├── requirements.txt
├── README.md
└── LICENSE.txt
```

## 🤝 Contributing

Feel free to open issues or submit pull requests if you want to improve the project.





# 📜 License
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.