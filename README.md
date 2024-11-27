# **Moneta API**

Moneta é uma API projetada para fornecer informações detalhadas do mercado financeiro, com foco em empresas listadas na B3 e fundos imobiliários. O nome Moneta foi inspirado na deusa romana da riqueza, simbolizando estabilidade, crescimento e prosperidade no universo financeiro.

---

## **Descrição do Projeto**
A Moneta API é uma ferramenta que permite consultar e analisar dados financeiros de maneira eficiente. Seja para investidores, analistas ou entusiastas do mercado, a API oferece insights precisos e atualizados sobre empresas e fundos imobiliários no mercado brasileiro.

---

## **Recursos**
- **Informações de Empresas:** Obtenha dados sobre empresas listadas na B3, incluindo desempenho financeiro e indicadores-chave.
- **Dados de Fundos Imobiliários (FIIs):** Acompanhe informações detalhadas sobre fundos imobiliários disponíveis no mercado.

---

## **Como Usar**

### **Requisitos**
- Linguagem de programação: `Python`
- Dependências: [`beautifulsoup4`, `requests`, `FastAPI`]

### **Instalação**
1. Clone este repositório:
   ```bash
   git clone <url-do-repositorio>
   cd moneta

### **Instale as dependências**
   ```bash
      pip install -r requirements.txt
   ```

### **Inicie o servidor**
```bash
     uvicorn main:app --reload
   ```

### **Visualize os endpoints disponiveis no projeto**
   - Acesse o Swagger:
   - Swagger UI: http://127.0.0.1:8000/docs

     
### **Realizando um request**
Exemplo de uma requisição:

1. Ações 
   ```bash
      curl -X POST "http://127.0.0.1:8000/stocks/by-name-ticket" \
     -H "Content-Type: application/json" \
     -d '{"name_ticket": "itub4"}'
   ```
2. FII's
   ```bash
         curl -X POST "http://127.0.0.1:8000/fii/by-name-ticket" \
        -H "Content-Type: application/json" \
        -d '{"name_ticket": "mxrf11"}'
   ```


