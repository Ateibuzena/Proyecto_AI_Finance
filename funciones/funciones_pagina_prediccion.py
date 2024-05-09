import pandas as pd
import time
import plotly.graph_objects as go
import streamlit as st

def funcion_mae(cuenta):
  df_metricas = pd.read_csv(f"./data/df_metricas_{cuenta}.csv")
    # Crear traza
  trace = go.Scatter(x=list(range(len(df_metricas["mae"].tolist()))), y=df_metricas["mae"].tolist(), mode='lines', name='Mae')
  val_trace = go.Scatter(x=list(range(len(df_metricas["val_mae"].tolist()))), y=df_metricas["val_mae"].tolist(), mode='lines', name='val_Mae')
    # Diseño del gráfico
  layout = go.Layout(
                    xaxis=dict(title='Época'),
                    yaxis=dict(title='Mae'))
    # Figura
  fig = go.Figure(data=[trace, val_trace], layout=layout)
  return fig

def funcion_mse(cuenta):
  df_metricas = pd.read_csv(f"./data/df_metricas_{cuenta}.csv")
  # Crear traza
  trace = go.Scatter(x=list(range(len(df_metricas["loss"].tolist()))), y=df_metricas["loss"].tolist(), mode='lines', name='Pérdida')
  val_trace = go.Scatter(x=list(range(len(df_metricas["val_loss"].tolist()))), y=df_metricas["val_loss"].tolist(), mode='lines', name='Pérdida Validación')
  # Diseño del gráfico
  layout = go.Layout(
                    xaxis=dict(title='Época'),
                    yaxis=dict(title='Mse'))
    # Figura
  fig = go.Figure(data=[trace, val_trace], layout=layout)
  return fig