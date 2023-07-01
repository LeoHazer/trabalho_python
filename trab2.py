"""
Trabalho 2 - Leonardo Peçanha

Data: 01/07/2023
Vídeo 15 min (máximo)
 -Explicar o arquivo CSV(ou JSON) escolhido
 -Apresentar a analise(gráfica) redigida, explicando o porquê de cada gráfico
 -"Código"
Serão sorteados alguns trabalhos para apresentação oral em sala
  -Critérios: 
  -Pode ser feito em "dupla"
  *Divisão do conteúdo
  *Clareza 
  *Escolha do tema
  *Gráfico escolhido
  *"Python"
 
  Fonte do artigo: https://onlinelibrary.wiley.com/doi/full/10.1002/oby.21247

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

nomeDataSet = "SonoEstVida.csv"

# Importar dataset
def criaDataFrame():
    dtSet = pd.read_csv(nomeDataSet)
    return dtSet

def ajustaDF_PressaoArt():
    dtSet = criaDataFrame()
    dtSet2 = pd.concat([dtSet, dtSet['Blood Pressure'].str.split('/', expand=True)], axis=1).drop('Blood Pressure', axis=1)
    dtSet2 = dtSet2.rename(columns={0: 'BloodPressure_high', 1: 'BloodPressure_low'})
    dtSet2['BloodPressure_high'] = dtSet2['BloodPressure_high'].astype(float)
    dtSet2['BloodPressure_low'] = dtSet2['BloodPressure_low'].astype(float)
    return dtSet2

def criaColunaHead():
    nomeColuna = ['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 'Stress Level',
                  'Heart Rate', 'Daily Steps', 'BloodPressure_high', 'BloodPressure_low']
    return nomeColuna

# Plot para a relação de distúrbios do sono
def geraHistPlot_DistSono(dtSet2, colHead):
    fig = plt.figure(figsize=(10, 10))
    for i in range(len(colHead)):
        plt.subplot(3, 3, i + 1)
        plt.title(colHead[i])
        sns.histplot(data=dtSet2, x=dtSet2[colHead[i]], hue='Sleep Disorder')
        plt.legend(fontsize=7, labels=dtSet2['Sleep Disorder'].unique())
    plt.tight_layout()
    plt.show()


def geraBoxplotGenero(dtSet2, colHead):
    fig = plt.figure(figsize=(8, 8))
    for i in range(len(colHead)):
        plt.subplot(3, 3, i + 1)
        plt.title(colHead[i])
        sns.boxplot(data=dtSet2, y=dtSet2['Gender'], x=dtSet2[colHead[i]])
    plt.tight_layout()
    plt.show()

def geraRelacaoSonoIMC_Idade(dtSet2):
    plt.figure(figsize=(5, 5))
    plt.legend(fontsize=10)
    plt.tick_params(labelsize=10)
    ax = sns.scatterplot(x=dtSet2['Age'], y=dtSet2['Sleep Duration'], hue=dtSet2['BMI Category'], data=dtSet2, sizes=(50, 500))
    plt.xticks(rotation=90)
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    x_lim = [25, 60]
    y_lim = [5.5, 8.5]
    plt.plot(x_lim, y_lim, color="red")
    plt.show()

def geraCategoriaIMC(dtSet2):
    dtSet2 = dtSet2.replace({'BMI Category': {'Normal': 0, 'Normal Weight': 1, 'Overweight': 2, 'Obese': 3}})
    
    plt.figure(figsize=(5, 5))
    plt.legend(fontsize=10, labels=dtSet2['BMI Category'].unique())
    plt.tick_params(labelsize=10)
    ax = sns.scatterplot(x=dtSet2['Age'], y=dtSet2['BMI Category'], hue=dtSet2['Sleep Duration'], data=dtSet2, sizes=(50, 500))
    plt.xticks(rotation=90)
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    x_lim = [25, 60]
    y_lim = [0, 3]
    plt.plot(x_lim, y_lim, color="red")
    plt.show()

# Duração de sono por idade - Gráfico de linha
def geraDuracaoSonoPorIdade(dtSet):
    
    #Gera um conjunto de idade por década
    dtSet['Age_bin'] = pd.cut(dtSet['Age'],[0, 30, 40, 50,60], labels=False)
    
    dtSet.groupby('Age_bin')['Sleep Duration'].mean().plot.line()

# Relação entre trabalho e qualidade do sono
def geraTrabVSQualSono(dtSet):
    organizaNome = dtSet.groupby('Occupation').SleepQuality.median().sort_values(ascending=False).index.values
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=dtSet, x="Occupation", y="Sleep Duration", order=organizaNome, ax=ax)
    plt.xticks(rotation=80)
    plt.xlabel('Emprego')
    plt.ylabel('Qualidade do sono')
    plt.title('Trabalho vs Qualidade do sono')
    plt.show()
    
    
    
    
def mostraMenu():
        print("Choose a graph to plot: ")
        print("1. Histograma de distúrbios do sono")
        print("2. Boxplot de Qualidade do Sono por Gênero")
        print("3. Scatterplot de duração de sono de acordo com IMC e Idade")
        print("4. Scatterplot IMC de acordo com sono e idade")
        print("5. Line plot duração de sono por idade")
        print("6. Boxplot de Qualidade do Sono de Acordo com a Profissão")
        print("0. Sair")

def main():
    dtSet2 = ajustaDF_PressaoArt()
    colHead = criaColunaHead()

    while True:
        mostraMenu()
        choice = int(input("Escolha um número: "))

        if choice == 1:
            geraHistPlot_DistSono(dtSet2, colHead)
        elif choice == 2:
            geraBoxplotGenero(dtSet2, colHead)
        elif choice == 3:
            geraRelacaoSonoIMC_Idade(dtSet2)
        elif choice == 4:
            geraCategoriaIMC(dtSet2)
        elif choice == 5:
            geraDuracaoSonoPorIdade(dtSet2)
        elif choice == 6:
            geraTrabVSQualSono(dtSet2)
        elif choice == 0:
            break
        else:
            print("Número inválido! Tente novamente")

if __name__ == '__main__':
    main()
  
