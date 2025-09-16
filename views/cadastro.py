import streamlit as st
from controllers.estudante_controller import adicionar_estudante, listar_estudantes

def show():
    st.title("📚 Cadastro de estudante")
    
    with st.form("cadastro_form"):
        nome = st.text_input("Nome do estudante")
        nota1 = st.number_input("Nota 1", min_value=0.0, max_value=10.0, step=0.1)
        nota2 = st.number_input("Nota 2", min_value=0.0, max_value=10.0, step=0.1)
        nota3 = st.number_input("Nota 3", min_value=0.0, max_value=10.0, step=0.1)
        submitted = st.form_submit_button("Cadastrar")

        if submitted:
            try:
                adicionar_estudante(nome, nota1, nota2, nota3)
                st.success("✅ Estudante cadastrado com sucesso!")
            except ValueError as e:
                st.error(f"Erro: {e}")

    st.subheader("Lista de estudante")
    estudante = listar_estudantes()
    for e in estudante:
        st.write(f"👤 {e.nome} — Notas: {e.nota1}, {e.nota2}, {e.nota3} — Média: {e.media:.2f}")
