import streamlit as st
from controllers.estudante_controller import listar_estudantes
import matplotlib.pyplot as plt
import numpy as np

def show():
    st.title("📊 Dashboard Escolar")

    estudante = listar_estudantes()
    total_estudante = len(estudante)

    if total_estudante == 0:
        st.warning("Nenhum estudante cadastrado ainda.")
        return

    # 🔹 Estatísticas principais
    st.metric("👨‍🎓 Total de estudantes", total_estudante)
    st.metric("📌 Último cadastrado", estudante[-1].nome)

    medias = [e.media for e in estudante]
    media_geral = sum(medias) / total_estudante
    maior_media = max(estudante, key=lambda e: e.media)
    menor_media = min(estudante, key=lambda e: e.media)

    col1, col2, col3 = st.columns(3)
    col1.metric("📊 Média geral", f"{media_geral:.2f}")
    col2.metric("🏆 Maior média", f"{maior_media.media:.2f} ({maior_media.nome})")
    col3.metric("📉 Menor média", f"{menor_media.media:.2f} ({menor_media.nome})")

    # 🔹 Dados individuais
    nota1s = [e.nota1 for e in estudante]
    nota2s = [e.nota2 for e in estudante]
    nota3s = [e.nota3 for e in estudante]
    nomes = [e.nome for e in estudante]

    # 📊 Gráfico 1 - Média por estudante
    st.subheader("📊 Média por estudante")
    fig, ax = plt.subplots()
    ax.bar(nomes, medias, color="skyblue")
    ax.set_ylabel("Média")
    ax.set_xticklabels(nomes, rotation=45, ha="right")
    st.pyplot(fig)

    # 📊 Gráfico 2 - Notas por estudante (barras agrupadas)
    st.subheader("📊 Notas por estudante")
    indices = np.arange(total_estudante)
    largura = 0.25
    fig, ax = plt.subplots()
    ax.bar(indices - largura, nota1s, largura, label="Nota 1")
    ax.bar(indices, nota2s, largura, label="Nota 2")
    ax.bar(indices + largura, nota3s, largura, label="Nota 3")
    ax.set_xticks(indices)
    ax.set_xticklabels(nomes, rotation=45, ha="right")
    ax.set_ylabel("Notas")
    ax.legend()
    st.pyplot(fig)

    # 📊 Gráfico 3 - Evolução das médias da turma
    st.subheader("📈 Evolução do desempenho (média por avaliação)")
    medias_avaliacoes = [
        sum(nota1s) / total_estudante,
        sum(nota2s) / total_estudante,
        sum(nota3s) / total_estudante
    ]
    fig, ax = plt.subplots()
    ax.plot(["Nota 1", "Nota 2", "Nota 3"], medias_avaliacoes, marker="o", color="green")
    ax.set_ylabel("Média da turma")
    st.pyplot(fig)

    # 📋 Lista de estudantes
    st.subheader("📋 Lista de estudantes")
    for e in estudante:
        st.write(f"👤 {e.nome} — Notas: {e.nota1}, {e.nota2}, {e.nota3} — Média: {e.media:.2f}")
