import gradio as gr
import pandas as pd
import plotly.express as px

# Importar o dataset
# Ler o arquivo Parquet
df = pd.read_csv("./data/dados_sensores.csv")

def top_bottom_10(tipo):
    colunas = {
        "Água": "agua_m3",
        "Energia": "energia_kwh",
        "CO2": "co2_emissoes"
    }
    col = colunas[tipo]
    df_sorted = df.sort_values(by=col, ascending=False)
    df_top10 = df_sorted.head(10)
    df_bottom10 = df_sorted.tail(10)
    df_combined = pd.concat([df_top10, df_bottom10])
    fig_top = px.bar(df_combined, x="Empresa", y=col, color="Setor", title=f"Top e Bottom Empresas em emissão/consumo de {tipo} por Setor")
    return fig_top

def consolidated_by_sector():
    df_sector = df.groupby("Setor")[["agua_m3", "energia_kwh", "co2_emissoes"]].sum().reset_index()
    df_long = df_sector.melt(id_vars=["Setor"], var_name="Recurso", value_name="Consumo")
    fig = px.bar(df_long, x="Setor", y="Consumo", color="Recurso", title="Consumo Consolidado por Setor", barmode="group")
    return fig

# Criando interface Gradio
with gr.Blocks() as demo:
    gr.Markdown("## Dashboard de Sustentabilidade 🌱")
    tipo_selecao = gr.Radio(["Água", "Energia", "CO2"], label="Escolha um tipo de emissão/consumo")
    output_plot = gr.Plot()
    output_sector = gr.Plot()
    
    tipo_selecao.change(top_bottom_10, inputs=tipo_selecao, outputs=output_plot)
    setor_summary_btn = gr.Button("Mostrar Consolidado por Setor")
    setor_summary_btn.click(consolidated_by_sector, outputs=output_sector)
    
    gr.Row([output_plot])
    gr.Row([output_sector])

if __name__ == "__main__":
    demo.launch(server_port=7878)