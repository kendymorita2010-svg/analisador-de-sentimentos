# 📊 Analisador de Sentimentos com Streamlit & NLTK

Uma aplicação web simples e eficiente para análise de sentimentos em frases em Português. O sistema utiliza a biblioteca **NLTK** (através do algoritmo VADER) combinado com a **deep-translator** para tradução em tempo real, permitindo uma análise precisa sem a necessidade de APIs pagas ou treinamentos complexos de modelos.

O projeto foi desenhado para rodar localmente no VS Code e está totalmente configurado para deploy gratuito no **Render**.

---

## 🚀 Funcionalidades

*   **Interface Intuitiva:** Interface limpa e reativa construída com Streamlit.
*   **Suporte a Português:** Tradução automática em segundo plano para processamento no motor VADER.
*   **Métrica de Score:** Exibição do *Compound Score* (métrica que varia de -1 a 1 indicando a intensidade do sentimento).
*   **Auditoria de Tradução:** Painel retrátil para visualizar como o modelo interpretou a frase em inglês.

---

## 🛠️ Tecnologias Utilizadas

*   [Python](https://www.python.org/) (v3.10+)
*   [Streamlit](https://streamlit.io/) - Para a interface web.
*   [NLTK (Natural Language Toolkit)](https://www.nltk.org/) - Para o motor de análise de sentimento (Léxico VADER).
*   [Deep Translator](https://github.com/nidhaloff/deep-translator) - Para a ponte de tradução PT-BR -> EN.

---

## 💻 Como Rodar Localmente (VS Code)

### 1. Clonar o Repositório
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio# analisador-de-sentimentos
