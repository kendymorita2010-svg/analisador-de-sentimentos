import streamlit as st
import nltk
from  nltk.corpus import treebank

nltk.download('treebank')

frases = "python é legal"

tokens = nltk.word_tokenize(frases)

print(tokens)

nltk.download('averaged_perceptron_tagger_eng')

tagged = nltk.pos_tag(tokens)

print(tagged)
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()
import streamlit as str
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Garante o download do léxico do VADER necessário para a análise
nltk.download('vader_lexicon', quiet=True)

# Configuração simples da página
st.title("Análise de Sentimentos com NLTK")
st.write("Digite uma frase (de preferência em inglês) para descobrir o sentimento dela.")

# Input de texto do usuário (Prompt)
user_input = st.text_input("Sua frase:", placeholder="Type something here...")

# Botão para executar a análise
if st.button("Analisar Sentimento"):
    if user_input.strip() != "":
        # Inicializa o analisador do NLTK
        sia = SentimentIntensityAnalyzer()
        scores = sia.polarity_scores(user_input)
        
        # Define o sentimento com base no 'compound' score
        # O score varia de -1 (muito negativo) a 1 (muito positivo)
        if scores['compound'] >= 0.05:
            sentimento = "😊 Positivo"
        elif scores['compound'] <= -0.05:
            sentimento = "😢 Negativo"
        else:
            sentimento = "😐 Neutro"
            
        # Mostra o resultado na tela
        st.write(f"**Resultado:** O sentimento predomintante é **{sentimento}**")
    else:
        st.write("Por favor, digite algo antes de clicar no botão.")